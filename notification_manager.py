import smtplib


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.mail = <mail>
        self.password = <password>
        self.connection = smtplib.SMTP('smtp.gmail.com', port=587)
        self.connection.starttls()
        self.connection.login(user=self.mail, password=self.password)

    def send_mail(self, to_mail, mail_subject, mail_content):
        self.connection.sendmail(from_addr=self.mail, to_addrs=to_mail, msg=f'Subject:{mail_subject}\n\n{mail_content}')

    def close_connection(self):
        self.connection.close()
