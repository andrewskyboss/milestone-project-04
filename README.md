[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/andrewskyboss/milestone-project-04)

# milestone-project-04
# Full Stack Frameworks with Django / The CUBE | GYM & Fitness Club

![logo](assets/images/gym-logo.png)
[Live site on Heroku](https://thecube-gym-fitness-club.herokuapp.com)

# Author
Andrej Cybovskij

## Project Overview

- Below is a picture of site that shows it in responsive states. 
[link to check a website to be responsive](http://ami.responsivedesign.is)
![picture of site](assets/images/responsive.jpg)
- The CUBE | GYM & Fitness Club is a website, where user can get all necessary information about the GYM & Fitness Club. Before or after getting Club membership, user can navigate and research all Club’s proposed services and facilities. There is a short information about Club’s stuff and their experience. Activities section is created to provide information about all Exercise plans and classes they have or will have in the future. Timetable section is created to provide information about all classes times and Fitness Instructors working on them. Shop Section is created to navigate user to fully functional Merchandise online Shop. In that section user can enjoy all ecommerce website possibilities and join a ﬁtness community and purchase Club’s exercise plans and merchandise.
- This is a version 1 and contents just a minimal options and features. However, this version has very high commercial feature, because during the last year all businesses are moving to online commerce. Ecommerce features allows even for the Gym and Fitness business to survive by selling their merchandise online. As well website has modern design and lot of visual components. Design was build using last UI/UX technologies.

- [Link to a deployed website](https://thecube-gym-fitness-club.herokuapp.com)

## UX

### Project Goals

#### The goals of this project are:
- Design, develop and implement a dynamic web application using HTML, CSS, JavaScript Python+Django, relational database (recommending MySQL or Postgres), Stripe payments and additional libraries and APIs
- Meet the target audience users’ needs using UI/UX design principles
- Implement a Django project backend by a relational database to create a website that allows users to store and manipulate data records
- Test a web application through the development, implementation, and deployment stages
- Deploy the final version of the web application to a Cloud platform Heroku
- Demonstrate and document the development process through a version control system
- Learn Python+Django theory and practically implement all gained knowledge


#### User Goals

- The target audience of this website is quite wide. They are different age, status, families or single people.

Common types of users are:
- **New customers.** The users’ main goal is to get a necessary recipe. They are ready to search and discover new recipes. As well, they could wonder how to share their recipes on this website. They need to get login information and discover user’s dashboard functionality, how to add their recipes to the system
- **Existing customers.** They knows website structure and knows how to login, search, add, update and delete recipes.
- **Admin.** He’s goal is to get access to the back end information to manage it. He needs to manage categories and cuisines such as create, edit update or delete them
- This website is proposing login system for users to create, update and delete user’s recipes.

#### Developer Goals
1.  Build a Django project backend by a relational database to create a website that allows users to store and manipulate data records.
2.  Use Multiple Apps structure.
3.  Data Modelling trough the relational database schema well-suited for the project.
4.  The project should include an authentication mechanism, allowing a user to register and log in.
5.  User Interaction to allow user to create and edit models in the backend.
6.  Use of Stripe for e-commerce functionality using Stripe.
7.  Incorporate a main navigation menu and structured layout.
8.  Use of some JavaScript logic you have written to enhance the user experience.
9.  Provide off necessary documentation through README.md file to explain what the project does and the value that it provides to its users.
10. Use of Git & GitHub for version control.
11. Made a clear attribution between code written by the author and code from external sources.
12. Deploy the final version of the code to a hosting platform such as Heroku.
13. Do not include any passwords or secret keys in the project repository.


#### Website Owner Goals
Main goals of website owner are:
- To sell more travel packages.
- Showcase existing destinations.
- To present relevant inform about countries and destinations.
- To make information more structural.
- To attract users to buy an existing packages.
- To represent contact information.

### User Stories

- Viewing and Navigation
  - As a Shoper, I want to be able to ..
    1. View a list of products select some to purchase
    2. View individual product details. Identify the price, description, product image
    3. Quickly identify deals, clearance items and special offers. Take advantage of special savings on products I'd like to purchase
    4. Easily view the total of my purchases at any time. Avoid spending too much

- Registration and User Accounts
  - As a Site User, I want to be able to ..
    1. Easity register to an account. Have a personal account and be able to view my profile
    2. Easily to login or logout. Access my personal account information
    3. Easily to recover my password in case I forgot it. Recover access to my account
    4. Receive an email confirmation after registering. Verify that my acount registration was successful
    5. Have a personalized user profile. View my personal order history and order confirmations and save my payment information

- Sorting and Searching 
  - As a Shoper, I want to be able to ..
    1.  Sort the list of available products Easily identify the best priced and categorically sorted products
    2.  Sort a specific category of product. Find the best priced product in a specific category or sort the product in that category by name
    3.  Sort multiple categories of products simultaneously. Find the best priced across broad categories, such as food or merch
    4.  Search for a product by name or description. Find a specific product I'd like topurchase
    5.  Easily see what I've searched for and the number of results. Quickly decide whether the product I want is available
    6.  Easily select the quantity of a product when purchasing it. Ensure I don’t accidentally select the wrong product
    7.  View items in my bag to be purchased. Identify the total cost of my purchase and all items I will receive
    8.  Adjust the quantity of individual items in my bag. Easily make changes to my purchase before checkout
    9.  Easily enter my payment information. Check out quickly and with no hassles
    10. Feel my personal and payment information is safe and secure. Confidently provide the needed information to make a purchase
    11. View an order confirmation after checkout. Verify that I haven't made any mistakes
    12. Receive an email confirmation after checking out. Keep the confirmation of what I've purchased for my records

- Admin and store manager
  - As a Store Owner, I want to be able to ..
    1.  Add a product. Add new items to my store
    2.  Edit / Update a product Change product price, description, images and other product criteria
    3.  Delete Product. Remove items that are no longer for sale

### Design Choices
This project was created based on the target audience needs and requirements. The target audience is a quite wide range of people who likes to cook. Based on the website theme, were chosen Red, orange and green colors as a main brand colors. They are associated with food and takes attention to themselves. The food theme involves visual attraction to the user that mean website should contain a lot of food imaginary but not overload attention. However existing trends like to use clean and simple design. As a small piece of attraction, website’s buttons contains corresponding icons. According to user requirements, website should stay useful, usable and valuable for everybody. To achieve value from design were used user experience five planes:

- **Strategy Plane**  – aiming to achieve in the first place and for whom. The users of this website are people who likes to cook and share their ideas. The website should be quite simple and universal for everybody. Navigation is used quite standard and known by every online users. Traditional rule is no more than 3 clicks to search or get other information.

- **Scope plane** - represents features we want to include into design. 
  - This project includes following features: 
      - Header/Mobile navigation.
      - Registration system.
      - Login functionality.
      - E Commerce functionality
      - Payment system functionality
      - Mail Notification/ Confirmation system
      - Toast notification System
      - Create, Read, Update and Delete functionality.
      - Intuitive design.
      - SVG logo on top of the page.
      - Grid/Card images as a visual representatives.
      - Search functionality.
      - Social media icons.

- **Structure plane** - this project’s information is structured and logically placed into the main navigation. As well, this project’s content is taken from the MongoDB database. The structure of Database tables are presented in this [link to a database schema](DATABASE.md).

- **Skeleton plane** - part for mock-ups:
  - Wireframes links are presented below:
    - [Link to a Wireframes for a Desctop view](assets/documents/project-4-desctop-wireframes.pdf)
    - [Link to a Wireframes for Tablet view ](assets/documents/project-4-tablet-wireframes.pdf)
    - [Link to a Wireframes for Mobile view ](assets/documents/project-4-mobile-wireframes.pdf)

- **Surface plane** - it is a final part of design procedure. The project is built in Classical design style with infusions of modern elements. This project is orientated more into the data manipulating. However, the website stays useful, usable and valuable for everybody.

#### Colors
The color palette were created according to people association with the food and professional information from the [Jenn David Design](https://jenndavid.com/colors-that-influence-food-sales-infographic/), food packaging Design Company that has over 20 years of successful experience partnering with specialty food brands.

- The color brand one is Red color (CG Red). It is using for many titles and buttons to attract attention. According to Jenn David Design: Red and yellow are the chief food colors, evoking the taste buds and stimulating the appetite. Both red and yellow are also effective at grabbing attention.
- The color brand two is Green color (Maximum Green). It is used for titles, subtitles, and buttons. According to Jenn David Design: Green color is connotes with eco-friendliness, healthy (think veggies).
- The color brand three is Orange color. It is used for hover statements and for user navigation links, to attract attention. According to Jenn David Design: Orange color is a blend of red and yellow, naturally lends itself to food as another appetizing color.
- The color brand four is Spanish Grey color. It is used as neutral base color and some lines color.
- The color brand five is a Jet Grey color. It is dark color and used for main content font and all dark design elements to make them visible to user.

- Color palete was created using [Coolors resources](https://coolors.co)
- ![color scheme](assets/images/colors.PNG)


#### Typography
- Raleway sans-serif typeface family font, were using in this project for the body text. Body font size is 16px. This body font is easy to read and good for design. It is very universal and has very wide range of font weights.
- All titles H1, H2 and H3 are in Dancing Scrip cursive font’s family.
- All H4 titles are in Raleway sans-serif typeface font’s family.
- According to Google Font, Dancing Script is a lively casual script where the letters bounce and change size slightly. Caps are big, and goes below the baseline. This font is associated with handwriting and is a good choice for recipe book titles. It is similar in style to everybody own hand written recipe book.
-  H1 as main title is in size of 52px. It is quite big size, but looks very stylish and attract attention. H2 title is in size of 42px. H3 titles are in size of 32px. H4 titles are in size of 26px.
- All fonts are reduced in size for mobile devices to fit into the small screen of devices:
- H1 = 40px, H2 = 30px, H3 = 25px, H4 = 22px.
- body font is in same size for mobile devices.

- Font examples are presented below:
- H1 Oswald 50px ![H1 Title Oswald 50px](assets/images/h1.PNG)
- H2 Oswald 40px ![H2 Title Oswald 40px](assets/images/h2.PNG)
- H3 Roboto Mono 30px ![H3 Title Roboto Mono 30px](assets/images/h3.PNG)
- Paragraph (body) Roboto 16px ![p Paragraph Roboto 16px](assets/images/p.PNG)
- [Oswald font can be found here](https://fonts.google.com/specimen/Oswald?query=oswa)
- [Roboto Mono font can be found here](https://fonts.google.com/specimen/Roboto+Mono?query=robot)
- [Roboto font can be found here](https://fonts.google.com/specimen/Roboto?query=robot)
 

#### Images
- To demonstrate main Gym and Fitness theme, in this project were used lot of colourful images.
- As well a lot of images were using for shopping pages.
- Font Awesome icons were used to visually represent all major social media resources and as additional information on buttons. 
- [Images and logo were taken from the Megapixl resources](https://www.megapixl.com)
- [Shopping page images were taken from the Boutique Ado and Kaggle website](https://www.kaggle.com/datasets)
- [nutrition images were taken from the HPnutrition website](https://www.hpnutrition.ie/)

#### Design Elements
List of all elements used on website: 
- top menu (desktop/mobile navigation)
- footer
- containers/cards
- check boxes
- buttons
- text input
- textarea inputs
- images (.png, .jpg, .svg)
- icons
- contact form


#### Animations and Transitions

Project has a limited range of animations. It draws attention to the element.
- Animation is added to the following elements:
  - **Hover** state is used for all icons, header navigation and buttons. On hover, they are changing background and text colors sliding from bottom to top.
  - **Sliding from the bottom** animation is added to buttons, h1, h2 titles. As well this animation is added to forms.

### Wireframes

The wireframes were created using [Balsamiq](https://balsamiq.com/wireframes/) software. It was a part of Scope Plane of design process.
- Wireframes links are presented below:
- [Link to a Wireframes for a Desctop view](assets/documents/project-4-desctop-wireframes.pdf)
- [Link to a Wireframes for Tablet view ](assets/documents/project-4-tablet-wireframes.pdf)
- [Link to a Wireframes for Mobile view ](assets/documents/project-4-mobile-wireframes.pdf)

### Features

Following features will be used in this project:

  - Intuitive design. Design is clear and understandable.
  - Designed with HTML5, CSS, JavaScript and Materialize.
  - Fixed Header navigation. Simple and easy to navigate.
  - Mobile navigation (sliding from the left).
  - Clickable Header logo.  
  - Search functionality.
  - Registration functionality.
  - Login functionality.
  - Create,read, update and delete functionality for the user.
  - Database connection and data handling.
  - Contact form with CTA, to be in touch with website's owner.
  - Social media icons are at the bottom of every page.

### Database Planning

The database "The CUBE | GYM & Fitness Club" will contain 4 collections: Users, Recipes, Cuisine and Categories:
- [Link to a database schema](DATABASE.md)


#### Implemented Features

All planned features are implemented and working properly

#### Future Features

Features to be implemented in the future:
- Add cuisine locations on the map
- Add recipe search on map functionality
- Add recipe to user favourites
- Preview and manage favourite’s collection
- Add image upload functionality
- Integrate partners adds to website

## Technologies Used

The following languages, frameworks, libraries, and other tools were used to construct this project:

### Programing Languages
- [HTML](https://www.w3schools.com/html/default.asp) The project uses **HTML** to define DOM elements.
- [CSS](https://www.w3schools.com/w3css/default.asp) The project uses **CSS** to define DOM appearance.
- [JavaScript](https://www.javascript.com) The project uses **JavaScript** to interact with content. 
- [Python](https://www.python.org) The project uses **Python+Flask** to manipulate with content.
- [Markdown](https://www.markdownguide.org/) Documentation within the readme was generated using markdown.

### Frameworks and Libraries:
- [Bootstrap](https://getbootstrap.com/) In the project were used **Bootstrap** framework for styling, layout and typography.
- [Django](https://www.djangoproject.com/) In the project were used **Django** framework to build the web application.
- [AWS](https://aws.amazon.com/) In the project were used **AWS** to store data objects.
- [Stripe](https://stripe.com/ie) In the project were used **Stripe** financial services software for payment.
- [Googlw Mail Service](https://www.google.ie/) In the project were used **Googlw Mail Service** for email notifications and confirmation.
- [Heroku](https://heroku.com/) In the project were used **Heroku** cloud platform for deployment.
- [GitHub](https://github.com) In the project were used **GitHub** hosting platform for version control.

### Fonts
Google Fonts:

- [Oswald font can be found here](https://fonts.google.com/specimen/Oswald?query=oswa)
- [Roboto Mono font can be found here](https://fonts.google.com/specimen/Roboto+Mono?query=robot)
- [Roboto font can be found here](https://fonts.google.com/specimen/Roboto?query=robot)


### Tools and Resources
- [Wirefames by Balsamiq](https://balsamiq.com/wireframes/) - to create professional looking wire frames
- [Am I Responsive](http://ami.responsivedesign.is/) - to checks for responsive website and mockup image generator.
- [Color palette resources](https://coolors.co) - to create color palette
- [Markdown table generator](https://www.tablesgenerator.com/markdown_tables)
- [Markdown table of contents](http://ecotrust-canada.github.io/markdown-toc/) to create table of contents
- [Youtube](https://www.youtube.com/watch?v=rz_8NDyC6Xk)- General resource.
- [Stack Overflow](https://stackoverflow.com/) - General resource.
- [W3Schools Online Web Tutorials](https://www.w3schools.com/)
- [ImgBB -free image hosting and sharing service](https://imgbb.com/)

## Testing
Details of testing can be found in a separate document
- [Link to a testing document](TESTING.md)


## Version Control
 - Used Git for version control.
 - Additional copy vere created localy
 - Constantly versions were updated and merged

## Heroku Deployment

This project was developed using open source Heroku cloud Platform.
To deploy this project, the following steps were taken:
1.  Inside GitHub application create requirements.txt file to put all required files there (pip freeze > requirements.txt)
2.  Inside GitHub application create Procfile to let Heroku know what file runs the application, (add there web: python app.py)
3.  Create an account on Heroku and create a new app. Follow all proposed steps
4.  Choose deployment method GitHub repository
5.  Connect to GitHub section make sure your GitHub profile is displayed
6.  Add repository name and click search
7.  When it is found, click connect button
8.  Go to the app settings on Heroku and click 'Reveal Config Vars'
9.  Add the required keys as they are in your local env.py (i.e IP, MONGO_DBNAME, MONGO_URI, PORT, SECRET_KEY )
10. In the Deployment tab enable Automatic Deployment
11. Deploy a GitHub branch choose your branch and press “Deploy Branch” button
12. After done and displaying sign “Your app was successfully deployed” click view to launch a new app
13. Deployed site is now available and should automatically update on any changes


## Credits

### Content

- [GO GYM Limerick](https://gogymlimerick.ie/) Go Gym Sport Club Limerick 
- [HPnutrition](https://www.hpnutrition.ie/)  Ireland’s largest online sports supplements store
- [Boutique Ado and Kaggle website] (https://www.kaggle.com/datasets)

### Media

- The images used in this project were obtained from the [Megapixl resources](https://www.megapixl.com)
- Icons [Font Awesome](https://fontawesome.com/v4.7.0/)
- SVG logo and favicon - base is taken from [Megapixl resources](https://www.megapixl.com) and modified on [Adobe Illustrator](https://www.adobe.com/products/illustrator.html)
- Image optimisation - self-made on [Adobe Photoshop](https://www.adobe.com/products/photoshop.html)

### Code Snippets and Tutorials

- [Materialize & Static Files Setup](https://www.youtube.com/watch?v=7R0qJ7QJ2-U) were created using [Code Institute Tutorials](https://www.youtube.com/watch?v=7R0qJ7QJ2-U)
- Code Institute Tutorials [User Authentication And Authorization 1](https://www.youtube.com/watch?v=r4qlVU20Aoc&t=357s)
- Code Institute Tutorials [User Authentication And Authorization 2](https://www.youtube.com/watch?v=Sfkg3358Igc&t=228s)
- Code Institute Tutorials [Login Functionality](https://www.youtube.com/watch?v=KzReYjMAgn8&t=14s)
- Code Institute Tutorials [Display User Profile Page](https://www.youtube.com/watch?v=1rfV6CPcFX0)
- Code Institute Tutorials [Logging Out](https://www.youtube.com/watch?v=7zEIYYHsTHA)
- Code Institute Tutorials [Add Categories To MongoDB](https://www.youtube.com/watch?v=vvt8RZPDeDg)
- Tutorial to round decimals [Stack overflow](https://stackoverflow.com/questions/11260155/how-to-use-float-filter-to-show-just-two-digits-after-decimal-point)

### Acknowledgments

I would like to thank:
- My mentor [Malia Havlicek](https://code-institute-room.slack.com/team/UERRFE54G) for help in testing, review and invaluable advices.
- Code Institute for Flask Mini-Project [tutorial](https://www.youtube.com/watch?v=y72Dq3GRxhc&t=14s)
- Code Institute for Flask Mini-Project [tutorial 2](https://www.youtube.com/watch?v=Z4caY2YtQLY&t=9s)