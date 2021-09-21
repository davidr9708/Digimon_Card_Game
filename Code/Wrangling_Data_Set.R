#Packages
library(tidyverse)

# Data set
load('Rdata/All_cards.rda')

# Wrangling
Decks <-
    Decks %>%
      ##Separating columms
      separate(Digivolve_Cost_1, 
               into = c('Cost_Digievolution1', 'Level_Digievolution1'), 
                      sep = '\\s*from\\s*Lv.') %>%
      separate(Digivolve_Cost_2, 
               into = c('Cost_Digievolution2', 'Level_Digievolution2'), 
               sep = '\\s*from\\s*Lv.') %>% 
      ## Transforming strings
      mutate(DP = as.numeric(str_replace_all(DP," ","")),                                              
             Play_Cost = as.numeric(Play_Cost),
             Cost_Digievolution1 = as.numeric(Cost_Digievolution1),
             Cost_Digievolution2 =  as.numeric(Cost_Digievolution2),
             Card_Level = str_match(Card_Level, "[:digit:]+"),
             Promo_info = str_to_title(
                              str_replace(
                                 str_replace(Promo_info, "\\s*&rtri;", ""), 
                                             "\\s*\\[[:graph:]*\\]", "")))%>%
      mutate(Promo_info = str_replace(
                              str_replace(Promo_info,"\\s*Deck\\s*", " Deck-"),
                              "\\s*Booster\\s*", "Booster-")) %>%
      separate(Promo_info, 
               into = c('Deck_Type', 'Deck_Name'), 
               sep = '-')

## Organizing columns
Decks <- Decks[,c(1:8,18,19,9:17)] 

## Creating CSV
write.csv(Decks, 'Digimon_Card_Game.csv', row.names = FALSE)
