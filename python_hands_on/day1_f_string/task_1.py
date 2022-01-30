message = "all is well"

print(message)
print(message.lower())
print(message.upper())
print(message.title())


# Traditional way of other programming languages
print("Amir Khan said " + message.title() + " in 3 Idiots")

# Python's way of doing the same
print(f"Amir Khan said {message.title()} in 3 Idiots")

