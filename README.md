# Clinical Appointments Web App

This web application allows users to view doctors, make appointments, and manage their bookings. The app is built using the Flask framework, with HTML, CSS, and JavaScript on the front end, and CSV files for data storage.

## Features

- **View Doctors**: Users can view a list of doctors and their available appointment slots.
- **Seach**: Users can search for a specific doctor name or spciality and see all doctors with that spciality.
- **Make Appointments**: Users can book appointments based on available dates and times.
- **Manage Appointments**: Users can edit or delete their bookings.
- **Doctor Availability**: Doctors have specific time slots on each day. Users select a date to see available slots.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Data Storage**: CSV files for storing doctor information, user data, and appointments.

## Prerequisites

- Python 3.9.9 or newer version
- Flask 3.0.3
- Werkzeug 3.0.4
- Jinja2 3.1.2
  
## Project Checklist
**Note that [x] refres to checked**
### - [x] It is available on GitHub. 
### - [x] It uses the Flask web framework.
### - [x] It uses at least one module from the Python Standard Library other than the random module. 
- CSV and OS to read, write, create, and store data in CSV files.
- JSON to convert python data types to js arrays.
### - [x] It contains at least one class written by you that has both properties and methods. It uses `__init__()` to let the class initialize the object's attributes (note that `__init__()` doesn't count as a method). This includes instantiating the class and using the methods in your app.
- In user.py file 
- class is defined at line 4
- user_id, first_name
- def user_validation() used in app.py line 119 and line 102 to validate if user email and password.
- def login() used in app.py line 122 to retrive user data after validation is true.
### - [x] It makes use of JavaScript in the front end and uses the localStorage of the web browser.
### - [x] It uses modern JavaScript (for example, let and const rather than var).
### - [x] It makes use of the reading and writing to the same file feature.
### - [x] It contains conditional statements.
- logout.js
- line 5 if statment is used to check to is_logged_out key.
### - [x] It contains loops.
- doctor.py
- line 13 for loop is used to display all of the doctors.
### - [x] It lets the user enter a value in a text box at some point. This value is received and processed by your back end Python code.
### - [x] It doesn't generate any error message even if the user enters a wrong input.
### - [x] It is styled using your own CSS.
### - [x] The code follows the code and style conventions as introduced in the course, is fully documented using comments and doesn't contain unused or experimental code. In particular, the code should not use `print()` or `console.log()` for any information the app user should see. Instead, all user feedback needs to be visible in the browser.
### - [x] All exercises have been completed as per the requirements and pushed to the respective GitHub repository. 

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/clinical-appointments-app.git
   cd clinical-appointments-app
2. **Install Dependencies**
   ```bash
   pip install -r libarary (name of library in prerequisites)
4. **Run the Application**
   ```bash
   set FLASK_APP=app.py
   $env:FLASK_APP = "app.py"
   python run app.py
6. Access the Application: Open your browser and navigate to:
   ```bash
   http://127.0.0.1:5000
7. View index page and start the app.
  ![Welcome — Mozilla Firefox 10_23_2024 1_24_55 PM](https://github.com/user-attachments/assets/b24130d5-1585-4f79-b456-a512039a94be)
   
   
## future improvments
- Implement a database (e.g., SQLite or PostgreSQL) instead of CSV for better scalability.
- Improve the UI/UX design with more dynamic elements and better responsiveness.
  
## Project Structure
   ```bash
    ├── app.py           # Main Flask application
    ├── appointments.py   #Appointments class 
    ├── doctors.py        # Doctors class
    ├── user.py            # user class
    ├── static               # Static files (CSS, JS, images, data)
    │    ├── style.css       # Main CSS file
    │    ├── data folder
    │    ├── imgs          #back grounds and logo
    │    ├── scripts.js 
    │
    ├── templates          # HTML templates
    │    ├── appointments.html # Display user appointment 
    │    ├── contact.html      # contact us fro users
    │    ├── contactguest.html   #contact us without creating an account
    │    ├── doctors.html     # Doctor details page
    │    ├── edit.html     #Editing appointment form 
    │    ├── home.html    #User home page
    │    ├── index.html   # Main page
    │    ├── reservation.html  #booking form
    │    ├── signin.html    #log in from
    │    └── signup.html    # create a new account form
    │  
    └── README.md   # Project documentation 



   




