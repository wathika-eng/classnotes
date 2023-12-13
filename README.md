[![Build and deploy Python app to Azure Web App - classnotes](https://github.com/wathika-eng/uninotes/actions/workflows/main_classnotes.yml/badge.svg)](https://github.com/wathika-eng/uninotes/actions/workflows/main_classnotes.yml)

**University Notes Project**


The University Notes Project is a web application designed to streamline the management, sharing, and accessibility of academic notes within a university or educational institution. 
It offers a centralized platform where students and faculty can upload, organize, and access course-related materials, fostering collaborative learning and resource sharing.

**Key Features**

* Note Upload: Users can upload notes, presentations, and study materials in various formats (PDFs, documents, images) for specific courses or subjects.
* Course Management: Organize notes by courses, departments, semesters, or academic years for easy navigation and retrieval.
* User Authentication: Secure user authentication and authorization to manage access control and ensure data privacy.
* Search and Filtering: Robust search functionalities to easily find notes by keywords, course names, or categories.
* Collaborative Sharing: Share notes within study groups, classes, or publicly, promoting collaboration and knowledge exchange.
* Responsive Design: A user-friendly interface accessible across devices, enabling students to access materials anytime, anywhere.


  **Installation**

To use the University Notes Project locally, follow these steps:

* Clone the repository: ```git clone https://github.com/wathika-eng/classnotes```
* Make a virtual environment: ```python -m virtualenv venv```
* Activate the venv: ```source venv/scripts/activate```
* or on Linux: ```source venv/bin/activate```
* Install dependencies: ```pip install -r requirements.txt```
* Set up the database and run migrations: ```python manage.py makemigrations``` ```python manage.py migrate```
* Create superuser ```python manage.py createsuperuser```
* Run the development server: ```python manage.py runserver`


***Script for getting started with Django***
      [![Django script](https://github.com/wathika-eng/resources/blob/main/django)]

**Usage**

Upon installation, users can sign up, log in, and start uploading and managing their notes. They can search for specific courses or subjects, upload materials, create study groups, and collaborate with peers for better academic performance.

**Configuration**

The project uses Django as the primary framework and requires specific configurations for database connections, environment variables for security, and storage options. Refer to the documentation or .env file for configuration details.

**Contributing**

Contributions to the University Notes Project are welcome! Fork the repository, make changes, and submit a pull request following the contribution guidelines specified in the CONTRIBUTING.md file.

**License**

This project is licensed under the MIT License. See the LICENSE file for more details.


Watch how to set-up Email configurations for forgot password:
      https://youtu.be/yuOK6D7deTo - SMTP server https://youtu.be/sFPcd6myZrY - forgot password functionality 

How to host for free on Ngrok:
    https://youtu.be/fE_TXcd2T4g
