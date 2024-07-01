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

**3. Running monitoring script to monitor website**

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

**4. Testing your monitoring script if it will send an email alert once it is down**

  - Stop the docker image from running to make the website not accessible
```bash
docker compose stop
```

  ![image](https://github.com/JRTugs/composetest/assets/29426766/96eaa5a8-2088-48be-8773-f6a6c77fd7f4)

  - Verifying website is not running

  ![image](https://github.com/JRTugs/composetest/assets/29426766/161c1797-754c-482b-bd63-1bc3e6cb14f4)

  - Once the monitoring.py script rerun again. it will detect that the website is down and should be able to send an email notification.

  ![image](https://github.com/JRTugs/composetest/assets/29426766/f100032c-6b16-4d1c-b55c-3837ac6baaf0)

  - Verify email if received

  ![image](https://github.com/JRTugs/composetest/assets/29426766/5c6823b8-52b5-49a9-8dca-1d552edd293e)

  - Once email is received, you can bring up the website again by running command below
```bash
docker compose up -d
```

  - Website should be up and running now

  ![image](https://github.com/JRTugs/composetest/assets/29426766/72aefd25-96c7-4303-be11-031c1014ab99)

  
  

