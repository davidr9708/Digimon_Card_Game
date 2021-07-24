# Packages
library(tidyverse)
library(rvest)

# Data frame for the Deck
Deck <- data.frame()

# ID links for decks
## Individual decks' ID
Start_decks <-seq(from = 508101, to = 508108, by = 1)
Booster_decks <-seq(from = 508001, to = 508007, by = 1)
## All decks' ID
All.ID <- c(Start_decks,Booster_decks)

# Function extract Nodes in text format
Node.text <- function(Nd) {
  page %>%
    html_nodes(Nd) %>%
    html_text()
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

  ## Adding levels
  ### Take cards without levels
  Tamers_Options <-
    Double.diamond %>%
      filter(Card_Type == 'Tamer' | Card_Type =='Option')
  ### Remove cards without levels
  Double.diamond <-
    Double.diamond %>%
      filter(Card_Type != 'Tamer', Card_Type !='Option') %>%
      data.frame(Card_Level) 
  
  ### Add back the cards without levels    
  Double.diamond<-
    bind_rows(Double.diamond, Tamers_Options) %>%
    mutate(Card_Level = ifelse(is.na(Card_Level) == TRUE, '-', Card_Level))
  
  ## Adding Combining the decks
  Deck <- rbind(Deck, Double.diamond)
  }

# Saving the data sets
save(Deck,file = 'Rdata/All_card.rda')
