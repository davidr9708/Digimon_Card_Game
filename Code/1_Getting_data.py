# Libraries
from requests_html import HTMLSession
import pandas as pd
import re

# Connecting
url = 'https://en.digimoncard.com/cardlist/?search=true&category=508008'
Session = HTMLSession()
response = Session.get(url)
print(response.status_code)

## Getting deck's links
urls = response.html.absolute_links
links = list()
for url in urls:
    try:
        deck_link = re.findall("^.*true&category.*", url)[0]
    except:
        continue
    links.append(deck_link)

# Extracting data
## Previous variables
col_choice  = 'black|red|white|purple|yellow|green|blue'
deck_choice = '(theme booster|booster|start deck)'
all_cards   = list()

## Getting deck's data
for link in links:
    response = Session.get(link)
    print('Retrieving {web}, status: {status}'.format(web = link, status = response.status_code))

    cards = response.html.find('li[class^=image_lists_item]')

    ### Getting card's data
    for card in cards:

        #### identification info
        color_html = card.find('div[class ~= card_detail]')[0].html

        color   = re.findall(col_choice, str(color_html))[0].title()
        code    = card.find('li[class = cardno]')[0].text
        name    = card.find('div.card_name')[0].text
        cd_type = card.find('li[class = cardtype]')[0].text
        try:
            level = re.findall('[0-9]+', card.find('li[class = cardlv]')[0].text)[0]
        except:
            level = 'NULL'

        #### Battle info
        battle = card.find('dl')

        for inf in battle:
            key = inf.find('dt')[0].text
            value = inf.find('dd')[0].text

            if value == '-':
                value = 'NULL'

            if key == 'Form':
                form   = value
            if key == 'Attribute':
                attribute = value
            if key == 'Type':
                dg_type   = value
            if key == 'DP':
                dp = value

            ##### Cost
            if key == 'Play Cost':
                play_cost  = value

            if key == 'Digivolve Cost 1':
                digivolve_1 = value
                try:
                    digivolve_cost_1 = re.findall('^([0-9]+)', digivolve_1)[0]
                    digivolve_level_1 = re.findall('([0-9]+)$', digivolve_1)[0]
                except:
                    digivolve_cost_1 = 'NULL'
                    digivolve_level_1 = 'NULL'

            if key == 'Digivolve Cost 2':
                digivolve_2 = value
                try:
                    digivolve_cost_2 = re.findall('^([0-9]+)', digivolve_2)[0]
                    digivolve_level_2 = re.findall('([0-9]+)$', digivolve_2)[0]
                except:
                    digivolve_cost_2 = 'NULL'
                    digivolve_level_2 = 'NULL'

            #### Effects
            if key == 'Effect':
                try:
                    effect = value.replace('"',"'")
                except:
                    effect = 'NULL'
            if key == 'Digivolve effect':
                try:
                    digivolve_effect = value.replace('"',"'")
                except:
                    digivolve_effect = 'NULL'
            if key == 'Security effect':
                try:
                    security_effect = value.replace('"',"'")
                except:
                    security_effect = 'NULL'
            if key == 'Promo Info':
                promo_info = value
                try:
                    deck_type = re.findall(deck_choice, promo_info)[0].title()
                    deck_name = value.split(deck_type.lower(), 1)[1].title()
                except:
                    deck_type = 'Promotion pack'
                    deck_name = promo_info.rstrip()

        ### Gathering card data
        data = {'Code':code, 'Name':name, 'Level':level, 'Card_type':cd_type, 'Color':color,
                'Form':form, 'Attribute':attribute, 'Digimon_type':dg_type, 'DP':dp,
                'Play_cost':play_cost, 'Digivolve_cost_1':digivolve_cost_1, 'Digivolve_level_1':digivolve_level_1,
                'Digivolve_cost_2':digivolve_cost_2, 'Digivolve_level_2':digivolve_level_2,
                'Effect':effect, 'Digivolve_effect':digivolve_effect, 'Security_effect':security_effect,
                'Deck_type':deck_type, 'Deck_name':deck_name}

        ## Gathering all the decks
        all_cards.append(data)
        data = dict()

# Creating the dataframe
Digimon_cards = pd.DataFrame(all_cards)
Digimon_cards = Digimon_cards.drop_duplicates(['Code'])

# Exporting the data as CSV
Digimon_cards.to_csv('Digimon_cards.csv', index = False)
