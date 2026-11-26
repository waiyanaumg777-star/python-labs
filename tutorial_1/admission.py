age = int(input("Enter your age: "))
is_accompanied = input("Are you accompanied by an adult? (yes/no): ").strip().lower() == "yes"
has_ticket = input("Do you have a valid ticket? (yes/no): ").strip().lower() == "yes"

is_allowed_entry = (age >= 13 or is_accompanied) and has_ticket

if is_allowed_entry:
    print("Admission Allowed")
else:
    print("Admission Denied")
