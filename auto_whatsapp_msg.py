import pywhatkit as pyw
import datetime

phone = input("Enter Reciver Number  With Country Code +91 = ")
message = input("Enter Your Message = ")
time_hour = int(input("send message on which Hour  in 24 hou"
                      "r formate \'like 22\' = "))
time_min = int(input("send message on which min \'like 20\' = "))
if time_hour < datetime.datetime.now().hour and time_min < datetime.datetime.now().minute:
    print("--------------------- - Wrong Timing -------------------------")
pyw.sendwhatmsg(phone,message,time_hour,time_min)

print("successfully send message ")