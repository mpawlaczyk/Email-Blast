import smtplib, ssl

# credential setup from config file
email = ""
passwd = ""
with open("config.txt") as cfg_file:
    for line in cfg_file:
        if "email" in line:
            email = line.split(":")[1].strip(" ")
        if "passwd" in line:
            passwd = line.split(":")[1].strip(" ")

# mail server setup
port = 465
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp.gmail.com, port, context=context) as mail_server:
    mail_server.login(email, passwd)
    
