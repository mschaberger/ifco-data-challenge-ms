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
    return pd.json_normalize(data)


# Function to calculate the distribution of crate types per company
def get_crate_distribution_per_company(orders_df):
    distribution = orders_df.groupby(['company_name', 'crate_type']).size().reset_index(name='order_count')
    return distribution


# Function to create a Dataframe with the fields 'order_id' and 'contact_full_name'
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


# Function to a Dataframe with the fields 'order_id' and 'contact_address'
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