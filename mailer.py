#Made By KunalMannu
#If You Copy Give Me Credits
#Thank You
from mailer import Mailer

mail = Mailer(email='your hotmail account Example:hotkunalmannu@hotmail.com', password='your hotmail password Example:kunalmannuishot')
mail.settings(provider=mail.MICROSOFT)
mail.send(receiver='whom to send Example:hot@hotmail.com',
subject='Your Subject', message='Your Message')

print("Email Sents Succesfuly")
