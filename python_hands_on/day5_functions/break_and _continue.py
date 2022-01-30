# Example of break

prompt = "Please enter something: "
active = True

while active:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)


# Example of continue

prompt = "Please enter something: "
active = True

while active:
    message = input(prompt)
    if message != 'quit':
        print(message)
        continue
    else:
        active = False