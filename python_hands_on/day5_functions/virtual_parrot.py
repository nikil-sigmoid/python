prompt = "Please enter something: "
active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)