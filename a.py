import smtplib
import getpass
content=input("enter the text to enter in mail:")
a=input("your mail address:")
b=getpass.getpass("your password:")
c=input("recievers mail address:")
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(a,b)
mail.sendmail(a,c,content)
mail.close()
