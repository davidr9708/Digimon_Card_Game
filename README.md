# Digimon Card Game (Data Set)
![](Logo/digimoncardgamelogo.png)

## Description
Web scrapping to get tidy data set for Digimon Card Game. There's only one code per card, parallel rare were excluded because they have the same features and code to their original card (no parallel rare).   
### Decks
 [1] Booster Battle Of Omega        
 [2] Booster Double Diamond         
 [3] Booster Great Legend           
 [4] Booster New Evolution          
 [5] Booster Ultimate Power         
 [6] Booster Union Impact          
 [7] Start Deck Cocytus Blue        
 [8] Start Deck Gaia Red           
 [9] Start Deck Gallantmon          
[10] Start Deck Giga Green       
[11] Start Deck Heaven's Yellow     
[12] Start Deck Mugen Black         
[13] Start Deck Ulforceveedramon    
[14] Start Deck Venom Violet        
[15] ThemeBooster Classic Collection

## Data source
Official website of [Digimon Card Game](https://en.digimoncard.com/cardlist/?search=true&category=508101)

## Files' description
1. **Digimon_Card_Game.csv:** Tidy data set with all cards. 
2. **Code:** 
   * *Getting_Data.R* Code to extract the data from the webpage
   * *Wrangling_Data_Set.R:* Code to clean the data set created in *Getting_Data.R*
3. **Rdata:**
   * *All_cards.rda:* Data set extacted in *Getting_Data.R*, with R format. 
