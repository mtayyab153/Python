import imaplib
import email
from email.header import decode_header
import os

def read_all_emails(username, password):
    # Connect to Gmail's IMAP server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")

    # Login to your Gmail account
    mail.login(username, password)

    # Select the mailbox you want to read (e.g., "inbox")
    mail.select("inbox")

    # Search for all emails in the selected mailbox
    status, messages = mail.search(None, "ALL")

    if status == "OK":
        # Get the list of email IDs
        email_ids = messages[0].split()

        # Loop through the email IDs and fetch the corresponding emails
        for email_id in email_ids:
            # Fetch the email by ID
            _, msg_data = mail.fetch(email_id, "(RFC822)")

            # Parse the email content
            msg = email.message_from_bytes(msg_data[0][1])

            # Extract email details (e.g., subject, sender, date)
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")

            sender, encoding = decode_header(msg.get("From"))[0]
            if isinstance(sender, bytes):
                sender = sender.decode(encoding or "utf-8")

            date = msg["Date"]

            # Print email details
            print(f"Subject: {subject}")
            print(f"From: {sender}")
            print(f"Date: {date}")

            # Print the email body
            # print("Body:")
            # body = get_email_body(msg)
            # print(body)

            # Print attachments
            # print("Attachments:")
            # print_attachments(msg)

            print("")

    # Logout from the Gmail account
    mail.logout()

def get_email_body(msg):
    """Get the plain text body of the email."""
    body = ""

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                break
    else:
        body = msg.get_payload()

    return body

def print_attachments(msg):
    """Print information about attachments and download them."""
    for part in msg.walk():
        if part.get_content_maintype() == "multipart" or part.get("Content-Disposition") is None:
            continue

        filename = part.get_filename()
        if filename:
            print(f"Attachment: {filename}")
            # download_attachment(part)

def download_attachment(part):
    """Download and save the attachment."""
    filename = part.get_filename()

    if filename:
        with open(filename, "wb") as f:
            f.write(part.get_payload(decode=True))


def read_unread_emails(username, password):
    # Connect to Gmail's IMAP server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")

    # Login to your Gmail account
    mail.login(username, password)

    # Select the mailbox you want to read (e.g., "inbox")
    mail.select("inbox")

    # Search for unread emails in the selected mailbox
    status, messages = mail.search(None, "(UNSEEN)")

    if status == "OK":
        # Get the list of email IDs for unread emails
        email_ids = messages[0].split()

        # Loop through the email IDs and fetch the corresponding unread emails
        for email_id in email_ids:
            # Fetch the email by ID
            _, msg_data = mail.fetch(email_id, "(RFC822)")

            # Parse the email content
            msg = email.message_from_bytes(msg_data[0][1])

            # Extract email details (e.g., subject, sender, date)
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")

            sender, encoding = decode_header(msg.get("From"))[0]
            if isinstance(sender, bytes):
                sender = sender.decode(encoding or "utf-8")

            date = msg["Date"]

            # Print email details
            print(f"Subject: {subject}")
            print(f"From: {sender}")
            print(f"Date: {date}")

            # Print the email body
            # print("Body:")
            # body = get_email_body(msg)
            # print(body)

            # Print attachments
            # print("Attachments:")
            # print_attachments(msg)

            print("")

    # Logout from the Gmail account
    mail.logout()


def read_emails_from_sender(username, password, sender_email):
    # Connect to Gmail's IMAP server
    mail = imaplib.IMAP4_SSL("imap.gmail.com")

    # Login to your Gmail account
    mail.login(username, password)

    # Select the mailbox you want to read (e.g., "inbox")
    mail.select("inbox")

    # Search for unread emails from the specific sender in the selected mailbox
    status, messages = mail.search(None, '(UNSEEN FROM "{0}")'.format(sender_email))

    if status == "OK":
        # Get the list of email IDs for unread emails from the specific sender
        email_ids = messages[0].split()

        # Loop through the email IDs and fetch the corresponding unread emails
        for email_id in email_ids:
            # Fetch the email by ID
            _, msg_data = mail.fetch(email_id, "(RFC822)")

            # Parse the email content
            msg = email.message_from_bytes(msg_data[0][1])

            # Extract email details (e.g., subject, sender, date)
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")

            sender, encoding = decode_header(msg.get("From"))[0]
            if isinstance(sender, bytes):
                sender = sender.decode(encoding or "utf-8")

            date = msg["Date"]

            # Print email details
            print(f"Subject: {subject}")
            print(f"From: {sender}")
            print(f"Date: {date}")

            # Print the email body
            # print("Body:")
            # body = get_email_body(msg)
            # print(body)

            # Print attachments
            # print("Attachments:")
            # print_attachments(msg)

            print("")

    # Logout from the Gmail account
    mail.logout()

# Replace 'YOUR_EMAIL' and 'YOUR_PASSWORD' with your Gmail credentials
# read_all_emails('YOUR_EMAIL', 'YOUR_PASSWORD')
# read_unread_emails('YOUR_EMAIL', 'YOUR_PASSWORD')
# read_emails_from_sender('YOUR_EMAIL', 'YOUR_PASSWORD', 'sender email')
