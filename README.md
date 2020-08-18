# swgoh-automation


Automation for taking screen shots and then doing OCR to parse out things like Territory Battles, Raid Tickets, and other guild management activities

## Install Python3 and git
1. https://www.python.org/downloads/
2. https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

## Setup this project
```sh
git clone git@github.com:kevinbuckley/swgoh-automation.git # download project
cd swgoh-automation # navigate to the project
pip3 install -r requirements.txt # install dependencies
```

## Setup the AWS API

1. setup an aws account in us-east2.  you'll end up needing to put a credit card # in but don't worry, the charges are in the single digits per month from my experience.  https://us-east-2.console.aws.amazon.com/

2. create a user for the scritp to use. navigate to https://console.aws.amazon.com/iam/home?region=us-east-2#/users, follow through the wizard with the following instructions:
    - Whatever name you want
    - Set Access Type to **Programmatic access**
    - Create a permission group, add the permission **AmazonTextractFullAccess** to it. 
    - Assign your user to the newly created group
    - Tags don't matter
    - IMPORTANT: Save the **Access key ID** and **Secret access key** locally


## Run the script

``` sh
PICTURE_PATH="/Users/yourname/Desktop/*.png"
AWS_ACCESS_KEY_ID=<access_key_id> AWS_SECRET_ACCESS_KEY=<secret> python3 main.py
