import smtplib
from email.mime.text import MIMEText

carriers = {
    'att': '@mms.att.net',
    'tmobile': '@tmomail.net',
    'verizon': '@vtext.com',
    'sprint': '@messaging.sprintpcs.com'
}


def send(auth, message, subject, address):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = auth[0]
    msg["To"] = address

    # Establish a secure session with gmail's outgoing SMTP
    # server using your gmail account
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])

    # Sends the message
    server.send_message(msg)


def send_text(auth, message, subject, number, carrier):
    to_number = number + carriers[carrier]
    print('Sending test to %s' % to_number)
    send(auth, message, subject, to_number)


def send_email(auth, message, subject, address):
    print('Sending email to %s' % address)
    send(auth, message, subject, address)
