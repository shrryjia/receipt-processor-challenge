import unittest
from utils import calculate_points

class TestCalculatePoints(unittest.TestCase):

    def test_retailer_name_points(self):
        receipt = {"retailer": "Wholefoods", "items": [], "total": "0.01"}
        points = calculate_points(receipt)
        # Assuming 'Wholefoods' earns 10 points
        self.assertEqual(points, 10)  

    def test_total_round_dollar_amount(self):
        receipt = {"retailer": "", "items": [], "total": "100"}
        points = calculate_points(receipt)
        # 50 points for round dollar amount + 25 points for being a multiple of 0.25
        self.assertEqual(points, 75)  

    def test_total_multiple_of_25_cents(self):
        receipt = {"retailer": "", "items": [], "total": "10.25"}
        points = calculate_points(receipt) 
        # 25 points for being a multiple of 0.25
        self.assertEqual(points, 25)  

    def test_points_for_items(self):
        receipt = {"retailer": "", "items": [
            {"shortDescription": "a" * 3, "price": "5"}
            ], "total": "0.01"}
        points = calculate_points(receipt)
        # 1 points for one item with description length multiple of 3
        self.assertEqual(points, 1)  

    def test_odd_day_points(self):
        receipt = {"retailer": "", "items": [], 
            "purchaseDate": "2022-03-21", "total": "0.01"}
        points = calculate_points(receipt)
        # 6 points for an odd day
        self.assertEqual(points, 6)

    def test_even_day_points(self):
        receipt = {"retailer": "", "items": [], 
            "purchaseDate": "2022-03-22", "total": "0.01"}
        points = calculate_points(receipt)
        # 0 points for an even day
        self.assertEqual(points, 0)

    def test_purchase_time_points(self):
        receipt = {"retailer": "", "items": [], 
            "purchaseTime": "14:30", "total": "0.01"}
        points = calculate_points(receipt)
        # 10 points for purchase time between 2:00pm and 4:00pm
        self.assertEqual(points, 10)

if __name__ == '__main__':
    unittest.main()
