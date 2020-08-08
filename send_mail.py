import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("sender_mailid","password")
message="message_to_be_sent"
s.sendmail=("sender_mailid","receiver_mailid",message)
s.quit()
