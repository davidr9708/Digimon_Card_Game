# Packages
library(tidyverse)
library(rvest)

# Data frame for the Deck
Decks <- data.frame()

# ID links for decks
## Individual decks' ID
Start_decks <-seq(from = 508101, to = 508108, by = 1)
Booster_decks <-seq(from = 508001, to = 508008, by = 1)
## All decks' ID
All.ID <- c(Start_decks,Booster_decks)

# Function extract Nodes in text format
Node.text <- function(Nd) {
  page %>%
    html_nodes(Nd) %>%
    html_text()
}

# Function to create data frame with codes and colors
Color_data <- function(Cd, Color){
  Identification <- page %>%
    html_nodes(Cd) %>% 
    html_nodes('.cardno') %>% 
    html_text()

  data.frame(Code = Identification, 
             Color = rep(Color, times =length(Identification)))
}


# Deck
for (ID in All.ID)
  {
  ## Raw Data
  Link <- paste0("https://en.digimoncard.com/cardlist/?search=true&category=", ID)
  page <- read_html(Link)
  ## Columms 
  ### General info
  Promo_info <- Node.text(".cardinfo_bottom a")
  Code <- Node.text(".cardno")
  Name <- Node.text(".card_name")
  Card_Type <- Node.text(".cardtype:nth-child(3)")
  Form <- Node.text(".cardinfo_top_body dl:nth-child(1) dd")
  Attribute <- Node.text(".cardinfo_top_body dl:nth-child(2) dd")
  Type <- Node.text(".cardinfo_top_body dl:nth-child(3) dd")
  ### Strength's info
  Card_Level <- Node.text(".cardlv")
  DP <- Node.text(".cardinfo_top_body dl:nth-child(4) dd")
  ### Costs
  Play_Cost <- Node.text(".cardinfo_top_body dl:nth-child(5) dd")
  Digivolve_Cost_1 <- Node.text("dl:nth-child(6) dd")
  Digivolve_Cost_2 <- Node.text("dl:nth-child(7) dd")
  ### Effects
  Effect <- Node.text(".cardinfo_bottom dl:nth-child(1) dd")
  Digivolve_Effect <- Node.text(".cardinfo_bottom dl:nth-child(2) dd")
  Security_Effect <- Node.text(".cardinfo_bottom dl:nth-child(3) dd")
  
  ## Creating the data frame - NOT levels
  Double.diamond <- data.frame(Promo_info, Code, Name, Card_Type, Form, 
                               Attribute, Type, DP, 
                               Play_Cost, Digivolve_Cost_1, Digivolve_Cost_2, 
                               Effect, Digivolve_Effect, Security_Effect,  
                               stringsAsFactors = FALSE)
  
  
  ## Colors
  ### Individual
  Red <- Color_data('.card_detail_red', 'Red')
  Blue <- Color_data('.card_detail_blue', 'Blue')
  Yellow <- Color_data('.card_detail_yellow', 'Yellow')
  Green <- Color_data('.card_detail_green', 'Green')
  Black <- Color_data('.card_detail_black', 'Black')
  Purple <- Color_data('.card_detail_purple', 'Purple')
  White <-  Color_data('.card_detail_white', 'White')
  ### Completed data frame
  All.colors <-unique(rbind(Red, Blue, Yellow, Green, Black, Purple, White))

  ## Adding colors
  Double.diamond <- merge(Double.diamond, All.colors, by = 'Code')
  
  ## Adding levels
  ### Take cards without levels
  Tamers_Options <- Double.diamond %>%
      filter(Card_Type == 'Tamer' | Card_Type =='Option')
  ### Remove cards without levels
  Double.diamond <- Double.diamond %>%
      filter(Card_Type != 'Tamer', Card_Type !='Option') %>%
      data.frame(Card_Level) 
  
  ### Add back the cards without levels    
  Double.diamond <- bind_rows(Double.diamond, Tamers_Options) %>%
      mutate(Card_Level = ifelse(is.na(Card_Level) == TRUE, '-', Card_Level))
  
  
  ## Adding Combining the decks
  Decks <- rbind(Decks, Double.diamond)
}

# Removing parallel rare and other artistic cards
Decks <- unique(Decks)
# Saving the data sets
save(Decks,file = 'Rdata/All_cards.rda')
