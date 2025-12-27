import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "ghoulamsoudani@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "ghoulamsoudani@gmail.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
