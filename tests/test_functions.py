import unittest
import pandas as pd
from src.functions import (
    get_crate_distribution_per_company,
    create_contact_full_name,
    create_contact_address,
    calculate_commissions,
    create_company_salesowners_df
)

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.orders_data = pd.DataFrame({
            'order_id': [1, 2, 3, 4, 5],
            'company_id': ['c111', 'c222', 'c111', 'c111', 'c222'],
            'company_name': ['Company A', 'Company B', 'Company aa', 'Company A', 'Company B'],
            'crate_type': ['Type 1', 'Type 2', 'Type 1', 'Type 2', 'Type 2'],
            'contact_data': [
                '[{"contact_name": "Alice", "contact_surname": "Smith", "city": "New York", "cp": "10001"}]',
                '[]', 
                '[{"contact_name": "Bob", "contact_surname": "Docker", "city": "Los Angeles"}]',
                '[{"contact_name": "Bobby", "contact_surname": "Jackson", "city": "Los Angeles", "cp": "20002"}]',
                '[{"contact_name": "", "contact_surname": "", "city": "", "cp": ""}'
            ],
            'salesowners': ['Alice Owner, Bob Owner, Jack Owner', 'Bob Owner, Jack Owner, Matt Owner, Michael Owner, Alice Owner', 'Charlie Owner, Alice Owner, Bob Owner', 'Michael Owner, Charlie Owner', 'Matt Owner, Alice Owner, Jack Owner, Bob Owner']
        })
        
        self.invoices_data = pd.DataFrame({
            'id': ['e1', 'e2', 'e3', 'e4', 'e5'],
            'orderId': [1, 2, 3, 4, 5],
            'companyId': ['c1', 'c2', 'c1', 'c1', 'c2'],
            'grossValue': [10000, 15000, 20000, 25000, 30000],
            'vat': [0, 19, 22, 0, 34]
        })

    #### Test case 1:
    def test_get_crate_distribution_per_company(self):
        result = get_crate_distribution_per_company(self.orders_data)
        expected = pd.DataFrame({
            'company_name': ['Company A', 'Company B', 'Company A'],
            'crate_type': ['Type 1', 'Type 2', 'Type 2'],
            'order_count': [2, 2, 1]
        })
        pd.testing.assert_frame_equal(result, expected)

    #### Test case 2:
    def test_create_contact_full_name(self):
        result = create_contact_full_name(self.orders_data)
        expected = pd.DataFrame({
            'order_id': [1, 2, 3, 4, 5],
            'contact_full_name': ['Alice Smith', 'John Doe', 'Bob Docker', 'Bobby Jackson', 'John Doe']
        })
        pd.testing.assert_frame_equal(result[['order_id', 'contact_full_name']], expected)

    #### Test case 3:
    def test_create_contact_address(self):
        result = create_contact_address(self.orders_data)
        expected = pd.DataFrame({
            'order_id': [1, 2, 3, 4, 5],
            'contact_address': ['New York, 10001', 'Unknown, UNK00', 'Los Angeles, UNK00', 'Los Angeles, 20002', 'Unknown, UNK00']
        })
        pd.testing.assert_frame_equal(result[['order_id', 'contact_address']], expected)

    #### Test case 4:
    def test_calculate_commissions(self):
        result = calculate_commissions(self.orders_data, self.invoices_data)
        expected = pd.DataFrame({
            'salesowner': ['Matt Owner', 'Alice Owner', 'Charlie Owner', 'Michael Owner', 'Bob Owner', 'Jack Owner'],
            'commission': [19.40, 18.49, 18.24, 15.00, 13.39, 7.54]
        })
        pd.testing.assert_frame_equal(result[['salesowner', 'commission']], expected)
        
        expected_order = [19.40, 18.49, 18.24, 15.00, 13.39, 7.54]  
        self.assertListEqual(result['commission'].tolist(), expected_order)

    #### Test case 5:
    def test_salesowners_sorted(self):
        result = create_company_salesowners_df(self.orders_data)
        for owners in result['list_salesowners']:
            owners_list = [owner.strip() for owner in owners.split(',')]
            self.assertEqual(owners_list, sorted(owners_list))
            self.assertEqual(len(owners_list), len(set(owners_list)))

        unique_companies = result['company_id'].nunique()
        self.assertEqual(unique_companies, len(result))

if __name__ == '__main__':
    unittest.main()
