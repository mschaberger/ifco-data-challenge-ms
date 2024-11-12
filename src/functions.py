import pandas as pd
import json

# Function to load orders data from a csv file 
def load_orders(file_path):
    orders_df = pd.read_csv(file_path, delimiter=';')
    return orders_df


# Function to load invoicing data from a json file 
def load_invoicing_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return pd.json_normalize(data['data'], 'invoices')


#### Case 1:
# Function to calculate the distribution of crate types per company
def get_crate_distribution_per_company(orders_df):
    distribution = orders_df.groupby(['company_name', 'crate_type']).size().reset_index(name='order_count')
    return distribution


#### Case 2:
# Function to create a DataFrame with the fields 'order_id' and 'contact_full_name'
def create_contact_full_name(orders_df):

    # Function to extract name and surname from the field 'contact_data'
    def extract_full_name(contact_data):
        if not contact_data: 
            return 'John Doe'
        try:
            contact_info = json.loads(contact_data) 
            if isinstance(contact_info, list) and len(contact_info) > 0:
                contact_name = contact_info[0].get('contact_name', 'John')
                contact_surname = contact_info[0].get('contact_surname', 'Doe')
                return f"{contact_name} {contact_surname}"
            else:
                return 'John Doe'  
        except (json.JSONDecodeError, IndexError, TypeError):
            return 'John Doe'

    orders_df['contact_full_name'] = orders_df['contact_data'].apply(extract_full_name)
    return orders_df[['order_id', 'contact_full_name']]


#### Case 3:
# Function to create a DataFrame with the fields 'order_id' and 'contact_address'
def create_contact_address(orders_df):

    def format_address(address_data):
        if not address_data:  
            return 'Unknown, UNK00'
        try:
            address_info = json.loads(address_data) 
            if isinstance(address_info, list) and len(address_info) > 0:
                city = address_info[0].get('city', 'Unknown')  
                postal_code = address_info[0].get('cp', 'UNK00')  
                return f"{city}, {postal_code}"
            else:
                return 'Unknown, UNK00' 
        except (json.JSONDecodeError, TypeError): 
            return 'Unknown, UNK00'  

    orders_df['contact_address'] = orders_df['contact_data'].apply(format_address)
    return orders_df[['order_id', 'contact_address']]


#### Case 4:
# Helper function to split and clean the salesowners list
def extract_salesowners(owners_str):
    return [owner.strip() for owner in owners_str.split(',')] if owners_str else []

# Helper function to calculate the commission based on the owner's position
def calculate_owner_commission(net_value, position):
    commission_rates = {
        0: 0.06,  
        1: 0.025, 
        2: 0.0095 
    }
    return commission_rates.get(position, 0) * net_value

# Helper function to calculate commissions for all sales owners involved in an order
def calculate_commissions_for_order(merged_df):
    sales_commissions = {}

    for _, row in merged_df.iterrows():
        net_value = int(row['grossValue']) - int(row['vat']) 
        salesowners = extract_salesowners(row['salesowners'])
        
        for position, owner in enumerate(salesowners[:3]): 
            commission = calculate_owner_commission(net_value, position)
            if owner not in sales_commissions:
                sales_commissions[owner] = 0
            sales_commissions[owner] += commission

    return sales_commissions

# Function to calculate the sales commissions by merging order and invoice data.
def calculate_commissions(orders_df, invoices_df):
    merged_df = pd.merge(orders_df, invoices_df, left_on='order_id', right_on='orderId')
    sales_commissions = calculate_commissions_for_order(merged_df)

    sales_commissions = {owner: round(commission / 100, 2) for owner, commission in sales_commissions.items()}

    commission_df = pd.DataFrame(list(sales_commissions.items()), columns=['salesowner', 'commission'])
    commission_df = commission_df.sort_values(by='commission', ascending=False).reset_index(drop=True)
    
    return commission_df


#### Case 5:
# Function to create a DataFrame with the fields 'company_id', 'company_name' and 'list_salesowners'
def create_company_salesowners_df(orders_df):
    unique_companies = orders_df.groupby('company_id').agg({
        'company_name': 'first', 
        'salesowners': lambda x: ', '.join(set(', '.join(x).split(',')))
    }).reset_index()

    unique_companies['list_salesowners'] = unique_companies['salesowners'].apply(
        lambda owners: ', '.join(sorted({owner.strip() for owner in owners.split(',') if owner.strip()}))
    )

    unique_companies = unique_companies.drop(columns='salesowners')
    return unique_companies