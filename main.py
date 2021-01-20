import requests,smtplib
import datetime as dt
evil=requests.get(url='https://evilinsult.com/generate_insult.php?lang=en&type=json')
data=evil.json()
insult=data['insult']
# print(insult)
mail='YOUR_MAIL.'
password='YOUR_PASSWORD'
connection=smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=mail,password=password)
# connection.sendmail(from_addr=mail,to_addrs='RECIEVING_MAIL',msg=f"Subject: Just a sweet insult\n\n{insult}")
# connection.sendmail(from_addr=mail,to_addrs='RECIEVING_MAIL',msg=f"Subject: Just a sweet insult\n\n{insult}")
# connection.sendmail(from_addr=mail,to_addrs='RECIEVING_MAIL',msg=f"Subject: Just a sweet insult\n\n{insult}")
# connection.sendmail(from_addr=mail,to_addrs='RECIEVING_MAIL',msg=f"Subject: Just a sweet insult\n\n{insult}")
connection.sendmail(from_addr=mail,to_addrs='RECIEVING_MAIL',msg=f'Subject:Just a sweet insult\n\n{insult}')
