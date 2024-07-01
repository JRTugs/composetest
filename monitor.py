import requests
import smtplib
from email.mime.text import MIMEText
import time

# Function to send email
def send_email(subject, message):
    sender_email = "your_email@example.com"  # Replace with your email address
    receiver_email = "your_email@example.com"      # Replace with the admin's email address
    password = "your_email_password"          # Replace with your email password

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Replace with your SMTP server address and port
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")

# Function to check the web application
def check_webapp(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return False

# Main function to run the monitoring
def main():
    webapp_url = "http://192.168.100.42:8000/" #Replace with the url of your website including the port
    while True:
        if not check_webapp(webapp_url):
            print("Web application is down. Sending email notification.")
            send_email("Web Application Down", "Your web application is not responding correctly.")
        else:
            print("Web application is up and running.")

        time.sleep(60)  # Sleep for 1 minute before checking again

if __name__ == "__main__":
    main()
