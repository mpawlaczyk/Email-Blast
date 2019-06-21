import smtplib, ssl

email = ""
passwd = ""

with open("config.txt") as cfg_file:
    for line in cfg_file:
        if "email" in line:
            email = line.split(":")[1].strip(" ")
            print email
        if "passwd" in line:
            passwd = line.split(":")[1].strip(" ")
            print passwd
