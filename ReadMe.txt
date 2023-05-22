README
This is a simple Flask application that fetches email addresses from a given URL. 
It uses regular expressions and the requests library to retrieve the HTML content of the provided URL, search for email addresses, 
and display them in a list format.


Prerequisites

Python 3.x
Flask
requests


Installation and Setup

Clone the repository to your local machine.
Make sure you have Python 3.x installed.
Install the required dependencies by running the following command in your terminal:

pip install flask requests


How to Run

Navigate to the project directory in your terminal.
Execute the following command to start the Flask development server:

python app.py

Open your web browser and go to http://localhost:5000 to access the application.


Usage

Enter a valid URL in the provided input field on the homepage.
Click the "Fetch Emails" button.
The application will retrieve the HTML content from the provided URL and search for email addresses.
If any valid email addresses are found, they will be displayed as a list.
If no valid email addresses are found or an error occurs during the request, an appropriate message will be displayed.


Notes

The regular expression used to search for email addresses is:

[A-Za-z0-9_%+-.]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,5}
It matches common email address patterns but may not cover all possible variations.
This application is for demonstration purposes only and should not be used for any malicious activities or unauthorized access to email accounts.
