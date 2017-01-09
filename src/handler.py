def handle(event, context):
    if event['city'].lower() == 'boulder city':
        return {
            'freeShipping': False,
            'shippingCost': 10
        }
    elif event['subtotal'] >= 40:
        return {
            'freeShipping': True,
            'shippingCost': 0
        }
    else:
        return {
            'freeShipping': False,
            'shippingCost': 5
        }
