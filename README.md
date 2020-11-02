# Pandemap Backend

This is backend of Pandemap, the winning submission for the IBM Call for Code 2020 Global University Track. 

Pandemap is a location suggestion system for college students that recommends the least crowded places nearby using computer vision and location data.

![Pandemap Screenshots](https://raw.githubusercontent.com/tejjogani/Pandemap/master/resources/screenshots.png)

## Demo Video
**CLICK THE THUMBNAIL BELOW TO WATCH**
[![Watch our Video](https://raw.githubusercontent.com/tejjogani/Pandemap/master/resources/thumbnail.jpg)](https://www.youtube.com/watch?v=IlYO2iSfS_o)

## The Architecture

![Pandemap Architecture](https://raw.githubusercontent.com/tejjogani/Pandemap/master/resources/architecture.png)

1. The user interacts with out React-Native Front End and looks for a location.
2. The application makes a request to our Django-based backend hosted on IBM Cloud Foundry to check how crowded that location is.
3. Our backend looks at data from our SQL Database and our Machine Learning model on Watson Studio to calculate what percentage of a specific location is full
4. If the location is filled over a threshold value, the server sends a response to the front end to redirect the user to another, safer location. 
5. The routing is done through the HERE Maps API and their flex-polyline module.

## Backend Using

1. IBM Cloud Foundry
2. Django
3. Elephant SQL

Visit ![Pandemap](https://raw.githubusercontent.com/tejjogani/Pandemap/) to view all the components of the submission.
