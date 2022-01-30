bikes = ['honda', 'yamaha', 'suzuki', 'bajaj', 'ducati', 'duke', 'bmw', 'kawasaki']

print(bikes)
print(bikes[1:4])
print(bikes[:4])
print(bikes[2:])

new_bikes = bikes[:]
new_bikes.append('tvs')
print(new_bikes)