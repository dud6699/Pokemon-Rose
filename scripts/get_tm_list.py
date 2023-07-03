import os

def get_tm_list(text):
    names = []
    pick_next = False
    add_next = False
    with open(text,'r') as file:
        for line in file:
            for word in line.split():
                if word == "Alolan":
                    names[-1] = "Alolan_"+names[-1]
                elif word == "Galarian":
                    del names[-1]
                elif word == "Male" and names[-1] == 'Meowstic':
                    names[-1] = "Meowstic_M"
                elif word == "Female" and names[-1] == 'Meowstic':
                    names[-1] = "Meowstic_F"
                elif word.isdigit() and len(word) == 3 and int(word) < 808:
                    if int(word) == 29:
                        names.append("Nidoran_F")
                    elif int(word) == 32:
                        names.append("Nidoran_M")
                    elif int(word) == 669:
                        names.append("Flabebe")
                    elif int(word) in [186,413,414,412,741]:
                        pass
                    else:
                        pick_next = True
                elif add_next:
                    names[-1] = names[-1] + " " + word
                    add_next = False
                elif pick_next:
                    if word == 'Mr.':
                        names.append("Mr. Mime")
                    elif word == 'Mime':
                        names.append("Mime Jr.")
                    elif word == 'Type:':
                        names.append("Type: Null")
                    else:
                        names.append(word)
                    if word == 'Tapu':
                        add_next = True
                    pick_next = False
    return names


def check_same(old,new):
    success = True
    for i in old:
        if i not in new:
            print("old: "+i)
            success = False
    for j in new:
        if j not in old:
            print("new: "+j)
            success = False
    print(success)
            
    
if __name__ == "__main__":
    tm_list = get_tm_list("tm_list_text.txt")
    #old = ['Squirtle','Wartortle','Blastoise','Psyduck','Golduck','Poliwag','Poliwhirl','Poliwrath','Tentacool','Tentacruel','Seel','Dewgong','Horsea','Seadra','Goldeen','Seaking','Staryu','Starmie','Gyarados','Lapras','Vaporeon','Omanyte','Omastar','Kabuto','Kabutops','Dratini','Dragonair','Dragonite','Mew','Totodile','Croconaw','Feraligatr','Chinchou','Lanturn','Marill','Azumarill','Wooper','Quagsire','Qwilfish','Remoraid','Octillery','Mantine','Kingdra','Suicune','Lugia','Mudkip','Marshtomp','Swampert','Lombre','Ludicolo','Azurill','Carvahna','Sharpedo','Wailmer','Wailord','Barboach','Whiscash','Corphish','Crawdaunt','Feebas','Milotic','Spheal','Sealeo','Walrein','Clamperl','Huntail','Gorebyss','Relicanth','Luvdisc','Latias','Latios','Kyogre','Rayquaza','Piplup','Prinplup','Empoleon','Bibarel','Buizel','Floatzel','Gastrodon','Finneon','Lumineon','Mantyke','Phione','Manaphy','Arceus','Oshawott','Dewott','Samurott','Panpour','Simipour','Basculin','Tirtouga','Carracosta','Frillish','Jellicent','Alomomola','Froakie','Frogadier','Greninja','Skrelp','Dragalge','Clauncher','Clawitzer','Popplio','Brionne','Primarina','Wishiwashi','Dewpider','Araquanid','Wimpod','Golisopod','Bruxish','Tapu Fini']
    #check_same(old,tm_list)
    print(tm_list)
