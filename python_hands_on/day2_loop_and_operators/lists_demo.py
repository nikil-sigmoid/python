bikes = ['honda', 'yamaha', 'suzuki', 'bajaj']

print(bikes[0])
print(bikes)

bikes.append('ducati') # append at the end

bikes.insert(1, 'tvs') # insert at specific position
print(bikes)

del bikes[-2]  # removing the 2nd list item

removed_bike = bikes.pop()
print(removed_bike)

