import smtplib

sender = "lukamtchedlidze@gmail.com"
receiver = "something@gmail.com"
password = "12345"
subject = "email test"
body = "I wrote an email"

message = f"""From: Michael Jackson{sender}
To: Jamal{receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("unable to sign in")