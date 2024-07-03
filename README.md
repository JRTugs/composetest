# Deploying Compose Test

## Instructions below on how to deploy a Flask website

**Required Applications**
1. Docker Compose
2. Git

```bash
Note: Installations on the required application will depend on the Operating System being used to deploy the Flask Website
```

**1. Cloning from git repository**

  - On the server, run command below to clone from github repository
```bash
git clone -b main https://github.com/JRTugs/composetest.git
```

  ![image](https://github.com/JRTugs/composetest/assets/29426766/8fe97961-8314-450c-9645-bf3838427713)

  - Verify files cloned
```bash
ls -alh
```

  ![image](https://github.com/JRTugs/composetest/assets/29426766/86d7a6a1-53cd-4671-853d-0f28daab06cc)

**2. Run website using docker compose**

  - On the server, run command below to run the flask website in the background
```bash
docker compose up -d
```

  - Verify if docker image is running
```bash
docker ps
```

  ![image](https://github.com/JRTugs/composetest/assets/29426766/41af188d-6b4e-4f8f-a025-c9936a465415)

  - Verifying using curl
```bash
curl http://localhost:8000/
```

  ![image](https://github.com/JRTugs/composetest/assets/29426766/4f3db177-e32e-456b-b3ee-dd87290cf41e)

# Monitoring the website

**Two Options to run monitoring**

**1. Running monitoring script by using email address and password**
  - email and password must be hard coded in the script in running this script

**2. Running monitoring script from AWS Simple Email Service (SES)**
  - Need to setup AWS resouces to allow the script to send email but password will not be hard coded in the script which makes this option much secure

## 1. Running monitoring.py script using email such as gmail
  - Python is needed to run the python monitoring.py script.
  - Edit monitoring.py script to update the script with your own email address, password, smtp server and port and website url
```bash
vi monitoring.py
```
  - change the values below
```bash
sender_email = "your_email@example.com"  # Replace with your email address
receiver_email = "your_email@example.com"      # Replace with the admin's email address
password = "your_email_password"          # Replace with your email password

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Replace with your SMTP server address and port

webapp_url = "http://192.168.100.42:8000/" #Replace with the url of your website including the port
```

```bash
Note: Depending on your email provider, smtp server and port maybe different. Some providers does not allow direct username and login and may need extra configuration to allow access to email account from an application.
```

  - Once details has been filled in, run the command below to run the monitoring script
```bash
python3 monitor.py
```

  ![image](https://github.com/JRTugs/composetest/assets/29426766/ce2e68f2-dbe2-4ae5-aeb7-fa6529759a65)

## 2. Running monitoring_aws.py to use AWS Simple Email Service (SES)

**1. Creating IAM user**

  - Need to create IAM user which will be used as credentials to be used by server to access AWS resouces
  - On AWS Management Console, search IAM
  - On IAM Dashboard, Click Users and Click "Create User"

  ![image](https://github.com/JRTugs/composetest/assets/29426766/509bdde8-641b-456d-9b57-ccd7cee946dc)

  - On Specify user details window, Fill in the name and Click "Next"
  - On Set Permission window, Select "Add user to group" and Click "Create group"
  - On Create user group window, Fill in the user group name
  - Under Permissions policies, Search on "AmazonSESFullAccess", Check the box next to "AmazonSESFullAccess" and Click "Create user group"

  ![image](https://github.com/JRTugs/composetest/assets/29426766/95e02559-302d-4e6d-8d95-a08d73cba3ef)

  - Once the User group has been created, Assign the group that has full permission to AWS SES to the new user and Click "Next"

  ![image](https://github.com/JRTugs/composetest/assets/29426766/05bec745-7e12-4317-a77c-f33e9b2fc9c9)

  - Once completed, Click "Create User"

**2. Creating Access keys**

  - On the IAM Dashboard, Click Users > Select the newly created user
  - On the newly created user window, Click "Security credentials"

  ![image](https://github.com/JRTugs/composetest/assets/29426766/a6c12813-f052-4437-ab51-7e34144888c6)

  - On Security Credentials windows, Go to Access keys > Click "Create Access Key"

  ![image](https://github.com/JRTugs/composetest/assets/29426766/6e15144a-5705-4bac-bb80-eaf4347a904d)

  - On the Access key best practices & alternatives window, Select Command Line Interface (CLI) > Check box under Confirmation in the bottom > Click "Next"
  - Add Tag (Optional) > Click "Create Access Key"
  - Copy Access Key and Secret Access Key

  ![image](https://github.com/JRTugs/composetest/assets/29426766/402acd2e-bdb0-4feb-9c4c-10ade5ef2a76)

**3. Creating AWS Simple Email Service(SES) Identity**

  - Go to AWS SES by searching in AWS Management Console
  - On AWS SES, Click Identities > Click "Create Identity"

  ![image](https://github.com/JRTugs/composetest/assets/29426766/137928d0-a54c-4f54-a35e-f333b3d314d7)

  - On Identity details, Click "Email Address"
  - Under Email Address field, Fill in your email address and Click "Create Identity"

  ![image](https://github.com/JRTugs/composetest/assets/29426766/7c451168-9b82-4e74-a28e-6a07330867ff)

  - Check you email and confirm the request to authorize use of email

  ![image](https://github.com/JRTugs/composetest/assets/29426766/357378c6-a8d6-426b-b1e6-5ddd871e6ac9)

  - Once confirmed, Identity status will be verified

  ![image](https://github.com/JRTugs/composetest/assets/29426766/e4998d8f-3872-4897-86d4-a6edacc0cb9b)

**4. Connecting server to AWS**

  - Install awscli from server

```bash
pip install awscli
```

  - Configure AWS and enter your Access keys and Secret Key and region name
```bash
aws configure
```
  ![image](https://github.com/JRTugs/composetest/assets/29426766/d7144261-1463-46d0-9007-6ef73463a753)

**5. Run moniroting Script**
```bash
python3 monitoring_aws.py
```
  
# Testing your monitoring script

  - Stop the docker image from running to make the website not accessible
```bash
docker compose stop
```

  ![image](https://github.com/JRTugs/composetest/assets/29426766/96eaa5a8-2088-48be-8773-f6a6c77fd7f4)

  - Verifying website is not running

  ![image](https://github.com/JRTugs/composetest/assets/29426766/161c1797-754c-482b-bd63-1bc3e6cb14f4)

  - Once the monitoring script rerun again. it will detect that the website is down and should be able to send an email notification.

  ![image](https://github.com/JRTugs/composetest/assets/29426766/f100032c-6b16-4d1c-b55c-3837ac6baaf0)

  - Verify email if received

  ![image](https://github.com/JRTugs/composetest/assets/29426766/5c6823b8-52b5-49a9-8dca-1d552edd293e)

  - Once email is received, you can bring up the website again by running command below
```bash
docker compose up -d
```

  - Website should be up and running now

  ![image](https://github.com/JRTugs/composetest/assets/29426766/72aefd25-96c7-4303-be11-031c1014ab99)



  
# EXPLANATION

**Docker Image**
  - The dockerfile as well as all necessary files needed to setup a website is provided in the https://docs.docker.com/compose/gettingstarted/ website. Everything is straight forward.

**Monitoring Script**
  - Creating a python script seems to be pretty much convenient as parameters that needed to be updated are already included in the script such as the email address, passowrd, smtp details as well as the url to be monitored. Tried to check on shell script and it requires additional application such as sendmail and must be configured to allow the server to send out email.





  

