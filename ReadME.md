# Meeting Management System

This is simple meeting management system build using Python-Django.

## Setup

### Clone the repository
git clone https://github.com/abbasidaniyal/Innovacer-SDK-challenge.git

### Setup Mailing Service

Set the following environment variable

```
USER_EMAIL= xxxxxxxxx@xxxxx.xxx
USER_PASSWORD= xxxxxxxxxxx
```

### Setup SMS
We are using twilio as an sms service. Obtain SID and Auth_Token from twilio from their website https://www.twilio.com/

Set the following environment variable


```
TWILIO_ACCOUNT_SID=XXXXXXXXXXXXX
TWILIO_AUTH_TOKEN=YYYYYYYYYYYY
TWILIO_NUMBER=+xxyyyyyyyyyy
```



### Make Migrations
Two database configuration are present in the setting.py. Sqlite for development and postgres for production.

### To Do
1. Add Design (Bootstrap the templates)
2. Add authentication to create Hosts