import pokemon
import sys
import moves
import ast
import poke
import pygame
import random
import poke_func
from pygame.locals import*

class Item:
    def __init__(self,name):
        self.name = name
        file = open("items/"+name+".txt","r")
        data = file.readlines()
        self.type = ast.literal_eval(data[0][:-1])
        self.desc = ast.literal_eval(data[1])
        self.price = ast.literal_eval(data[2])

    def aan(self):
        if self.name[0] in ['A','E','I','O','U']:
            return "an"
        else:
            return "a"

    def mod(self) -> float:
        if self.name in ['Miracle Seed','Rose Incense']:
            return 'Grass'
        if self.name in ['Rock Incense','Hard Stone','Stone Plate']:
            return 'Rock'
        if self.name == 'Odd Incense':
            return 'Psychic'
        if self.name in ['Sea Incense','Mystic Water','Splash Plate']:
            return 'Water'
        if self.name in ['Icicle Plate','Never-Melt Ice']:
            return 'Ice'
        if self.name == 'Smoke Incense':
            return 'Fire'
        if self.name == 'Metal Coat':
            return 'Steel'
        if self.name in ['Poke Ball','Premier Ball','Friend Ball','Luxury Ball','Heal Ball']:
            return 1
        if self.name == 'Great Ball':
            return 1.5
        if self.name == 'Ultra Ball':
            return 2
        if self.name == 'Master Ball':
            return 255
        if self.type[0] == 'Ball':
            return -1
        if self.name == 'Oran Berry':
            return 10
        if self.name == 'Cheri Berry':
            return [['Par'],"Paralysis"]
        if self.name == 'Pecha Berry':
            return [['Psn','BPs'],"Poisoning"]
        if self.name == 'Aspear Berry':
            return [['Frz'],"Filler"]
        if self.name == 'Rawst Berry':
            return [['Brn'],"Filler"]
        if self.name == 'Chesto Berry':
            return [['Slp'],"Filler"]
        if self.name == 'Lum Berry':
            return [['Slp','Brn','Frz','Psn','BPs','Par'],"Filler"]
        if self.name == 'Persim Berry':
            return [['Cfs'],"Confusion"]
        if self.name == 'Potion':
            return 20
        if self.name == 'Super Potion':
            return 60
        if self.name == 'Fresh Water':
            return 30
        if self.name == 'Pinap Berry':
            return [80,'All']
        if self.name == 'Poffin':
            return [50,'All']
        if self.name == 'Cinnamon Roll':
            return [100,'Ground']
        if self.name == 'Coffee':
            return [100,'Dark']
        if self.name == 'Jello':
            return [100,'Psychic']
        if self.name == 'Lava Cake':
            return [100,'Fire']
        if self.name == 'Cupcake':
            return [100,'Fairy']
        if self.name == 'Sundae':
            return [100,'Ice']
        if self.name == 'Cotton Candy':
            return [100,'Flying']
        if self.name == 'Donut':
            return [100,'Normal']
        if self.name == 'Fruit Salad':
            return [100,'Grass']
        if self.name == 'Taiyaki':
            return [100,'Water']
        if self.name == 'Sponge Cake':
            return [100,'Flying']
        if self.name == 'Gummy Worms':
            return [100,'Bug']
        if self.name == 'TM01 Work Up':
            return ['Bulbasaur','Ivysaur','Venusaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate','Spearow','Fearow','Alolan_Sandshrew','Alolan_Sandslash','Clefairy','Clefable','Jigglypuff','Wigglytuff','Alolan_Diglett','Alolan_Dugtrio','Meowth','Alolan_Meowth','Persian','Alolan_Persian','Mankey','Primeape','Poliwrath','Machop','Machoke','Machamp',"Farfetch'd",'Doduo','Dodrio','Hitmonlee','Hitmonchan','Lickitung','Chansey','Kangaskhan','Tauros','Eevee','Vaporeon','Jolteon','Flareon','Snorlax','Mew','Chikorita','Bayleef','Meganium','Cyndaquil','Quilava','Typhlosion','Totodile','Croconaw','Feraligatr','Sentret','Furret','Hoothoot','Noctowl','Cleffa','Igglybuff','Togepi','Togetic','Marill','Azumarill','Aipom','Espeon','Umbreon','Girafarig','Snubbull','Granbull','Heracross','Teddiursa','Ursaring','Stantler','Tyrogue','Hitmontop','Miltank','Blissey','Treecko','Grovyle','Sceptile','Torchic','Combusken','Blaziken','Mudkip','Marshtomp','Swampert','Zigzagoon','Linoone','Taillow','Swellow','Breloom','Slakoth','Vigoroth','Slaking','Whismur','Loudred','Exploud','Makuhita','Hariyama','Azurill','Skitty','Delcatty','Meditite','Medicham','Zangoose','Spinda','Castform','Kecleon','Turtwig','Grotle','Torterra','Chimchar','Monferno','Infernape','Piplup','Prinplup','Empoleon','Starly','Staravia','Staraptor','Bidoof','Bibarel','Ambipom','Buneary','Lopunny','Glameow','Purugly','Happiny','Chatot','Munchlax','Riolu','Lucario','Croagunk','Toxicroak','Lickilicky','Togekiss','Leafeon','Glaceon','Gallade','Arceus','Victini','Snivy','Servine','Serperior','Tepig','Pignite','Emboar','Oshawott','Dewott','Samurott','Patrat','Watchog','Lillipup','Herdier','Stoutland','Pansage','Simisage','Panpour','Simipour','Pansear','Simisear','Pidove','Tranquill','Unfezant','Audino','Timburr','Gurdurr','Conkeldurr','Throh','Sawk','Darumaka','Darmanitan','Scraggy','Scrafty','Minccino','Cinccino','Deerling','Sawsbuck','Mienfoo','Mienshao','Bouffalant','Rufflet','Braviary','Deino','Zweilous','Hydreigon','Cobalion','Terrakion','Virizion','Keldeo','Meloetta','Chespin','Quilladin','Chesnaught','Fennekin','Braixen','Delphox','Froakie','Frogadier','Greninja','Bunnelby','Diggersby','Fletchling','Fletchinder','Talonflame','Litleo','Pyroar','Skiddo','Gogoat','Pancham','Pangoro','Furfrou','Espurr','Meowstic_M','Meowstic_F','Sylveon','Hawlucha','Rowlet','Dartrix','Decidueye','Torracat','Litten','Incineroar','Popplio','Brionne','Primarina','Pikipek','Trumbeak','Toucannon','Yungoos','Gumshoos','Crabrawler','Crabominable','Oricorio','Stufful','Bewear','Passimian','Oranguru','Type: Null','Silvally','Komala','Turtonator','Togedemaru','Mimikyu','Drampa','Jangmo-o','Kommo-o','Hakamo-o','Tapu Koko','Tapu Bulu','Solgaleo','Lunala','Buzzwole','Marshadow','Zeraora']
        if self.name == 'TM05 Roar':
            return ['Venusaur','Charizard','Blastoise','Raticate','Alolan_Raticate','Nidoqueen','Nidoking','Vulpix','Ninetales','Alolan_Vulpix','Alolan_Ninetales','Persian','Alolan_Persian','Growlithe','Arcanine','Golem','Alolan_Golem','Onix','Rhydon','Rhyhorn','Kangaskhan','Gyarados','Lapras','Vaporeon','Jolteon','Flareon','Aerodactyl','Articuno','Zapdos','Moltres','Dragonite','Mew','Quilava','Typhlosion','Croconaw','Feraligatr','Steelix','Snubbull','Granbull','Teddiursa','Ursaring','Swinub','Piloswine','Skarmory','Houndour','Houndoom','Phanpy','Donphan','Stantler','Raikou','Entei','Suicune','Tyranitar','Lugia','Ho-Oh','Sceptile','Blaziken','Swampert','Poochyena','Mightyena','Linoone','Vigoroth','Slaking','Whismur','Loudred','Exploud','Aron','Lairon','Aggron','Electrike','Manectric','Sharpedo','Wailmer','Wailord','Camerupt','Altaria','Zangoose','Tropius','Sealeo','Walrein','Bagon','Shelgon','Salamence','Latias','Latios','Kyogre','Groudon','Rayquaza','Torterra','Infernape','Empoleon','Shinx','Luxio','Luxray','Cranidos','Rampardos','Shieldon','Bastiodon','Floatzel','Purugly','Stunky','Skuntank','Gible','Gabite','Garchomp','Riolu','Lucario','Hippopotas','Hippowdon','Drapion','Rhyperior','Leafeon','Glaceon','Mamoswine','Dialga','Palkia','Heatran','Giratina','Arceus','Tepig','Pignite','Emboar','Lillipup','Herdier','Stoutland','Sandile','Krokorok','Krookodile','Darumaka','Darmanitan','Scraggy','Scrafty','Archen','Archeops','Zorua','Zoroark','Eelektross','Axew','Fraxure','Haxorus','Beartic','Druddigon','Deino','Zweilous','Hydreigon','Cobalion','Terrakion','Virizion','Keldeo','Chespin','Quilladin','Chesnaught','Litleo','Pyroar','Skiddo','Gogoat','Pancham','Pangoro','Furfrou','Tyrunt','Tyrantrum','Amaura','Aurorus','Avalugg','Xerneas','Volcanion','Litten','Torracat','Incineroar','Gumshoos','Rockruff','Lycanroc','Mudbray','Mudsdale','Stufful','Bewear','Type: Null','Silvally','Turtonator','Drampa','Jangmo-o','Hakamo-o','Kommo-o','Tapu Koko','Tapu Bulu','Solgaleo','Lunala']
        if self.name == 'TM07 Hail':
            return ['Squirtle','Wartortle','Blastoise','Alolan_Sandshrew','Alolan_Sandslash','Alolan_Vulpix','Alolan_Ninetales','Psyduck','Golduck','Poliwag','Poliwhirl','Poliwrath','Tentacool','Tentacruel','Slowpoke','Slowbro','Seel','Dewgong','Shellder','Cloyster','Krabby','Kingler','Chansey','Kangaskhan','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Jynx','Gyarados','Lapras','Vaporeon','Omanyte','Omastar','Kabuto','Kabutops','Articuno','Dratini','Dragonair','Dragonite','Mewtwo','Mew','Totodile','Croconaw','Feraligatr','Chinchou','Lanturn','Marill','Azumarill','Wooper','Quagsire','Slowking','Qwilfish','Sneasel','Swinub','Piloswine','Corsola','Delibird','Mantine','Kingdra','Smoochum','Blissey','Suicune','Lugia','Mudkip','Marshtomp','Swampert','Lotad','Lombre','Ludicolo','Wingull','Pelipper','Azurill','Carvanha','Sharpedo','Wailmer','Wailord','Barboach','Whiscash','Corphish','Crawdaunt','Feebas','Milotic','Castform','Absol','Snorunt','Glalie','Spheal','Sealeo','Walrein','Clamperl','Huntail','Gorebyss','Relicanth','Luvdisc','Regice','Kyogre','Piplup','Prinplup','Empoleon','Buizel','Floatzel','Shellos','Gastrodon','Happiny','Finneon','Lumineon','Mantyke','Snover','Abomasnow','Weavile','Glaceon','Mamoswine','Froslass','Palkia','Phione','Manaphy','Arceus','Oshawott','Dewott','Samurott','Panpour','Simipour','Tympole','Palpitoad','Seismitoad','Basculin','Ducklett','Swanna','Vanillite','Vanillish','Vanilluxe','Frillish','Jellicent','Alomomola','Cubchoo','Beartic','Cryogonal','Kyurem','Keldeo','Skrelp','Dragalge','Amaura','Aurorus','Carbink','Goodra','Bergmite','Avalugg','Xerneas','Diancie','Popplio','Brionne','Primarina','Crabominable','Wishiwashi','Mareanie','Toxapex','Wimpod','Golisopod','Pyukumuku','Type: Null','Silvally']
        if self.name == 'TM12 Taunt':
            return ['Spooky_Wobbuffet','Rattata','Alolan_Rattata','Raticate','Alolan_Raticate','Nidoqueen','Nidoking','Zubat','Golbat','Meowth','Alolan_Meowth','Persian','Alolan_Persian','Mankey','Primeape','Abra','Kadabra','Alakazam','Dodrio','Grimer','Alolan_Grimer','Muk','Alolan_Muk','Gastly','Haunter','Gengar','Onix','Drowzee','Hypno','Voltorb','Electrode','Koffing','Weezing','Mr. Mime','Jynx','Electabuzz','Magmar','Gyarados','Aerodactyl','Mewtwo','Mew','Crobat','Sudowoodo','Aipom','Umbreon','Murkrow','Misdreavus','Gligar','Steelix','Snubbull','Granbull','Qwilfish','Sneasel','Teddiursa','Ursaring','Skarmory','Houndour','Houndoom','Larvitar','Pupitar','Tyranitar','Poochyena','Mightyena','Ralts','Kirlia','Gardevoir','Vigoroth','Slaking','Loudred','Exploud','Nosepass','Sableye','Mawile','Aggron','Carvanha','Sharpedo','Spoink','Grumpig','Zangoose','Seviper','Corphish','Crawdaunt','Shuppet','Banette','Duskull','Dusclops','Chimecho','Absol','Glalie','Deoxys','Chimchar','Monferno','Infernape','Bidoof','Bibarel','Kricketune','Shieldon','Bastiodon','Floatzel','Ambipom','Mismagius','Honchkrow','Glameow','Purugly','Chingling','Stunky','Skuntank','Mime Jr.','Chatot','Spiritomb','Skorupi','Drapion','Croagunk','Toxicroak','Weavile','Electivire','Magmortar','Gliscor','Gallade','Probopass','Dusknoir','Froslass','Azelf','Heatran','Victini','Darkrai','Snivy','Servine','Serperior','Tepig','Pignite','Emboar','Oshawott','Dewott','Samurott','Purrloin','Liepard','Pansage','Simisage','Panpour','Simipour','Pansear','Simisear','Pidove','Tranquill','Unfezant','Woobat','Swoobat','Timburr','Gurdurr','Conkeldurr','Throh','Sawk','Cottonee','Whimsicott','Basculin','Sandile','Krokorok','Krookodile','Darumaka','Darmanitan','Scraggy','Scrafty','Archen','Archeops','Zorua','Zoroark','Gothita','Gothorita','Gothitelle','Vanillite','Vanillish','Vanilluxe','Emolga','Frillish','Jellicent','Litwick','Lampent','Chandelure','Axew','Fraxure','Haxorus','Beartic','Mienfoo','Mienshao','Druddigon','Pawniard','Bisharp','Bouffalant','Vullaby','Mandibuzz','Heatmor','Deino','Zweilous','Hydreigon','Cobalion','Terrakion','Virizion','Thundurus','Tornadus','Keldeo','Chespin','Quilladin','Chesnaught','Froakie','Frogadier','Greninja','Fletchling','Fletchinder','Talonflame','Litleo','Pyroar','Pangoro','Inkay','Malamar','Binacle','Barbaracle','Hawlucha','Noibat','Noivern','Yveltal','Hoopa','Litten','Torracat','Incineroar','Yungoos','Gumshoos','Oricorio','Rockruff','Lycanroc','Salandit','Salazzle','Stufful','Bewear','Comfey','Oranguru','Passimian','Wimpod','Golisopod','Pyukumuku','Turtonator','Mimikyu','Bruxish','Jangmo-o','Hakamo-o','Kommo-o','Tapu Koko','Tapu Lele','Tapu Bulu','Tapu Fini','Buzzwole','Pheromosa','Blacephalon','Zeraora']
        if self.name == 'TM18 Rain Dance':
            return ['Squirtle','Wartortle','Blastoise','Butterfree','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate','Alolan_Rattata','Alolan_Raticate','Spearow','Fearow','Ekans','Arbok','Pikachu','Raichu','Alolan_Raichu','Nidoran_M','Nidoran_F','Nidorina','Nidorino','Nidoking','Nidoqueen','Clefairy','Clefable','Alolan_Vulpix','Alolan_Ninetales','Jigglypuff','Wigglytuff','Zubat','Golbat','Meowth','Alolan_Meowth','Persian','Alolan_Persian','Psyduck','Golduck','Mankey','Primeape','Poliwag','Poliwhirl','Poliwrath','Abra','Kadabra','Alakazam','Machop','Machoke','Machamp','Tentacool','Tentacruel','Slowpoke','Slowbro','Magnemite','Magneton','Seel','Dewgong','Grimer','Muk','Alolan_Grimer','Alolan_Muk','Shellder','Cloyster','Gastly','Haunter','Gengar','Drowzee','Hypno','Krabby','Kingler','Voltorb','Electrode','Alolan_Marowak','Hitmonlee','Hitmonchan','Lickitung','Koffing','Weezing','Rhyhorn','Rhydon','Chansey','Kangaskhan','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Mr. Mime','Scyther','Jynx','Electabuzz','Pinsir','Tauros','Gyarados','Lapras','Eevee','Vaporeon','Jolteon','Flareon','Porygon','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Snorlax','Articuno','Zapdos','Moltres','Dratini','Dragonair','Dragonite','Mewtwo','Mew','Totodile','Croconaw','Feraligatr','Sentret','Furret','Hoothoot','Noctowl','Crobat','Chinchou','Lanturn','Pichu','Cleffa','Igglybuff','Togepi','Togetic','Natu','Xatu','Mareep','Flaaffy','Ampharos','Marill','Azumarill','Aipom','Wooper','Quagsire','Espeon','Umbreon','Murkrow','Slowking','Misdreavus','Girafarig','Dunsparce','Gligar','Snubbull','Granbull','Qwilfish','Scizor','Heracross','Sneasel','Teddiursa','Ursaring','Swinub','Piloswine','Corsola','Remoraid','Octillery','Delibird','Mantine','Kingdra','Porygon2','Stantler','Tyrogue','Hitmontop','Smoochum','Elekid','Miltank','Blissey','Raikou','Entei','Suicune','Larvitar','Pupitar','Tyranitar','Lugia','Ho-Oh','Celebi','Mudkip','Marshtomp','Swampert','Poochyena','Mightyena','Zigzagoon','Linoone','Lotad','Lombre','Ludicolo','Taillow','Swellow','Wingull','Pelipper','Ralts','Kirlia','Gardevoir','Surskit','Masquerain','Slakoth','Vigoroth','Slaking','Whismur','Loudred','Exploud','Makuhita','Hariyama','Azurill','Skitty','Delcatty','Sableye','Mawile','Aron','Lairon','Aggron','Meditite','Medicham','Electrike','Manectric','Plusle','Minun','Volbeat','Illumise','Roselia','Gulpin','Swalot','Carvanha','Sharpedo','Wailmer','Wailord','Spoink','Grumpig','Spinda','Swablu','Altaria','Zangoose','Seviper','Solrock','Lunatone','Barboach','Whiscash','Corphish','Crawdaunt','Baltoy','Claydol','Feebas','Milotic','Castform','Kecleon','Shuppet','Banette','Duskull','Dusclops','Dusknoir','Chimecho','Absol','Snorunt','Glalie','Spheal','Sealeo','Walrein','Clamperl','Huntail','Gorebyss','Relicanth','Luvdisc','Bagon','Shelgon','Salamence','Metang','Metagross','Regice','Registeel','Latias','Latios','Kyogre','Rayquaza','Jirachi','Deoxys','Piplup','Prinplup','Empoleon','Starly','Staravia','Staraptor','Bidoof','Bibarel','Kricketune','Shinx','Luxio','Luxray','Budew','Roserade','Cranidos','Rampardos','Shieldon','Bastiodon','Vespiquen','Pachirisu','Buizel','Floatzel','Shellos','Gastrodon','Ambipom','Drifloon','Drifblim','Buneary','Lopunny','Mismagius','Honchkrow','Glameow','Purugly','Chingling','Stunky','Skuntank','Bronzor','Bronzong','Mime Jr.','Happiny','Chatot','Spiritomb','Gible','Gabite','Garchomp','Munchlax','Riolu','Lucario','Skorupi','Drapion','Croagunk','Toxicroak','Finneon','Lumineon','Mantyke','Snover','Abomasnow','Weavile','Magnezone','Lickilicky','Rhyperior','Electivire','Togekiss','Leafeon','Glaceon','Gliscor','Mamoswine','Porygon-Z','Gallade','Froslass','Rotom','Uxie','Mesprit','Azelf','Dialga','Palkia','Regigigas','Giratina','Cresselia','Phione','Manaphy','Darkrai','Arceus','Oshawott','Dewott','Samurott','Patrat','Watchog','Lillipup','Herdier','Stoutland','Purrloin','Liepard','Panpour','Simipour','Munna','Musharna','Pidove','Tranquill','Unfezant','Blitzle','Zebstrika','Woobat','Swoobat','Audino','Timburr','Gurdurr','Conkeldurr','Tympole','Palpitoad','Seismitoad','Throh','Sawk','Basculin','Maractus','Scraggy','Scrafty','Sigilyph','Yamask','Cofagrigus','Tirtouga','Carracosta','Trubbish','Garbodor','Zorua','Zoroark','Minccino','Cinccino','Gothita','Gothorita','Gothitelle','Solosis','Duosion','Reuniclus','Ducklett','Swanna','Vanillite','Vanillish','Vanilluxe','Deerling','Sawsbuck','Emolga','Karrablast','Escavalier','Foongus','Amoonguss','Frillish','Jellicent','Alomomola','Joltik','Galvantula','Eelektrik','Eelektross','Elgyem','Beheeyem','Axew','Fraxure','Haxorus','Cubchoo','Beartic','Cryogonal','Shelmet','Accelgor','Stunfisk','Mienfoo','Mienshao','Druddigon','Golett','Golurk','Pawniard','Bisharp','Bouffalant','Rufflet','Braviary','Vullaby','Mandibuzz','Heatmor','Deino','Zweilous','Hydreigon','Tornadus','Thundurus','Reshiram','Zekrom','Kyurem','Keldeo','Meloetta','Fennekin','Braixen','Delphox','Froakie','Frogadier','Greninja','Vivillon','Litleo','Pyroar','Flabebe','Floette','Florges','Skiddo','Gogoat','Pancham','Pangoro','Furfrou','Espurr','Meowstic_M','Meowstic_F','Honedge','Doublade','Aegislash','Spritzee','Aromatisse','Swirlix','Slurpuff','Inkay','Malamar','Binacle','Barbaracle','Skrelp','Dragalge','Clauncher','Clawitzer','Helioptile','Heliolisk','Amaura','Aurorus','Sylveon','Hawlucha','Dedenne','Goomy','Sliggoo','Goodra','Klefki','Bergmite','Avalugg','Xerneas','Yveltal','Hoopa','Popplio','Brionne','Primarina','Grubbin','Charjabug','Vikavolt','Crabrawler','Crabominable','Wishiwashi','Mareanie','Toxapex','Dewpider','Araquanid','Shiinotic','Oranguru','Passimian','Wimpod','Golisopod','Pyukumuku','Type: Null','Silvally','Bruxish','Drampa','Dhelmise','Tapu Koko','Tapu Fini','Xurkitree']
        if self.name == 'TM22 Solar Beam':
            return ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charizard', 'Butterfree', 'Beedrill', 'Clefairy', 'Clefable', 'Ninetales', 'Alolan_Ninetales', 'Jigglypuff', 'Wigglytuff', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Arcanine', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Ponyta', 'Rapidash', 'Exeggcute', 'Exeggutor', 'Alolan_Exeggutor', 'Lickitung', 'Chansey', 'Tangela', 'Kangaskhan', 'Mr. Mime', 'Tauros', 'Lapras', 'Porygon', 'Snorlax', 'Moltres', 'Mewtwo', 'Mew', 'Chikorita', 'Bayleef', 'Meganium', 'Typhlosion', 'Sentret', 'Furret', 'Ledyba', 'Ledian', 'Spinarak', 'Ariados', 'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Natu', 'Xatu', 'Bellossom', 'Hoppip', 'Skiploom', 'Jumpluff', 'Aipom', 'Sunkern', 'Sunflora', 'Yanma', 'Pineco', 'Forretress', 'Dunsparce', 'Snubbull', 'Granbull', 'Magcargo', 'Houndour', 'Houndoom', 'Porygon2', 'Stantler', 'Miltank', 'Blissey', 'Entei', 'Ho-Oh', 'Celebi', 'Treecko', 'Grovyle', 'Sceptile', 'Blaziken', 'Beautifly', 'Dustox', 'Lotad', 'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Surskit', 'Masquerain', 'Shroomish', 'Breloom', 'Slakoth', 'Vigoroth', 'Slaking', 'Nincada', 'Ninjask', 'Shedinja', 'Whismur', 'Loudred', 'Exploud', 'Skitty', 'Delcatty', 'Mawile', 'Aggron', 'Volbeat', 'Illumise', 'Roselia', 'Gulpin', 'Swalot', 'Camerupt', 'Torkoal', 'Trapinch', 'Vibrava', 'Flygon', 'Cacnea', 'Cacturne', 'Swablu', 'Altaria', 'Zangoose', 'Solrock', 'Baltoy', 'Claydol', 'Lileep', 'Cradily', 'Castform', 'Kecleon', 'Tropius', 'Latias', 'Latios', 'Groudon', 'Rayquaza', 'Deoxys', 'Turtwig', 'Grotle', 'Torterra', 'Infernape', 'Budew', 'Roserade', 'Cherubi', 'Cherrim', 'Ambipom', 'Buneary', 'Lopunny', 'Bronzor', 'Bronzong', 'Mime Jr.', 'Happiny', 'Munchlax', 'Carnivine', 'Snover', 'Abomasnow', 'Lickilicky', 'Tangrowth', 'Magmortar', 'Togekiss', 'Yanmega', 'Leafeon', 'Porygon-Z', 'Uxie', 'Heatran', 'Cresselia', 'Shaymin', 'Shaymin', 'Arceus', 'Victini', 'Snivy', 'Servine', 'Serperior', 'Tepig', 'Pignite', 'Emboar', 'Pansage', 'Simisage', 'Pansear', 'Simisear', 'Gigalith', 'Audino', 'Sewaddle', 'Swadloon', 'Leavanny', 'Venipede', 'Whirlipede', 'Scolipede', 'Cottonee', 'Whimsicott', 'Petilil', 'Lilligant', 'Darumaka', 'Darmanitan', 'Maractus', 'Dwebble', 'Crustle', 'Sigilyph', 'Garbodor', 'Deerling', 'Sawsbuck', 'Emolga', 'Foongus', 'Amoonguss', 'Ferroseed', 'Ferrothorn', 'Litwick', 'Lampent', 'Chandelure', 'Cryogonal', 'Golurk', 'Heatmor', 'Larvesta', 'Volcarona', 'Virizion', 'Reshiram', 'Genesect', 'Chespin', 'Quilladin', 'Chesnaught', 'Fennekin', 'Braixen', 'Delphox', 'Talonflame', 'Vivillon', 'Litleo', 'Pyroar', 'Flabebe', 'Floette', 'Floette', 'Florges', 'Skiddo', 'Gogoat', 'Phantump', 'Trevenant', 'Pumpkaboo', 'Gourgeist', 'Noibat', 'Noivern', 'Volcanion', 'Rowlet', 'Dartrix', 'Decidueye', 'Vikavolt', 'Ribombee', 'Fomantis', 'Lurantis', 'Morelull', 'Shiinotic', 'Bounsweet', 'Steenee', 'Tsareena', 'Comfey', 'Minior', 'Turtonator', 'Drampa', 'Dhelmise', 'Tapu Bulu', 'Solgaleo', 'Lunala', 'Xurkitree', 'Celesteela', 'Necrozma', 'Necrozma', 'Necrozma', 'Magearna']
        if self.name == 'TM27 Return':
            return ['Reverse','Spooky_Wobbuffet','Caterpie','Metapod','Weedle','Kakuna','Magikarp','Ditto','Unown','Wobbuffet','Smeargle','Wurmple','Silcoon','Cascoon','Wynaut','Beldum','Kricketot','Combee','Tynamo','Scatterbug','Spewpa','Pyukumuku','Cosmog','Cosmoem']
        if self.name == 'TM37 Sandstorm':
            return ['Sandshrew','Sandslash','Nidoqueen','Nidoking','Diglett','Alolan_Diglett','Dugtrio','Alolan_Dugtrio','Geodude','Alolan_Geodude','Graveler','Alolan_Graveler','Golem','Alolan_Golem','Onix','Cubone','Marowak','Alolan_Marowak','Lickitung','Rhyhorn','Rhydon','Chansey','Kangaskhan','Tauros','Gyarados','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Snorlax','Articuno','Zapdos','Moltres','Dragonite','Mew','Mewtwo','Sudowoodo','Wooper','Quagsire','Pineco','Forretress','Gligar','Steelix','Scizor','Shuckle','Magcargo','Swinub','Piloswine','Corsola','Skarmory','Phanpy','Donphan','Hitmontop','Miltank','Blissey','Raikou','Entei','Suicune','Larvitar','Pupitar','Tyranitar','Lugia','Ho-Oh','Celebi','Nincada','Ninjask','Shedinja','Nosepass','Mawile','Aron','Lairon','Aggron','Numel','Camerupt','Trapinch','Vibrava','Flygon','Cacnea','Cacturne','Lunatone','Solrock','Barboach','Whiscash','Baltoy','Claydol','Lileep','Cradily','Anorith','Armaldo','Castform','Absol','Relicanth','Metang','Metagross','Regirock','Registeel','Latias','Latios','Groudon','Rayquaza','Jirachi','Torterra','Cranidos','Rampardos','Shieldon','Bastiodon','Gastrodon','Bronzor','Bronzong','Bonsly','Gible','Gabite','Garchomp','Munchlax','Hippopotas','Hippowdon','Lickilicky','Rhyperior','Gliscor','Mamoswine','Probopass','Uxie','Mesprit','Azelf','Dialga','Palkia','Arceus','Roggenrola','Boldore','Gigalith','Drilbur','Excadrill','Sandile','Krokorok','Krookodile','Dwebble','Crustle','Tirtouga','Carracosta','Archen','Archeops','Ferrothorn','Klink','Klang','Klinklang','Accelgor','Stunfisk','Pawniard','Bisharp','Durant','Cobalion','Terrakion','Landorus','Bunnelby','Diggersby','Binacle','Barbaracle','Helioptile','Heliolisk','Tyrunt','Tyrantrum','Amaura','Aurorus','Carbink','Zygarde','Diancie','Volcanion','Yungoos','Gumshoos','Mudbray','Mudsdale','Sandygast','Palossand','Type: Null','Silvally','Minior','Jangmo-o','Hakamo-o','Kommo-o','Nihilego','Stakataka']
        if self.name == 'TM39 Rock Tomb':
            return ['Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Ekans','Arbok','Sandshrew','Sandslash','Nidoqueen','Nidoking','Diglett','Alolan_Diglett','Dugtrio','Alolan_Dugtrio','Mankey','Primeape','Poliwrath','Machop','Machoke','Machamp','Geodude','Alolan_Geodude','Graveler','Alolan_Graveler','Golem','Alolan_Golem','Grimer','Alolan_Grimer','Muk','Alolan_Muk','Onix','Krabby','Kingler','Cubone','Marowak','Alolan_Marowak','Hitmonlee','Hitmonchan','Lickitung','Rhyhorn','Rhydon','Chansey','Kangaskhan','Pinsir','Tauros','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Snorlax','Dragonite','Mewtwo','Mew','Typhlosion','Totodile','Croconaw','Feraligatr','Sudowoodo','Quagsire','Pineco','Forretress','Dunsparce','Gligar','Steelix','Granbull','Shuckle','Heracross','Teddiursa','Ursaring','Slugma','Magcargo','Swinub','Piloswine','Corsola','Mantine','Skarmory','Phanpy','Donphan','Miltank','Blissey','Larvitar','Pupitar','Tyranitar','Treecko','Grovyle','Sceptile','Torchic','Combusken','Blaziken','Mudkip','Marshtomp','Swampert','Nuzleaf','Shiftry','Breloom','Slakoth','Vigoroth','Slaking','Loudred','Exploud','Makuhita','Hariyama','Nosepass','Sableye','Mawile','Aron','Lairon','Aggron','Meditite','Medicham','Sharpedo','Wailmer','Wailord','Numel','Camerupt','Torkoal','Spinda','Trapinch','Vibrava','Flygon','Zangoose','Lunatone','Solrock','Barboach','Whiscash','Corphish','Crawdaunt','Baltoy','Claydol','Lileep','Cradily','Anorith','Armaldo','Kecleon','Dusclops','Absol','Spheal','Sealeo','Walrein','Huntail','Relicanth','Bagon','Shelgon','Salamence','Metang','Metagross','Regirock','Regice','Registeel','Kyogre','Groudon','Rayquaza','Deoxys','Torterra','Monferno','Infernape','Piplup','Prinplup','Empoleon','Cranidos','Rampardos','Shieldon','Bastiodon','Buizel','Floatzel','Gastrodon','Bronzor','Bronzong','Bonsly','Spiritomb','Gible','Gabite','Garchomp','Munchlax','Riolu','Lucario','Hippopotas','Hippowdon','Skorupi','Drapion','Croagunk','Toxicroak','Abomasnow','Lickilicky','Rhyperior','Tangrowth','Electivire','Magmortar','Gliscor','Mamoswine','Gallade','Probopass','Dusknoir','Dialga','Palkia','Heatran','Regigigas','Darkrai','Arceus','Tepig','Pignite','Emboar','Lillipup','Herdier','Stoutland','Pansage','Simisage','Panpour','Simipour','Pansear','Simisear','Munna','Musharna','Roggenrola','Boldore','Gigalith','Drilbur','Excadrill','Timburr','Gurdurr','Conkeldurr','Seismitoad','Throh','Sawk','Scolipede','Sandile','Krokorok','Krookodile','Darumaka','Darmanitan','Dwebble','Crustle','Scraggy','Scrafty','Tirtouga','Carracosta','Archen','Archeops','Gothita','Gothorita','Gothitelle','Solosis','Duosion','Reuniclus','Eelektross','Elgyem','Beheeyem','Axew','Fraxure','Haxorus','Cubchoo','Beartic','Stunfisk','Mienfoo','Mienshao','Druddigon','Golett','Golurk','Pawniard','Bisharp','Bouffalant','Rufflet','Braviary','Vullaby','Mandibuzz','Heatmor','Durant','Hydreigon','Terrakion','Reshiram','Zekrom','Landorus','Kyurem','Chespin','Quilladin','Chesnaught','Froakie','Frogadier','Greninja','Bunnelby','Diggersby','Pancham','Pangoro','Binacle','Barbaracle','Helioptile','Heliolisk','Tyrunt','Tyrantrum','Amaura','Aurorus','Hawlucha','Carbink','Bergmite','Avalugg','Diancie','Yungoos','Gumshoos','Crabrawler','Crabominable','Rockruff','Lycanroc','Mudbray','Mudsdale','Stufful','Bewear','Passimian','Golisopod','Sandygast','Palossand','Minior','Turtonator','Jangmo-o','Hakamo-o','Kommo-o','Tapu Bulu','Solgaleo','Buzzwole','Guzzlord','Necrozma','Marshadow','Stakataka']
        if self.name == 'TM55 Scald':
            return ['Squirtle','Wartortle','Blastoise','Psyduck','Golduck','Poliwag','Poliwhirl','Poliwrath','Tentacool','Tentacruel','Slowpoke','Slowbro','Krabby','Kingler','Horsea','Seadra','Kingdra','Goldeen','Seaking','Staryu','Starmie','Gyarados','Vaporeon','Omanyte','Omastar','Kabuto','Kabutops','Mew','Totodile','Croconaw','Feraligatr','Chinchou','Lanturn','Marill','Azumarill','Wooper','Quagsire','Slowking','Qwilfish','Corsola','Remoraid','Octillery','Mantine','Raikou','Suicune','Mudkip','Marshtomp','Swampert','Lotad','Lombre','Ludicolo','Wingull','Pelipper','Surskit','Masquerain','Azurill','Carvanha','Sharpedo','Wailmer','Wailord','Barboach','Whiscash','Corphish','Crawdaunt','Feebas','Milotic','Castform','Clamperl','Huntail','Gorebyss','Relicanth','Luvdisc','Kyogre','Piplup','Prinplup','Empoleon','Bibarel','Buizel','Floatzel','Shellos','Gastrodon','Finneon','Lumineon','Mantyke','Phione','Manaphy','Emboar','Oshawott','Dewott','Samurott','Panpour','Simipour','Tympole','Palpitoad','Seismitoad','Basculin','Tirtouga','Carracosta','Ducklett','Swanna','Frillish','Jellicent','Alomomola','Stunfisk','Keldeo','Froakie','Frogadier','Greninja','Binacle','Barbaracle','Skrelp','Dragalge','Clauncher','Clawitzer','Volcanion','Popplio','Brionne','Primarina','Crabrawler','Crabominable','Wishiwashi','Mareanie','Toxapex','Dewpider','Araquanid','Wimpod','Golisopod','Bruxish','Tapu Fini']
        if self.name == 'TM69 Rock Polish':
            return ['Geodude','Graveler','Golem','Alolan_Geodude','Alolan_Graveler','Alolan_Golem','Alolan_Grimer','Alolan_Muk','Onix','Rhyhorn','Rhydon','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Mew','Sudowoodo','Forretress','Gligar','Steelix','Shuckle','Magcargo','Corsola','Donphan','Larvitar','Pupitar','Tyranitar','Nosepass','Aron','Lairon','Aggron','Camerupt','Lunatone','Solrock','Baltoy','Claydol','Lileep','Cradily','Anorith','Armaldo','Relicanth','Metang','Metagross','Regirock','Regice','Registeel','Groudon','Torterra','Cranidos','Rampardos','Shieldon','Bastiodon','Bronzor','Bronzong','Bonsly','Rhyperior','Gliscor','Probopass','Regigigas','Roggenrola','Boldore','Gigalith','Dwebble','Crustle','Tirtouga','Carracosta','Archen','Archeops','Garbodor','Ferroseed','Ferrothorn','Klink','Klang','Klinklang','Golett','Golurk','Pawniard','Bisharp','Durant','Cobalion','Terrakion','Landorus','Genesect','Binacle','Barbaracle','Tyrunt','Tyrantrum','Amaura','Aurorus','Carbink','Bergmite','Avalugg','Diancie','Rockruff','Lycanroc','Sandygast','Palossand','Minior','Kommo-o','Necrozma','Stakataka']
        if self.name == 'TM74 Gyro Ball':
            return ['Pineapple_Oddish','Squirtle','Wartortle','Blastoise','Sandshrew','Sandslash','Alolan_Sandshrew','Alolan_Sandslash','Jigglypuff','Wigglytuff','Geodude','Graveler','Golem','Alolan_Geodude','Alolan_Graveler','Alolan_Golem','Magnemite','Magneton','Onix','Voltorb','Electrode','Koffing','Weezing','Staryu','Starmie','Omanyte','Omastar','Mew','Typhlosion','Pineco','Forretress','Dunsparce','Steelix','Qwilfish','Shuckle','Magcargo','Donphan','Hitmontop','Miltank','Torkoal','Lunatone','Solrock','Baltoy','Claydol','Glalie','Metagross','Metang','Rayquaza','Drifloon','Drifblim','Bronzor','Bronzong','Magnezone','Lickilicky','Tepig','Pignite','Emboar','Munna','Musharna','Woobat','Swoobat','Venipede','Whirlipede','Scolipede','Darumaka','Darmanitan','Solosis','Duosion','Reuniclus','Ferroseed','Ferrothorn','Golett','Golurk','Chespin','Quilladin','Chesnaught','Honedge','Doublade','Aegislash','Spritzee','Aromatisse','Carbink','Pumpkaboo','Gourgeist','Bergmite','Avalugg','Diancie','Volcanion','Passimian','Minior','Togedemaru','Dhelmise','Solgaleo','Buzzwole','Celesteela','Guzzlord','Necrozma','Magearna','Stakataka']
        if self.name == 'TM78 Bulldoze':
            return ['Venusaur','Charizard','Blastoise','Ekans','Arbok','Sandshrew','Alolan_Sandshrew','Sandslash','Alolan_Sandslash','Nidoqueen','Nidoking','Diglett','Alolan_Diglett','Dugtrio','Alolan_Dugtrio','Mankey','Primeape','Arcanine','Poliwag','Poliwhirl','Poliwrath','Machop','Machoke','Machamp','Geodude','Graveler','Golem','Alolan_Geodude','Alolan_Graveler','Alolan_Golem','Slowpoke','Slowbro','Onix','Exeggutor','Alolan_Exeggutor','Cubone','Marowak','Alolan_Marowak','Hitmonlee','Hitmonchan','Lickitung','Rhyhorn','Rhydon','Chansey','Kangaskhan','Pinsir','Tauros','Gyarados','Lapras','Aerodactyl','Snorlax','Dragonite','Mewtwo','Mew','Meganium','Typhlosion','Feraligatr','Ampharos','Azumarill','Sudowoodo','Wooper','Quagsire','Slowking','Girafarig','Pineco','Forretress','Dunsparce','Gligar','Steelix','Snubbull','Granbull','Shuckle','Heracross','Teddiursa','Ursaring','Magcargo','Swinub','Piloswine','Corsola','Mantine','Phanpy','Donphan','Stantler','Tyrogue','Hitmontop','Miltank','Blissey','Raikou','Entei','Suicune','Larvitar','Pupitar','Tyranitar','Lugia','Ho-Oh','Sceptile','Blaziken','Marshtomp','Swampert','Vigoroth','Slaking','Loudred','Exploud','Makuhita','Hariyama','Nosepass','Aron','Lairon','Aggron','Swalot','Sharpedo','Wailmer','Wailord','Numel','Camerupt','Torkoal','Grumpig','Trapinch','Vibrava','Flygon','Altaria','Seviper','Lunatone','Solrock','Barboach','Whiscash','Baltoy','Claydol','Cradily','Armaldo','Milotic','Dusclops','Tropius','Glalie','Spheal','Sealeo','Walrein','Relicanth','Salamence','Metang','Metagross','Regirock','Regice','Registeel','Latias','Latios','Kyogre','Groudon','Rayquaza','Torterra','Infernape','Empoleon','Bibarel','Cranidos','Rampardos','Shieldon','Bastiodon','Gastrodon','Purugly','Bronzor','Bronzong','Gible','Gabite','Garchomp','Munchlax','Riolu','Lucario','Hippopotas','Hippowdon','Drapion','Croagunk','Toxicroak','Mantyke','Abomasnow','Lickilicky','Rhyperior','Tangrowth','Electivire','Magmortar','Gliscor','Mamoswine','Gallade','Probopass','Dusknoir','Dialga','Palkia','Heatran','Regigigas','Giratina','Arceus','Pignite','Emboar','Roggenrola','Boldore','Gigalith','Drilbur','Excadrill','Conkeldurr','Palpitoad','Seismitoad','Throh','Sawk','Scolipede','Sandile','Krokorok','Krookodile','Darmanitan','Dwebble','Crustle','Tirtouga','Carracosta','Archen','Archeops','Ferrothorn','Haxorus','Beartic','Stunfisk','Druddigon','Golett','Golurk','Bouffalant','Hydreigon','Terrakion','Landorus','Chespin','Quilladin','Chesnaught','Bunnelby','Diggersby','Litleo','Pyroar','Skiddo','Gogoat','Pancham','Pangoro','Binacle','Barbaracle','Helioptile','Heliolisk','Tyrunt','Tyrantrum','Amaura','Aurorus','Goodra','Phantump','Trevenant','Avalugg','Zygarde','Volcanion','Incineroar','Gumshoos','Crabrawler','Crabominable','Wishiwashi','Mudbray','Mudsdale','Stufful','Bewear','Oranguru','Passimian','Sandygast','Palossand','Minior','Komala','Turtonator','Drampa','Dhelmise','Jangmo-o','Hakamo-o','Kommo-o','Solgaleo','Buzzwole','Celesteela','Guzzlord','Necrozma','Stakataka']
        if self.name == 'TM83 Infestation':
            return ['Pineapple_Oddish','Butterfree','Beedrill','Ekans','Arbok','Oddish','Gloom','Vileplume','Venonat','Venomoth','Bellsprout','Weepinbell','Victreebel','Tentacool','Tentacruel','Grimer','Alolan_Grimer','Muk','Alolan_Muk','Gastly','Haunter','Gengar','Exeggcute','Exeggutor','Alolan_Exeggutor','Koffing','Weezing','Tangela','Mr. Mime','Mew','Ledyba','Ledian','Spinarak','Ariados','Bellossom','Hoppip','Skiploom','Jumpluff','Wooper','Quagsire','Shuckle','Slugma','Magcargo','Beautifly','Dustox','Surskit','Masquerain','Volbeat','Illumise','Gulpin','Swalot','Seviper','Lileep','Cradily','Banette','Duskull','Dusclops','Huntail','Gorebyss','Kricketune','Vespiquen','Shellos','Gastrodon','Mime Jr.','Spiritomb','Skorupi','Drapion','Carnivine','Tangrowth','Dusknoir','Tympole','Palpitoad','Seismitoad','Venipede','Whirlipede','Scolipede','Yamask','Cofagrigus','Trubbish','Garbodor','Solosis','Duosion','Reuniclus','Karrablast','Escavalier','Joltik','Galvantula','Shelmet','Accelgor','Stunfisk','Genesect','Vivillon','Pangoro','Binacle','Barbaracle','Goomy','Sliggoo','Goodra','Cutiefly','Ribombee','Mareanie','Toxapex','Dewpider','Araquanid','Sandygast','Palossand','Mimikyu','Stakataka']
        if self.name == 'TM86 Grass Knot':
            return ['Pineapple_Oddish','Bulbasaur','Ivysaur','Venusaur','Rattata','Alolan_Rattata','Raticate','Alolan_Raticate','Pikachu','Raichu','Alolan_Raichu','Clefairy','Clefable','Jigglypuff','Wigglytuff','Oddish','Gloom','Vileplume','Paras','Parasect','Abra','Kadabra','Alakazam','Bellsprout','Weepinbell','Victreebel','Slowpoke','Slowbro','Drowzee','Hypno','Exeggcute','Exeggutor','Alolan_Exeggutor','Chansey','Tangela','Starmie','Mr. Mime','Jynx','Mewtwo','Mew','Chikorita','Bayleef','Meganium','Sentret','Furret','Pichu','Cleffa','Igglybuff','Togepi','Togetic','Natu','Xatu','Bellossom','Marill','Azumarill','Hoppip','Skiploom','Jumpluff','Aipom','Sunkern','Sunflora','Espeon','Slowking','Girafarig','Smoochum','Blissey','Celebi','Treecko','Grovyle','Sceptile','Zigzagoon','Linoone','Lotad','Lombre','Ludicolo','Seedot','Nuzleaf','Shiftry','Ralts','Kirlia','Gardevoir','Shroomish','Breloom','Skitty','Delcatty','Mawile','Meditite','Medicham','Plusle','Minun','Roselia','Spoink','Grumpig','Cacnea','Cacturne','Lunatone','Solrock','Baltoy','Claydol','Lileep','Cradily','Kecleon','Tropius','Chimecho','Metang','Metagross','Latias','Latios','Jirachi','Deoxys','Turtwig','Grotle','Torterra','Chimchar','Monferno','Infernape','Piplup','Prinplup','Empoleon','Bidoof','Bibarel','Budew','Roserade','Pachirisu','Cherubi','Cherrim','Ambipom','Buneary','Lopunny','Chingling','Bronzor','Bronzong','Mime Jr.','Happiny','Carnivine','Snover','Abomasnow','Tangrowth','Togekiss','Leafeon','Gallade','Uxie','Mesprit','Azelf','Cresselia','Phione','Manaphy','Shaymin','Arceus','Victini','Snivy','Servine','Serperior','Tepig','Pignite','Emboar','Oshawott','Dewott','Samurott','Patrat','Watchog','Purrloin','Liepard','Pansage','Simisage','Panpour','Simipour','Pansear','Simisear','Audino','Timburr','Gurdurr','Conkeldurr','Seismitoad','Throh','Sawk','Sewaddle','Swadloon','Leavanny','Cottonee','Whimsicott','Petilil','Lilligant','Krokorok','Krookodile','Darumaka','Darmanitan','Maractus','Scraggy','Scrafty','Cofagrigus','Zorua','Zoroark','Minccino','Cinccino','Gothita','Gothorita','Gothitelle','Reuniclus','Deerling','Sawsbuck','Foongus','Amoonguss','Ferrothorn','Eelektross','Haxorus','Cubchoo','Beartic','Mienfoo','Mienshao','Golett','Golurk','Pawniard','Bisharp','Virizion','Tornadus','Thundurus','Landorus','Meloetta','Chespin','Quilladin','Chesnaught','Fennekin','Braixen','Delphox','Froakie','Frogadier','Greninja','Bunnelby','Diggersby','Flabebe','Floette','Florges','Skiddo','Gogoat','Pancham','Pangoro','Furfrou','Binacle','Barbaracle','Helioptile','Heliolisk','Hawlucha','Dedenne','Phantump','Trevenant','Pumpkaboo','Gourgeist','Xerneas','Zygarde','Hoopa','Rowlet','Dartrix','Decidueye','Fomantis','Lurantis','Morelull','Shiinotic','Bounsweet','Steenee','Tsareena','Comfey','Passimian','Togedemaru','Drampa','Dhelmise','Tapu Koko','Tapu Lele','Tapu Bulu','Tapu Fini','Nihilego','Xurkitree','Celesteela','Magearna','Marshadow','Zeraora']
        if self.name == 'TM94 Surf':
            return ['Squirtle','Wartortle','Blastoise','Alolan_Raichu','Nidoqueen','Nidoking','Psyduck','Golduck','Poliwag','Poliwhirl','Poliwrath','Tentacool','Tentacruel','Slowpoke','Slowbro','Seel','Dewgong','Shellder','Cloyster','Krabby','Kingler','Lickitung','Rhydon','Kangaskhan','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Tauros','Gyarados','Lapras','Vaporeon','Omanyte','Omastar','Kabuto','Kabutops','Snorlax','Dratini','Dragonair','Dragonite','Mew','Totodile','Croconaw','Feraligatr','Sentret','Furret','Chinchou','Lanturn','Marill','Azumarill','Wooper','Quagsire','Slowking','Qwilfish','Sneasel','Corsola','Remoraid','Octillery','Mantine','Kingdra','Miltank','Suicune','Tyranitar','Lugia','Mudkip','Marshtomp','Swampert','Zigzagoon','Linoone','Lotad','Lombre','Ludicolo','Pelipper','Exploud','Makuhita','Hariyama','Azurill','Aggron','Carvanha','Sharpedo','Wailmer','Wailord','Barboach','Whiscash','Corphish','Crawdaunt','Feebas','Milotic','Spheal','Sealeo','Walrein','Clamperl','Huntail','Gorebyss','Relicanth','Luvdisc','Latias','Latios','Kyogre','Rayquaza','Piplup','Prinplup','Empoleon','Bibarel','Rampardos','Buizel','Floatzel','Shellos','Gastrodon','Garchomp','Munchlax','Finneon','Lumineon','Mantyke','Weavile','Lickilicky','Rhyperior','Palkia','Phione','Manaphy','Arceus','Oshawott','Dewott','Samurott','Herdier','Stoutland','Panpour','Simipour','Audino','Tympole','Palpitoad','Seismitoad','Basculin','Tirtouga','Carracosta','Ducklett','Swanna','Frillish','Jellicent','Alomomola','Haxorus','Cubchoo','Beartic','Stunfisk','Druddigon','Bouffalant','Hydreigon','Keldeo','Froakie','Frogadier','Greninja','Bunnelby','Diggersby','Skiddo','Gogoat','Pancham','Pangoro','Furfrou','Swirlix','Slurpuff','Binacle','Barbaracle','Skrelp','Dragalge','Clauncher','Clawitzer','Helioptile','Heliolisk','Goodra','Bergmite','Avalugg','Popplio','Brionne','Primarina','Wishiwashi','Mareanie','Toxapex','Dewpider','Araquanid','Wimpod','Golisopod','Silvally','Bruxish','Drampa','Dhelmise','Tapu Fini']
        if self.name == 'TM95 Snarl':
            return ['Alolan_Rattata','Alolan_Raticate','Alolan_Persian','Growlithe','Arcanine','Alolan_Grimer','Alolan_Muk','Mew','Umbreon','Murkrow','Snubbull','Granbull','Sneasel','Houndour','Houndoom','Raikou','Entei','Suicune','Larvitar','Pupitar','Tyranitar','Poochyena','Mightyena','Nuzleaf','Shiftry','Sableye','Electrike','Manectric','Carvanha','Sharpedo','Crawdaunt','Absol','Shinx','Luxio','Luxray','Honchkrow','Stunky','Skuntank','Spiritomb','Drapion','Weavile','Drapion','Darkrai','Arceus','Lillipup','Herdier','Stoutland','Purrloin','Liepard','Sandile','Krokorok','Krookodile','Scraggy','Scrafty','Zorua','Zoroark','Druddigon','Pawniard','Bisharp','Vullaby','Mandibuzz','Litleo','Pyroar','Pangoro','Furfrou','Yveltal','Incineroar','Rockruff','Lycanroc','Golisopod','Silvally','Drampa','Tapu Bulu','Solgaleo','Guzzlord','Naganadel','Zeraora']
        if self.name == 'TM98 Waterfall':
            return ['Squirtle','Wartortle','Blastoise','Psyduck','Golduck','Poliwag','Poliwhirl','Poliwrath','Tentacool','Tentacruel','Seel','Dewgong','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Gyarados','Lapras','Vaporeon','Omanyte','Omastar','Kabuto','Kabutops','Dratini','Dragonair','Dragonite','Mew','Totodile','Croconaw','Feraligatr','Chinchou','Lanturn','Marill','Azumarill','Wooper','Quagsire','Qwilfish','Remoraid','Octillery','Mantine','Kingdra','Suicune','Lugia','Mudkip','Marshtomp','Swampert','Lombre','Ludicolo','Azurill','Carvanha','Sharpedo','Wailmer','Wailord','Barboach','Whiscash','Corphish','Crawdaunt','Feebas','Milotic','Spheal','Sealeo','Walrein','Clamperl','Huntail','Gorebyss','Relicanth','Luvdisc','Latias','Latios','Kyogre','Rayquaza','Piplup','Prinplup','Empoleon','Bibarel','Buizel','Floatzel','Gastrodon','Finneon','Lumineon','Mantyke','Phione','Manaphy','Arceus','Oshawott','Dewott','Samurott','Panpour','Simipour','Basculin','Tirtouga','Carracosta','Frillish','Jellicent','Alomomola','Froakie','Frogadier','Greninja','Skrelp','Dragalge','Clauncher','Clawitzer','Popplio','Brionne','Primarina','Wishiwashi','Dewpider','Araquanid','Wimpod','Golisopod','Bruxish','Tapu Fini']
        if self.name == 'Old Candy':
            return 300
        if self.name == 'Common Candy':
            return 1000
        if self.name == 'Rare Candy':
            return 5000
        if self.name == 'Shiny Candy':
            return 10000
        if self.name == 'Mythical Candy':
            return 30000
        if self.type[0] == 'Gem':
            print(self.name[:self.name.find(' ')])
            return self.name[:self.name.find(' ')]
        return None

    def use_spe(self,P):
        box = poke_func.load("p/team_box_1.png")
        back = poke_func.load("p/load_back.png")
        hp_b = poke_func.load("p/team_hp.png")
        item_ico = pygame.transform.scale(poke_func.load("p/item_icon.png"),(20,25))
        mega = pygame.transform.scale(poke_func.load("p/mega_symbol.png"),(30,30))
        nurse = pygame.transform.scale(poke_func.load("p/nurse_icon.png"),(30,30))
        able = P.font.render("ABLE",True,(255,255,255))
        notable = P.font.render("NOT ABLE",True,(255,255,255))
        learned = P.font.render("LEARNED",True,(255,255,255))
        end = True
        current = 0
        a = 0
        while end:
            pos = 0
            x = 0
            y = 0
            P.surface.blit(back,(0,0))
            for p in P.party:
                if pos == current:
                    box = poke_func.load("p/team_box_2.png")
                    if p.code[-2:] == '_S':
                        box = poke_func.load("p/team_box_2_S.png")
                else:
                    box = poke_func.load("p/team_box_1.png")
                    if p.code[-2:] == '_S':
                        box = poke_func.load("p/team_box_1_S.png")
                if pos % 2 == 0:
                    x = 0
                else:
                    x = 400
                y = int(pos/2)*150
                lvl = P.font_s.render("Lv."+str(p.lvl),True,(255,255,255))
                nme = P.font.render(p.name,True,(255,255,255))
                name_size = P.font.size(p.name)[0]
                hp = P.font_s.render(str(p.ch)+"/"+str(p.hp),True,(255,255,255))
                P.surface.blit(box,(x,y))
                if self.type[1] == 'TM':
                    cod = p.code
                    if cod[-2:] == '_S':
                        cod = cod[:-2]
                    if cod[:5] == 'Mega_':
                        cod = cod[5:]
                    if cod[-2:] in ['_X','_Y','_T']:
                        cod = cod[:-2]
                    if cod[-2:] in ['_M','_F'] and cod[:-2] not in ['Nidoran','Meowstic']:
                        cod = cod[:-2]
                    if cod[-5:] in ['_rotF','_rotM','_rotR','_rotW','_rotH']:
                        cod = cod[:-5]
                    if p.has_move(self.type[0]):
                        P.surface.blit(learned,(x+150,y+70))
                    elif (cod in self.mod() and self.mod()[0] != 'Reverse') or (cod not in self.mod() and self.mod()[0] == 'Reverse'):
                        P.surface.blit(able,(x+150,y+70))
                    else:
                        P.surface.blit(notable,(x+150,y+70))
                elif self.type[0] == 'Heart Scale':
                    if self.can_hs(p):
                        P.surface.blit(able,(x+150,y+70))
                    else:
                        P.surface.blit(notable,(x+150,y+70))
                elif self.type[0] == 'Petal':
                    if self.can_petal(p) == 0:
                        P.surface.blit(able,(x+150,y+70))
                    else:
                        P.surface.blit(notable,(x+150,y+70))
                elif self.type[0] == 'Evo':
                    if (p.code_nos() == 'Kirlia' and self.name == 'Dawn Stone' and p.gen == 0) or (p.code_nos() == 'Slowpoke' and self.name == 'King\'s Rock' and poke_func.in_party(P,"Shellder")) or (p.code_nos() == 'Clamperl' and self.name in ['Deep Sea Scale','Deep Sea Tooth']) or (p.code_nos() == 'Eevee' and self.name in ['Water Stone','Fire Stone','Thunder Stone']) or (p.code_nos() == 'Gloom' and self.name in ['Leaf Stone','Sun Stone']) or (p.evo != [] and p.evo[0] == self.name):
                        P.surface.blit(able,(x+150,y+70))
                    else:
                        P.surface.blit(notable,(x+150,y+70))
                elif self.type[0] == 'Balm Mushroom':
                    if poke_func.has_shiny(p):
                        P.surface.blit(able,(x+150,y+70))
                    else:
                        P.surface.blit(notable,(x+150,y+70))
                P.surface.blit(p.icon,(x+30,y+20))
                P.surface.blit(lvl,(x+30,y+90))
                P.surface.blit(nme,(x+110,y+20))
                if p.code[:5] == 'Mega_':
                    P.surface.blit(mega,(x+115+name_size,y+30))
                if p.nurse:
                    P.surface.blit(nurse,(x+115+name_size,y+30))
                if p.item != None:
                    P.surface.blit(item_ico,(x+70,y+70))
                pos += 1
            for event in pygame.event.get(eventtype = KEYDOWN):
                if event.key == pygame.key.key_code(P.controls[5]) and a > 10:
                    end = False
                elif event.key == pygame.key.key_code(P.controls[0]) and current > 1:
                    current -= 2
                elif event.key == pygame.key.key_code(P.controls[1]) and current < 4 and current+2 < len(P.party):
                    current += 2
                elif event.key == pygame.key.key_code(P.controls[3]) and current % 2 == 0 and current+1 < len(P.party):
                    current += 1
                elif event.key == pygame.key.key_code(P.controls[2]) and current % 2 != 0:
                    current -= 1
                elif event.key == pygame.key.key_code(P.controls[4]) and a > 10:
                    if self.type[1] == 'TM':
                        cod = P.party[current].code
                        if cod[-2:] == '_S':
                            cod = cod[:-2]
                        if cod[:5] == 'Mega_':
                            cod = cod[5:]
                        if cod[-2:] in ['_X','_Y']:
                            cod = cod[:-2]
                        if cod[-2:] in ['_M','_F']:
                            cod = cod[:-2]
                        if  P.party[current].has_move(self.type[0]):
                            poke_func.txt(P,P.party[current].name+" already knows",self.type[0]+".")
                        elif (cod in self.mod() and self.mod()[0] != 'Reverse') or (cod not in self.mod() and self.mod()[0] == 'Reverse'):
                            if P.party[current].learn(P,moves.Move(self.type[0]),False):
                                end = False
                        else:
                            poke_func.txt(P,P.party[current].name +" is not compatible","with "+self.type[0]+".")
                            poke_func.txt(P,self.type[0]+" can't be", "learned.")
                        a = 1
                    elif self.type[0] == 'Heart Scale':
                        if self.can_hs(P.party[current]):
                            poke_func.fade_out(P)
                            if poke_func.use_hs(P,P.party[current]):
                                poke_func.add_item(P,'Heart Scale',-1)
                                return
                            else:
                                a = -1
                        else:
                            poke_func.txt(P,"It won't have any effect.")
                            a = 1
                    elif self.type[0] == 'Petal':
                        result = self.can_petal(P.party[current])
                        if result == 0:
                            P.party[current].petals.append(self.petal_to_stat())
                            poke_func.add_item(P,self.name,-1)
                            poke_func.txt(P,P.party[current].name+" took the",self.name+".")
                            P.party[current].update_stats
                            end = False
                        elif result == 1:
                            poke_func.txt(P,P.party[current].name + " can only hold up","to five petals.")
                            a = 1
                        else:
                            poke_func.txt(P,P.party[current].name + " can only hold up","to three of the same petal.")
                            a = 1
                    elif self.type[0] == 'Evo':
                        if P.party[current].evo != [] and P.party[current].evo[0] == self.name:
                            song = P.song
                            poke_func.fade_out(P,P.song)
                            copy = P.party[current].copy()
                            P.party[current] = poke.Poke(copy.evo[1],[copy.lvl,copy.gen,copy.ch,copy.m1,copy.p1,copy.m2,copy.p2,copy.m3,copy.p3,copy.m4,copy.p4,copy.item,copy.status,copy.exp,copy.ball,copy.friend,copy.ability,True])
                            poke_func.evolve(P,copy,P.party[current])
                            poke_func.play_music(P,song)
                            poke_func.add_item(P,self.name,-1)
                            return
                        elif P.party[current].code_nos() == 'Clamperl' and self.name in ['Deep Sea Scale','Deep Sea Tooth']:
                            song = P.song
                            poke_func.fade_out(P,P.song)
                            copy = P.party[current].copy()
                            ev = 'Huntail'
                            if self.name == 'Deep Sea Scale':
                                ev = 'Gorebyss'
                            P.party[current] = poke.Poke(ev,[copy.lvl,copy.gen,copy.ch,copy.m1,copy.p1,copy.m2,copy.p2,copy.m3,copy.p3,copy.m4,copy.p4,copy.item,copy.status,copy.exp,copy.ball,copy.friend,copy.ability,True])
                            poke_func.evolve(P,copy,P.party[current])
                            poke_func.play_music(P,song)
                            poke_func.add_item(P,self.name,-1)
                            return
                        elif P.party[current].code_nos() == 'Slowpoke' and self.name =='King\'s Rock' and poke_func.in_party(P,"Shellder"):
                            song = P.song
                            poke_func.fade_out(P,P.song)
                            copy = P.party[current].copy()
                            for p in range(len(P.party)):
                                if P.party[p].code_nos() == 'Shellder':
                                    P.party.remove(P.party[p])
                                    break
                            P.party[current] = poke.Poke('Slowking',[copy.lvl,copy.gen,copy.ch,copy.m1,copy.p1,copy.m2,copy.p2,copy.m3,copy.p3,copy.m4,copy.p4,copy.item,copy.status,copy.exp,copy.ball,copy.friend,copy.ability,True])
                            poke_func.evolve(P,copy,P.party[current])
                            poke_func.play_music(P,song)
                            poke_func.add_item(P,self.name,-1)
                            return
                        elif P.party[current].code_nos() == 'Eevee' and self.name in ['Water Stone','Fire Stone','Thunder Stone']:
                            song = P.song
                            poke_func.fade_out(P,P.song)
                            copy = P.party[current].copy()
                            ev = 'Vaporeon'
                            copy.evo[2] = 'Water Gun'
                            if self.name == 'Fire Stone':
                                ev = 'Flareon'
                                copy.evo[2] = 'Ember'
                            elif self.name == 'Thunder Stone':
                                ev = 'Jolteon'
                                copy.evo[2] = 'Thunder Shock'
                            P.party[current] = poke.Poke(ev,[copy.lvl,copy.gen,copy.ch,copy.m1,copy.p1,copy.m2,copy.p2,copy.m3,copy.p3,copy.m4,copy.p4,copy.item,copy.status,copy.exp,copy.ball,copy.friend,copy.ability,True])
                            poke_func.evolve(P,copy,P.party[current])
                            poke_func.play_music(P,song)
                            poke_func.add_item(P,self.name,-1)
                            return
                        elif P.party[current].code_nos() == 'Gloom' and self.name in ['Leaf Stone','Sun Stone']:
                            song = P.song
                            poke_func.fade_out(P,P.song)
                            copy = P.party[current].copy()
                            ev = 'Bellossom'
                            if self.name == 'Leaf Stone':
                                ev = 'Vileplume'
                            P.party[current] = poke.Poke(ev,[copy.lvl,copy.gen,copy.ch,copy.m1,copy.p1,copy.m2,copy.p2,copy.m3,copy.p3,copy.m4,copy.p4,copy.item,copy.status,copy.exp,copy.ball,copy.friend,copy.ability,True])
                            poke_func.evolve(P,copy,P.party[current])
                            poke_func.play_music(P,song)
                            poke_func.add_item(P,self.name,-1)
                            return
                        elif P.party[current].code_nos() == 'Kirlia' and self.name == 'Dawn Stone' and P.party[current].gen == 0:
                            song = P.song
                            poke_func.fade_out(P,P.song)
                            copy = P.party[current].copy()
                            copy.evo.append('Slash')
                            P.party[current] = poke.Poke('Gallade',[copy.lvl,copy.gen,copy.ch,copy.m1,copy.p1,copy.m2,copy.p2,copy.m3,copy.p3,copy.m4,copy.p4,copy.item,copy.status,copy.exp,copy.ball,copy.friend,copy.ability,True])
                            poke_func.evolve(P,copy,P.party[current])
                            poke_func.play_music(P,song)
                            poke_func.add_item(P,self.name,-1)
                            return
                        else:
                            poke_func.txt(P,"It won't have any effect.")
                            a = 1
                    elif self.type[0] == 'Balm Mushroom':
                        if poke_func.has_shiny(P.party[current]):
                            P.party[current].code += '_S'
                            P.party[current].icon = pygame.transform.scale(pygame.image.load("p/poke/"+P.party[current].code+"_ico.png"),(70,70))
                            poke_func.txt(P,"Something strange happened","to "+P.party[current].name+"!")
                            poke_func.add_item(P,'Balm Mushroom',-1)
                            end = False
                        else:
                            poke_func.txt(P,"It won't have any effect.")
                            a = 1
            if a == 0:
                poke_func.fade_in(P)
            if a == 2:
                P.surface.set_clip(Rect(0,0,800,600))
                poke_func.new_txt(P)
                poke_func.write(P,"Use on which Pokemon?")
                P.surface.set_clip(Rect(0,0,800,450))
            a += 1
            P.clock.tick(P.ani_spd)
            poke_func.update_screen(P)
        P.surface.set_clip(Rect(0,0,800,600))
        poke_func.fade_out(P)

    def use_item(self,P,battle = False):
        back = poke_func.load("p/load_back.png")
        hp_b = poke_func.load("p/team_hp.png")
        item_ico = pygame.transform.scale(poke_func.load("p/item_icon.png"),(20,25))
        mega = pygame.transform.scale(poke_func.load("p/mega_symbol.png"),(30,30))
        nurse = pygame.transform.scale(poke_func.load("p/nurse_icon.png"),(30,30))
        target = None
        end = True
        current = 0
        a = 0
        while end:
            pos = 0
            x = 0
            y = 0
            P.surface.blit(back,(0,0))
            for p in P.party:
                if pos == current:
                    box = poke_func.load("p/team_box_2.png")
                    if p.code[-2:] == '_S':
                        box = poke_func.load("p/team_box_2_S.png")
                else:
                    box = poke_func.load("p/team_box_1.png")
                    if p.code[-2:] == '_S':
                        box = poke_func.load("p/team_box_1_S.png")
                if pos % 2 == 0:
                    x = 0
                else:
                    x = 400
                y = int(pos/2)*150
                lvl = P.font_s.render("Lv."+str(p.lvl),True,(255,255,255))
                nme = P.font.render(p.name,True,(255,255,255))
                name_size = P.font.size(p.name)[0]
                hp = P.font_s.render(str(p.ch)+"/"+str(p.hp),True,(255,255,255))
                P.surface.blit(box,(x,y))
                if p.ch/p.hp >= 0.5:
                    P.surface.fill((0,255,0), Rect(x+154,y+70,int(200*(p.ch/p.hp)),10))
                elif p.ch/p.hp >= 0.25:
                    P.surface.fill((255,255,0), Rect(x+154,y+70,int(200*(p.ch/p.hp)),10))
                else:
                    P.surface.fill((255,50,0), Rect(x+154,y+70,int(200*(p.ch/p.hp)),10))
                P.surface.blit(p.icon,(x+30,y+20))
                P.surface.blit(lvl,(x+30,y+90))
                P.surface.blit(nme,(x+110,y+20))
                if p.code[:5] == 'Mega_':
                    P.surface.blit(mega,(x+115+name_size,y+30))
                if p.nurse:
                    P.surface.blit(nurse,(x+115+name_size,y+30))
                P.surface.blit(hp,(x+200,y+90))
                P.surface.blit(hp_b,(x+110,y+65))
                if p.status != None:
                    status = poke_func.load("p/"+p.status+"_ico.png")
                    status = pygame.transform.scale(status,(50,20))
                    P.surface.blit(status,(x+145,y+95))
                if p.item != None:
                    P.surface.blit(item_ico,(x+70,y+70))
                pos += 1
            if poke_func.item_in_bag(P,self.name) == 0:
                poke_func.txt(P,"You used your last",self.name+".")
                end = False
                a = 5
            for event in pygame.event.get(eventtype = KEYDOWN):
                if event.key == pygame.key.key_code(P.controls[5]) and a > 10:
                    end = False
                elif event.key == pygame.key.key_code(P.controls[0]) and current > 1:
                    current -= 2
                elif event.key == pygame.key.key_code(P.controls[1]) and current < 4 and current+2 < len(P.party):
                    current += 2
                elif event.key == pygame.key.key_code(P.controls[3]) and current % 2 == 0 and current+1 < len(P.party):
                    current += 1
                elif event.key == pygame.key.key_code(P.controls[2]) and current % 2 != 0:
                    current -= 1
                elif event.key == pygame.key.key_code(P.controls[4]) and a > 10:
                    if self.type[0] == 'Potion' and P.party[current].ch < P.party[current].hp and P.party[current].status != 'Faint':
                        if battle:
                            target = P.party[current]
                            end = False
                        else:
                            heal = self.mod()
                            P.party[current].ch += heal
                            if P.party[current].ch > P.party[current].hp:
                                heal -= P.party[current].ch - P.party[current].hp
                                P.party[current].ch = P.party[current].hp
                            poke_func.txt(P,P.party[current].name+"'s HP was restored","by "+str(heal)+" points!")
                            poke_func.add_item(P,self.name,-1)
                    elif self.type[0] == 'Food' and P.party[current].friend != 400:
                        if self.mod()[1] == 'All' or self.mod()[1] in P.party[current].type:
                            P.party[current].gain_friend(self.mod()[0])
                            poke_func.txt(P,P.party[current].name+" eagerly ate the",self.name + " and grew", "friendlier!")
                            poke_func.add_item(P,self.name,-1)
                        else:
                            P.party[current].gain_friend(self.mod()[0]/2)
                            poke_func.txt(P,P.party[current].name+" ate the",self.name + " and grew", "friendlier!")
                            poke_func.add_item(P,self.name,-1)
                    elif (self.name == 'Sitrus Berry' or self.name == 'Oran Berry') and P.party[current].ch < P.party[current].hp and P.party[current].status != 'Faint':
                        if battle:
                            target = P.party[current]
                            end = False
                        else:
                            if self.name == 'Sitrus Berry':
                                heal = int(P.party[current].hp/4)
                            else:
                                heal = 10
                            P.party[current].ch += heal
                            if P.party[current].ch > P.party[current].hp:
                                heal -= P.party[current].ch - P.party[current].hp
                                P.party[current].ch = P.party[current].hp
                            poke_func.txt(P,P.party[current].name+"'s HP was restored","by "+str(heal)+" points!")
                            poke_func.add_item(P,self.name,-1)
                    elif self.type[0] == 'Battle Berry' and (type(self.mod()) == list and P.party[current].status in self.mod()[0]) or ((self.name == 'Lum Berry' or self.name == 'Persim Berry') and P.party[current].cfs > 0):
                        if battle:
                            target = P.party[current]
                            end = False
                        else:
                            s = self.mod()[0][0]
                            if self.name == 'Lum Berry':
                                if P.party[current].cfs > 0:
                                    P.party[current].cfs = 0
                                    poke_func.txt(P,P.party[current].name + " was cured", "of confusion!")
                                s = P.party[current].status
                            if s == None:
                                pass
                            elif s == 'Slp':
                                poke_func.txt(P,P.party[current].name + " woke up!")
                            elif s == 'Frz':
                                poke_func.txt(P,P.party[current].name + " thawed","out!")
                            elif s == 'Brn':
                                poke_func.txt(P,P.party[current].name + " burn was","healed!")
                            else:
                                sta = self.mod()[1]
                                if self.name == 'Lum Berry':
                                    if s == 'Par':
                                        sta = 'Paralysis'
                                    else:
                                        sta = 'Poisoning'
                                poke_func.txt(P,P.party[current].name + " was cured", "of "+sta+"!")
                            if self.name == 'Persim Berry':
                                P.party[current].cfs = 0
                            else:
                                P.party[current].status = None
                            poke_func.add_item(P,self.name,-1)
                    elif self.type[0] == 'Candy' and poke_func.poke_max(P,P.party[current]) == False:
                        if self.name == 'Expired Candy':
                            poke_func.txt(P,P.party[current].name + "'s level dropped!")
                            perc = P.party[current].exp/P.party[current].get_exp()
                            P.party[current].lvl -= 1
                            P.party[current].exp = perc*P.party[current].get_exp()
                            P.party[current].update_stats()
                            box = poke_func.load("p/team_box_2.png")
                            if P.party[current].code[-2:] == '_S':
                                box = poke_func.load("p/team_box_2_S.png")
                            if current % 2 == 0:
                                x = 0
                            else:
                                x = 400
                            y = int(current/2)*150
                            lvl = P.font_s.render("Lv."+str(P.party[current].lvl),True,(255,255,255))
                            nme = P.font.render(P.party[current].name,True,(255,255,255))
                            name_size = P.font.size(P.party[current].name)[0]
                            hp = P.font_s.render(str(P.party[current].ch)+"/"+str(P.party[current].hp),True,(255,255,255))
                            P.surface.blit(box,(x,y))
                            if P.party[current].ch/P.party[current].hp >= 0.5:
                                P.surface.fill((0,255,0), Rect(x+154,y+70,int(200*(P.party[current].ch/P.party[current].hp)),10))
                            elif P.party[current].ch/P.party[current].hp >= 0.25:
                                P.surface.fill((255,255,0), Rect(x+154,y+70,int(200*(P.party[current].ch/P.party[current].hp)),10))
                            else:
                                P.surface.fill((255,50,0), Rect(x+154,y+70,int(200*(P.party[current].ch/P.party[current].hp)),10))
                            P.surface.blit(P.party[current].icon,(x+30,y+20))
                            P.surface.blit(lvl,(x+30,y+90))
                            P.surface.blit(nme,(x+110,y+20))
                            if P.party[current].code[:5] == 'Mega_':
                                P.surface.blit(mega,(x+115+name_size,y+30))
                            if P.party[current].nurse:
                                P.surface.blit(nurse,(x+115+name_size,y+30))
                            P.surface.blit(hp,(x+200,y+90))
                            P.surface.blit(hp_b,(x+110,y+65))
                            if P.party[current].status != None:
                                status = poke_func.load("p/"+P.party[current].status+"_ico.png")
                                status = pygame.transform.scale(status,(50,20))
                                P.surface.blit(status,(x+145,y+95))
                            if P.party[current].item != None:
                                P.surface.blit(item_ico,(x+70,y+70))
                        else:
                            poke_func.txt(P,P.party[current].name + " gained "+str(self.mod()),"Exp. Points!")
                            ende = True
                            exp = self.mod()
                            while ende:
                                P.party[current].exp += exp
                                if P.party[current].exp >= P.party[current].get_exp():
                                    exp = P.party[current].exp - P.party[current].get_exp()
                                    P.party[current].exp = P.party[current].get_exp()
                                else:
                                    exp = 0
                                    ende = False
                                if poke_func.poke_max(P,P.party[current]):
                                    break
                                if P.party[current].exp == P.party[current].get_exp():
                                    poke_func.txt(P,P.party[current].name + " leveled up!")
                                    P.party[current].lvlup(P,False,True)
                                    box = poke_func.load("p/team_box_2.png")
                                    if P.party[current].code[-2:] == '_S':
                                        box = poke_func.load("p/team_box_2_S.png")
                                    if current % 2 == 0:
                                        x = 0
                                    else:
                                        x = 400
                                    y = int(current/2)*150
                                    lvl = P.font_s.render("Lv."+str(P.party[current].lvl),True,(255,255,255))
                                    nme = P.font.render(P.party[current].name,True,(255,255,255))
                                    name_size = P.font.size(P.party[current].name)[0]
                                    hp = P.font_s.render(str(P.party[current].ch)+"/"+str(P.party[current].hp),True,(255,255,255))
                                    P.surface.blit(box,(x,y))
                                    if P.party[current].ch/P.party[current].hp >= 0.5:
                                        P.surface.fill((0,255,0), Rect(x+154,y+70,int(200*(P.party[current].ch/P.party[current].hp)),10))
                                    elif P.party[current].ch/P.party[current].hp >= 0.25:
                                        P.surface.fill((255,255,0), Rect(x+154,y+70,int(200*(P.party[current].ch/P.party[current].hp)),10))
                                    else:
                                        P.surface.fill((255,50,0), Rect(x+154,y+70,int(200*(P.party[current].ch/P.party[current].hp)),10))
                                    P.surface.blit(P.party[current].icon,(x+30,y+20))
                                    P.surface.blit(lvl,(x+30,y+90))
                                    P.surface.blit(nme,(x+110,y+20))
                                    if P.party[current].code[:5] == 'Mega_':
                                        P.surface.blit(mega,(x+115+name_size,y+30))
                                    if P.party[current].nurse:
                                        P.surface.blit(nurse,(x+115+name_size,y+30))
                                    P.surface.blit(hp,(x+200,y+90))
                                    P.surface.blit(hp_b,(x+110,y+65))
                                    if P.party[current].status != None:
                                        status = poke_func.load("p/"+P.party[current].status+"_ico.png")
                                        status = pygame.transform.scale(status,(50,20))
                                        P.surface.blit(status,(x+145,y+95))
                                    if P.party[current].item != None:
                                        P.surface.blit(item_ico,(x+70,y+70))
                        poke_func.add_item(P,self.name,-1)
                    else:
                        poke_func.txt(P,"It won't have any effect.")
                        if battle:
                            end = False
                    a = 1
            if a == 0:
                poke_func.fade_in(P)
            if a == 2:
                P.surface.set_clip(Rect(0,0,800,600))
                poke_func.new_txt(P)
                poke_func.write(P,"Use on which Pokemon?")
                P.surface.set_clip(Rect(0,0,800,450))
            a += 1
            P.clock.tick(P.ani_spd)
            poke_func.update_screen(P)
        P.surface.set_clip(Rect(0,0,800,600))
        poke_func.fade_out(P)
        if battle:
            return target

    def petal_to_stat(self):
        if self.name == 'Red Petal':
            return 'hp'
        elif self.name == 'Blue Petal':
            return 'ak'
        elif self.name == 'Purple Petal':
            return 'sak'
        elif self.name == 'Brown Petal':
            return 'df'
        elif self.name == 'Green Petal':
            return 'sdf'
        else:
            return 'spd'

    def can_petal(self,poke):
        if len(poke.petals) == 5:
            return 1
        elif poke.petals.count(self.petal_to_stat()) >= 3:
            return 2
        return 0

    def can_hs(self,poke):
        for move in poke.moveset[1]:
            if poke.has_move(move) == False:
                return True
        for lvl in poke.moveset:
            if lvl != 1:
                if poke.has_move(poke.moveset[lvl]) == False:
                    return True
        return False

    def give_item(self,P):
        box = poke_func.load("p/team_box_1.png")
        back = poke_func.load("p/load_back.png")
        hp_b = poke_func.load("p/team_hp.png")
        item_ico = pygame.transform.scale(poke_func.load("p/item_icon.png"),(20,25))
        mega = pygame.transform.scale(poke_func.load("p/mega_symbol.png"),(30,30))
        nurse = pygame.transform.scale(poke_func.load("p/nurse_icon.png"),(30,30))
        end = True
        current = 0
        a = 0
        while end:
            pos = 0
            x = 0
            y = 0
            P.surface.blit(back,(0,0))
            for p in P.party:
                if pos == current:
                    box = poke_func.load("p/team_box_2.png")
                else:
                    box = poke_func.load("p/team_box_1.png")

                if pos % 2 == 0:
                    x = 0
                else:
                    x = 400
                y = int(pos/2)*150
                lvl = P.font_s.render("Lv."+str(p.lvl),True,(255,255,255))
                nme = P.font.render(p.name,True,(255,255,255))
                name_size = P.font.size(p.name)[0]
                hp = P.font_s.render(str(p.ch)+"/"+str(p.hp),True,(255,255,255))
                P.surface.blit(box,(x,y))
                if p.ch/p.hp >= 0.5:
                    P.surface.fill((0,255,0), Rect(x+154,y+70,int(200*(p.ch/p.hp)),10))
                elif p.ch/p.hp >= 0.25:
                    P.surface.fill((255,255,0), Rect(x+154,y+70,int(200*(p.ch/p.hp)),10))
                else:
                    P.surface.fill((255,50,0), Rect(x+154,y+70,int(200*(p.ch/p.hp)),10))
                P.surface.blit(p.icon,(x+30,y+20))
                P.surface.blit(lvl,(x+30,y+90))
                P.surface.blit(nme,(x+110,y+20))
                if p.code[:5] == 'Mega_':
                    P.surface.blit(mega,(x+115+name_size,y+30))
                if p.nurse:
                    P.surface.blit(nurse,(x+115+name_size,y+30))
                P.surface.blit(hp,(x+200,y+90))
                P.surface.blit(hp_b,(x+110,y+65))
                if p.status != None:
                    status = poke_func.load("p/"+p.status+"_ico.png")
                    status = pygame.transform.scale(status,(50,20))
                    P.surface.blit(status,(x+145,y+95))
                if p.item != None:
                    P.surface.blit(item_ico,(x+70,y+70))
                pos += 1
            for event in pygame.event.get(eventtype = KEYDOWN):
                if event.key == pygame.key.key_code(P.controls[5]) and a > 10:
                    end = False
                elif event.key == pygame.key.key_code(P.controls[0]) and current > 1:
                    current -= 2
                elif event.key == pygame.key.key_code(P.controls[1]) and current < 4 and current+2 < len(P.party):
                    current += 2
                elif event.key == pygame.key.key_code(P.controls[3]) and current % 2 == 0 and current+1 < len(P.party):
                    current += 1
                elif event.key == pygame.key.key_code(P.controls[2]) and current % 2 != 0:
                    current -= 1
                elif event.key == pygame.key.key_code(P.controls[4]) and a > 10:
                    if P.party[current].item == None:
                        P.party[current].item = self.name
                        poke_func.add_item(P,self.name,-1)
                        poke_func.txt(P,P.party[current].name + " was given the", self.name + " to hold.")
                        end = False
                    else:
                        aan = "a "
                        if P.party[current].item[0] in ['A','E','I','O','U']:
                            aan = "an "
                        poke_func.txt(P,P.party[current].name + " is already holding",aan +P.party[current].item+".")
                        poke_func.new_txt(P)
                        poke_func.write(P,"Would you like to switch the","two items?")
                        if poke_func.choice(P,550,600):
                            poke_func.txt(P,"The "+P.party[current].item + " was taken and","replaced with the "+self.name+".")
                            end = False
                            poke_func.add_item(P,P.party[current].item,1)
                            P.party[current].item = self.name
                            poke_func.add_item(P,self.name,-1)
                        else:
                            end = False
            if a == 0:
                poke_func.fade_in(P)
            if a == 2:
                P.surface.set_clip(Rect(0,0,800,600))
                poke_func.new_txt(P)
                poke_func.write(P,"Give to which Pokemon?")
                P.surface.set_clip(Rect(0,0,800,450))
            a += 1
            P.clock.tick(P.ani_spd)
            poke_func.update_screen(P)
        P.surface.set_clip(Rect(0,0,800,600))
        poke_func.fade_out(P)

    def battle_menu(self,P,num) -> str:
        options = []
        use = P.font.render("Use",True,(0,0,0))
        cancel = P.font.render("Cancel",True,(0,0,0))
        boxy = 0
        if self.type[0] == 'Ball' or self.type[0] == 'Potion' or self.type[0] == 'Battle Berry':
            tbox = poke_func.load("p/2_box.png")
            options.append(cancel)
            options.append(use)
            boxy = 330
        else:
            tbox = poke_func.load("p/1_box.png")
            options.append(cancel)
            boxy = 380
        back_t = P.surface.copy()
        poke_func.new_txt(P)
        poke_func.write(P,self.name+" is selected.")
        P.surface.blit(tbox,(550,boxy))
        P.clock.tick(5)
        ay = 390-(50*(len(options)-1))
        txty = 390
        for x in options:
            P.surface.blit(x,(597,txty))
            txty -= 50
        temp3 = P.surface.copy()
        P.surface.blit(P.arrow,(550,ay))
        poke_func.update_screen(P)
        ans = len(options)-1
        tim = 0
        end = True
        while end:
            for event in pygame.event.get(eventtype = KEYDOWN):
                if event.key == pygame.key.key_code(P.controls[4]) and tim > 10:
                    if options[ans] == cancel:
                        return ''
                    if options[ans] == use:
                        return self.name
                elif event.key == pygame.key.key_code(P.controls[5]) and tim > 10:
                    end = False
                elif event.key == pygame.key.key_code(P.controls[0]) and ans != (len(options)-1):
                    ans += 1
                    ay -= 50
                    P.surface.blit(temp3,(0,0))
                    P.surface.blit(P.arrow,(550,ay))
                elif event.key == pygame.key.key_code(P.controls[1]) and ans != 0:
                    ans -= 1
                    ay += 50
                    P.surface.blit(temp3,(0,0))
                    P.surface.blit(P.arrow,(550,ay))
            poke_func.update_screen(P)
            P.clock.tick(P.ani_spd)
            tim += 1
        return ''
            
    def menu(self,P,num) -> bool:
        options = []
        use = P.font.render("Use",True,(0,0,0))
        register = P.font.render("Register",True,(0,0,0))
        deselect = P.font.render("Deselect",True,(0,0,0))
        give = P.font.render("Give",True,(0,0,0))
        toss = P.font.render("Toss",True,(0,0,0))
        cancel = P.font.render("Cancel",True,(0,0,0))
        boxy = 0
        if self.type[0] in ['Held','Gem','Ball'] or self.name == 'Persim Berry':
            tbox = poke_func.load("p/3_box.png")
            options.append(cancel)
            options.append(toss)
            options.append(give)
            boxy = 280
        elif self.type[1] == 'TM':
            tbox = poke_func.load("p/2_box.png")
            options.append(cancel)
            options.append(use)
            boxy = 330
        elif self.type[0] in ['Evo','Food','Heart Scale','Balm Mushroom','Candy','Potion','Petal'] or (self.type[0] == 'Battle Berry' and self.name != 'Persim Berry'):
            tbox = poke_func.load("p/4_box.png")
            options.append(cancel)
            options.append(toss)
            options.append(give)
            options.append(use)
            boxy = 230
        elif self.type[0] == 'Use':
            tbox = poke_func.load("p/3_box.png")
            options.append(cancel)
            if self.name in P.save_data.register:
                options.append(deselect)
            else:
                options.append(register)
            options.append(use)
            boxy = 280
        elif self.type[0] in ['Mega Stone','Misc']:
            tbox = poke_func.load("p/1_box.png")
            options.append(cancel)
            boxy = 380
        back_t = P.surface.copy()
        poke_func.new_txt(P)
        poke_func.write(P,self.name+" is selected.")
        P.surface.blit(tbox,(550,boxy))
        P.clock.tick(5)
        ay = 390-(50*(len(options)-1))
        txty = 390
        for x in options:
            P.surface.blit(x,(597,txty))
            txty -= 50
        temp3 = P.surface.copy()
        P.surface.blit(P.arrow,(550,ay))
        poke_func.update_screen(P)
        ans = len(options)-1
        tim = 0
        end = True
        while end:
            for event in pygame.event.get(eventtype = KEYDOWN):
                if event.key == pygame.key.key_code(P.controls[4]) and tim > 10:
                    if options[ans] == cancel:
                        end = False
                    if options[ans] == give:
                        poke_func.fade_out(P)
                        self.give_item(P)
                        return True
                    if options[ans] == register:
                        if None not in P.save_data.register:
                            P.surface.blit(back_t,(0,0))
                            poke_func.txt(P,"You can only register up to","four items.")
                        else:
                            if P.save_data.register[0] == None:
                                P.save_data.register[0] = self.name
                            elif P.save_data.register[1] == None:
                                P.save_data.register[1] = self.name
                            elif P.save_data.register[2] == None:
                                P.save_data.register[2] = self.name
                            else:
                                P.save_data.register[3] = self.name
                        end = False
                    if options[ans] == deselect:
                        P.save_data.register[P.save_data.register.index(self.name)] = None
                        end = False
                    if options[ans] == use:
                        if self.type[1] == 'TM':
                            P.surface.blit(back_t,(0,0))
                            poke_func.txt(P,"Booted up a TM.")
                            poke_func.txt(P,"It contained " + self.type[0]+".")
                            poke_func.new_txt(P)
                            poke_func.write(P,"Teach "+self.type[0]+" to a","Pokemon?")
                            if poke_func.choice(P):
                                poke_func.fade_out(P)
                                self.use_spe(P)
                                return True
                            else:
                                end = False
                        elif self.type[0] == 'Use':
                            P.use_key_item = self.name
                            if self.name == 'Map':
                                P.use_key_item = None
                                poke_func.fade_out(P)
                                poke_func.open_map(P,True)
                                return True
                            elif self.name == 'Memo Pad':
                                P.use_key_item = None
                                poke_func.fade_out(P)
                                poke_func.memo_pad(P)
                                return True
                            end = False
                        elif self.type[0] in ['Heart Scale','Evo','Balm Mushroom','Petal']:
                            poke_func.fade_out(P)
                            self.use_spe(P)
                            return True
                        else:
                            poke_func.fade_out(P)
                            self.use_item(P)
                            return True
                    if options[ans] == toss:
                        P.surface.blit(back_t,(0,0))
                        poke_func.new_txt(P)
                        poke_func.write(P,"Toss out how many ",self.name+"(s)?")
                        bak = P.surface.copy()
                        num_t = poke_func.choose_num(P,num)
                        P.surface.blit(bak,(0,0))
                        if num_t == 0:
                            end = False
                        else:
                            poke_func.new_txt(P)
                            poke_func.write(P,"Is it okay to throw away "+str(num_t),self.name+"(s)?")
                            if(poke_func.choice(P,550,600,ans)):
                                poke_func.new_txt(P)
                                poke_func.write(P,"Threw away " + str(num_t) + " " + self.name + "(s).")
                                poke_func.cont(P)
                                poke_func.add_item(P,self.name,num_t*(-1))
                                end = False
                            else:
                                end = False
                elif event.key == pygame.key.key_code(P.controls[5]) and tim > 10:
                    end = False
                elif event.key == pygame.key.key_code(P.controls[0]) and ans != (len(options)-1):
                    ans += 1
                    ay -= 50
                    P.surface.blit(temp3,(0,0))
                    P.surface.blit(P.arrow,(550,ay))
                elif event.key == pygame.key.key_code(P.controls[1]) and ans != 0:
                    ans -= 1
                    ay += 50
                    P.surface.blit(temp3,(0,0))
                    P.surface.blit(P.arrow,(550,ay))
            poke_func.update_screen(P)
            P.clock.tick(P.ani_spd)
            tim += 1
        return False

