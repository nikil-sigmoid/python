favourite_languages = {
    'ram': 'java',
    'tim': 'c',
    'sam': 'python',
    'brad': 'ruby'
}

language = favourite_languages['tim'].title()
print(f"Tim's favourite language is {language}")

del favourite_languages['brad']

print(favourite_languages)

second_language = favourite_languages.get('tim', "nice")
print(second_language)

for k, v in favourite_languages.items():
    print(f"{k.title()}'s favourite language is {v.title()}")
