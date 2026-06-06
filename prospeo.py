def find_decision_makers(companies):
    print("\nFinding decision makers...")

    contacts = []

    for company in companies:
        contacts.append({
            "company": company,
            "name": "John Doe",
            "designation": "CEO",
            "linkedin": "https://linkedin.com/in/johndoe"
        })

    return contacts