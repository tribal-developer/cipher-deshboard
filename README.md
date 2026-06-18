# Cipher Management System

## Overview

Cipher Management System is a secure Django-based web application designed to manage cipher records and control user access through an authorization workflow.

The application provides:

* Role-based authentication
* User authorization management
* Cipher record management
* Cipher key protection
* Search and filtering
* Secure key viewing and copying
* Audit-friendly record storage

---

# Features

## Authentication

### Administrator

* Login to Admin Dashboard
* Authorize users
* Add Cipher Records
* Edit Cipher Records
* Delete Cipher Records
* Search records
* View all records

### User

* Register only if authorized
* Login to User Dashboard
* Search records
* View Cipher Keys
* Copy Cipher Keys

---

# User Authorization Workflow

Users cannot register directly.

Registration process:

1. Administrator authorizes a user.
2. User information is stored in User Verification.
3. User opens Registration page.
4. Employee ID is verified.
5. User creates account.
6. User can login.

---

# Cipher Record Workflow

Administrator can:

* Add Record
* Edit Record
* Delete Record

Record fields:

| Field         | Description            |
| ------------- | ---------------------- |
| Name          | Record Name            |
| Agent Name    | Unique Identifier      |
| IP Address    | Optional               |
| Section       | Department/Section     |
| Cipher Key    | Uploaded from TXT file |
| Uploaded Date | Auto-generated         |

---

# Cipher Key Security

Cipher keys are stored securely.

Example:

Original:

asdqwertghyujkiolpjhgfrtghyasbnv

Displayed:

asd******bnv

Rules:

* First 3 characters visible
* Last 3 characters visible
* Middle section hidden
* Full key available only through popup

---

# Technology Stack

## Backend

* Python
* Django

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* Bootstrap Icons
* JavaScript

## Database

* SQLite

---

# Project Structure

```text
cipher_dashboard/
│
├── accounts/
├── dashboard/
├── core/
├── templates/
├── static/
├── media/
├── .env
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

---

# Installation Guide

## Linux Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/cipher-dashboard.git

cd cipher-dashboard
```

### Step 2: Create Virtual Environment

```bash
python3 -m venv venv
```

### Step 3: Activate Environment

```bash
source venv/bin/activate
```

### Step 4: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 5: Create Environment File

```bash
touch .env
```

Add:

```env
SECRET_KEY=your-secret-key

DEBUG=True

ALLOWED_HOSTS=127.0.0.1,localhost

CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000
```

### Step 6: Apply Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

### Step 7: Create Superuser

```bash
python manage.py createsuperuser
```

### Step 8: Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

# Windows Installation

## Step 1: Clone Repository

```cmd
git clone https://github.com/yourusername/cipher-dashboard.git

cd cipher-dashboard
```

## Step 2: Create Virtual Environment

```cmd
python -m venv venv
```

## Step 3: Activate Environment

```cmd
venv\Scripts\activate
```

## Step 4: Install Requirements

```cmd
pip install -r requirements.txt
```

## Step 5: Create .env File

Create:

```text
.env
```

Add:

```env
SECRET_KEY=your-secret-key

DEBUG=True

ALLOWED_HOSTS=127.0.0.1,localhost

CSRF_TRUSTED_ORIGINS=http://127.0.0.1:8000
```

## Step 6: Apply Migrations

```cmd
python manage.py makemigrations

python manage.py migrate
```

## Step 7: Create Superuser

```cmd
python manage.py createsuperuser
```

## Step 8: Run Server

```cmd
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

# Administrator Functions

* Add User
* View Users
* Add Cipher Record
* Edit Record
* Delete Record
* Search Records
* View Cipher Keys

---

# User Functions

* Register
* Login
* Search Records
* View Cipher Keys
* Copy Cipher Keys

---

# Security Guidelines

* Do not share Cipher Keys.
* Authorize only valid users.
* Keep credentials secure.
* Logout after use.
* Use strong passwords.
* Regularly back up the database.

---

# Version

Current Version: 1.0

Cipher Management System
Django Based Secure Cipher Record Management Application
