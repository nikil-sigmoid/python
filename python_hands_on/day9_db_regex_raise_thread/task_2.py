import re

foul_words = ['Monday', 'Tuesday', 'Youday', 'Anyday', 'Friday', 'Someotherday', 'Isday', 'Areday']

email = "Today is monday"
email_lower = email.lower()

flag = True

for word in foul_words:
    if re.search(word.lower(), email_lower):
        print("Your email has been blocked.")
        flag = False
        break

if flag:
    print("Message sent")

