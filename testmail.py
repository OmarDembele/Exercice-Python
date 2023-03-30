from email import message
import smtplib

def automatic_mail():
    user=input('Enter your username: ')
    email_receive=input('Enter your email: ')
    email_sender='omardembele820@gmail.com'
    password='onqgkmpmpbkuyvwn'
    s=smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(email_sender , password)
    message=f"Cher {user}, Bienvenue chez Bems"    
    s.sendmail(email_sender , email_receive, message)
    print('Email Sent')
    
automatic_mail()    
#dembeledjibrildk@gmail.com