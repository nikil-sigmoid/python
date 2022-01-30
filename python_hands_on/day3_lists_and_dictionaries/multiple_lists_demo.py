bikes_in_showroom1 = ['yamaha', 'tvs', 'bajaj']
bikes_in_showroom2 = ['ducati', 'duke', 'yamaha', 'bmw', 'bajaj']

for bike in bikes_in_showroom1:
    if bike in bikes_in_showroom2:
        print(f"Bike {bike.title()} is present in both the showrooms")