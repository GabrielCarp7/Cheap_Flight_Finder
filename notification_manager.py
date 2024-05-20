import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, email, password, to_addrs):
        self.email = email
        self.password = password
        self.to_addrs = to_addrs

    def send_email(self, price, from_flight, to_flight, start_date, end_date):
        message = (f"Subject:Flight Notification\n\n Low price alert! Only £{price} to fly from {from_flight} to "
                   f"{to_flight} from {start_date} to {end_date}")

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(from_addr=self.email, to_addrs=self.to_addrs, msg=message.encode('utf-8'))
