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
    * [404 Page](#404-page)
* [Future Features](#future-features)
* [Testing](#testing)
* [Manual Testing](#manual-testing)
* [Compatibility and Responsive Testing](#compatibility-and-responsive-testing)
    * [Code Validation](#code-validation)
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

## Features
### Home Page
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/8b9aa9aa-9e7c-42b8-9e68-6b6624b4a9d5)
- The home page of iHealthy features a captivating hero image with a welcoming message, "Welcome to iHealthy". It provides an overview of the platform's features, services, and benefits. The prominent "Book Now" button enables users to quickly register or log in, ensuring easy access to iHealthy's comprehensive health and wellness services. 

### Sign Up Page
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/30b3eca1-be14-4f12-a1c1-1d4f1fba4126)
- The sign-up page allows new users to create an account on the iHealthy website. User can provide their personal information, such as name, email address (optional) and password, to register abd gain full access to the platform's features.

### Login Page
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/df298fc9-a080-4edf-a658-7d67b55b468b)
- The login page provides a form where registered users can enter their credentials (username and password) to log into iHealthy accounts. Once logged in users can access their personalized information and utilize the functionalities of the website. 

### Home Page - If the user is Authenticated
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/15df4461-f368-4bed-b13f-a0c612cadc23)
- This version of the home page is displayed when a user is authenticated and logged into their iHealthy account. The user can have access of their appointment just clicking in the navbar "Appointments" section.  

### Appointment List
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/731326d8-7fe1-45f3-ac4d-7908b01c4a92)
- The Appointment list page presents a list of all the appointments schedule by the user. It provides a brief overview of each appointment, incluiding details like date, time and nutritionist name. Users can view, update or delete appointments from this page just clicking in the icons on the right of the details. 

### Create Appointment
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/52a47d93-cba8-420f-8eda-78971366f823)
The create feature allows users to schedule a new appointment with a nutritionist. Users can select the desired date, time, nutritionist and provide a reason for the appointment. Upon submission, the appointment is added to the user's appointment list. 

### View Appointment Details
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/673020c4-8e3f-45b5-83df-db21e2496b81)
- This feature enables users to view the details of a specific appointment. It displays comprehensive information about the appointment, incluiding the date, time, nutritionist and reason. 

### Update Appointment
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/04a403b9-c0ed-46ab-9df5-a35bc1a315dc)
- User can use the update appointment feature to modify the details of an existing appointment. They can change the appointment date, time, nutritionist and reason.

### Delete Appointment
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/ff746b6c-881a-4b14-8dd9-f8d22b43647a)
- The delete appointment feature allows users to remove an appointment from their schedule. It prompts the user to confirm the deletion before permanently removing the appointment from their list. 

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

### 404 Page
![image](https://github.com/Giov3ss/iHealthy/assets/112728772/aa78af4b-24a3-4f6d-b6dd-663437e6946a)
- The 404 Page is displayed when a user tries to acces a page or resource that does not exist. It provides a user-friendly message indicating that the requested page could not be found, along with suggestions with a link on click "Here" to help the user navigate back to a valid page.

## Future Features
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
- Registering with valid information display a success message.
- Logging in with the registered username and password display a success message.
- Registering with an already registered email displays an error message.
- Registering with invalid information displays relevant error message.
- Registering without filling in required fiels displays error message indicating the missing fields.

### Manual Testing Login:
- Logging in with the registered username and password display a success message.
- Incorrect credential display an error messsage indicating invalid credentials.
- Leave the username or password field empty display an error message, indicating that fields is required.

### Manual Testing Create Appointment:
- Fill all the required fiels such as date, time, reason and nutritionist with valid inputs, the appointment is create successfully and a success message displayed on the screen. 
- Leave any required fields empty an error message appear on the screen.
- Choose a past date for the appointment and submit the form, an error message is displayed on the screen.
- Conflicts of dates, times and nutritionist with existing appointments, an error message is displayed on the screen.

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