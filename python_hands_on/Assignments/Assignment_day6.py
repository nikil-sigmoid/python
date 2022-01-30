# Q1
def show_messages(messages):
    for message in messages:
        print(message)


text_messages = ["Good Morning!", "How are you doing?", "Thank you!", "Bye-Bye", "All is Well"]
show_messages(text_messages)
print()

# Q2
sent_messages = []


def send_messages(messages):
    for message in messages:
        print(message)
        sent_messages.append(message)


send_messages(text_messages)
print(text_messages)
print(sent_messages)
