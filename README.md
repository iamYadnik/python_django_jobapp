💼 Django Job Listings Platform
A modern, scalable job listings platform built with Django. Features job posting management, employer profiles, job search, and subscription functionality with AWS S3 integration for media storage.

Django
Python
PostgreSQL
AWS S3
License

Live Demo: yadnik72.eu.pythonanywhere.com

✨ Key Features
Job Management
Post Job Listings - Employers can create and manage job postings

Advanced Search - Filter by location, job type, salary, industry

Job Details - Rich job descriptions with company information

Application Tracking - Candidates can apply to jobs and track applications

Featured Jobs - Promote important job listings

Employer Features
Employer Dashboard - Manage posted jobs and applications

Company Profiles - Showcase company information and branding

Custom Admin Panel - Manage all job listings and employers

Application Management - Review and track candidate applications

Candidate Features
Search & Filter - Find jobs by location, salary, type

Save Jobs - Bookmark favorite job listings

Apply to Jobs - Simple application process

Profile Management - Maintain professional profile

Subscription System
Premium Features - Featured job listings, priority support

Subscription Plans - Flexible pricing options

Automated Billing - Secure payment processing

🛠️ Tech Stack
Component	Technology
Backend	Django 5.2.7, Python 3.10+
Database	PostgreSQL 12+
Media Storage	AWS S3
Frontend	HTML5, CSS3, Bootstrap 5
Authentication	Django Built-in Auth
Static Files	WhiteNoise + AWS S3
File Upload	Django Storages (S3Boto3)
Hosting	PythonAnywhere
Version Control	Git, GitHub
📋 Prerequisites
Python 3.10 or higher

PostgreSQL 12 or higher

pip (Python package manager)

Git

AWS S3 account (for media storage)

Virtual environment support

🚀 Quick Start
1. Clone the Repository
bash
git clone https://github.com/iamYadnik/job-listings.git
cd job-listings
2. Create Virtual Environment
bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
3. Install Dependencies
bash
pip install -r requirements.txt
4. Configure Environment Variables
bash
# Copy the example file
cp .env.example .env

# Edit .env with your settings
# Important variables needed:
# - SECRET_KEY: Django secret key
# - DEBUG: Development/Production mode
# - DB_ENGINE: PostgreSQL database engine
# - DB_NAME: Database name
# - DB_USER: Database user
# - DB_PASSWORD: Database password
# - DB_HOST: Database host
# - DB_PORT: Database port
# - AWS_ACCESS_KEY_ID: AWS S3 access key
# - AWS_SECRET_ACCESS_KEY: AWS S3 secret key
# - AWS_STORAGE_BUCKET_NAME: S3 bucket name
5. Run Database Migrations
bash
python manage.py migrate
6. Create Superuser (Admin Account)
bash
python manage.py createsuperuser

# Follow prompts to create admin account
# Username: admin
# Email: your_email@example.com
# Password: (choose secure password)
7. Collect Static Files
bash
python manage.py collectstatic --noinput
8. Start Development Server
bash
python manage.py runserver

# Server runs at http://localhost:8000/
# Admin panel at http://localhost:8000/admin/
Visit http://localhost:8000/ in your browser!

📁 Project Structure
text
job-listings/
├── jobapp/                       # Main Django project
│   ├── __init__.py
│   ├── settings.py              # Django settings (PostgreSQL + AWS S3)
│   ├── urls.py                  # Main URL routing
│   ├── asgi.py
│   └── wsgi.py
│
├── app/                          # Main jobs application
│   ├── migrations/              # Database migrations
│   ├── static/                  # CSS, JS, images
│   ├── templates/               # HTML templates
│   │   ├── job_list.html        # Job listings page
│   │   ├── job_detail.html      # Job detail page
│   │   ├── post_job.html        # Post job form
│   │   ├── employer_dashboard.html
│   │   └── search.html          # Search results
│   ├── __init__.py
│   ├── admin.py                 # Admin configuration
│   ├── apps.py
│   ├── forms.py                 # Django forms
│   ├── models.py                # Job, Employer, Application models
│   ├── tests.py
│   ├── urls.py                  # App URL routing
│   └── views.py                 # Views and handlers
│
├── subscribe/                   # Subscription app
│   ├── models.py               # Subscription plans
│   ├── views.py                # Payment handling
│   └── templates/
│
├── uploadapp/                   # File upload handling
│   ├── models.py               # Upload configurations
│   └── views.py
│
├── templates/                   # Project-wide templates
│   ├── base.html               # Base template
│   ├── navbar.html             # Navigation
│   └── footer.html
│
├── media/                       # User uploads (AWS S3)
├── staticfiles/                 # Collected static files (AWS S3)
├── manage.py
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (NOT committed)
├── .env.example                # Environment template
├── .gitignore
└── README.md                   # This file
🔧 Environment Variables
Create a .env file with these variables:

text
# Django Configuration
SECRET_KEY=your-django-secret-key-here
IS_DEVELOPMENT=True
APP_HOST=localhost
DEBUG=True

# PostgreSQL Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=job_listings_db
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# AWS S3 Configuration
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_STORAGE_BUCKET_NAME=your-bucket-name

# Security (for production)
CSRF_TRUSTED_ORIGINS=http://localhost:8000,https://yourdomain.com
⚠️ Important: Never commit .env file! It's included in .gitignore for security.

🗄️ Database Models
Job Model
Title

Description

Location

Salary range

Job type (Full-time, Part-time, Contract)

Company/Employer

Required skills

Posting date

Deadline

Featured status

Employer Model
Company name

Logo (AWS S3)

Company description

Website

Location

Contact information

Subscription status

Application Model
Job posting

Candidate

Resume/CV

Cover letter

Application status

Applied date

Reviewed status

Subscription Model
Plan name

Price

Features

Duration

Featured job slots

🔐 Security Features
Environment Variables
All sensitive data stored in .env file

Database credentials encrypted

AWS S3 keys secured

Django SECRET_KEY protected

Authentication & Authorization
Django built-in authentication

Password hashing and validation

User permissions and groups

Employer-only job posting

Data Protection
CSRF protection enabled

XFrame options configured

Secure headers set

SQL injection prevention via ORM

AWS S3 Integration
Secure file uploads

Public read access for media

Cache control for optimization

File overwrite protection

🚀 Deployment
Deploy to PythonAnywhere
bash
# 1. Push to GitHub
git push

# 2. Go to PythonAnywhere.com
# 3. Link your GitHub repository
# 4. Configure PostgreSQL database
# 5. Set environment variables in Web app console
# 6. Configure AWS S3 bucket
# 7. Collect static files
# 8. Reload web app
Setting Up PostgreSQL
bash
# On PythonAnywhere:
# 1. Purchase PostgreSQL database
# 2. Add database credentials to .env
# 3. Run migrations
# 4. Create superuser
Configuring AWS S3
bash
# 1. Create S3 bucket on AWS
# 2. Create IAM user with S3 access
# 3. Set bucket policy for public read access
# 4. Add credentials to .env file
# 5. Update S3_CUSTOM_DOMAIN if using custom domain
📊 Database Queries
Find Jobs by Location
python
jobs = Job.objects.filter(location='New York').order_by('-posted_date')
Get Top Employers
python
employers = Employer.objects.annotate(job_count=Count('job')).order_by('-job_count')[:10]
Search Jobs
python
jobs = Job.objects.filter(
    Q(title__icontains='Django') |
    Q(description__icontains='Python')
).filter(job_type='Full-time')
Get Featured Jobs
python
featured = Job.objects.filter(featured=True)[:5]
🧪 Running Tests
bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test app

# Run with verbose output
python manage.py test -v 2

# Test coverage
coverage run --source='.' manage.py test
coverage report
📝 Admin Features
Access the admin panel at http://localhost:8000/admin/

Admin Capabilities:

View all job listings

Manage employers and candidates

Review applications

Manage subscriptions

Set featured jobs

View analytics

🐛 Troubleshooting
PostgreSQL Connection Error
bash
# Verify PostgreSQL is running
# Check credentials in .env
# Ensure DB_HOST and DB_PORT are correct

# Try connecting directly
psql -U postgres -h localhost
AWS S3 Upload Errors
bash
# Verify AWS credentials in .env
# Check S3 bucket exists
# Ensure IAM user has proper permissions
# Verify bucket policy allows uploads
Static Files Not Loading
bash
# Collect static files
python manage.py collectstatic

# Verify AWS_STORAGE_BUCKET_NAME in .env
# Check static/ folder in S3 bucket
Database Migration Errors
bash
# Create new migration
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Check migration status
python manage.py showmigrations
📚 Learning Resources
Django Official Documentation

PostgreSQL Documentation

AWS S3 Documentation

Django + PostgreSQL Tutorial

Django + AWS S3 Integration

🤝 Contributing
Fork the repository

Create a feature branch (git checkout -b feature/add-feature)

Make your changes

Add tests for new features

Commit your changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature/add-feature)

Open a Pull Request

Coding Standards
Follow PEP 8

Write docstrings

Add unit tests

Keep commits atomic

📄 License
MIT License - See LICENSE file for details

👨‍💻 Author
Yadnik Gaonkar

📧 Email: Yadnik72@gmail.com

🔗 LinkedIn: linkedin.com/in/yadnikgaonkar

🐙 GitHub: @iamYadnik

🙏 Acknowledgments
Django framework and community

PostgreSQL database

AWS S3 storage

Made by Yadnik Gaonkar

Key Highlights
✅ Production-ready Django configuration

✅ PostgreSQL for scalable database

✅ AWS S3 for media storage and static files

✅ WhiteNoise for static file serving

✅ Environment variables for security

✅ Multiple Django apps (modularity)

✅ PythonAnywhere deployment ready

✅ Subscription system with billing

✅ Job application tracking

✅ Employer management dashboard