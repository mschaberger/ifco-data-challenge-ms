import os
from functions import (
    load_orders,
    load_invoicing_data,
    get_crate_distribution_per_company,
    create_contact_full_name,
    create_contact_address,
    calculate_commissions,
    create_company_salesowners_df
)

def main():
    # Data file paths
    orders_file_path = os.path.join('data', 'orders.csv')
    invoicing_file_path = os.path.join('data', 'invoicing_data.json')

    # Load data
    orders_df = load_orders(orders_file_path)
    invoicing_df = load_invoicing_data(invoicing_file_path)

    # Test 1: Distribution of Crate Type per Company
    crate_distribution = get_crate_distribution_per_company(orders_df)
    print("Test 1: Distribution of crate types per company:")
    print(crate_distribution)

    # Test 2: DataFrame of Orders with Full Name of the Contact
    df_1 = create_contact_full_name(orders_df)
    print("Test 2: DataFrame with order id and contact name:")
    print(df_1)

    # Test 3: DataFrame of Orders with Contact Address
    df_2 = create_contact_address(orders_df)
    print("Test 3: DataFrame of Orders with Contact Address:")
    print(df_2)

    # Test 4: Calculation of Sales Team Commissions
    sales_owner_commission = calculate_commissions(orders_df, invoicing_df)
    print("Test 4: List of sales owners and their respective commission:")
    print(sales_owner_commission)

    # Test 5: DataFrame of Companies with Sales Owners
    df_3 = create_company_salesowners_df(orders_df)
    print("Test 5: DataFrame of Companies with Sales Owners:")
    print(df_3)

if __name__ == '__main__':
    main()