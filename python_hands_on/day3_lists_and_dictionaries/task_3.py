usernames = ['Tim23', 'John264', 'admin', 'Ron34', 'Alice12']

if usernames:
    for user in usernames:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thankyou for logging in again.")
else:
    print("We need to find some users")