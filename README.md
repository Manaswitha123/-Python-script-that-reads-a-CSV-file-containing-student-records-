# -Python-script-that-reads-a-CSV-file-containing-student-records-
# Student Portal

A simple Flask web application for managing student records. This project includes functionalities to read a CSV file, submit student details via a form, display submitted details, and manage user authentication.

## Features

- Read student records from a CSV file
- Calculate the average grade and find the student with the highest grade
- Submit student details via a web form
- Display submitted details
- User authentication (registration and login)
- API endpoint to return user data in JSON format

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/student-portal.git
   cd student-portal
2. **Create a virtual environment**:
python -m venv venv

3. **Activate the virtual environment**:
On Windows:
venv\Scripts\activate

On macOS and Linux:
source venv/bin/activate

4. **Install the required packages**:
pip install -r requirements.txt

5. **Running the Application**
Initialize the database:
python
>>> from app import db
>>> db.create_all()
>>> exit()

Run the Flask application:
python app.py

Open your web browser and go to:
http://127.0.0.1:5000/

Project Structure
student-portal/
│
├── app.py
├── csv_handler.py
├── extensions.py
├── requirements.txt
├── templates/
│   ├── home.html
│   ├── form.html
│   ├── display.html
│   ├── register.html
│   ├── login.html
├── static/
│   └── styles.css
└── README.md
