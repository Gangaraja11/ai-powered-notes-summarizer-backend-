import smtplib
import os
from email.mime.text import MIMEText

def send_email(recipient, summary):
    try:
        sender_email = os.getenv("EMAIL_USER")
        sender_pass = os.getenv("EMAIL_PASS")

        msg = MIMEText(summary, "plain")
        msg["Subject"] = "Meeting Summary"
        msg["From"] = sender_email
        msg["To"] = recipient

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_pass)
            server.sendmail(sender_email, recipient, msg.as_string())
        return True
    except Exception as e:
        print("Email error:", e)
        return False