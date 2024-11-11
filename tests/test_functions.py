import unittest
import pandas as pd
from src.functions import (
    get_crate_distribution_per_company,
    create_contact_full_name
)

class TestFunctions(unittest.TestCase):

    def setUp(self):
        # Datos de prueba
        self.orders_data = pd.DataFrame({
            'order_id': [1, 2, 3],
            'company': ['Company A', 'Company B', 'Company A'],
            'crate_type': ['Type 1', 'Type 2', 'Type 1'],
            'first_name': ['Alice', None, 'Bob'],
            'last_name': ['Smith', 'Doe', None]
        })

    def test_get_crate_distribution_per_company(self):
        result = get_crate_distribution_per_company(self.orders_data)
        expected = pd.DataFrame({
            'company': ['Company A', 'Company B'],
            'crate_type': ['Type 1', 'Type 2'],
            'order_count': [2, 1]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_create_contact_full_name(self):
        result = create_contact_full_name(self.orders_data)
        expected = pd.DataFrame({
            'order_id': [1, 2, 3],
            'contact_full_name': ['Alice Smith', 'John Doe', 'Bob Doe']
        })
        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()