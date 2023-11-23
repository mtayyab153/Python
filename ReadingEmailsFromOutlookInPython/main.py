from threading import Timer
import win32com.client
import pythoncom  # Add this import

# Get Outlook application object
outlook_app = win32com.client.Dispatch("Outlook.Application")

# Get the MAPI namespace
namespace = outlook_app.GetNamespace("MAPI")

def get_all_emails():
    # Get the Inbox folder
    inbox = namespace.GetDefaultFolder(6)  # 6 corresponds to the Inbox folder

    # get all messages
    messages = inbox.Items

    # Access and print email subjects
    for message in messages:
        print("============START============")
        print("Subject: ", message.Subject)
        print("Sender Email: ", message.SenderEmailAddress)
        print("Email Body: ", message.Body)
        print("Received Time: ", message.ReceivedTime)
        for attachment in message.Attachments:
            print("Attachment:", attachment.FileName)
        print("============END============\n")

def get_email_from_specific_sender(sender_email):
    inbox = namespace.GetDefaultFolder(6)  # 6 corresponds to the Inbox folder

    # Filter and print emails from a specific sender
    sender_email = sender_email
    for item in inbox.Items:
        if item.Class == 43 and item.SenderEmailAddress.lower() == sender_email.lower():  # 43 corresponds to MailItem class
            print("============START============")
            print("Subject:", item.Subject)
            print("Body:", item.Body)
            print("Received Time:", item.ReceivedTime)
            print("============END============\n")

def get_emails_with_specific_subject(email_subject):
    inbox = namespace.GetDefaultFolder(6)  # 6 corresponds to the Inbox folder

    # Search for emails with a specific subject
    search_subject = email_subject
    for item in inbox.Items:
        if item.Class == 43 and item.Subject.lower() == search_subject.lower():  # 43 corresponds to MailItem class
            print("============START============")
            print("Subject:", item.Subject)
            print("Body:", item.Body)
            print("Received Time:", item.ReceivedTime)
            print("============END============\n")

def get_unread_emails():
    inbox = namespace.GetDefaultFolder(6)  # 6 corresponds to the Inbox folder

    # Filter unread emails
    unread_emails = [item for item in inbox.Items if item.UnRead]

    # Print information about unread emails
    for email in unread_emails:
        print("Subject:", email.Subject)
        print("Body:", email.Body)
        print("Received Time:", email.ReceivedTime)
        print("Sender:", email.SenderName)
        print("----")

def get_unread_emails_from_specific_sender(sender_email):
    # Get the Inbox folder
    inbox = namespace.GetDefaultFolder(6)  # 6 corresponds to the Inbox folder

    # Specify the email address of the specific sender
    target_sender_email = sender_email

    # Filter unread emails from the specific sender
    unread_emails_from_sender = [item for item in inbox.Items if
                                 item.UnRead and item.SenderEmailAddress.lower() == target_sender_email.lower()]

    # Print information about unread emails from the specific sender
    for email in unread_emails_from_sender:
        print("Subject:", email.Subject)
        print("Received Time:", email.ReceivedTime)
        print("Sender:", email.SenderName)
        print("----")
def forward_unread_emails_from_specific_sender(from_sender, to_receiver, file_path="forwarded_emails.txt"):
    try:
        # Initialize the COM library
        pythoncom.CoInitialize()

        # Create Outlook Application object
        outlook_app = win32com.client.Dispatch("Outlook.Application")
        namespace = outlook_app.GetNamespace("MAPI")

        # Get the Inbox folder
        inbox = namespace.GetDefaultFolder(6)  # 6 corresponds to the Inbox folder

        # Load previously forwarded email IDs
        try:
            with open(file_path, "r") as file:
                forwarded_email_ids = set(file.read().splitlines())
        except FileNotFoundError:
            forwarded_email_ids = set()

        # Filter unread emails from the specific sender
        unread_emails_from_sender = [item for item in inbox.Items if
                                     item.UnRead and item.SenderEmailAddress.lower() == from_sender.lower()]

        # Forward unread emails to the specific receiver
        for email in unread_emails_from_sender:
            # Check if the email has been forwarded
            is_forwarded = email.UserProperties("IsForwarded")
            if not is_forwarded:
                # Mark the email as forwarded
                email.UserProperties.Add("IsForwarded", True)
                email.Save()

                # Forward the email
                forwarded_email = email.Forward()
                forwarded_email.To = to_receiver
                forwarded_email.Send()

                forwarded_email_ids.add(email.EntryID)
                print(f"Email sent: Subject - {email.Subject}")
            else:
                print(f"Email not sent: Already forwarded - Subject - {email.Subject}")

        # Save updated forwarded email IDs
        with open(file_path, "w") as file:
            file.write("\n".join(forwarded_email_ids))

        # Schedule the next execution after 1 second
        Timer(1, forward_unread_emails_from_specific_sender, (from_sender, to_receiver, file_path)).start()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# get_all_emails()
# get_email_from_specific_sender("testing@gmail.com")
# get_emails_with_specific_subject("hi")
# get_unread_emails()
# get_unread_emails_from_specific_sender("mtaeyyab15@gmail.com")
# forward_unread_emails_from_specific_sender("testing@gmail.com", "testing@gmail.com")