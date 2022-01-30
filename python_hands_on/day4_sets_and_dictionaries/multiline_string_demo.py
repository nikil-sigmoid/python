message = """Today is Monday 
And tomorrow will be Tuesday
And then it will be Wednesday"""

message = "Do good find good"
for character in message:
    print(character)

print(message[3])

print(f"Total number of characters = {len(message)}")

# count() gives number of times a particular item repeats

bikes = ['honda', 'yamaha', 'suzuki', 'bajaj']
number = bikes.count('bajaj')
print(number)

bikes.append('bajaj')
number = bikes.count('bajaj')
print(number)