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
        if self.name == 'Fresh Water':
            return 30
        if self.name == 'Pinap Berry':
            return [50,'All']
        if self.name == 'Poffin':
            return [20,'All']
        if self.name == 'Cinnamon Roll':
            return [50,'Ground']
        if self.name == 'Coffee':
            return [50,'Dark']
        if self.name == 'Jello':
            return [50,'Psychic']
        if self.name == 'Lava Cake':
            return [50,'Fire']
        if self.name == 'Cupcake':
            return [50,'Fairy']
        if self.name == 'Sundae':
            return [50,'Ice']
        if self.name == 'TM18 Rain Dance':
            return []
        if self.name == 'TM69 Rock Polish':
            return ['Geodude','Graveler','Golem','Alolan_Geodude','Alolan_Graveler','Alolan_Golem','Alolan_Grimer','Alolan_Muk','Onix','Rhyhorn','Rhydon','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Mew','Sudowoodo','Forretress','Gligar','Steelix','Shuckle','Magcargo','Corsola','Donphan','Larvitar','Pupitar','Tyranitar','Nosepass','Aron','Lairon','Aggron','Camerupt','Lunatone','Solrock','Baltoy','Claydol','Lileep','Cradily','Anorith','Armaldo','Relicanth','Metang','Metagross','Regirock','Regice','Registeel','Groudon','Torterra','Cranidos','Rampardos','Shieldon','Bastiodon','Bronzor','Bronzong','Bonsly','Rhyperior','Gliscor','Probopass','Regigigas','Roggenrola','Boldore','Gigalith','Dwebble','Crustle','Tirtouga','Carracosta','Archen','Archeops','Garbodor','Ferroseed','Ferrothorn','Klink','Klang','Klinklang','Golett','Golurk','Pawniard','Bisharp','Durant','Cobalion','Terrakion','Landorus','Genesect','Binacle','Barbaracle','Tyrunt','Tyrantrum','Amaura','Aurorus','Carbink','Bergmite','Avalugg','Diancie','Rockruff','Lycanroc','Sandygast','Palossand','Minior','Kommo-o','Necrozma','Stakataka']
        if self.name == 'TM27 Return':
            return ['Reverse','Caterpie','Metapod','Weedle','Kakuna','Magikarp','Ditto','Unown','Wobbuffet','Smeargle','Wurmple','Silcoon','Cascoon','Wynaut','Beldum','Kricketot','Combee','Tynamo','Scatterbug','Spewpa','Pyukumuku','Cosmog','Cosmoem']
        if self.name == 'TM83 Infestation':
            return ['Pineapple_Oddish','Butterfree','Beedrill','Ekans','Arbok','Oddish','Gloom','Vileplume','Venonat','Venomoth','Bellsprout','Weepinbell','Victreebel','Tentacool','Tentacruel','Grimer','Alolan_Grimer','Muk','Alolan_Muk','Gastly','Haunter','Gengar','Exeggcute','Exeggutor','Alolan_Exeggutor','Koffing','Weezing','Tangela','Mr. Mime','Mew','Ledyba','Ledian','Spinarak','Ariados','Bellossom','Hoppip','Skiploom','Jumpluff','Wooper','Quagsire','Shuckle','Slugma','Magcargo','Beautifly','Dustox','Surskit','Masquerain','Volbeat','Illumise','Gulpin','Swalot','Seviper','Lileep','Cradily','Banette','Duskull','Dusclops','Huntail','Gorebyss','Kricketune','Mothim','Vespiqueen','Shellos','Gastrodon','Mime Jr.','Spiritomb','Skorupi','Drapion','Carnivine','Tangrowth','Dusknoir','Tympole','Palpitoad','Seismitoad','Venipede','Whirlipede','Scolipede','Yamask','Cofagrigus','Trubbish','Garbodor','Solosis','Duosion','Reuniclus','Karrablast','Escavalier','Joltik','Galvantula','Shelmet','Accelgor','Stunfisk','Genesect','Vivillon','Pangoro','Binacle','Barbaracle','Goomy','Sliggoo','Goodra','Cutiefly','Ribombee','Mareanie','Toxapex','Dewpider','Araquanid','Sandygast','Palossand','Mimikyu','Stakataka']
        if self.name == 'TM78 Bulldoze':
            return ['Venasaur','Charizard','Blastoise','Ekans','Arbok','Sandshrew','Alolan_Sandshrew','Sandslash','Alolan_Sandslash','Nidoqueen','Nidoking','Diglett','Alolan_Diglett','Dugtrio','Alolan_Dugtrio','Mankey','Primeape','Arcanine','Poliwag','Poliwhirl','Poliwrath','Machop','Machoke','Machamp','Geodude','Graveler','Golem','Alolan_Geodude','Alolan_Graveler','Alolan_Golem','Slowpoke','Slowbro','Onix','Exeggutor','Alolan_Exeggutor','Cubone','Marowak','Alolan_Marowak','Hitmonlee','Hitmonchan','Lickitung','Rhyhorn','Rhydon','Chansey','Kangaskhan','Pinsir','Tauros','Gyarados','Lapras','Aerodactyl','Snorlax','Dragonite','Mewtwo','Mew','Meganium','Typhlosion','Feraligatr','Ampharos','Azumarill','Sudowoodo','Politoed','Wooper','Quagsire','Slowking','Girafarig','Pineco','Forretress','Dunsparce','Gligar','Steelix','Snubbull','Granbull','Shuckle','Heracross','Teddiursa','Ursaring','Magcargo','Swinub','Piloswine','Corsola','Mantine','Phanpy','Donphan','Stantler','Tyrogue','Hitmontop','Miltank','Blissey','Raikou','Entei','Suicune','Larvitar','Pupitar','Tyranitar','Lugia','Ho-Oh','Sceptile','Blaziken','Marshtomp','Swampert','Vigoroth','Slaking','Loudred','Exploud','Makuhita','Hariyama','Nosepass','Aron','Lairon','Aggron','Swalot','Sharpedo','Wailmer','Wailord','Numel','Camerupt','Torkoal','Grumpig','Trapinch','Vibrava','Flygon','Altaria','Seviper','Lunatone','Solrock','Barboach','Whiscash','Baltoy','Claydol','Cradily','Armaldo','Milotic','Dusclops','Tropius','Glalie','Spheal','Sealeo','Walrein','Relicanth','Salamence','Metang','Metagross','Regirock','Regice','Registeel','Latias','Latios','Kyogre','Groudon','Rayquaza','Torterra','Infernape','Empoleon','Bibarel','Cranidos','Rampardos','Shieldon','Bastiodon','Gastrodon','Purugly','Bronzor','Bronzong','Gible','Gabite','Garchomp','Munchlax','Riolu','Lucario','Hippopotas','Hippowdon','Drapion','Croagunk','Toxicroak','Mantyke','Abomasnow','Lickilicky','Rhyperior','Tangrowth','Electivire','Magmortar','Gliscor','Mamoswine','Gallade','Probopass','Dusknoir','Dialga','Palkia','Heatran','Regigigas','Giratina','Arceus','Pignite','Emboar','Roggenrola','Boldore','Gigalith','Drilbur','Excadrill','Conkeldurr','Palpitoad','Seismitoad','Throh','Sawk','Scolipede','Sandile','Krokorok','Krookodile','Darmanitan','Dwebble','Crustle','Tirtouga','Carracosta','Archen','Archeops','Ferrothorn','Haxorus','Beartic','Stunfisk','Druddigon','Golett','Golurk','Bouffalant','Hydreigon','Terrakion','Landorus','Chespin','Quilladin','Chesnaught','Bunnelby','Diggersby','Litleo','Pyroar','Skiddo','Gogoat','Pancham','Pangoro','Binacle','Barbaracle','Helioptile','Tyrunt','Tyrantrum','Amaura','Aurorus','Goodra','Phantump','Trevenant','Avalugg','Zygarde','Volcanion','Incineroar','Gumshoos','Crabrawler','Crabominable','Wishiwashi','Mudbray','Mudsdale','Stufful','Bewear','Oranguru','Passimian','Sandygast','Palossand','Minior','Komala','Turtonator','Drampa','Dhelmise','Jangmo-o','Hakamo-o','Kommo-o','Solgaleo','Buzzwole','Celesteela','Guzzlord','Necrozma','Stakataka']
        if self.name == 'TM07 Hail':
            return ['Squirtle','Wartortle','Blastoise','Alolan_Sandshrew','Alolan_Sandslash','Alolan_Vulpix','Alolan_Ninetales','Psyduck','Golduck','Poliwag','Poliwhirl','Poliwrath','Tentacool','Tentacruel','Slowpoke','Slowbro','Seel','Dewgong','Shellder','Cloyster','Krabby','Kingler','Chansey','Kangaskhan','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Jynx','Gyrados','Lapras','Vaporeon','Omanyte','Omastar','Kabuto','Kabutops','Articuno','Dratini','Dragonair','Dragonite','Mewtwo','Mew','Totodile','Croconaw','Feraligatr','Chinchou','Lanturn','Marill','Azumarill','Wooper','Quagsire','Slowking','Qwilfish','Sneasel','Swinub','Piloswine','Corsola','Delibird','Mantine','Kingdra','Smoochum','Blissey','Suicune','Lugia','Mudkip','Marshtomp','Swampert','Lotad','Lombre','Ludicolo','Wingull','Pelipper','Azurill','Carvanha','Sharpedo','Wailmer','Wailord','Barboach','Whiscash','Corphish','Crawdaunt','Feebas','Milotic','Castform','Absol','Snorunt','Glalie','Spheal','Sealeo','Walrein','Clamperl','Huntail','Gorebyss','Relicanth','Luvdisc','Regice','Kyogre','Piplup','Prinplup','Empoleon','Buizel','Floatzel','Shellos','Gastrodon','Happiny','Finneon','Lumineon','Mantyke','Snover','Abomasnow','Weavile','Glaceon','Mamoswine','Froslass','Palkia','Phione','Manaphy','Arceus','Oshawott','Dewott','Samurott','Panpour','Simipour','Tympole','Palpitoad','Seismitoad','Basculin','Ducklett','Swanna','Vanillite','Vanillish','Vanilluxe','Frillish','Jellicent','Alomomola','Cubchoo','Beartic','Cryogonal','Kyurem','Keldeo','Skrelp','Dragalge','Amaura','Aurorus','Carbink','Goodra','Bergmite','Avalugg','Xerneas','Diancie','Popplio','Brionne','Primarina','Crabominable','Wishiwashi','Mareanie','Toxapex','Wimpod','Golisopod','Pyukumuku','Type: Null','Silvally']
        if self.name == 'TM37 Sandstorm':
            return ['Sandshrew','Sandslash','Nidoqueen','Nidoking','Diglett','Alolan_Diglett','Dugtrio','Alolan_Dugtrio','Geodude','Alolan_Geodude','Graveler','Alolan_Graveler','Golem','Alolan_Golem','Onix','Cubone','Marowak','Alolan_Marowak','Lickitung','Rhyhorn','Rhydon','Chansey','Kangaskhan','Tauros','Gyrados','Omanyte','Omastar','Kabuto','Kabutops','Aerodactyl','Snorlax','Articuno','Zapdos','Moltres','Dragonite','Mew','Mewtwo','Sudowoodo','Wooper','Quagsire','Pineco','Forretress','Gligar','Steelix','Scizor','Shuckle','Magcargo','Swinub','Piloswine','Corsola','Skarmory','Phanpy','Donphan','Hitmontop','Miltank','Blissey','Raikou','Entei','Suicune','Larvitar','Pupitar','Tyranitar','Lugia','Ho-Oh','Celebi','Ninjask','Ninjask','Shedinja','Nosepass','Mawile','Aron','Lairon','Aggron','Numel','Camerupt','Trapinch','Vibrava','Flygon','Cacnea','Cacturne','Lunatone','Solrock','Barboach','Whiscash','Baltoy','Claydol','Lileep','Cradily','Anorith','Armaldo','Castform','Absol','Relicanth','Metang','Metagross','Regirock','Registeel','Latias','Latios','Groudon','Rayquaza','Jirachi','Torterra','Cranidos','Rampardos','Shieldon','Bastiodon','Gastrodon','Bronzor','Bronzong','Bonsly','Gible','Gabite','Garchomp','Munchlax','Hippopotas','Hippopowdon','Lickilicky','Rhyperior','Gliscor','Mamoswine','Probopass','Uxie','Mesprit','Azelf','Dialga','Palkia','Arceus','Roggenrola','Boldore','Gigalith','Drilbur','Excadrill','Sandile','Krokorok','Krookodile','Dwebble','Crustle','Tirtouga','Carracosta','Archen','Archeops','Ferrothorn','Klink','Klang','Klinklang','Accelgor','Stunfisk','Pawniard','Bisharp','Durant','Cobalion','Terrakion','Landorus','Bunnelby','Diggersby','Binacle','Barbaracle','Helioptile','Heliolisk','Tyrunt','Tyrantrum','Amaura','Aurorus','Carbink','Zygarde','Diancie','Volcanion','Yungoos','Gumshoos','Mudbray','Mudsdale','Sandygast','Palossand','Type: Null','Silvally','Minior','Jangmo-o','Hakamo-o','Kommo-o','Nihilego','Stakataka']
        if self.name == 'TM74 Gyro Ball':
            return ['Squirtle','Wartortle','Blastoise','Pineapple_Oddish','Sandshrew','Sandslash','Alolan_Sandshrew','Alolan_Sandslash','Jigglypuff','Wigglytuff','Geodude','Graveler','Golem','Alolan_Geodude','Alolan_Graveler','Alolan_Golem','Magnemite','Magneton','Onix','Voltorb','Electrode','Koffing','Weezing','Staryu','Starmie','Omanyte','Omastar','Mew','Typhlosion','Pineco','Forretress','Dunsparce','Steelix','Qwilfish','Shuckle','Magcargo','Donphan','Hitmontop','Miltank','Torkoal','Lunatone','Solrock','Baltoy','Claydol','Glalie','Metagross','Metang','Rayquaza','Drifloon','Drifblim','Bronzor','Bronzong','Magnezone','Lickilicky','Tepig','Pignite','Emboar','Munna','Musharna','Woobat','Swoobat','Venipede','Whirlipede','Scolipede','Darumaka','Darmanitan','Solosis','Duosion','Reuniclus','Ferroseed','Ferrothorn','Golett','Golurk','Chespin','Quilladin','Chesnaught','Honedge','Doublade','Aegislash','Spritzee','Aromatisse','Carbink','Pumpkaboo','Gourgeist','Bergmite','Avalugg','Diancie','Volcanion','Passimian','Minior','Togedemaru','Dhelmise','Solgaleo','Buzzwole','Celesteela','Guzzlord','Necrozma','Magearna','Stakataka']
        if self.name == 'TM01 Work Up':
            return ['Bulbasaur','Ivysaur','Venasaur','Charmander','Charmeleon','Charizard','Squirtle','Wartortle','Blastoise','Pidgey','Pidgeotto','Pidgeot','Rattata','Raticate','Spearow','Fearow','Alolan_Sandshrew','Alolan_Sandslash','Clefairy','Clefable','Jigglypuff','Wigglytuff','Alolan_Diglett','Alolan_Dugtrio','Meowth','Alolan_Meowth','Persian','Alolan_Persian','Mankey','Primeape','Poliwrath','Machop','Machoke','Machamp',"Farfetch'd",'Doduo','Dodrio','Hitmonlee','Hitmonchan','Lickitung','Chansey','Kanghaskhan','Tauros','Eevee','Vaporean','Jolteon','Flareon','Snorlax','Mew','Chikorita','Bayleef','Meganium','Cyndaquil','Quilava','Typhlosion','Totodile','Croconaw','Feraligatr','Sentret','Furret','Hoothoot','Noctowl','Cleffa','Igglybuff','Togepi','Togetic','Marill','Azumarill','Aipom','Espeon','Umbreon','Girafarig','Snubbull','Granbull','Heracross','Teddiursa','Ursaring','Stantler','Tyrogue','Hitmontop','Miltank','Blissey','Treecko','Grovyle','Sceptile','Torchic','Combusken','Blaziken','Mudkip','Marshtomp','Swampert','Zigzagoon','Linoone','Taillow','Swellow','Breloom','Slakoth','Vigoroth','Slaking','Whismur','Loudred','Exploud','Makuhita','Hariyama','Azurill','Skitty','Delcatty','Meditite','Medicham','Zangoose','Spinda','Castform','Kecleon','Turtwig','Grotle','Torterra','Chimchar','Monferno','Infernape','Piplup','Prinplup','Empoleon','Starly','Staravia','Staraptor','Bidoof','Bibarel','Ambipom','Buneary','Lopunny','Glameow','Purugly','Happiny','Chatot','Munchlax','Riolu','Lucario','Croagunk','Toxicroak','Lickilicky','Togekiss','Leafeon','Glaceon','Gallade','Arceus','Victini','Snivy','Servine','Serperior','Tepig','Pignite','Emboar','Oshawott','Dewott','Samurott','Patrat','Watchog','Lillipup','Herdier','Stoutland','Pansage','Simisage','Panpour','Simipour','Pansear','Simisear','Pidove','Tranquill','Unfezant','Audino','Timburr','Gurdurr','Conkeldurr','Throh','Sawk','Darumaka','Darmanitan','Scraggy','Scrafty','Minccino','Cinccino','Deerling','Sawsbuck','Mienfoo','Mienshao','Bouffalant','Rufflet','Braviary','Deino','Zweilous','Hydreigon','Cobalion','Terrakion','Virizion','Keldeo','Meloetta','Chespin','Quilladin','Chesnaught','Fenniken','Braixen','Delphox','Froakie','Frogadier','Greninja','Bunnelby','Diggersby','Fletchling','Fletchinder','Talonflame','Litleo','Pyroar','Skiddo','Gogoat','Pancham','Pangoro','Furfrou','Espurr','Meowstic_M','Meowstic_F','Sylveon','Hawlucha','Rowlet','Dartrix','Decidueye','Torracat','Litten','Incineroar','Popplio','Brionne','Primarina','Pikipek','Trumbeak','Toucannon','Yungoos','Gumshoos','Crabrawler','Crabominable','Oricorio','Stufful','Bewear','Passimian','Oranguru','Type: Null','Silvally','Komala','Turtonator','Togedemaru','Mimikyu','Drampa','Jangmo-o','Kommo-o','Hakamo-o','Tapu Koko','Tapu Bulu','Solgaleo','Lunala','Buzzwole','Marshadow','Zeraora']
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
                    if cod[-2:] in ['_X','_Y']:
                        cod = cod[:-2]
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
                elif self.type[0] == 'Evo':
                    if (p.code_nos() == 'Clamperl' and self.name in ['Deep Sea Scale','Deep Sea Tooth']) or (p.evo != [] and p.evo[0] == self.name):
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
        elif self.type[0] == 'Evo' or self.type[0] == 'Food' or self.type[0] == 'Heart Scale' or self.type[0] == 'Balm Mushroom' or self.type[0] == 'Candy' or self.type[0] == 'Potion' or (self.type[0] == 'Battle Berry' and self.name != 'Persim Berry'):
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
        elif self.type[0] == 'Mega Stone':
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
                            end = False
                        elif self.type[0] in ['Heart Scale','Evo','Balm Mushroom']:
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

