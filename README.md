# iHealthy Nutrition

![image](https://github.com/Giov3ss/iHealthy/assets/112728772/86e85c5a-39f3-4b28-930c-a0840c303b4d)

## live site goes here

This project is built using Django framework, along with PostgreSQL, Python, HTML, CSS and JavaScript. iHealthy is an appointment booking website that connects users with our professional nutritionists. With the ability to make, edit, and delete appointments, user can easily manage their schedules. This project has been developed for educational purposes.

## Autor
Giovani Fonseca

# Table of Contents
<details>
<summary>Table of Contents</summary>

* [UX](#ux)
    * [Target Audience](#target-audience)
    * [Design Choices](#design-choices)
        * [Colors](#colors)
        * [Typography](#typography)
        * [Images](#images)
        * [Frameworks](#frameworks)
        * [Custom Javascript](#custom-javascript)
    * [Strategy](#strategy)
    * [Wireframes](#wireframes)
* [Information Architecture](#information-architecture)
    * [Entity Relationship Diagram](#entity-relationship-diagram)
    * [Database Choice](#database-choice)
    * [Data Models](#data-models)
    * [CRUD Diagrams](#crud-diagrams)
* [Agile Methodology](#agile-methodology)
    * [Project Goals](#project-goals)
    * [User Stories](#user-stories)
* [Structure](#structure)
    * [Database](#database)
    * [Skeleton](#skeleton)
    * [Surface](#surface)
* [Features](#features)
    * [Home Page](#home-page)
    * [Appointments](#appointments)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
    * [Code Validation](#code-validation)
    * [Manual Testing](#manual-testing)
* [Bugs and Fixes](#bugs-and-fixes)
    * [Fixed Bugs](#fixed-bugs)
    * [Unfixed Bugs](#unfixed-bugs)
* [Deployment](#deployment)
    * [Github & Gitpod](#github-&-gitpod)
    * [Forking the Github Repository](#forking-the-github-repository)
    * [Making a Local Clone](#making-a-local-clone)
    * [Deployment to Heroku](#dployment-to-heroku)
* [Credits](#credtis)
</details>
<hr>

## UX
iHealthy is a platform for booking appointments with nutritionist, it allows user to select from a variety of reasons for their appointment, such as weight loss, weight gain, better healthy, meal planning, nutrition education or other. The site is designed to be easy to navigate, with a clear and simple layout. iHealthy offers a user-friendly appointment booking system that allows users to easily book appointments with their preferred nutritionist. User can easily register or loign to their account and access the appointment booking form with just a few clicks. The design features a light blue and white color scheme, creating a clean and inviting look.

### Target Audience
iHealthy is for anyone who is interested in improving their health and nutrition, regardless of gender or age. This could include individuals looking to lose or gain weight, athletes seeking to optimize their performance through nutrition, people with specific health conditions or anyone simply looking to adopt a healthier lifestyle.

### Design Choices
- ### Colors
<img width="951" alt="image" src="https://user-images.githubusercontent.com/112728772/235238056-ab23dafc-1325-46be-8f86-86335cd508e6.png">
All the colors is designed to create a calming and inviting atmosphere for users of the iHealthy. The soft shades of gray and white provide a clean and minimalist backdrop for the more vibrant and green and tan colors, which symbolize growth, health and balance.

- ### Typography
<img width="1110" alt="image" src="https://user-images.githubusercontent.com/112728772/235248226-ec43c4aa-f1b4-46d1-b95f-8d4426510f2b.png">
The font choice of Lato, sans-serif for my website is a good choice due to its readability on both desktop and mobile devices. For headers, I chose a larger font size to emphasize important information, while general text uses a smaller font size for easier reading. The font type and size choices tie into the user experience by making the website easy to read and navigate, which is important for user satisfaction.

### Images
Icons and images are an important part of website design as they can help convey information quickly and visually. I chose to use social icons such as Facebook, Twitter and Instagram to make it easy for users to connect with the business on their preferred social media platforms. The Hero image aligns with the theme of promoting healthy nutrition and crates an appealing visual representation of the services. The pictures of the nutricionists were included to give users a sense of familiarity and trust, as well as to introduce them to the team behind the business.

### Frameworks
I chose to use Bootstrap for my website because it allowed me to quickly and easily create a responsive design that works well on different devices. the pre-designed templates and components also helped me to save time in the development process.

### Custom Javascript
**** PUT THE CODE HERE *****
This code is used to automatically remove alert messages from the DOM after a certain amout of time, improving the user experience by reducing clutter and distractions on the page. 

### Strategy
The strategy for the iHealthy site is to follow the core UX principles in design thinking, which includes creating a persona profile user Code Institute template. This profile will help guide the design process to ensure that the website meets the needs and preferences of the target users. The site aims to provide all the necessary feature for the persona while ensuring intuitive navigation and ease of use, the design is resposive using Bootstrap grid, cards, elements and custom CSS.

### Wireframes 

- Mobile 
<img width="299" alt="image" src="https://user-images.githubusercontent.com/112728772/236647700-e6e5fc72-7690-4572-a17e-a8faa3031804.png">

<img width="298" alt="image" src="https://user-images.githubusercontent.com/112728772/236647712-d24bbdbd-e739-461b-9738-d5886cae484c.png">

<img width="305" alt="image" src="https://user-images.githubusercontent.com/112728772/236647722-f62eb25c-8b91-4a86-9ff0-4b0d68aca9a7.png">

<img width="233" alt="image" src="https://user-images.githubusercontent.com/112728772/236647733-434aea3b-3c3d-4518-8bcf-03d0df81abcf.png">

- Desktop
<img width="596" alt="image" src="https://user-images.githubusercontent.com/112728772/236647750-55153b39-5910-4e58-ae09-abbba35ef3bc.png">

<img width="593" alt="image" src="https://user-images.githubusercontent.com/112728772/236647753-9e96ce8e-a59c-44b6-a67d-5bea6b26ff27.png">

<img width="443" alt="image" src="https://user-images.githubusercontent.com/112728772/236647759-db57b843-ddcd-4079-aa62-18517d262918.png">

<img width="444" alt="image" src="https://user-images.githubusercontent.com/112728772/236647766-70413afe-5ae6-4354-82c1-3e25d5aacd32.png">

## Information Architecture

For the iHealthy website, I have implemented a customer data model called "Appointment" in Django. The Appointment model represents a user's appointment for a nutrition session. Here is how the data model is structured:

 - User: This is a foreign key to built-in User model provided by Django's authentication system. It represents the user who has scheduled the appointment.
 - Date: This field stores the date of the appointment.
 - Time: This field stores the time of the appointment.
 - Reason: This field represents the reason for the appointment and is implemented as a choice field with predefined options. The available options are: Weight Loss, Weight Gain, Better Healthy, Meal Plan, Nutrition Education and Other.

The CRUD functionality is achieved through Django's model forms and views. The website provides appropriate forms and views to create, display, update, and delete appointments, ensuring a seamless user experience when managing their nutrition appointments, providing a convenient and efficient way to manage their health goals.

### Entity Relationship Diagram
![mermaid-diagram-2023-05-15-211715](https://github.com/Giov3ss/iHealthy/assets/112728772/87b8397c-ecb9-4c3b-a25f-1ec13716ff3f)

### Database Choice
I used PostgreSQL as the database for this project. Hosting the application on Heroku allows for easy deployment and scalability, and PostgreSQL is one of the supported and recommemdede databases on the Heroku platform.

### Data Models

#### Fields:
- 'user' (ForeingKey to User model): The user associated with the appointment. 
- 'date' (DateField): The date of the appointment.
- 'time' (TimeField): The time of the appointment.
- 'reason' (CharField with choices): The reason for the appointment.
Valid choices include:
 - Weight Loss
 - Weight Gain
 - Better Healthy
 - Meal Planning
 - Nutrition Education
 - Other
- 'nutritionist' (CharField with choices): The assigned nutritionist for the appointment.
Valid choices include:
 - Anna Smith
 - John Doe

#### Validation:
- 'user': Required field, as it represents the user associated with the appointment.
- 'date': No specific validation. 
- 'time': No specific validation. 
- 'reason': Required field, with predefined choices. The default choice is "Weight Loss"
- 'nutritionist': Required field, with predefined choices. The default choice is "Anna Smith".

#### CRUD Operations: 
- Create: An appointment is created when a user schedules a new appointment. The user selects the date, time, reason and nutritionist from the available options.

- Read: The appointments table is read when displaying the user's scheduled appointments. The appointments are retrieved based on the user's ID.

- Update: Appointments can be updated when a user reschedules an existing appointment. The user can modify the date, time, reason and nutritionist for the appointment.

- Delete: Appointments can be deleted if a user cancels their scheduled appointment.

### CRUD Diagrams
![mermaid-diagram-2023-05-15-220416](https://github.com/Giov3ss/iHealthy/assets/112728772/91a9b38f-6666-4b76-ba3e-5438fae99e01)

## Agile Process

### Project Goals
The purpose of the iHealthy website is to provide a convenient platform for users to schedule appointments with nutritionist. The website aims to steamline the process of connecting users with qualified professionals to receive personalized nutrition guidance and support.

For users:
- Easily navigate the website to fing nutritionists and their availability.
- Schedule appointments with nutritionists based on their preferred date and time. 
- Provide necessary information and health details for nutritionist's assessment.
- Access secure and private storage of their personal and health-related information. 

For administrators:
- Update and maintain the appointment scheduling system. 
- Monitor and track user appointments and ensure efficient communication between users and nutritionists. 
- Implement necessary security measures to protect user data and privacy.

### User Stories:
- As a visitor, I want to register an account so that I can access personalized features and manage my appointments effectively.
- As a user, I want to log in to my account so that I can securely access my appointments and personalized information. 
- As a user, I want to book an appointment with a nutritionist providing necessary details such as my preferred date and time.
- As a user, I want to choose a nutritionist from a list of available options so that I can select the one who best suits my needs. 
- As a user, I want to select the date and time for my appointment using user-friendly interface, such as a date picker or dropdowns, so that I can easily choose a suitable time slot.
- As a user, I want to update the detail of an appointment, such as the nutritionist, date, time or reason, so that I can make changes if necessary.
- As a user, I want to delete an appointment that I no longer need so that it does not clutter my schedule.
- As a user, I want to view my appointment details, allowing me to track my appointments.
- As a user, I want to view the details of an appointment, including the nutritionist's name, appointment date, time and reason, so that I can review the information before the consultation.
- As a user, I want to have a user-friendly interface that guides me through the appointment booking process and provides clear instructions on how to correct any errors or issues with form submission. 
- As a user, I want my personal information and appointment details to be securely stored and kept private, ensuring the confidentiality of my healthcare-related data. 
- As an admin, I want to log in to the admin panel so that I can access the administrative features of the website.
- As an admin, I want to view a list of all appointments made by users so that I can see an overview of the scheduled consultations.
- As an admin, I want to view the details of a specific appointment, including the user's name, selected nutritionist, appointment date, time and reason, so that I can gatherall the necessary information.
- As an admin, I want to delete an apppointment made by a user if it is no longer required or if the user requests its removal, so that the appointment schedule remains accurate and updated, ensuring better organization and resource management, and providing a satisfactory user experience.
- As an admin, I want to add a new appointment on behalf of a user if it is requested or necessary, providing user's name, selected nutritionist, appointment date, time and reason, so that the user's appointment needs are met, the schedule is properly managed and the user receives the necessary services and support.
- As an admin, I want to delete a user's account if requested or if it violates the website's policies, ensuring that their personal information is securely removed, so that the user's data privacy is protected, the website maintains compliance with policies and regulations, and the overall integrity and security of the platform are maintained. 


![image](https://github.com/Giov3ss/iHealthy/assets/112728772/fe7f0ffd-1840-4e50-afc8-08bf7c4075ec)

