import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(subject, body, to_email, cc_email=None, bcc_email=None):
    try:
        # Your Gmail email credentials
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        username = 'testing@gmail.com'  # Update with your Gmail username
        password = 'testing app password'  # Update with your Gmail password or App Password

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach body to the email
        msg.attach(MIMEText(body, 'plain'))

        # Add CC and BCC recipients if provided
        if cc_email:
            msg['Cc'] = cc_email.strip()  # Check and strip if cc_email is not None
        if bcc_email:
            msg['Bcc'] = bcc_email.strip()  # Check and strip if bcc_email is not None

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # Login to your Gmail account
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

# Send Email with no attachment:
# send_email("Test Subject", "This is a simple email body.", "tayyabjan3@outlook.com", cc_email="lifihit747@ikanid.com")



def send_email_with_attachments(subject, body, to_email, cc_email=None, bcc_email=None, attachment_paths=None):
    try:
        # Your Gmail email credentials
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        username = 'testing@gmail.com'  # Update with your Gmail username
        password = 'testing app password'  # Update with your Gmail password or App Password

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

        # Login to your Gmail account
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

# Send Email with one attachment:
# attachment_paths = ["attachment1.txt"]
# send_email_with_attachments("Test Subject", "This is a simple email body with attachments.", "tayyabjan3@outlook.com", cc_email="lifihit747@ikanid.com", attachment_paths=attachment_paths)

# Send Email with multiple attachment:
# attachment_paths = ["attachment1.txt", "attachment2.txt"]
# send_email_with_attachments("Test Subject", "This is a simple email body with attachments.", "tayyabjan3@outlook.com", cc_email="lifihit747@ikanid.com", bcc_email="mtaeyyab15@gmail.com", attachment_paths=attachment_paths)