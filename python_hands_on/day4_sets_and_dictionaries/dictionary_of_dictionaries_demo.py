computers = {
    'dell':{
        'make': 'dell',
        'ram': '8gb',
        'processor_core': 2,
        'hard_disk': '500gb'
    },

    'hp': {
        'make': 'hp',
        'ram': '4gb',
        'processor_core': 3,
        'hard_disk': '1tb'
    }
}

for k, v in computers.items():
    print(f"Make of the computer = {v['make'].title()}")
    print(f"RAM of the computer = {v['ram']}")
    print(f"Number of processor cores = {v['processor_core']}")
    print(f"Hard Disk = {v['hard_disk']}")
    print()