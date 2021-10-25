# RaaS: Recipes as a Service
## About
This project was developed as part of a 24 hour hackathon [Hallothon] hosted by PES University, and was ranked top 10, out of more than 50 teams.
### *Built by*:
[Rahul S Srinivas](https://www.linkedin.com/in/rahulssrinivas/), [Santosh Bishnoi](https://github.com/santoshbishnoi), [Rohit Ravindra](https://github.com/sir-rohitravindra), [Mihir M Kestur](https://github.com/mihirkestur)


## Application in action!
![demonstration](./media/demo.gif)

## Description
The input to the application is an image consisting of all the ingredients that the user has and the output is a list of recipes that can be made using the ingredients, alas! The user need not think about what dish to prepare everytime now! Simply follow the link provided and use the detailed instructions mentioned. Just RaaS it! 

## Installation and running

Install the required packages from requirements.txt
```bash
$ pip install requirements.txt
```
To launch the streamlit application
```bash
$ streamlit run streamlit_app.py
```
#### Dataset source
https://www.kaggle.com/kanishk307/6000-indian-food-recipes-dataset?select=IndianFoodDatasetCSV.csv

### Note 
The application requires credentials to access the google vision API. Replace the credentials with yours.