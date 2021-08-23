
coins = [
    {'weight': 2.5, 'diameter': .75, 'thickness': 1.52, 'value_in_cents': 1, 'valid': False},
    {'weight': 5.0, 'diameter': .835, 'thickness': 1.95, 'value_in_cents': 5, 'valid': True}
]

def identify_coin(weight, diameter, thickness):
    return next((c for c in coins if _compare_dimensions(c, weight, diameter, thickness)), None)


def _compare_dimensions(coin, weight, diameter, thickness):
    return coin['weight'] == weight and coin['diameter'] == diameter and coin['thickness'] == thickness