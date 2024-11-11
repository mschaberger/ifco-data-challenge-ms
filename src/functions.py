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

# Function to alculate the distribution of crate types per company
def get_crate_distribution_per_company(orders_df):
    distribution = orders_df.groupby(['company_name', 'crate_type']).size().reset_index(name='order_count')
    
    return distribution


# Function to create A Dataframe with the fields 'order_id' y 'contact_full_name'
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
    orders_df = orders_df[['order_id', 'contact_full_name']]

    return orders_df