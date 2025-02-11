import smtplib
import os  

email = input("Sender email: ")
receiver_email = input("Receiver email: ")
subject = input("Subject: ")
message = input("Message: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

email_api_key = os.getenv("GMAIL_APP_PASSWORD") 

if not email_api_key:
    print("Error: GMAIL_APP_PASSWORD is not available")
    exit()

server.login(email, email_api_key)

server.sendmail(email, receiver_email, text)

server.quit()

print(f"Email has been sent successfully to {receiver_email}")
