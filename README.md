# Major-Project-BCA
🗓️ Web-Based Task Scheduler for Students
A full-stack task management web application built using Flask that allows students to manage academic tasks efficiently. The application includes secure user authentication and personalized CRUD operations for task handling.

🚀 Features
🔐 User Authentication

Registration and login functionality

Passwords securely stored using hashing (werkzeug.security)

Session-based login system to ensure secure access

📋 Task Management (CRUD)

Create, Read, Update, Delete academic tasks

Each task linked to a specific user — access control implemented

Tasks displayed in a clean, minimal dashboard UI

🎨 Responsive Frontend

Built using HTML, CSS, and Jinja2 templating

Form validation and user-friendly interface

🔒 Security

Session handling and access validation

Route-level security to prevent unauthorized data access

🧠 Tech Stack
Layer	Technology
Framework	Flask (Python)
Frontend	HTML, CSS, Jinja2, JavaScript
Database	SQLite (via SQLAlchemy ORM)
Auth & Security	Werkzeug, Flask Sessions

🗂️ Project Structure
.
└── flask_auth_app
    ├── auth
    ├── instance
    |   └── db. SQLite
    |
    ├──project
    |    ├── __init__.py           # Setup the app
    |    ├── auth.py               # the auth routes for the app
    |    ├── main.py               # the non-auth routes for the app
    |    ├── models.py             # the user model
    |    ├── static
    |    |   ├── css
    |    |   |   └── style.css     # stylesheet of the frontend
    |    |   |
    |    |   ├── index page.png    # index page photo
    |    |   └── to-do-list.png    # title bar icon photo
    |    |   
    |    |
    |    └── templates
    |        ├── base.html         # contains a common layout and links
    |        ├── index.html        # Show the home page
    |        ├── login.html        # Show the log in form
    |        ├── home.html         # show the todo list page
    |        ├── update.html       # show the update page of todo
    |        └── signup.html       # Show the signup form
    |
    └── run.py

✅ Future Improvements
Email reminders or push notifications for upcoming tasks

Task categorization by subject or priority

Role-based access (admin vs. student)

REST API with JSON responses for frontend frameworks or mobile integration

Deployment on Heroku, Render, or AWS EC2

📷 Screenshots 

•	Home page:
![image](https://github.com/user-attachments/assets/f8c40458-8bdf-49e3-bd12-ddab0b7a07ba)

•	SignUp page:
 ![image](https://github.com/user-attachments/assets/f8233d7c-4815-4e86-a846-b59172ae63bb)

•	Login page:
![image](https://github.com/user-attachments/assets/68c88df2-3bb3-44c4-8d05-9d0fe2f90a2c) 

•	ToDo page:
![image](https://github.com/user-attachments/assets/3abfdc6a-63a0-4e02-bc0a-81ddd25e9bb2)

•	Update page:
![image](https://github.com/user-attachments/assets/4e9ba9cf-e03c-4108-81a8-a2fd63ff2b07)


