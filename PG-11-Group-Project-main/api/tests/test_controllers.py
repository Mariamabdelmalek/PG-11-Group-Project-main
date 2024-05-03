import unittest
from unittest.mock import MagicMock
from sqlalchemy.orm import Session
import Customers.controllers
from Customers.models import Customers


class TestCustomerController(unittest.TestCase):

    def setUp(self):
        self.db_session = MagicMock(spec=Session)

    def test_create_customer(self):
        # Mocking add and commit methods of session
        self.db_session.add.return_value = None
        self.db_session.commit.return_value = None

        new_customer = create_customer(
            self.db_session, name="Test Name", email="test@example.com",
            phone_number="123456789", address="Test Address"
        )

        self.assertIsInstance(new_customer, Customers)

    def test_read_customer(self):
        # Mocking query method of session
        self.db_session.query().filter().first.return_value = Customers(
            customer_id=1, name="Test Name", email="test@example.com",
            phone_number="123456789", address="Test Address"
        )

        customer = read_customer(self.db_session, 1)
        self.assertEqual(customer.customer_id, 1)

    # Similar tests for other controller functions


if __name__ == '__main__':
    unittest.main()
