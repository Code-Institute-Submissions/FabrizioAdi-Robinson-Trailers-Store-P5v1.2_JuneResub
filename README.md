# Robinson Trailers Store

This is the fifth and last portfolio project for the Code Institute Diploma in Fullstack Software Development and E-Commerce Applications. Web Application Store is dedicated to a real trailers manufacturing company. Located in Portarlington Co. Laoise.
Robinson Trailers is created for customers seeking to purchase trailers online. Users can create accounts and administrators have full write and delete access to all data.

[You can view the deployed site -](https://robinson-trailers-store.herokuapp.com/)

## Table of Contents

### Project Overview
### Agile Workflow
### User Experience

Project goals
Business goals
User Goals
Site Owner goals
Target audience

Strategy
Primary Goals
The site owners primary goals are:
A potential customers primary goals are:

Business Model
Marketing
Search Engine Optimisation

### Structure
Pages
Accessible to all users
Accessible to signed in users
Accessible to Admin users
Pages provided by Django


### Technical Design
Code Structure
Other Directories and files
Database

Data Models
The following models have been used to populate the database and for the site to function as it should:

User - the built in Django User model, facilitates the users basic information

Category - the category in which the product is placed

Brand - the brand of the product

Product - the model for the product itself and its details

Review - a model for users to give the product a rating and a review

Order - a users successful purchase leads to an instance of the Order model being created, storing delivery and user data

OrderLineItem - a model holding the product information for a single product, binding the product model together with the order

UserProfile - the model storing the users product and order information

WishListItem - the customer has the option to save an item, which will then appear in their wish list on the My StepUp page


Schema of models
<Diagrams images>

### Scope - Epics and User Stories
Epic 1: Base functionality and ease of use
Epic 2: Products
Epic 3: The Cart
Epic 4: Checkout
Epic 5: User registration and account
Epic 6: The Wish List
Epic 7: Reviews
Epic 8: Contact
Epic 9: Site Owner functionality
Epic 10: Terms and Policy

### Wireframes
Surface
Colors
Design Choices
Typography

### Existing Features
Feature 1: The Navbar
Feature 2: The Home Page
Feature 3: The Footer
Feature 4: The Products List
Feature 5: The Product Detail Page
Feature 6: The Cart
Feature 7: The Checkout Page
Feature 8: The Order Successful Page
Feature 9: The Sign Up/In/Out Pages
Feature 10: My StepUp
Feature 11: The Wishlist
Feature 12: The Contact Page
Feature 13: The Admin Features
Feature 14: The Django Admin

### Features Yet to Implement
### Technologies Used
#### Languages
Python 3.8 was used for backend of the project.
HTML5 was used for building all web pages.
jQuery is used for implementation of Bootstrap.
CSS3 used for styling the website.
JavaScript for alert and location fnunctionality.

#### Frameworks, Libraries and Other Resources
This project is built through the framework Django.

GitPod is used to develop the project. All code was written and tested with the Gitpod web-based IDE.
Git control system was used for version control to commit to Git and push to GitHub.
GitHub projects repository is used to host the project.
Heroku is used to host the project/Used to deploy the application.
Bootstrap 5 as a framework used for styling.
Pip3 is used for installing the necessary tools, libraries and frameworks.
Spycopg2 is used to enable the PostGreSQL database to connect with Django.
AWS Amazon used to store static and media files.(CSS and JavaScript)
Boto3 is used for compatibility in AWS.
Gunicorn is used to enable deployment to Heroku.
Google Fonts is used to provide the font roboto for all the text that is used in the project.
Font Awesome fonts were used for all icons in this project.
Figma/Balsamiq used to create the mockup designs for the project.
Django Crispy Forms is used to style the Django forms

I have used Bootstrap 4 as a framework for styling for efficiency purposes.

The JavaScript framework JQuery was used to minimize written code.

Font Awesome fonts were used for all icons in this project.

Google Fonts - Were used for all fonts in this project.

Facebook Pages was used to create the Facebook Business Page that is linked on the site.

Mailchimp was used to create the newsletter signup form.

Git - Version control system used to commit and push to Github via Gitpod.

Github - The projects repository and all its branches were commited, and pushed to Github.

Heroku - Used to deploy the application.

AWS S3 Bucket - Used to host media (images) and static(CSS and JavaScript) files for the site.

Stripe - Used to process the users payments and handle webhooks.

Gitpod - All code was written and tested with the Gitpod web-based IDE.

Balsamiq Wireframes was used to create wireframe images of the website which you can view here.

Lucidchart was used to create the visual model schema of the project.

#### Database
PostgreSQL is used as the production database.
SQlite3 is used as the development database.
### Testing
### Other Services
Stripe

### Validation
Chrome DevTools is used to detect problems and test responsiveness.
Autoprefixer is used to parse the CSS and to add vendor prefixes to CSS rules.
W3C Markup Validation Service is used to check whether there were any errors in the HTML5 code.
W3C CSS validator is used to check whether there were any errors in the CSS3 code.
JShint is a JavaScript validator that is used to check whether there were any errors in the JavaScript code.
PEP8 validator is used to check whether there were any errors in the Python code.
PEP8 Validation

HTML Validation

CSS Validation

Performance/Accessibility

Devices

Testing for User Stories

### Deployment
GitHub Repository

1. Access your GitHub account and find the relevant repository.
2. Click on 'Fork' on the top right of the page.
3. You will find a copy of the repository in your own Github account.

Making a Local Clone

1. Access your GitHub account and find the relevant repository.
2. Click the 'Code' button next to 'Add file'.
3. To clone the repository using HTTPS, under clone with HTTPS, copy the link.
4. Open Git Bash.
5. Access the directory you want the clone to be have.
6. In your IDE's terminal type 'git clone' and the paste the URL you copied.
7. Press Enter.
8. You now have a local clone.

Heroku

1. Create an account at heroku.com
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars, add your sensitive data (creds.json for example)
6. For this project, I set buildpacks to and in that order.
7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
8. Enter your repository name and click on it when it shows below
9. Choose the branch you want to buid your app from
10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository

Manualy deploy to heroku from gitpod workspace.

1. Open the terminal.
2. For those of you who are using MFA/2FA: please scroll down to see the additional steps required.
For those of you not using MFA/2FA: Log in to Heroku and enter your details.
command: heroku login -i
3. Get your app name from heroku.
command: heroku apps
4. Set the heroku remote. (Replace <app_name> with your actual app name and remove the <> characters)
command: heroku git:remote -a <app_name>
5. Add and commit any changes to your code if applicable
command: git add . && git commit -m "Deploy to Heroku via CLI"
6. Push to both GitHub and Heroku
command: git push origin main
command: git push heroku main

AWS S3
1. Create an account at aws.amazon.com
2. Navigate to the IAM application and create a user and group
3. Set the AmazonS3FullAccess for the user and copy the AWS ACCESS and SECRET keys as config vars to your workspace and deployment environment
4. Create a new Bucket within the S3 application with an appropriate name.
5. Enable public access for your bucket so users can access and use the services on your website (upload, view, download, etc.
More info can be read in the official documentation: https://aws.amazon.com/s3/

Google API

1. Login or create a Google account and navigate to https://console.cloud.google.com/
2. Create a new Project by clicking on the New Project icon
3. Add Project name and details
4. Under API's and services, enable the relevant API for your project (in this case Google Drive, Sheets and Calendar)
5. IF the API requires, create a credential (service account in this case) for your project
6. Save the API key as a secret in config vars in your workspace and deployment environment
7. Under API's and services, enable the relevant API for your project (in this case Google Drive, Sheets and Calendar)
8. Search for the needed tasks to be performed in the documentation for the specific API, for example here for the calendar API: Google Maps API Reference
9. Add them to your code.

### Performance
Performance was tested using Google Chrome's Lighthouse tool in DevTools built into the browser. The performance tests can be viewed

### Accessibility

### Bugs

### Credits
Reference
Websites, movies that I used while working on the project.

Copyrights
Coding Tips and Tricks
Acknowledgments

