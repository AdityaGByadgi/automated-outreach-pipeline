from ocean import find_similar_companies
from prospeo import find_decision_makers
from eazyreach import find_emails
from brevo import send_emails


def main():
    # Step 1 - Input
    domain = input("Enter company domain: ")

    # Step 2 - Similar companies
    companies = find_similar_companies(domain)

    print("\n=== Similar Companies Found ===")
    for company in companies:
        print(company)

    # Step 3 - Decision makers
    contacts = find_decision_makers(companies)

    print("\n=== Decision Makers Found ===")
    for contact in contacts:
        print(
            f"{contact['name']} | "
            f"{contact['designation']} | "
            f"{contact['company']}"
        )

    # Step 4 - Emails
    contacts = find_emails(contacts)

    print("\n=== Emails Found ===")
    for contact in contacts:
        print(
            f"{contact['name']} | "
            f"{contact['email']}"
        )

    # Safety Checkpoint
    print("\n===================================")
    print("SUMMARY")
    print("===================================")
    print(f"Companies Found: {len(companies)}")
    print(f"Contacts Found : {len(contacts)}")

    choice = input(
        "\nDo you want to send emails? (yes/no): "
    ).lower()

    if choice == "yes":
        send_emails(contacts)
    else:
        print("\nEmail sending cancelled.")


if __name__ == "__main__":
    main()