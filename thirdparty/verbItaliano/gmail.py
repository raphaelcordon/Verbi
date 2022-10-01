from email.message import EmailMessage
from smtplib import SMTP_SSL


class EmailPassword:
    def __init__(self, email_address, name, password):
        msg = EmailMessage()
        msg['Subject'] = 'Verbi, reset de senha'
        msg['From'] = 'Pratica i Verbi'
        msg['To'] = email_address
        msg.set_content(f"Olá {name}.\n\n"
                        f"Sua nova senha é '{password}'.\n "
                        f"Ao se logar no site você será redirecionado para alterá-la.\n\n"
                        )

        with SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('cordonraphael@gmail.com', 'piuxeaxjwrqifhcw')
            smtp.send_message(msg)


class UserEmail:
    def __init__(self, name, email, subject, message):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = f'PracticeTheVerb Talk To us: {name}'
        msg['To'] = 'cordonraphael@gmail.com'
        msg.set_content(f"Sent by:  {name}.\n\n"
                        f"eMail address: '{email}'.\n "
                        f"Message:\n "
                        f"{message}\n\n"
                        )

        with SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('cordonraphael@gmail.com', 'piuxeaxjwrqifhcw')
            smtp.send_message(msg)
