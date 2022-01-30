try:
    first_number = int(input("Please enter a number: "))
    second_number = int(input("Please enter another number: "))
    print(f"Result of division of {first_number} by {second_number} = {first_number / second_number}")
except ZeroDivisionError:
    print("Please do not enter a zero in the denominator.")
except ValueError:
    print("Only integer values are allowed. Please don't enter any other input.")

# All other exceptions other than specific mentioned above
except:
    print("Please enter a valid input.")

# Executed only if no exception is thrown by try block
else:
    print("No exception occurred. That calls for a party")

# Code written under finally block is always executed whether an exception occurs or not
finally:
    print("Close the DB connection.")