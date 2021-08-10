# Digimon Card Game (Data Set)
![](Logo/digimoncardgamelogo.png)

## Description
Web scrapping to get tidy data set for Digimon Card Game. There's only one code per card, parallel rare were excluded because they have the same features and code to their original card (no parallel rare).   
### Decks
 - ThemeBooster Classic Collection
 - Booster Battle Of Omega        
 - Booster Double Diamond         
 - Booster Great Legend           
 - Booster New Evolution          
 - Booster Ultimate Power         
 - Booster Union Impact          
 - Start Deck Cocytus Blue        
 - Start Deck Gaia Red           
 - Start Deck Gallantmon          
 - Start Deck Giga Green       
 - Start Deck Heaven's Yellow     
 - Start Deck Mugen Black         
 - Start Deck Ulforceveedramon    
 - Start Deck Venom Violet        

## Data source
Official website of [Digimon Card Game](https://en.digimoncard.com/cardlist/?search=true&category=508101)

## Files' description
1. **Digimon_Card_Game.csv:** Tidy data set with all cards. 
2. **Code:** 
   - *Getting_Data.R* Code to extract the data from the webpage
   - *Wrangling_Data_Set.R:* Code to clean the data set created in *Getting_Data.R*
3. **Rdata:**
   - *All_cards.rda:* Data set extacted in *Getting_Data.R*, with R format. 
