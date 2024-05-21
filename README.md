# Rental Property Management System

## Overview
The Rental Property Management System is a web application designed to streamline the management of rental properties. It provides landlords and property managers with an easy-to-use platform to manage properties, tenants, leases, and maintenance requests. This project utilizes HTML, CSS, and JavaScript for the front end and Django for the back end.

## Features
- *User Authentication:* Secure login and registration for property managers and tenants.
- *Property Management:* Add, edit, and remove properties with details such as location, rent, and availability status.
- *Tenant Management:* Manage tenant information and track rental payments.
- *Lease Management:* Create and manage lease agreements with start and end dates, rent amounts, and tenant details.
- *Maintenance Requests:* Tenants can submit maintenance requests, which can be tracked and managed by property managers.
- *Payment Tracking:* Record and track rental payments, with the ability to generate payment reports.

## Technologies Used
- *Frontend:*
  - HTML
  - CSS
  - JavaScript
- *Backend:*
  - Django
- *Database:*
  - SQLite (default with Django)
- *Version Control:*
  - Git

## Installation

### Prerequisites
- Python 3.x
- Django
- Git

### Steps
1. *Clone the Repository:*
    sh
    git clone https://github.com/hp0530/Renty.com.git
    cd rpms
    

2. *Create a Virtual Environment:*
    sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    

3. *Install Dependencies:*
    sh
    pip install -r requirements.txt
    

4. *Apply Migrations:*
    sh
    python manage.py migrate
    

5. *Create a Superuser:*
    sh
    python manage.py createsuperuser
    

6. *Run the Development Server:*
    sh
    python manage.py runserver
    

7. Open your browser and navigate to http://127.0.0.1:8000/ to view the application.

## Usage
- *Admin Dashboard:* Accessible via /admin URL, where property managers can manage properties, tenants, leases, and maintenance requests.
- *User Dashboard:* Accessible after login, providing tenants with the ability to view their lease details and submit maintenance requests.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
For any inquiries or feedback, please contact us at [ompathan111003@gmail.com ](mailto:ompathan111003@gmail.com).
