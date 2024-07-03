import requests
import boto3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import logging
import email.utils  # Import for generating Message-ID

# AWS SES configuration
AWS_REGION = 'us-east-1'  # Replace with your AWS region
SENDER_EMAIL = 'your_email@example.com'  # Replace with your verified SES email address

# Configure logging
logging.basicConfig(filename='monitoring.log', level=logging.INFO)

# Function to send email using AWS SES
def send_email(subject, body, recipient_email):
    ses_client = boto3.client('ses', region_name=AWS_REGION)

    # Create a unique Message-ID
    message_id = email.utils.make_msgid()

    # Create a multipart/mixed MIME message
    msg = MIMEMultipart('mixed')
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg['Message-ID'] = message_id

    # Attach a text/plain part to the message
    text_part = MIMEText(body.encode('utf-8'), 'plain', 'utf-8')
    msg.attach(text_part)

    try:
        # Send the email
        response = ses_client.send_raw_email(
            Source=SENDER_EMAIL,
            Destinations=[recipient_email],
            RawMessage={'Data': msg.as_string()}
        )
        logging.info(f"Email sent successfully. Message-ID: {message_id}")
    except Exception as e:
        logging.error(f"Failed to send email. Error: {str(e)}")

# Function to check the web application
def check_webapp(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        logging.error(f"Exception occurred during HTTP request: {str(e)}")
        return False

# Main function to run the monitoring
def main():
    recipient_email = 'your_email@example.com'  # Replace with recipient's email address
    subject = 'Web Application is DOWN'
    body = 'Your web application is not responding correctly.'

    webapp_url = "http://192.168.100.42:8000/"  # Replace with your website URL including the port
    while True:
        if not check_webapp(webapp_url):
            logging.warning("Web application is down. Sending email notification.")
            send_email(subject, body, recipient_email)
        else:
            logging.info("Web application is up and running.")

        time.sleep(60)  # Sleep for 1 minute before checking again

if __name__ == '__main__':
    main()
