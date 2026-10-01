import ipadress
import socket


while True:
    target = int(input("enter the targetted ip_address or press (q) to quite"))

    if target.lower() == q:
       print("program ended")
        break
    try:
        ipadress = ipadress.ip_adress(target)
        print(target , "is a valid ipadress")
    except:
        print(target "is not a valid ipaddress")
        print("please enter a valid ipaddress ")
