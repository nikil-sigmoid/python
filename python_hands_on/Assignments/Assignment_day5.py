def print_dictionary(mob_os):
    for k, v in mob_os.items():
        print(f"OS- {k}, Mobile- {v}")


mobile_os = {
    'android': 'samsung',
    'iOS': 'apple',
    'windows': 'microsoft',
    'symbian': 'nokia'
}

print_dictionary(mobile_os)