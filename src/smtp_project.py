import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Step 1: Create read_recipients function
# Input: file_path
# Output: recipients list
def read_recipients(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            if 'Email' not in line:
                data.append(line[1])
    return data


def send_email(sender_email, subject, body, smtp_server, smtp_port, smtp_username, smtp_password, email_recipients):
    # Step 2: Pass the recipients list to the function on loop over them before sending an email
    for receiver_email in email_recipients:
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Connect to SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.login(smtp_username, smtp_password)

            # Send the email
            server.sendmail(sender_email, receiver_email, message.as_string())

            print(f"Email sent to ({receiver_email}) successfully!")


if __name__ == "__main__":
    sender_email = 'mnalam@student.fitchburgstate.edu'
    file_path = "C:/Users/parim/OneDrive/Desktop/Recievers.csv"
    subject = 'Test Email'
    body = 'This is a test email sent using SMTP protocol.'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'mnalam@student.fitchburgstate.edu'
    smtp_password = 'bdznfrefpetihvuj'

    # Step 3: Call the read_recipients_function, passing the path toe your CSV file
    # Assign the result of the read_recipients function to a variable called recipients_list
    # Pass the recipients_list variable to the send_email function.
    email_recipients = read_recipients(file_path)

    send_email(sender_email, subject, body, smtp_server, smtp_port, smtp_username, smtp_password, email_recipients)
