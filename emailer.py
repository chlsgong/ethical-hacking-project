import smtplib

user = "myethicalproject"
password = "easypasswor"
toaddr = "jsvangeffencrap@gmail.com"
subject = "Just another test message"
body = "Just another test message"

sendMail(user, password, toaddr, subject, body)

def sendMail(user, password, toaddr, subject, body):

  usermail = user + "@gmail.com"

  msg = "\r\n".join([
    "From: " + user + "@gmail.com",
    "To: " + toaddr,
    "Subject: " + subject,
    "",
    body
    ])

  server = smtplib.SMTP("smtp.gmail.com:587")
  server.ehlo()
  server.starttls()
  server.login(usermail,password)
  server.sendmail(usermail, toaddr, msg)
  server.quit()

