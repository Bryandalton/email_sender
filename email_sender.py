# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.message import EmailMessage
from string import Template
from pathlib import Path
from dotenv import load_dotenv
import sys
import os

load_dotenv()

sender= os.getenv('SENDER_EMAIL')

html = Template(Path('index.html').read_text())

msg = EmailMessage()
# the subject line
msg['Subject'] = 'Winner! 1,000,000 Dollhairs!'
# the sender's email address
msg['From'] = sender
# the recipient's email address
msg['To'] = sys.argv[1]
# email content
msg.set_content(html.substitute({'name': sys.argv[2]}), 'html')


# Send the message via gmail.
with smtplib.SMTP(host='smtp.gmail.com', port= 587) as smpt:
    smpt.ehlo()
    smpt.starttls()
    smpt.login(sender, os.getenv('PASSWORD'))
    smpt.send_message(msg)
    print('Emails Sent!')
