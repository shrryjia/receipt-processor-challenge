import unittest
import json

from main import app

class FlaskApiTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_process_receipt_endpoint(self):
        # Example receipt data
        receipt_data = {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6.49"
                },{
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
                },{
                "shortDescription": "Knorr Creamy Chicken",
                "price": "1.26"
                },{
                "shortDescription": "Doritos Nacho Cheese",
                "price": "3.35"
                },{
                "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
                "price": "12.00"
                }
            ],
            "total": "35.35"
        }
        response = self.app.post('/receipts/process', data=json.dumps(receipt_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', json.loads(response.data))

    def test_get_points_endpoint(self):
        # Assuming you have a utility to add a receipt and get its ID
        receipt_id = self.add_receipt_get_id()
        response = self.app.get(f'/receipts/{receipt_id}/points')
        self.assertEqual(response.status_code, 200)
        # Ensure the response contains expected keys
        data = json.loads(response.data)
        self.assertIn('id', data)
        self.assertIn('points', data)

    # Additional fixture to add a receipt and get its ID
    def add_receipt_get_id(self):
        # This method would add a receipt and returning its ID for testing
        receipt_data = {
            "retailer": "Trade Joes",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "items": [
                {
                "shortDescription": "Mountain Dew 12PK",
                "price": "6.49"
                },{
                "shortDescription": "Emils Cheese Pizza",
                "price": "12.25"
                }
            ],
            "total": "18.84"
        }
        response = self.app.post('/receipts/process', 
            data=json.dumps(receipt_data), content_type='application/json')
        data = json.loads(response.data)
        return data["id"]

if __name__ == '__main__':
    unittest.main()
