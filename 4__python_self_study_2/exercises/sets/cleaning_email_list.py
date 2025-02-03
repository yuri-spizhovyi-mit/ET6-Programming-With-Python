"""
You have an email list and need to ensure no duplicates
before sending a newsletter"""

emails = [
    "alice@example.com",
    "bob@example.com",
    "alice@example.com",
    "charlie@example.com",
]

unique_emails = list(set(emails))

print("Unique emails: ", unique_emails)
