import smtplib
from config import EMAIL, EMAIL_PASSWORD

def send_email(to_email, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, EMAIL_PASSWORD)

    server.sendmail(EMAIL, to_email, message)
    server.quit()