import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
#Next, log in to the server
server.login("siddharthmishra1537@gmail.com", "**********")

#Send the mail
msg = "type program and text ra rae (-_-)"
server.sendmail("siddharthmishra1537@gmail.com", "thennavanpmohan@gmail.com", msg)
server.quit()
print('Message sent!------------------------------------------------------------')
