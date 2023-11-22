import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email(subject, body, to_email, cc_email=None, bcc_email=None):
    try:
        # Your Outlook email credentials
        smtp_server = 'smtp-mail.outlook.com'
        smtp_port = 587
        username = 'testing@outlook.com'
        password = 'testing'

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach body to the email
        msg.attach(MIMEText(body, 'plain'))

        # Add CC and BCC recipients if provided
        if cc_email:
            msg['Cc'] = cc_email
        if bcc_email:
            msg['Bcc'] = bcc_email

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to your Outlook account
        server.login(username, password)

        # Send the email
        recipients = [to_email]
        if cc_email:
            recipients.append(cc_email)
        if bcc_email:
            recipients.append(bcc_email)

        server.sendmail(username, recipients, msg.as_string())

        # Close the connection
        server.quit()
        print("Email sent successfully!")

    except Exception as e:
        print("Error: ", e)

# Send email with no attachments:
# send_email("Message from outlook 3", "This is a simple email body 3.", "testing@gmail.com","lifihit747@ikanid.com", "behijo8340@marksia.com")


def send_email_with_attachments(subject, body, to_email, cc_email=None, bcc_email=None, attachment_paths=None):
    try:
        # Your Outlook email credentials
        smtp_server = 'smtp-mail.outlook.com'
        smtp_port = 587
        username = 'testing@outlook.com'  # Update with your Outlook username
        password = 'testing'  # Update with your Outlook password

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach body to the email
        msg.attach(MIMEText(body, 'plain'))

        # Add CC and BCC recipients if provided
        if cc_email:
            msg['Cc'] = cc_email
        if bcc_email:
            msg['Bcc'] = bcc_email

        # Attach multiple files if attachment_paths is provided
        if attachment_paths:
            for attachment_path in attachment_paths:
                with open(attachment_path, "rb") as attachment:
                    part = MIMEApplication(attachment.read())
                    part.add_header('Content-Disposition', 'attachment', filename=attachment_path)
                    msg.attach(part)

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to your Outlook account
        server.login(username, password)

        # Send the email
        recipients = [to_email]
        if cc_email:
            recipients.append(cc_email)
        if bcc_email:
            recipients.append(bcc_email)

        server.sendmail(username, recipients, msg.as_string())

        # Close the connection
        server.quit()
        print("Email with attachments sent successfully!")

    except Exception as e:
        print("Error: ", e)



# Send email with one attachment
# attachment_path_single = ["attachment1.txt"]
# send_email_with_attachments("Test Subject", "This is a simple email body with one attachment.", "testing@gmail.com", cc_email="cc@example.com", attachment_paths=attachment_path_single)

# Send email with multiple attachments
# attachment_paths_multiple = ["attachment1.txt", "attachment2.txt"]
# send_email_with_attachments("Test Subject", "This is a simple email body with multiple attachments.", "testing@gmail.com", cc_email="cc@example.com", attachment_paths=attachment_paths_multiple)
