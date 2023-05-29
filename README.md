# iHealthy Nutrition

![image](https://github.com/Giov3ss/iHealthy/assets/112728772/86e85c5a-39f3-4b28-930c-a0840c303b4d)

## Click [here](https://ihealthy.herokuapp.com/) to live site.

---

This project is built using Django framework, along with PostgreSQL, Python, HTML, CSS and JavaScript. iHealthy is an appointment booking website that connects users with our professional nutritionists. With the ability to make, edit, and delete appointments, user can easily manage their schedules. This project has been developed for educational purposes.

## Autor
### Giovani Fonseca

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
    * [Feasibility vs Importance](#feasibility-vs-importance)
    * [Scope](#scope)
    * [Agile Tool](#agile-tool)
        * [User Story Template](#user-story-template)
        * [Epic Stories](#epic-stories)
* [Structure](#structure)
    * [Database](#database)
    * [Skeleton](#skeleton)
    * [Surface](#surface)
* [Features](#features)
    * [Home Page](#home-page)
    * [Sign Up Page](#sign-up-page)
    * [Login Page](#login-page)
    * [Home Page - If the user is authenticated](#home-page---if-the-user-is-authenticated)
    * [Appointment List](#appointment-list)
    * [Create Appointment](#create-appointment)
    * [View Appointment Details](#view-appointment-details)
    * [Update Appointment](#update-appointment)
    * [Delete Appointment](#delete-appointment)
    * [NavBar](#navbar)
    * [NavBar Mobile](#navbar-mobile)
    * [Messages Display](#messages-display)
        * [Sign in Message](#sign-in-message)
        * [Logout Message](#logout-message)
        * [Date cannot be in the past](#date-cannot-be-in-the-past)
        * [Appointment Created Message](#appointment-created-message)
        * [Appointment Updated Message](#appointment-updated-message)
        * [Confirm Appointment Deletion Message](#confirm-appointment-deletion-message)
        * [Appointment Deleted Sucessfully Message](#appointment-deleted-sucessfully-message)
        * [Conflicts Date/Time/Nutritionist Appointments Message](#conflicts-datetimenutritionist-appointments-message)
        * [Admin Panel/Superuser](#admin-panel-superuser)
    * [403 Page](#403-page)
    * [404 Page](#404-page)
    * [500 Page](#500-page)
* [Future Features](#future-features)
* [Testing](#testing)
* [Manual Testing](#manual-testing)
* [Compatibility and Responsive Testing](#compatibility-and-responsive-testing)
* [Accessibility Testing](#accessibility-testing)
    * [Accessibility Audits](#accessibility-audits)
* [Validation Testing](#validation-testing)
    * [CSS Validation](#css-validation)
    * [HTML validation](#html-validation)
    * [JavaScript Validation](#javascript-validation)
    * [Python Validation](#python-validation)
* [Defects](#defects)
* [Defects of Note](#defects-of-note)
* [Outstanding Defects](#outstanding-defects)
* [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
* [Deployment](#deployment)
    * [Prerequisites](#prerequisites)
    * [Forking the Github Repository](#forking-the-github-repository)
    * [Making a Local Clone](#making-a-local-clone)
    * [Production Deployment](#production-deployment)
* [Credits](#credtis)
* [Media](#media)
* [Acknowledgments](#acknowledgments)
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
- [JS Code - Appointments](static/js/appointments.js)
- [JS Code - Messages](static/js/messages.js)

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
- 'user': Required field, as it represents the user associated with the appointment, is also auto associated based on the user being logged in, you cannot create an appointment unless your are logged in.
- 'date': The form widget doesn't allow the user pick past dates and only gives 30 days of dates to pick from.
- 'time': The time interval is set by the javascript to only allow appointments for 1 hour starting at 10:00am - 18:00pm.
- 'reason': Required field, with predefined choices. The default choice is "Weight Loss"
- 'nutritionist': Required field, with predefined choices. The default choice is "Anna Smith". 
- Once a nutritionist is selected and a date/time submitted, the database of appointments is checked to make sure there is no conflict.

#### CRUD Operations: 
- Create: An appointment is created when a user schedules a new appointment. The user selects the date, time, reason and nutritionist from the available options. A user must be logged in to create an appointment. A custom clean function was built on the Appointment Form to make sure there is not an existing appointment for the nutritionist at the given time. The form also makes sure the date isn't in the past in the event that the user tries to hack data being set.

- Read: The appointments table is read when displaying the user's scheduled appointments. The appointments are retrieved based on the user's ID.

- Update: Appointments can be updated when a user reschedules an existing appointment. The user can modify the date, time, reason and nutritionist for the appointment. Like create, conflicts are checked to make sure the user isn't double booking the nutritionist unless it's the appointment they are updating. There is also a check that the user can only update their own appointments.

- Delete: Appointments can be deleted if a user cancels their scheduled appointment. User can only delete appointments they have created, not another user's appointment, if they try to hack the url with a different id. 

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

### Feasibility vs Importance

![image](https://github.com/Giov3ss/iHealthy/assets/112728772/fe7f0ffd-1840-4e50-afc8-08bf7c4075ec)

### Scope

To align the project goals with the available resources and skill set, the scope has been refined to focus on delivering a MVP that prioritizes essential features and functionality. The MVP will include the following key user stories:
- As a user, I want to register an account so that I can access personalized features and manage my appointments effectively.
- As a user, I want to choose a nutritionist from a list of available options so that I can select the one who best suits my needs.
- As a user, I want to be able to schedule an appointment with a nutritionist by selecting a date, time and reason.
- As a user, I want to be able to view details of my appointments, such as nutritionist's name, reason, date and time.
- As a user, I want to be able to update or delete my appointments.
- As an admin, I want to be able to view a list of user appointments and manage them.
- As an admin, I want to be able to delete user accounts if necessary, ensuring the removal of personal information. 

By focusing on these core features, the MVP will provide users with the ability to register, schedule appointments and manage their appointments. The admin will have the tools to oversee appointments and perform adminitrative tasks.

### Agile Tool
#### User Story Template
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/b20ffaac-2629-4f1c-85ce-ba27b8ebfbc1)
- [Agile Tool](https://github.com/users/Giov3ss/projects/3)

## Features
### Home Page
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/8b9aa9aa-9e7c-42b8-9e68-6b6624b4a9d5)
- The home page of iHealthy features a captivating hero image with a welcoming message, "Welcome to iHealthy". It provides an overview of the platform's features, services, and benefits. The prominent "Book Now" button enables users to quickly register or log in, ensuring easy access to iHealthy's comprehensive health and wellness services. 

### Sign Up Page
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/30b3eca1-be14-4f12-a1c1-1d4f1fba4126)
- The sign-up page allows new users to create an account on the iHealthy website. User can provide their personal information, such as name, email address (optional) and password, to register abd gain full access to the platform's features. During the registration process, the user is required to provide a unique user ID. The system ensures that the user ID is not repeated, thereby maintaining uniqueness among all registered users, In addition, the system checks whether the password is strong and warns you if the password is too short or too common. This ensures that users choose a strong and secure password.

### Login Page
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/df298fc9-a080-4edf-a658-7d67b55b468b)
- The login page provides a form where registered users can enter their credentials (username and password) to log into iHealthy accounts. Once logged in users can access their personalized information and utilize the functionalities of the website. 

### Home Page - If the user is Authenticated
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/15df4461-f368-4bed-b13f-a0c612cadc23)
- This version of the home page is displayed when a user is authenticated and logged into their iHealthy account. The user can have access of their appointment just clicking in the navbar "Appointments" section.  

### Appointment List
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/731326d8-7fe1-45f3-ac4d-7908b01c4a92)
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/63ccff7e-c0a6-4085-b75b-1c306af892f0)
- The Appointment list page presents a list of all the appointments schedule by the user. It provides a brief overview of each appointment, incluiding details like date, time and nutritionist name. Users can view, update or delete appointments from this page just clicking in the icons on the right of the details, when the user performs actions such as updating, creating or deleting appointments, informative messages are displayed on the Appointment List page. These messages confirm the success of the action and provide a relevant feedback in case of errors or issues.
- Also if the user doesn't have any appointments scheduled, a special condition is implemented to handle this scenario. A message is displayed on the page to inform the user that there are "No Appointments found.". This ensure clarity and provides guidance on how to proceed, such as "Create Appointment" button.


### Create Appointment
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/52a47d93-cba8-420f-8eda-78971366f823)
- The create feature allows users to schedule a new appointment with a nutritionist. Users can select the desired date, time, nutritionist and provide a reason for the appointment. Upon submission, the appointment is added to the user's appointment list. If the selected time for the appointment are already booked by another user, a message displayed on the Create Appointment page to inform the user that the choosen slot is not available.
- To ensure that the appointments are scheduled for future dates, a warning message is displayed on the Create Appointment page if the user selects a past date, as a reminder to choose a valid and future date for the appointment.
- Access to the Create Appointment page is restricted to authenticated user only. If a user is not logged in, they will be prompted to log in or create an account before being able to access the page.

### View Appointment Details
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/673020c4-8e3f-45b5-83df-db21e2496b81)
- This feature enables users to view the details of a specific appointment. It displays comprehensive information about the appointment, incluiding the date, time, nutritionist and reason. 

### Update Appointment
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/04a403b9-c0ed-46ab-9df5-a35bc1a315dc)
- User can use the update appointment feature to modify the details of an existing appointment. They can change the appointment date, time, nutritionist and reason. If the selected date, time and nutritionist have already been booked by another user, a message is displayed on the Update Appointment page to inform the user that chosen is not available.
- To ensure that the appointments are updated for future dates, a warning message is displayed on the Update Appointment page if the user selects a past date, as a reminder to choose a valid and future date for the appointment modification.
- Access to the Update Appointment page is restricted to authenticated user only. If a user is not logged in, they will be prompted to log in or create an account before being able to access the page. In addition to being logged in, the user must be the owner of the appointment to access the Update Appointment page. This prevents unauthorized user from modifying appointments that do not belong to them and ensures that only the appointment creator can make changes. 

### Delete Appointment
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/ff746b6c-881a-4b14-8dd9-f8d22b43647a)
- The delete appointment feature allows users to remove an appointment from their schedule. It prompts the user to confirm the deletion before permanently removing the appointment from their list. 
- Access to the Delete Appointment page is restricted to authenticated user only. If a user is not logged in, they will be prompted to log in or create an account before being able to proceed with the deletion.In addition to being logged in, the user must be the owner of the appointment in order to delete it. This security measure prevents unauthorized deletion of appointments that do not belong to the user. Only the user who created the appointment can access the Delete Appointment page and initiate the deletion process.

### NavBar 
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/2cd79574-6500-43b4-88fb-33a518a7db08)
- The navbar provides a quick access to essential features of the iHealthy website such as, Home, Register and Login if the user is not authenticated. 

### NavBar - if the user is Authenticated 
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/6a5e18b8-30fc-4a4b-a9f0-e5f7dd0faeaa)
- The navbar provides a quick access to essential features of the iHealthy website such as, Home, Logout and Appointments if the user is authenticated. 

### Navbar mobile
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/e2fd2347-b033-4163-9ed3-05a456026725)
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/8ef97d6a-8d4c-4f53-9906-3afcf3cd6c3c)
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/10f0d5b0-a64b-4754-87be-ffae2eb68945)
- The Navbar is fully responsive, collapsing into a hamburguer menu when the screen size becomes smaller.
- From the Navbar the user has option to register or login into their account. 
- Once the user is authenticated, logout and appointments sections will appear. 

## Messages Display
### Sign in Message
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/675273ca-3ff4-45fc-a875-6175cbb0de89)
- After successful registration or login, it will pop up in the screen a successful message, alert the user is login into their account.

### Logout Message
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/a6c9826d-9211-4b0a-b8f1-9a9b5ade5e70)
- When the user logs out their iHealthy account, it will pop up in the screen a logout message to acknowledge the successful logout.

### Date cannot be in the past 
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/343a849a-b988-4937-a538-7eaa5cb4fa03)
- This message is displayed when a user attempts to book an appointment with a date that has alrady passed. It serves as a validation to ensure that appointments are scheduled for future dates only. 

### Appointment Created Message
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/d59d6ce0-d840-42a4-9e45-1035294005aa)
- This message confirms the succesful creation of an appointment and provides a positive feedback to the user, indicating that the appointment has been successfully scheduled.

### Appointment Updated Message
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/3148c0e1-12df-4fb7-9c7f-806d9c15d4ca)
- This message is displayed when an existing appointment is successfully updated with new information. It informs the user that their changes have been saved. 

### Confirm Appointment Deletion Message
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/56a7be92-33f7-4333-a8ee-cf7153349872)
- This message prompts the user to confirm their intention to delete an appointment. It includes option such as "Yes, delete" and "No, go back", allowing the user to make a decision regarding the deletion.

### Appointment Deleted Sucessfully Message
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/ca3d40f8-5606-4784-a8ba-971b3f71efd5)
- This message is shown after an appointment has been sucessfully deleted. It serves as a confirmation to the user that the appointment has been removed from their schedule.

### Conflicts Date/Time/Nutritionist Appointments Message
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/efda6fe8-1514-4e9f-8fde-31ab60ea7582)
- This message appears when a user tries to create an appointment that conflicts with an existing appointment in terms of date, time and nutritionist of another user. It alerts the user about the conflict, so they can choose another time, date or nutritionist. 

### Admin Panel/ Superuser 
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/9e78bb95-87fe-4126-aa86-1783b9961e4e)
- On the Admin Panel, as an admin/superuser I have full access to CRUD functionality so I can view, create, edit and delete the appointments or users. 

### 403 Page 
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/cc564011-718a-47bb-865c-ae855fd46467)
- The 403 Page is displayed when a user tries to access a page or resource for which they do not have the necessary permissions. It provides a user-friendly message indicating that the access is forbidden, along with suggestions with a link on click "Here" to help the user navigate back to a valid page.

### 404 Page
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/c30aa744-06a2-4105-9b22-f4e2245a0fa8)
- The 404 Page is displayed when a user tries to acces a page or resource that does not exist. It provides a user-friendly message indicating that the requested page could not be found, along with suggestions with a link on click "Here" to help the user navigate back to a valid page.

### 500 Page
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/fe9515e9-cb65-41df-bf85-281207dfab70)
- The 500 Page is displayed when an internal server error occurs, indicating that there was an issue with the server that prevented it from fulfilling the request. It provides a user-friendly message acknowledging error, along with suggestions with a link on click "Here" to help the user navigate back to a valid page.


## Future Features
- **Improved business logic:** Make sure user's can't book themselves twice.
- **Personalized Meal Plans:** Allow users to generate personalized meal plans based on their dietary perferences and goals, this can include, meal suggestion, recipes and shopping list.
- **Fitness Tracking:** Integrate fitness tracking capabilities into the platform, allowing users to track their physical actives, set fitness goals and monitor their progress.
- **Community Forums:** A community where the users can engage discussions, share their experience, ask question and seek advice from nutritionist and fellow users.
- **Integration with Health Devices:** This integration will allow users to seamlessly sync their health data with the iHealthy platform for a more comprehensive health tracking experience, for example: smart scales and blood pressure monitors.
- **Recipe Repository:** Build a respository of healthy recipes that users can access for meal inspiration, or even submit their own recipes to contribute to the community. 
- **iHealthy Elements:** Incorporate elementes into the platform to make the health and wellness journey more engaging and motivating. This can include challenges, achievements and rewards for reaching health milestones or consistently following healthy habits. 
- **Mobile App:** Create a mobile app to iHealthy, providing users with convenient access to their appointments, meal plans, fitness tracking and other features on their smartphone. 
- **Language Support:** Support to cater to a wider user base, allowing users from different regions and languages preferences to access and use the iHealthy platform. 

## Testing
In the Testing section of the README, I extensively conducted manual testing to ensure the functionality and usability of the iHealthy website. The manual testing process involved following predefined scenarios and documenting the results using a custom issue template on GitHub.
To view the detailed testing results, please [CLICK HERE](https://github.com/Giov3ss/iHealthy/issues).

## Manual Testing
### Manual Testing Register:
- [Register](https://github.com/Giov3ss/iHealthy/issues/29)
- The Sign Up page displays a registration form with required fields.
- Upon successful submission of the form, a new user account is created.
- Registering with valid information display a success message.
- Logging in with the registered username and password display a success message.
- The user is redirected to the authenticated user's Home page after registration.
- Registering with an already registered email displays an error message.
- Registering with invalid information displays relevant error message.
- In case of invalid inputs or errors, appropriate error messages are displayed to guide the user is correcting the information.
- User that's logged in gets redirected to home page if they try to use a register bookmark.   

### Manual Testing Login:
- [Login](https://github.com/Giov3ss/iHealthy/issues/30)
- The login page displays a login form with fields for username and password.
- Logging in with the registered username and password display a success message.
- Incorrect credential display an error messsage indicating invalid credentials.
- Leave the username or password field empty display an error message, indicating that fields is required.
- The user session is managed correctly, allowing the user to access authenticated features and pages without having to log in repeatedly. 
- User that's logged in gets redirected to home page if they try to use a login bookmark.

### Manual Testing Create Appointment:
- [Create Appointment](https://github.com/Giov3ss/iHealthy/issues/33)
- Fill all the required fields such as date, time, reason and nutritionist with valid inputs, the appointment is create successfully and a success message displayed on the screen. 
- Leave any required fields empty an error message appear on the screen.
- Choose a past date for the appointment and submit the form, an error message is displayed on the screen.
- Conflicts of dates, times and nutritionist with existing appointments, an error message is displayed on the screen.
- The created appointment is successfully saved and displayed on the appointment list page with accurate information.  
- User that's not logged in gets redirected to login page if they try to use a login bookmark.

### Manual Testing View Appointment Details:
- [View Appointment Details](https://github.com/Giov3ss/iHealthy/issues/34)
- The appointment details page accurately display all the relevant information of the selected appointment, such as, nutritionist name, reason, date and time.
- The "Back to appointment list" button is available on the details page and successfully navigates the user back to the appointment list.
- Users that's logged out gets redirected to home page if they to user bookmark.

### Manual Testing Delete Appointment:
- [Delete Appointment](https://github.com/Giov3ss/iHealthy/issues/36)
- The user is redirected to a confirmation page before deleting an appointment.
- The appointment is successfully deleted from the system when the user chooses "Yes, delete".
- The user is redirected to the appointment list page after successful deletion.
- Appropriate success message are displayed to indicate the successful deletion of the appointment,
- The appointment remains unchanged in the system when the user chooses "No, go back"
- The user is redirected back to the appointment list page without any changes.
- Only user that owns a given appointment can delete it.
- User that's not logged in gets redirected to logi page if they try to user a delete appointment bookmark.

### Manual Testing Appointment List:
- [Appointment List](https://github.com/Giov3ss/iHealthy/issues/32)
- The appointment list page successfully retrieves and display the user's appointments.
- Each appointment is presented with accurate and complete relevant information such as date and time.
- The Appointment list display buttons for each appointment: View, Update and Delete
- The user is redirected to the appointment details page for the selected appointment.
- The Appointment details page display information about the appointment, such as nutritionist, reason, date and time.
- The appointment update page allows the user to modify the appointment details, such as, nutritionist, reason, date and time.
- The user can make changes to the appointment and save the updates.
- The user is prompted to confirm the deletion of the selected appointment.
- If the user confirms the deletion, the appointment is successfully removed from the list.
- The user can create new appointments, which are then displayed on the appointment list.
- Appointments are present with all relevant information for easy reference.
- User that's not logged in gets redirected to login page if they try to use bookmark to the appointments page.
- If the user doesn't have any appointments they see a customize message in the screen. 

### Manual Testing Update Appointment: 
- [Update Appointment](https://github.com/Giov3ss/iHealthy/issues/35)
- The appointment update form allow the user to edit and update the details of an existing appointment.
- The updated appointment is successfully saved and reflected in the system.
- The appointment update page allows the user to modify the appointment details, such as, nutritionist, reason, date and time.
- The user can make changes to the appointment and save the updates.
- Validation is performed on the inputs, and appropriate error messages are displayed for invalid or missing information.
- User that's not logged in gets redirected to login page if they try to use bookmark to the update appointments page.

### Manual Testing Home Page Authenticated User:
- [Home Page Authenticated User](https://github.com/Giov3ss/iHealthy/issues/31)
- After logging in, the home page display personalized content, including in the appointment section in the NavBar.
- Logging out successfully logs the user out and user has no access to authenticated user-specific pages or features.
- Display of a message on the screen alerting the user that his logout was successful.

### Manual Testing NavBar Authenticated User:
- [NavBar Authenticated User](https://github.com/Giov3ss/iHealthy/issues/38)
- The Home link is displayed in the NavBar.
- The Logout link is displayed in the NavBar.
- The Appointments link is displayed in the NavBar.
- Navigation links in the NavBar correctly redirect to the intended pages.
- Clicking in the Home link redirect to the home page.
- Clicking on the Logout link, the user is logged out and a message is displayed on the screen alerting the user that he/she has successfully logged out.
- Clicking on the appointments link the user is redirect to the appointments list page.
- The menu in the NavBar functions properly on different devices.
- The NavBar is responsive and accessible on different screen sizes.

### Manual Testing NavBar Unauthenticated User:
- [NavBar Unauthenticated User](https://github.com/Giov3ss/iHealthy/issues/37)
- The Home link is displayed in the NavBar.
- The Register link is displayed in the NavBar.
- The Login link is displayed in the NavBar.
- Navigation links in the NavBar correctly redirect to the intended pages.
- The menu in the NavBar functions properly on different devices.
- The NavBar is responsive and accessible on different screen sizes.

### Manual Testing Home Page and Welcome Message:
- [Home Page and Welcome Message](https://github.com/Giov3ss/iHealthy/issues/28)
- Hero image is displayed prominently on the Home page.
- The welcome message is visible and prominently states "Welcome to iHealthy".
- The "Book Now" button is functional and redirects the user to the appropriate registration or login page.

## Compatibility and Responsive Testing

I ensure my site was worked well, and looked nice on a variety of devices & browsers as noted in the table below:

| TOOL/Device             | Browser    | OS             | Viewport      |
|-------------------------|------------|----------------|---------------|
| iPhone 14 Plus          | Chrome     | iOS, v16.0     | 428 x 746 px  |
| Moto G9 Play            | Firefox    | Android, v10.0 | 412 x 804 px  |
| Samsung Galaxy J7 Prime | Samsung    | Android, v8.1  | 360 x 560 px  |
| Google Pixel 7 Pro      | Chrome     | Android, v13.0 | 412 x 775 px  |
| iPhone 12 Mini          | Safari     | iOS, v14.2     | 375 x 629 px  |
| iPad 10th               | Safari     | iOS, v16.0     | 393 x 786 dp  |
| iPad Mini 2021          | Chrome     | iOS, v15.5     | 744 x 1059 px |
| Browserstack windows PC | Edge       | windows 11     | 1336 x 667 px |
| Browserstack windows PC | Chrome 113 | windows 10     | 1336 x 667 px |
| Browserstack Mac PC     | Safari     | Safari 15.6    | 1336 x 667 px |


### Most Popular browser & Operating System

| Device             | Browser               | Operating System | Description                                              |
|--------------------|-----------------------|------------------|----------------------------------------------------------|
| iPhone             | Safari                | iOS              | Popular combination with significant market share        |
| Android Smartphone | Chrome                | Android          | Widely used browser on the Android platform              |
| Desktop/Laptop     | Chrome                | Windows          | Popular browser on the Windows operating system          |
| Desktop/Laptop     | Chrome                | MacOS            | Popular browser on the macOS operating system            |
| Desktop/Laptop     | Edge                  | Windows          | Microsoft Edge is gaining popularity among users         |
| Other              | Firefox/Samsung/Opera | Various          | Represents a compromise due to limited testing resources |

The choices in the table are base on the browser market share data provided by [gs.statcounter.com](https://gs.statcounter.com/). Chome and Safari are the dominant browsers, so they are included for testing on different devices and operating systems. Edge is also included as it has a noticeable market share. Since firefox, Samsung Internet and Opera have smaller market shares, they are grouped under the "Other" category to represent a compromise due to limited testing resources.

**Browser Version Market Share:**
- Chrome: 63.51%
- Safari: 20.43%
- Edge: 4.96%
- Firefox: 2.77%
- Samsung Internet: 2.59%
- Opera: 2.39%

## Accessibility Testing 
### Accessibility Audits
- Desktop
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/189e1601-2de2-4265-9d92-2b239a62b0ee)

- Mobile 
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/ea1401f5-38e1-4e25-a502-88af9c7e1d26)

I notice that I got a 97 with a false positive on a contrast issue around the "Book Now" button. When I further inspected with [webaim](https://webaim.org/resources/contrastchecker/), I determined that a 20px font-size with those colors is considered large text, which actually passes WCAG AA standards of accessibility.

## Validation Testing
### CSS Validation
- i-style.css
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/96e7e589-9b83-47b4-a49f-bfbb1d84eba1)

### HTML validation
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/ccf3af92-43db-4fcc-a8f6-ae56f47fa5b7)
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/158a679c-bbd9-4e10-9f89-d8564a925e52)

### JavaScript Validation
- Appointments.JS
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/de0647cf-c70f-4887-b327-80be6ddc01b7)

- messages.JS
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/7ea444de-33cd-493c-9f8b-756f5277c6b7)

### Python Validation
- appointments.py
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/8d1b474e-77ce-4f06-bcfd-22c0a2bedd5a)

- homepage.py
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/822d3e5f-cad1-4330-8117-3b0ad6f02394)

- admin.py
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/cb4edf0e-2793-4f2f-ab7e-600af1b9e4d7)

- apps.py
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/fa2e5e57-48f3-48be-b0e5-81608167e178)

- forms.py
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/62b0b269-9774-4fb7-96c3-d6b697304df0)

- models.py 
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/2a1fbf32-fe0b-49f0-8345-a6916d3c46b8)

- urls.py
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/c56f69c4-c89e-4ad3-97ba-239a4b1bcffb)

- settings.py
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/209a7205-297f-4dae-b618-e03ea8dc8916)

- urls.py (iHealthy folder)
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/9b3a1c3f-5851-4b4e-8f2a-a416d0fcd3ed)

- wsgi.py
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/bd9008bd-e424-46e5-a86b-fcb4302377e5)

- manage.py
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/8d0c7a10-d568-4cca-a58a-f8b4d7a2bdcb)

## Defects
**DEFECTS** were documented in github using a custom issue template. 
I created a milestone to group all defects together so they'd be easier to manage.
- Here is my [DEFECT Template](https://github.com/Giov3ss/iHealthy/issues/new?assignees=&labels=&projects=&template=bug-report.md&title=DEFECT%3A+%3Ctitle%3E)
- Here is my [DEFECT Milestone](https://github.com/Giov3ss/iHealthy/milestones)

## Defects of Note
- **Issue with Conflict Dates, time and Nutritionist:**
One of the significant defects that posed a challenge was related to conflicts in appointment scheduling. Users were able to schedule appointments even if there was a conflicting appointment already booked for the same date, time and nutritionist. 
Resolving this issue required careful analysis of the code logic and understanding the data flow within the system, it took several debugging sessions to identify the root cause and devise an appropriate solution.
- Issue [link](https://github.com/Giov3ss/iHealthy/issues/39)

- **Integration of Timepicker Functionality:**
Integrating the timepicker functionality into the appointment form proved to be a time-consuming and complex task. Configuring the timepicker library, ensuring it functioned correctly and synchronizing with other components required careful consideration of dependencies, script placements and compatibility issues.
- Issue [link](https://github.com/Giov3ss/iHealthy/issues/41)

## Outstanding Defects
Users with slow network connections may experience a delay in image loading, resulting in a slower website performance affecting the overall user experience. This issue is primarily dependent on network conditions and the user's internt speed. 

## Technologies Used
Several technologies have been used to enable this website works:
| Technology               | Description                                                                                                                                          |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Django                   | Django is the framework that has been used in the project, enables efficient development, database interactions and secure authentication.           |
| Python                   | Python is the core programming language that was used to write all of the code in this application, to make it fully functional.                     |
| JavaScript               | JavaScript was used to provide dynamic interactivity to the messages and enhancing the functionality of the  timepicker.                             |
| Bootstrap                | Bootstrap was utilized to ensure a responsive design.                                                                                                |
| Git                      | Git was utilized as the version control system for tracking changes, and maintaining the project's codebase.                                         |
| PostgreSQL               | PostgreSQL was employed as the relational database management system to store and manage the project's data.                                         |
| GitHub                   | Github was used as development environment, code management and tracking of changes.                                                                 |
| Font Awesome             | Font Awesome was used to obtain the icons of the website, enhancing the overall design.                                                              |
| Google Developer Tools   | DevTools was the primary toll for bug detection, testing the responsiveness and resolving issues across the website.                                 |
| Heroku                   | Heroku was used to deploy the website.                                                                                                               |
| CI's pep8                | CI's pep8 tool was used to validate all the python code.                                                                                             |
| Jigsaw                   | Jigsaw was used to validate CSS code.                                                                                                                |
| W3 HTML                  | W3 HTML was used to validate HTML code.                                                                                                              |
| Jshint                   | Jshint was used to validate JavaScript Code.                                                                                                         |
| Coloors                  | Coloors was utilized to generate color palette for the website design.                                                                               |
| Cloudinary               | Cloudinary was utilized to store all of my static files and images.                                                                                  |
| Lighthouse               | Lighthouse was used to test the accessibility of the website.                                                                                        |
| Balsamiq                 | Balsamiq was utilized as a tool for creating wireframes, providing a visual representation of the website layout and structure.                      |
| AmIResponsive            | AmIResponsive was used to generate screenshots of the website in various device sizes, allowing for a quick visual assessment of its responsiveness. |
| Markdown Table Generator | Markdown Table Generator was utilized as a tool to create tables in Markdown format.                                                                 |
| Gitpod                   | Gitpod was used to write and edit the project code.                                                                                                  |
| Mermaid                  | Mermaid was used to create all the diagrams.                                                                                                         |                                                                                                 |

### Languages
- HTML
- CSS
- Python
- JavaScript 

### Frameworks, Libraries & Programs Used
- Django
- Bootstrap
- Git 
- PostgreSQL
- GitHub
- Font Awesome
- Google Developer Tools
- Heroku
- CI's pep8
- W3 HTML
- Jshint
- Coloors
- Cloudinary
- Lighthouse
- Balsamiq
- AmIResponsive
- Markdown Table Generator
- Gitpod
- Mermaid 

## Deployment

### Prerequisites
To run this project, you need a CLOUDINARY_URL:
1. **Cloudinary Account:**
- Create an account on [Cloudinary](https://cloudinary.com/users/register_by_email) if you don't have one.
- Access the Cloudinary dashboard.
2. **Obtain API Key and Secret URL:**
- In the Cloudinary dashboard, navigate to your account settings.
- Look for the section related to API credentials or environments variable.
- Locate the API Key and Secret URL.
- Copy the API Key and Secret URL, as you will need them to configure the application.
3. **Set Environmental Variables:**
- Once you have obtained the API Key and Secret URL, you need to set them as environmental variables in your development environment.
- Depending on your operating system and development environment, the steps to set environmental variable may vary.

### Forking the Github Repository

To make a copy or ‘fork’ the repository:

1. Login to your own GitHub account
2. Navigate to [my repository](https://github.com/Giov3ss/iHealthy)
3. In the top right corner of the page, click 'fork' option to create and copy of the original

### Making a Local Clone

1. Under the repository name, click on the ‘code’ tab
2. In the clone box, HTTPS tab, click on the clipboard icon 
3. In your IED open GitBash
4. Changed the current working directory to the location you want the cloned directory to be made
5. Type ‘git clone’ and then paste the URL copied from GitHub
6. Press enter and the local clone will be created 

### Production Deployment

To get started with local development in GitPod or your preferred IDE, follow these steps:

1. Install the GitPod Chrome extension from the Chrome Web Store.
- [GitPod Chrome Extension](https://chrome.google.com/webstore/detail/gitpod-always-ready-to-co/dodmmooeoklaejobgleioelladacbeki)

2. Once the extension is installed, navigate to your forked repository on GitHub.
3. Click on the green "GitPod" button to open the repository in GitPod.
4. After the workspace is created, you can start the development process.
5. Install the Python packages by running the following command in the terminal:
- **pip3 install -r requirements.txt**
6. Create an **'env.py** file in the project's root directory to store your environment variables.
7. In the **'env.py** file, add the following variables, but make sure not to disclose real values:
- **SECRET_KEY=<YOUR_VALUE>**
- **CLOUDINARY_URL=<YOUR_VALUE>**
- **DATABASE_URL=<YOUR_VALUE>**
8. Apply databse migrations to set up the database by running the following command:
- **python3 manage.py migrate**
9. Create a superuser account that allows you add and inspect data via Django admin by running the following command:
- **python3 manage.py createsuperuser**
10. Start the server by running the following command:
- **python3 manage.py runserver**
11. Now you can access the application by opening the provided URL in your browser.

## Credits
Throughout the process of building the iHealthy website, I would like to acknowledge the following:

**Online Sources:**
- [Code Institue Template](https://github.com/Code-Institute-Org/python-essentials-template)
- [Stack Overflow](https://stackoverflow.co/)
- [Django Documentation](https://docs.djangoproject.com/en/4.2/)
- [MDN Web Docs](https://developer.mozilla.org/en-US/)

**Modules and Libraries:**
- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [JavaScript](https://www.javascript.com/)
- [Font Awesome](https://fontawesome.com/)
- [jQuery](https://jquery.com/)
- [Timepicker](https://timepicker.co/)
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Django allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
- [Cloudinary](https://cloudinary.com/)
- [Git](https://git-scm.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Pexels](https://www.pexels.com/)
- [Markdown Best Practices](https://www.markdownguide.org/basic-syntax/)
- [Mermaid](https://mermaid.live/)


## Media 
- [Pexels](https://www.pexels.com/) - The Hero Image was taken from Pexels. 
- [Font Awesome](https://fontawesome.com/) - The icons was taken from Font Awesome.

## Acknowledgments

**Tutorials and Inspiration:**
- The walkthrough project 'I think Therefore I blog' from Code Institute.
- The Template for the GUI for this project was provided by [Code Institue Template](https://github.com/Code-Institute-Org/python-essentials-template)
- Templates from [Bootstrap Examples](https://getbootstrap.com/docs/4.4/examples/) helped me to get an overview of the site and footer specifically.

**Peoples:**
- Malia - A heartfelt appreciation goes to our mentor from Code Institute, whose guidance and support have been invaluable throughout this project.
- The Team at Tutor support at Code Insitute - A huge thanks to the team at Tutor Support for their prompt assistance in addressing any bugs and GitPod related issues I encountered along the way. 
- Gustavo Chahm - Special thanks to Gustavo Chahm for his valuable contributions in testing the application and providing insightful feedback, which greatly contributed to improving the overall quality and user experience.
