from email.message import EmailMessage
import ssl
import smtplib

# Input the Email address of the sender, this would typically be your own Email address.
sender = ""
# Here past the password generated from your Google account as instructed to in the "read me" file.
password = ""

# Input the Email address of the receiver.
receiver = ""

# Here write the subject of the Email. This will appear in the Subject field of the Email.
subject = ""
# Here you write the Email itself.
body = """

"""

email = EmailMessage()
email["From"] = sender
email["To"] = receiver
email["subject"] = subject
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, email.as_string())