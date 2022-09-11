# Digimon Card Game (Database)
![](Logo/digimoncardgamelogo.png)

## Description
From webscrapping to inserting the data in SQLite, using python. There's only one code per card, parallel rare were excluded because they have the same features and code to their original card (no parallel rare). 

The code is design to webscrap even the newest decks, it doesn't care when the date update, if the deck is in the page, it will get it.  

The data were taken from the official website of [Digimon Card Game](https://en.digimoncard.com/cardlist/?search=true&category=508101)

## Files' description
1. **Digimon_cards.csv:** Tidy data set with all cards. 
2. **Code:** 
   - **1_Getting_data.py:** To webscrap and get a clean dataset for all the decks.
   - **2_Database_creation.py:** To create the database and the tables in SQLite
   - **3_Data_insertion.py:** To insert the data from the dataset created in *1_Getting_data.py* into the database created in *2_Database_creation.py*

## Dashboard
You can find a dashboard that compares individual cards with a group of card here: https://public.tableau.com/app/profile/davidr9708/viz/DigimonCardsDashboard/Dashboard1
