from requests.api import get
import zerosms
import getpass
def sms_send() :
    u = getpass.getpass("Enter Username : ")
    p = getpass.getpass("Enter Password : ")
    msg = input("Message : ")
    to = getpass.getpass("Send to : ")
    zerosms.sms(phno = u, passwd = p, message = msg, receivernum = to)

sms_send()