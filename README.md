 ## END TO END MACHINE LEARNING PROJECT

## CREATED A VIRTUAL ENVIRONMENT
```conda create -p venv python==3.8```

## install all necessary libries
```pip install -r requirements.txt```

## github code
```
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/SHAYANSINHA/ML-PROJECT-1.git
git push -u origin main

```
## ECR REPO URL
``` 
  103216491235.dkr.ecr.ap-south-1.amazonaws.com/diamondpriceprediction
```
## Docker Setup In EC2 commands to be Executed
``` 
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

```
## Configure EC2 as self-hosted runner:

## Setup github secrets:
```  
AWS_ACCESS_KEY_ID = AKIARQCBOVLRUFHRZDPI


AWS_SECRET_ACCESS_KEY = 9zgHfZs3uztopVQunxroG/mlByDxWfkX6LiDgB19


AWS_REGION = ap-south-1

AWS_ECR_LOGIN_URI = 103216491235.dkr.ecr.ap-south-1.amazonaws.com

ECR_REPOSITORY_NAME = diamondpriceprediction

```