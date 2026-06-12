# Secure Login System

A secure web-based authentication system developed using Flask, SQLite, and bcrypt. This project demonstrates secure user registration and login functionality while implementing essential cybersecurity practices such as password hashing, input validation, SQL injection prevention, and session management.

## Features

* User Registration
* User Login Authentication
* Secure Password Hashing using bcrypt
* Input Validation for Email, Username, and Password
* SQL Injection Protection using Parameterized Queries
* Session-Based Authentication
* Protected Dashboard Access
* Logout Functionality
* Flash Messages for Success and Error Notifications
* Show/Hide Password Feature
* Responsive Bootstrap UI

## Security Features

### Password Hashing

User passwords are securely hashed using bcrypt before being stored in the database.

### SQL Injection Protection

Parameterized SQL queries are used to prevent SQL injection attacks.

### Session Management

Authenticated users are managed using secure Flask sessions, and protected routes require active login sessions.

### Input Validation

The application validates:

* Username length
* Email format
* Password complexity requirements

## Technologies Used

* Python
* Flask
* SQLite
* bcrypt
* HTML5
* Bootstrap 5
* JavaScript


### Registration

* Create a new account with valid credentials.
* Verify that duplicate email registration is blocked.

### Login

* Login using valid credentials.
* Verify incorrect credentials display an error message.


## Future Enhancements

* Two-Factor Authentication (2FA)
* Password Strength Meter
* Password Reset Functionality
* Login Attempt Limiting
* Account Lockout Mechanism

## Learning Outcomes

This project demonstrates:

* Secure Authentication Implementation
* Password Hashing with bcrypt
* SQL Injection Prevention
* Session Management
* Input Validation
* Secure Coding Practices
* Web Application Security Fundamentals

## Author

**Jyoti Kumbhar**

Cyber Security Project – Secure Login System 🛡️
