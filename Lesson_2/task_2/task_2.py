import json
from datetime import datetime


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json', 'r', encoding='windows-1251') as file:
        orders = json.load(file)['orders']
    orders.append({
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    })
    with open('orders.json', 'w', encoding='windows-1251') as file:
        json.dump({'orders': orders}, file, indent=4, default=str)


for i in range(5):
    write_order_to_json(f'item_{i}', quantity=i, price=100 + i, buyer=f'buyer_{i}', date=datetime.now())
