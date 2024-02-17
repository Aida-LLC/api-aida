# API AIDA

## Deploy Guide

Step by step  guide to deploying Flask app in digital ocean droplet using gunicorn and nginx.

Things we are going to cover

1. Creating digital ocean droplet
2. Preparing environment
3. Actual deployment guide

## Creating digital ocean droplet

Go to digital ocean and create an account if you don't have one. here is the link <br> ✨ [Digital Ocean](https://m.do.co/c/a8690363c67d) 🎉 ~ This is a referral link, you will get **$200** credit for **60 days**. so no more excuses to why your projects are not deployed.

After creating an account, click on the create button and select droplets. You will be presented with a list of options. Select the Ubuntu 20.04 LTS. Choose the plan of your preference. You can choose any data center region you want. I usually choose the one closest to me.

Choose the authentication method. SSH keys are the best but for this guide, we are going to use a password. You can always add SSH keys later.

if you are a windows user get yourself a virtual box and install Ubuntu. or use WSL 😂.

## Preparing environment

Now that we have our droplet up and running, let's prepare our environment.
connect to your droplet using ssh.

```bash
ssh root@your_droplet_ip
```

Provide your password and you are in.

### Update and upgrade

```bash
sudo apt update
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
```

### Create a virtual environment

```bash
sudo apt install python3-venv
```

Create a directory for your project and navigate to it.

```bash
mkdir apps
cd apps
```

Create a virtual environment

```bash
python3 -m venv venv
```

Activate the virtual environment

```bash
source venv/bin/activate
```

### Clone your project

let's call our project `flask_app`

```bash
git clone your_project_url.git
cd let's call our project `flask_app`
```

### Install project dependencies

```bash
pip install -r flask_app/requirements.txt
```

now that we have your project up and running, let's run it and see if everything is working as expected.
first lets allow the port we are going to use.

```bash
sudo ufw allow 5000

```

run the app

```bash
python app.py
```

if everything is working as expected, you should be able to access your app using your droplet ip and port 5000.
something like this `http://your_droplet_ip:5000`

## Actual deployment guide

### Create WSGI entry point

Create a file called `wsgi.py` in your project root directory.
or just copy app.py to wsgi.py

```bash
cp app.py wsgi.py
```

### Configure Gunicorn

Safe check if gunicorn is installed

```bash
gunicorn --version
```

if not installed install it using pip

```bash
pip install gunicorn
```

try running your app using gunicorn

```bash
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

Check your app using your droplet ip and port 5000. something like this `http://your_droplet_ip:5000`

if everything is working as expected, let's move to the next step.

### Create a systemd service file

Create a systemd service file for gunicorn, this will allow gunicorn to automatically start on boot.
first deactivate your virtual environment

```bash
deactivate
```

Then create a file called `flask_app.service` in `/etc/systemd/system/` directory.

```bash
sudo nano /etc/systemd/system/flask_app.service
```

Add the following configuration to the file

```bash
[Unit]
Description=Gunicorn instance to serve flask_app
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/root/apps/flask_app
Environment="PATH=/root/apps/venv/bin"
ExecStart=/root/apps/venv/bin/gunicorn --workers 3 --bind unix:flask_app.sock -m 007 wsgi:app

[Install]
WantedBy=multi-user.target
```

After creating the file, start the gunicorn service and enable it to start on boot.

```bash
sudo systemctl start flask_app
sudo systemctl enable flask_app
```

Check the status of the service to make sure it's running without any issues.

```bash
sudo systemctl status flask_app
```
