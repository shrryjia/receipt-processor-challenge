import math
from datetime import datetime

def calculate_points(receipt):
    points = 0

    # One point for every alphanumeric character in the retailer name
    retailer_name = receipt.get('retailer', '')
    points += sum(c.isalnum() for c in retailer_name)

    # 50 points if the total is a round dollar amount with no cents
    total = float(receipt.get('total', 0))
    if total.is_integer():
        points += 50

    # 25 points if the total is a multiple of 0.25
    if total % 0.25 == 0:
        points += 25

    # 5 points for every two items on the receipt
    num_items = len(receipt.get('items', []))
    points += (num_items // 2) * 5

    # Points for item descriptions and their prices
    for item in receipt.get('items', []):
        description = item.get('shortDescription', '').strip()
        if len(description) % 3 == 0:
            item_price = float(item.get('price', 0))
            points += math.ceil(item_price * 0.2)

    # 6 points if the day in the purchase date is odd
    purchase_date_str = receipt.get('purchaseDate', None)
    if purchase_date_str:
        purchase_date = datetime.strptime(purchase_date_str, '%Y-%m-%d')
        if purchase_date.day % 2 == 1:
            points += 6

    # 10 points if the time of purchase is after 2:00pm and before 4:00pm
    purchase_time_str = receipt.get('purchaseTime', None)
    if purchase_time_str:
        purchase_time = datetime.strptime(purchase_time_str, '%H:%M').time()
        if purchase_time >= datetime.strptime('14:00', '%H:%M').time() and \
            purchase_time <= datetime.strptime('16:00', '%H:%M').time():
            points += 10

    return points