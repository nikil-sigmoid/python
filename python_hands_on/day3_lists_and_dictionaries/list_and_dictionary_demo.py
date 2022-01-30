
favourite_languages = {
    'ram': 'java',
    'tim': 'c',
    'sam': ['python', 'c#', 'go', 'java'],
    'brad': 'ruby'
}

for k, v in favourite_languages.items():
    if(type(v) == list):
        print(f"Favourite languages of {k.title()} are -")
        for lang in v:
            print(lang)
    else:
        print(f"Favourite language of {k.title()} is - {v.title()}")