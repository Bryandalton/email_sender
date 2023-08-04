# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.message import EmailMessage
from string import Template
from pathlib import Path
import os

pw = os.getenv('PASSWORD')

html = Template(Path('index.html').read_text())

msg = EmailMessage()
# the subject line
msg['Subject'] = 'Winner! 1,000,000 Dollhairs!'
# the sender's email address
msg['From'] = 'moonhighowl@gmail.com'
# the recipient's email address
msg['To'] = 'bryantdalton19@gmail.com'
# email content
msg.set_content(html.substitute({'name': 'TinTin'}), 'html')


# Send the message via gmail.
with smtplib.SMTP(host='smtp.gmail.com', port= 587) as smpt:
    smpt.ehlo()
    smpt.starttls()
    smpt.login('moonhighowl@gmail.com', f'{pw}')
    smpt.send_message(msg)
    print('All good boss!')

#future update: import sys and use arg v for name and recipient
