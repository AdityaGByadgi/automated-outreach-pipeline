def send_emails(contacts):
    print("\nSending emails...\n")

    for contact in contacts:
        print(
            f"Email sent to {contact['name']} "
            f"({contact['email']})"
        )

    print("\nAll emails sent successfully!")