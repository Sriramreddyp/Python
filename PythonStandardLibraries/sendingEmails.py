from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message["from"] = "Sriram Reddy"
message["to"] = "sriramreddyp123@gmail.com"
message["Subject"] = "Test Mail Automation"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("sriramreddyp123@gmail.com", "sriramaaram123")
    smtp.send_message(message)
    print("Sent....")
