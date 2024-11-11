import os
from functions import (
    load_orders,
    load_invoicing_data,
    get_crate_distribution_per_company,
    create_contact_full_name
)

def main():
    # Data file paths
    orders_file_path = os.path.join('data', 'orders.csv')
    invoicing_file_path = os.path.join('data', 'invoicing_data.json')

    # Load data
    orders_df = load_orders(orders_file_path)
    invoicing_df = load_invoicing_data(invoicing_file_path)

    # Test 1: Calculate the distribution of crate types per company
    crate_distribution = get_crate_distribution_per_company(orders_df)
    print("Test 1: Distribution of crate types per company:")
    print(crate_distribution)

    # Test 2: Create A Dataframe with order id and contact name
    df_1 = create_contact_full_name(orders_df)
    print("Test 2: Dataframe with order id and contact name:")
    print(df_1)

if __name__ == '__main__':
    main()