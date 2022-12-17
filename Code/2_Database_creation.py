# Library
import sqlite3

# Connecting with the database
con = sqlite3.connect('Digimon_Cards.sqlite')
cur = con.cursor()

# Creating tables
cur.executescript('''
DROP TABLE IF EXISTS Card_types;
DROP TABLE IF EXISTS Colors;
DROP TABLE IF EXISTS Forms;
DROP TABLE IF EXISTS Attributes;
DROP TABLE IF EXISTS Digimon_types;
DROP TABLE IF EXISTS Deck_types;
DROP TABLE IF EXISTS Effects;
DROP TABLE IF EXISTS Digimons;
CREATE TABLE Card_types(
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    VARCHAR(255)
);
CREATE TABLE Colors(
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    VARCHAR(255)
);
CREATE TABLE Forms(
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    VARCHAR(255)
);
CREATE TABLE Attributes(
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    VARCHAR(255)
);
CREATE TABLE Digimon_types(
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    VARCHAR(255)
);
CREATE TABLE Deck_types(
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    VARCHAR(255)
);
CREATE TABLE Effects(
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT
);
CREATE TABLE Digimons(
    code                VARCHAR(255) NOT NULL PRIMARY KEY,
    name                VARCHAR(255) NOT NULL,
    level               INTEGER      NULL,
    card_type_id        INTEGER      NULL,
    color_id            INTEGER      NULL,
    form_id             INTEGER      NULL,
    attribute_id        INTEGER      NULL,
    digimon_type_id     INTEGER      NULL,
    deck_type_id        INTEGER      NULL,
    Deck_name           INTEGER      NULL,
    DP                  INTEGER      NULL,
    Play_cost           INTEGER      NULL,
    Digivolve_cost_1    INTEGER      NULL,
    Digivolve_level_1   INTEGER      NULL,
    Digivolve_cost_2    INTEGER      NULL,
    Digivolve_level_2   INTEGER      NULL,
    effect_id           INTEGER      NULL,
    digivolve_effect_id INTEGER      NULL,
    security_effect_id  INTEGER      NULL,
    Image_link          TEXT             ,
    FOREIGN KEY(card_type_id)        REFERENCES Card_types(id),
    FOREIGN KEY(color_id)            REFERENCES Colors(id),
    FOREIGN KEY(form_id)             REFERENCES Forms(id),
    FOREIGN KEY(attribute_id)        REFERENCES Attributes(id),
    FOREIGN KEY(digimon_type_id)     REFERENCES Digimon_types(id),
    FOREIGN KEY(deck_type_id)        REFERENCES Deck_types(id),
    FOREIGN KEY(effect_id)           REFERENCES Effectss(id),
    FOREIGN KEY(digimon_type_id)     REFERENCES Effects(id),
    FOREIGN KEY(digivolve_effect_id) REFERENCES Effects(id),
    FOREIGN KEY(security_effect_id)  REFERENCES Effects(id)
);''')

con.commit()

# Disconnecting to the database
con.close()
