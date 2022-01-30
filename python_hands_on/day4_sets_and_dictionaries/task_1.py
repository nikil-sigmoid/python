users = {
    'einstein': {
        'first': 'albert',
        'last': 'einstein',
        'country': 'germany'
    },

    'curie':{
        'first': 'marie',
        'last': 'curie',
        'country': 'italy'
    }
}

for k, v in users.items():
    print(f"Full Name - {v['first'].title()} {v['last'].title()}")
    print(f"Location - {v['country'].title()}")
    print()