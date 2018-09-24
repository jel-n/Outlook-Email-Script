# ------ REQUIREMENTS ------ #
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

recipient_address = []
file = open('FILE').readlines()
for item in file:
    recipient_address.append(item)

for a in recipient_address:
    # ------ CREDENTIALS ------ #
    sender_address = "sender address"
    sender_password = "sender password"

    # ------ RECIPIENT(S) ------ #
    recipient_address = a

    # Subject for the email
    subject = 'This was sent via a Python Script'

    # Main content of the email
    body = 'This is a test'

    msg = MIMEMultipart()
    msg['From']=sender_address
    msg['To']=recipient_address
    msg['Subject']=subject

    # Creates a plaintext message
    msg.attach(MIMEText(body, 'plain'))

    email_content = msg.as_string()

    server = smtplib.SMTP('MAIL GATEWAY:PORT')

    # Puts the SMTP connection in TLS mode
    # All SMTP commands that follow will be encrypted
    server.starttls()

    # Log in on an SMTP server that require authentication
    # Arguments are the username and password
    server.login(sender_address, sender_password)

    # Send the email, pass the sender, recipient, and contents of the email
    server.sendmail(sender_address, recipient_address, email_content)

# Break the connection to the server
server.quit()
