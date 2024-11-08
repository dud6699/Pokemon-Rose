import os
import ast

#get pokemon with no habitats. Run in poke folder
def get_no_habitats():
    pokemon = []
    for file in os.listdir():
        if file.endswith(".txt") and file.startswith("OUTLINE") == False:
            f = open(file,"r")
            data = f.readlines()
            #ignore
            if file[:-4] in ['Whimsicott','Wynaut','Wobbuffet','Vileplume','Vaporeon','Victreebel','Umbreon','Togepi','Togetic','Togekiss','Sylveon','Spiritomb','Slowking','Shiftry','Scizor','Steelix','Pinsir','Pineapple_Oddish','Spooky_Wobbuffet','Pichu','Pikachu','Raichu','Ninetales','Nidoking','Nidoqueen','Mr Mime','Munchlax','Snorlax','Mime Jr','Magby','Magmar','Magmortar','Mantine','Mantyke','Ludicolo','Leafeon','Lucario','Riolu','Smoochum','Jynx','Jolteon','Igglybuff','Jigglypuff','Wigglytuff','Huntail','Tyrogue','Hitmontop','Hitmonlee','Hitmonchan','Gorebyss','Gallade','Glaceon','Gliscor','Flareon','Espeon','Electabuzz','Electivire','Elekid','Cleffa','Clefable','Clefairy','Litwick','Chandelure','Lampent','Chingling','Chimecho','Bounsweet','Steenee','Tsareena','Poliwag','Poliwrath','Poliwhirl','Talonflame','Fletchling','Fletchinder','Bonsly','Sudowoodo','Budew','Roselia','Roserade','Blissey','Chansey','Happiny','Bellossom','Kangaskhan_M','Alolan_Marowak','Arcanine','Azumarill','Azurill','Marill'] or file[:5] == 'Rotom' or file[:5] == 'Mega_':
                pass
            elif len(data) < 10:
                pokemon.append(file[:-4])
            elif len(ast.literal_eval(data[9])) == 0:
                pokemon.append(file[:-4])
            f.close()
    print(pokemon)

if __name__ == "__main__":
    get_no_habitats()
    #trevenant
    #shift_num(114,180,-2)
