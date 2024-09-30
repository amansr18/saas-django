# SaaS_Django Base

Welcome to **SaaS_Django Base**! This project provides a robust foundation for developers to quickly build and deploy SaaS applications tailored to their specific needs. With its comprehensive set of features already implemented, developers can focus on adding unique functionalities and deploying their applications in just days or weeks.

## Key Features

- **Built on Django**: Take advantage of Django's secure and scalable architecture.
- **Tailwind CSS Integration**: Utilize Tailwind’s utility-first CSS framework for a modern, responsive design.
- **Dynamic User Interfaces**: Enhance interactivity with HTMX for seamless user experiences.
- **PostgreSQL Database**: Store your application data using a powerful relational database.
- **Redis Caching**: Improve performance with built-in caching and background task management.
- **Social Authentication**: Easily implement social login options to enhance user convenience.
- **Stripe Integration**: Manage subscriptions with various pricing options directly from the admin panel, allowing you to add new plans and subscriptions effortlessly.
- **Flexible Authorization Controls**: Design and manage user roles and permissions with Django’s group functionality, including the ability to provide beta plans or special permissions directly from the admin panel.
- **Management Commands**: Fetch the latest details from Stripe using built-in management commands.
- **Email Verification**: Secure user logins with email verification for all accounts.
- **Containerized Deployment**: Deploy your applications effortlessly using Docker.



## References

- Deploy Django on [Railway](https://kirr.co/qysgeu) with [this Dockerfile and guide]
- Create a One-Off Secret Key for Django [blog post]




## Getting Started

SaaS_Django Base serves as a customizable framework, allowing developers to add new features according to their SaaS requirements. Follow the installation instructions to set up your environment and start building your application today!

### Clone
```bash
mkdir -p ~/dev/saas
cd ~/dev/saas
git clone https://github.com/amansr18/saas-django.git .
```

### Create Virtual Environment

### Create a Virtual Environment

*For macOS/Linux:*
```bash
# Verify that Python 3.11 or higher is installed
python3 --version  

# Create a virtual environment named 'venv'
python3 -m venv venv  

# Activate the virtual environment
source venv/bin/activate 

*For Windows*
# Create a virtual environment named 'venv'
```bash
c:\Python312\python.exe -m venv venv 

.\venv\Scripts\activate 
```

### Install Requirements
```bash
# with venv activated
pip install pip --upgrade && pip install -r requirements.txt
```

### Sample dotenv to dotnev

```bash
cp .env.sample .env
cat .env
```
Ensure that your .env file includes the following configuration values:
- `DJANGO_DEBUG=1`
- `DJANGO_SECRET_KEY=""`
- `DATABASE_URL=""`
- `EMAIL_HOST="smtp.gmail.com"`
- `EMAIL_PORT="587"`
- `EMAIL_USE_TLS=True`
- `EMAIL_USE_SSL=False`
- `EMAIL_HOST_USER=""`
- `EMAIL_HOST_PASSWORD=""`
- `ADMIN_USER_EMAIL=""`
- `STRIPE_SECRET_KEY=""`


### Create the _DJANGO_SECRET_KEY_

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
or
```bash
openssl rand -base64 64
```
or
```bash
python -c 'import secrets; print(secrets.token_urlsafe(64))'
```

Once you have this value, add update `DJANGO_SECRET_KEY` in `.env`.




### Run Migrations

```bash
source venv/bin/activate 
# or .\venv\Scripts\activate if windows
cd src
python manage.py migrate
```

### Create a Superuser

```bash
python manage.py createsuperuser
```

### Pull Vendor Static Files

```bash
python manage.py vendor_pull
```


### Create a Stripe Account

1. Sign up on [Stripe.com](https://www.stripe.com) for an account
2. Get or create a Stripe Secret API Key (Dashboard > Developers > API keys > _Secret key_ )
3. Update _dotenv_ (`.env`) with the value `STRIPE_SECRET_KEY` with your key.


### Run the Server

```bash
python manage.py runserver
```

Ready to roll! 🚀

Much more coming soon!