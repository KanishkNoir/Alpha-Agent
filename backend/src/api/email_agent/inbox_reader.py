import os
from api.email_agent.gmail_parser import GmailImapParser


EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def read_inbox(hours_ago:int = 24, unread:bool = True, verbose=False):
    parser = GmailImapParser(
        email_address = EMAIL_ADDRESS,
        app_password = EMAIL_PASSWORD)

    emails = parser.fetch_emails(
        hours=hours_ago,
        unread_only=unread)

    for email in emails:
        print(f"From: {email['from']}")
        print(f"Subject: {email['subject']}")
        print(f"Date: {email['timestamp']}")
        print("--------------------------------")

    return emails









