#Packages
library(tidyverse)

# Data set
load('Rdata/All_card.rda')

# Wrangling
Decks <-
    Deck %>%
      ##Separating columms
      separate(Digivolve_Cost_1, 
               into = c('Cost_Digievolution1', 'Level_Digievolution1'), 
                      sep = '\\s*from\\s*') %>%
      separate(Digivolve_Cost_2, 
               into = c('Cost_Digievolution2', 'Level_Digievolution2'), 
               sep = '\\s*from\\s*') %>% 
      mutate(DP = as.numeric(str_replace_all(DP," ","")),                                              
             Play_Cost = as.numeric(Play_Cost),
             Cost_Digievolution1 = as.numeric(Cost_Digievolution1),
             Cost_Digievolution2 =  as.numeric(Cost_Digievolution2),
             Promo_info = str_to_title(
                              str_replace(
                                 str_replace(Promo_info, "\\s*&rtri;", ""), 
                                             "\\s*\\[[:graph:]*\\]", "")),
             Promo_info = str_replace(Promo_info, 
                                      "\\s*Deck\\s*", " Deck-"),
             Promo_info = str_replace(Promo_info, 
                                      "\\s*Booster\\s*", " Booster-")) %>%
      separate(Promo_info, 
           into = c('Deck_Type', 'Deck_Name'), 
           sep = '-')
  
## Creating CSV
write.csv(Decks, 'Digimon_Card_Game.csv')
