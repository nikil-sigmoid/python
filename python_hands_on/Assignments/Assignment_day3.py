cars = {
    'bmw': 'germany',
    'suzuki': 'japan',
    'mercedes': 'germany',
    'porsche': 'germany',
    'tesla': 'usa',
    'ferrari': 'italy'
}

countries = ['usa', 'japan', 'italy']
for k, v in cars.items():
    if v in countries:
        print(f"{k.title()} brand lies in {v.title()}.")
