def find_emails(contacts):
    print("\nFinding email addresses...")

    for contact in contacts:
        name = contact["name"].lower().replace(" ", ".")
        company = contact["company"].split(".")[0]

        contact["email"] = f"{name}@{company}.com"

    return contacts