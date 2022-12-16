# Libraries
import pandas as pd
import re, sqlite3

# Reading the data
data = pd.read_csv('Digimon_cards.csv')

# Connecting with the database
con = sqlite3.connect('Digimon_Cards.sqlite')
cur = con.cursor()

# Inserting the data
## Card type's table
insert_card_type = 'INSERT INTO Card_types(name) VALUES'

insert_card_type += '('
for card_type in data['Card_type'].unique():
    insert_card_type += '"'+str(card_type) + '"'+'),('
insert_card_type = insert_card_type[:-2] +';'

cur.execute(insert_card_type)
con.commit()

## Color's table
insert_color = 'INSERT INTO Colors(name) VALUES'

insert_color += '('
for color in data['Color'].unique():
    insert_color += '"'+str(color) + '"'+'),('
insert_color = insert_color[:-2] +';'

cur.execute(insert_color)
con.commit()

## Form's table
insert_form = 'INSERT INTO Forms(name) VALUES'

insert_form += '('
for form in data['Form'].unique():
    insert_form += '"'+str(form) + '"'+'),('
insert_form = insert_form[:-2] +';'
insert_form = re.sub('\("-"\),', '', insert_form)

cur.execute(insert_form)
con.commit()

## Atribute's table
insert_attribute = 'INSERT INTO Attributes(name) VALUES'

insert_attribute += '('
for attribute in data['Attribute'].unique():
    insert_attribute += '"'+str(attribute) + '"'+'),('
insert_attribute = insert_attribute[:-2] +';'
insert_attribute = re.sub('\("-"\),', '', insert_attribute)

cur.execute(insert_attribute)
con.commit()

## Digimon type's table
insert_digimon_type = 'INSERT INTO Digimon_types(name) VALUES'

insert_digimon_type += '('
for digimon_type in data['Digimon_type'].unique():
    insert_digimon_type += '"'+str(digimon_type) + '"'+'),('
insert_digimon_type = insert_digimon_type[:-2] +';'

cur.execute(insert_digimon_type)
con.commit()

## Deck type's table
insert_deck_type = 'INSERT INTO Deck_types(name) VALUES'

insert_deck_type += '('
for deck_type in data['Deck_type'].unique():
    insert_deck_type += '"'+str(deck_type) + '"'+'),('
insert_deck_type = insert_deck_type[:-2] +';'

cur.execute(insert_deck_type)
con.commit()

## Effect's table
### Combining all the effects features into one dataframe
Effects = list(data['Effect'])
Effects.extend(data['Digivolve_effect'])
Effects.extend(data['Security_effect'])

Effects = pd.DataFrame(Effects)[0].unique()

### Inserting the values
insert_effect = "INSERT INTO Effects(name) VALUES"

insert_effect = insert_effect + '('
for effect in Effects:
    insert_effect = insert_effect + '"' + str(effect) + '"' + '),('
insert_effect = insert_effect[:-2]+ ';'

cur.execute(insert_effect)
con.commit()

## Digimon's data
colum_names = ['Card_type', 'Color', 'Form', 'Attribute','Digimon_type',
               'Effect', 'Digivolve_effect', 'Security_effect', 'Deck_type']

insert_digimon = '''INSERT INTO Digimons(code, name, level, card_type_id, color_id, form_id, attribute_id,
                                        digimon_type_id, DP, Play_cost, Digivolve_cost_1,
                                        Digivolve_level_1, Digivolve_cost_2, Digivolve_level_2,
                                        effect_id, digivolve_effect_id, security_effect_id, deck_type_id, 'Deck_name') VALUES'''

for row in range(0,len(data)):
    i = 0
    insert_digimon += '('

    for feature in data.iloc[row]:
        title   = data.columns.values[i]
        feature = feature

        if title in ['Effect', 'Digivolve_effect', 'Security_effect']:
            title = 'Effect'

        if title in colum_names:
            select_query = 'SELECT id FROM '
            select_query += str(title) + 's' + ' WHERE name = ? ;'
            cur.execute(select_query, (feature, ))
            try:
                feature_id = cur.fetchone()[0]
                insert_digimon += '"'+str(feature_id) + '"'+','
            except:
                insert_digimon += 'NULL,'
        elif pd.isna(feature):
            insert_digimon += 'NULL,'

        else:
            insert_digimon += '"' + str(feature) + '"'+','

        i = i+1

    insert_digimon = insert_digimon[:-1] +'),'

insert_digimon = insert_digimon[:-2] +');'

cur.execute(insert_digimon)
con.commit()

# Disconnecting from the database
con.close()
