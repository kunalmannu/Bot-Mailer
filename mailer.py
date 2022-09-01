from mailer import Mailer

mail = Mailer(email='your hotmail account', password='your hotmail password')
mail.settings(provider=mail.MICROSOFT)
mail.send(receiver='whom to send',
subject='Your Subject', message='Your Message')

print("Email Sents Succesfuly")
