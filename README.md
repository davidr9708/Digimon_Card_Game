# Digimon Card Game 2021 (Database)
![](Logo/digimoncardgamelogo.png)

## Description
From webscrapping to inserting the data in SQLite, from python. There's only one code per card, parallel rare were excluded because they have the same features and code to their original card (no parallel rare). 

The data were taken from the official website of [Digimon Card Game](https://en.digimoncard.com/cardlist/?search=true&category=508101)

## Files' description
1. **Digimon_Card_Game.csv:** Tidy data set with all cards. 
2. **Code:** 
   - *Getting_Data.R* Code to extract the data from the webpage
   - *Wrangling_Data_Set.R:* Code to clean the data set created in *Getting_Data.R*
3. **Rdata:**
   - *All_cards.rda:* Data set extacted in *Getting_Data.R*, with R format. 
