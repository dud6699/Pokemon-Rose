import pokemon
import poke
import math
import ast
import os
import sys
import pygame
import save
import random
import moves
import datetime
import items

from pygame.locals import*

class cut_tree:
    def __init__(self,P,x,y,num):
        self.P = P
        self.x = x
        self.y = y
        self.num = num
        self.is_cut = False
        u = P.prog[10][num][0]
        d = P.prog[10][num][1]
        l = P.prog[10][num][2]
        r = P.prog[10][num][3]
        if u == -1:
            self.is_cut = True
        else:
            if u == 1:
                self.ucut = True
            else:
                self.ucut = False
            if d == 1:
                self.dcut = True
            else:
                self.dcut = False
            if l == 1:
                self.lcut = True
            else:
                self.lcut = False
            if r == 1:
                self.rcut = True
            else:
                self.rcut = False
            self.img = load("p/cut_tree.png")
            self.dimg = load("p/front_cut.png")
            self.limg = load("p/left_cut.png")
            self.rimg = load("p/right_cut.png")

    def blit(self,x = None,y = None):
        if self.is_cut == False:
            if x == None:
                x = self.P.px
            if y == None:
                y = self.P.py
            self.P.surface.blit(self.img,(x+self.x-50,y+self.y-100))
            if self.dcut:
                self.P.surface.blit(self.dimg,(x+self.x-50,y+self.y-100))
            if self.lcut:
                self.P.surface.blit(self.limg,(x+self.x-50,y+self.y-100))
            if self.rcut:
                self.P.surface.blit(self.rimg,(x+self.x-50,y+self.y-100))

    def get_rect(self):
        if self.is_cut:
            return (0,0,0,0)
        return (self.P.px+self.x,self.P.py+self.y,50,40)

    def cut(self,from_bag = False):
        if self.is_cut == False:
            te = self.P.surface.copy()
            if from_bag == False:
                txt(self.P,"This tree looks like it can be", "cut down.")
            if item_in_bag(self.P,"Felling Axe") == 0:
                pass
            else:
                ans = False
                if from_bag == False:
                    new_txt(self.P)
                    write(self.P,"Use the Felling Axe?")
                    ans = choice(self.P)
                else:
                    ans = True
                if ans:
                    if self.num == 16:
                        txt(self.P,"Your swing goes right through","the tree.")
                        if get_time() > 19 or get_time() < 6:
                            txt(self.P,"The tree swung back in","retaliation!")
                            self.P.song = "music/wild_battle.wav"
                            pygame.mixer.music.load(self.P.song)
                            set_mixer_volume(self.P,self.P.vol)
                            pygame.mixer.music.play(0)
                            battle(self.P,[poke.Poke('Phantump',[20,random.randint(0,1),334,'Feint Attack',-1,'Confuse Ray',-1,'Ingrain',-1,'Growth',-1,None,None,0,"Poke Ball"])])
                            self.is_cut = True
                            self.P.prog[10][self.num][0] = -1
                            play_music(self.P,"music/route_2.wav")
                            self.P.surface.blit(te,(0,0))
                            fade_in(self.P)
                    elif 375-self.P.px-self.x > 0:
                        if self.lcut:
                            txt(self.P,"You chopped the tree down.")
                            self.is_cut = True
                            self.P.prog[10][self.num][0] = -1
                        elif self.rcut:
                            txt(self.P,"There's already a notch in","this side of the tree.")
                        else:
                            txt(self.P,"You made a notch in the tree.")
                            self.P.prog[10][self.num][3] = 1
                            self.rcut = True
                    elif 375-self.P.px-self.x < 0:
                        if self.rcut:
                            txt(self.P,"You chopped the tree down.")
                            self.is_cut = True
                            self.P.prog[10][self.num][0] = -1
                        elif self.lcut:
                            txt(self.P,"There's already a notch in","this side of the tree.")
                        else:
                            txt(self.P,"You made a notch in the tree.")
                            self.P.prog[10][self.num][2] = 1
                            self.lcut = True
                    elif 275-self.P.py-self.y > 0:
                        if self.ucut:
                            txt(self.P,"You chopped the tree down.")
                            self.is_cut = True
                            self.P.prog[10][self.num][0] = -1
                        elif self.dcut:
                            txt(self.P,"There's already a notch in","this side of the tree.")
                        else:
                            txt(self.P,"You made a notch in the tree.")
                            self.P.prog[10][self.num][1] = 1
                            self.dcut = True
                    else:
                        if self.dcut:
                            txt(self.P,"You chopped the tree down.")
                            self.is_cut = True
                            self.P.prog[10][self.num][0] = -1
                        elif self.ucut:
                            txt(self.P,"There's already a notch in","this side of the tree.")
                        else:
                            txt(self.P,"You made a notch in the tree.")
                            self.P.prog[10][self.num][0] = 1
                            self.ucut = True

    def y_dist(self):
        return 275-self.P.py-self.y

def blit_small_door(P,y):
    P.surface.blit(P.small_door,(377,252-(y-P.py)))

def blit_rain(P,rain):
    x = 0
    y = 0
    if rain < 20 and rain >= 0:
        x -= 200
        y -= 600
    if rain < 20:
        x += 200
        y += 600
    rain = rain%20
    y += rain*30
    x += rain*10
    P.surface.blit(P.rain_img,(0+x,0+y))
    P.surface.blit(P.rain_img,(-800+x,0+y))
    P.surface.blit(P.rain_img,(-200+x,-600+y))
    P.surface.blit(P.rain_img,(-1000+x,-600+y))

def print_mega_area(P):
    if P.prog[0] < 87:
        if P.loc in ['scarab_l','scarab_r']:
            txt(P,"It would probably be best to","leave them alone for now.")
        else:
            txt(P,"It would probably be best to","leave it alone for now.")
    else:
        if P.prog[8][0][0] < 3:
            txt(P,"If your research skill was","higher you might be able to","do something here.")
        else:
            txt(P,"Colress might know something","that could help you here.")
            txt(P,"You can probably find him at","his lab in Egida City.")

def train_det_r(P,x,y,dist):
    if x+P.px < 375 and x+P.px > 325-(dist*50) and y+P.py == 265 and (P.px-25)%50 == 0:
        return True
    return False

def train_det_l(P,x,y,dist):
    if x+P.px > 375 and x+P.px < 425+(dist*50) and y+P.py == 265 and (P.px-25)%50 == 0:
        return True
    return False

def train_det_u(P,x,y,dist):
    if x+P.px == 375 and y+P.py < 315-(dist*50) and y+P.py > 265 and (P.py-15)%50 == 0:
        return True
    return False

def train_det_d(P,x,y,dist):
    if x+P.px == 375 and x+P.px > 215-(dist*50) and y+P.py < 265 and (P.py-15)%50 == 0:
        return True
    return False

def print_box(P,l,off):
    for x in range(5):
        for y in range(6):
            if l[x][y] != 0:
                P.surface.blit(l[x][y].icon,(20+70*y+off,160+70*x))

def type_eff(type1, type2) -> float:
    if type1 == 'Normal':
        if type2 == 'Ghost':
            return 0
        if type2 in ['Steel','Rock']:
            return 0.5
    elif type1 == 'Fighting':
        if type2 == 'Ghost':
            return 0
        if type2 in ['Steel','Rock','Normal','Ice','Dark']:
            return 2
        if type2 in ['Bug','Fairy','Flying','Poison','Psychic']:
            return 0.5
    elif type1 == 'Flying':
        if type2 in ['Bug','Fighting','Grass']:
            return 2
        if type2 in ['Electric','Rock','Steel']:
            return 0.5
    elif type1 == 'Poison':
        if type2 == 'Steel':
            return 0
        if type2 in ['Fairy','Grass']:
            return 2
        if type2 in ['Poison','Ground','Rock','Ghost']:
            return 0.5
    elif type1 == 'Ground':
        if type2 == 'Flying':
            return 0
        if type2 in ['Electric','Fire','Poison','Rock','Steel']:
            return 2
        if type2 in ['Bug','Grass']:
            return 0.5
    elif type1 == 'Rock':
        if type2 in ['Bug','Fire','Flying','Ice']:
            return 2
        if type2 in ['Fighting','Ground','Steel']:
            return 0.5
    elif type1 == 'Bug':
        if type2 in ['Dark','Grass','Psychic']:
            return 2
        if type2 in ['Fairy','Fighting','Fire','Flying','Ghost','Poison','Steel']:
            return 0.5
    elif type1 == 'Ghost':
        if type2 == 'Normal':
            return 0
        if type2 in ['Ghost','Psychic']:
            return 2
        if type2 == 'Dark':
            return 0.5
    elif type1 == 'Steel':
        if type2 in ['Fairy','Ice','Rock']:
            return 2
        if type2 in ['Electric','Fire','Steel','Water']:
            return 0.5
    elif type1 == 'Fire':
        if type2 in ['Bug','Grass','Ice','Steel']:
            return 2
        if type2 in ['Dragon','Fire','Rock','Water']:
            return 0.5
    elif type1 == 'Water':
        if type2 in ['Fire','Ground','Rock']:
            return 2
        if type2 in ['Dragon','Grass','Water']:
            return 0.5
    elif type1 == 'Grass':
        if type2 in ['Ground','Rock','Water']:
            return 2
        if type2 in ['Bug','Dragon','Fire','Flying','Grass','Poison','Steel']:
            return 0.5
    elif type1 == 'Electric':
        if type2 == 'Ground':
            return 0
        if type2 in ['Flying','Water']:
            return 2
        if type2 in ['Dragon','Electric','Grass']:
            return 0.5
    elif type1 == 'Psychic':
        if type2 == 'Dark':
            return 0
        if type2 in ['Fighting','Poison']:
            return 2
        if type2 in ['Psychic','Steel']:
            return 0.5
    elif type1 == 'Ice':
        if type2 in ['Dragon','Flying','Grass','Ground']:
            return 2
        if type2 in ['Ice','Water']:
            return 0.5
    elif type1 == 'Dragon':
        if type2 == 'Fairy':
            return 0
        if type2 == 'Dragon':
            return 2
        if type2 == 'Steel':
            return 0.5
    elif type1 == 'Dark':
        if type2 in ['Ghost','Psychic']:
            return 2
        if type2 in ['Dark','Fairy','Fighting']:
            return 0.5
    elif type1 == 'Fairy':
        if type2 in ['Dark','Dragon','Fighting']:
            return 2
        if type2 in ['Fire','Poison','Steel']:
            return 0.5
    return 1

def date_diff(old, new = None):
    if old == None:
        return 40000
    if new == None:
        new = datetime.datetime.now()
    old_time = datetime.datetime.strptime(old,("%m/%d/%Y, %H:%M:%S"))
    diff = new-old_time
    print("seconds:"+str(diff.total_seconds()))
    return diff.total_seconds()


def gain_skill(P,skill,amount,lvl = False):
    mod = 0.25 + ((P.prog[8][skill][0]-1)*0.1)
    if P.prog[8][skill][0] != 10:
        P.prog[8][skill][1] += int(amount/mod)
        # max = True
        # if P.prog[8][skill][0] == 3:
        #     max = False
        #     if P.prog[8][skill][1] > 100:
        #         P.prog[8][skill][1] = 100
        if P.prog[8][skill][1] >= 100:
            amount = int((P.prog[8][skill][1] - 100)*mod)
            P.prog[8][skill][0] += 1
            if P.prog[8][skill][0] == 10:
                P.prog[8][skill][1] = 100
            else:
                P.prog[8][skill][1] = 0
                return gain_skill(P,skill,amount,True)
    return lvl

def research_game(P,gem_count,points = [0,True]):
    back = load("p/research/research_overlay.png")
    cmenu = load("p/research/change_menu.png")
    gmenu = load("p/research/change_menu.png")
    n_lens = load("p/research/neutral_lens.png")
    icon_high = load("p/research/ico_high.png")
    icon_shad = load("p/research/ico_shadow.png")
    shadow = load("p/research/research_shadow.png")
    high = load("p/research/high.png")
    type_list = ['Bug','Dark','Dragon','Electric','Fairy','Fighting','Fire','Flying','Ghost','Grass','Ground','Ice','Normal','Poison','Psychic','Rock','Steel','Water']
    gem_type = type_list[random.randint(0,17)]
    #gem_type = 'Bug'
    used_list = []
    guessed_list = []
    crossed_out = 0
    research_lvl = (P.prog[8][0][0]-1)/3
    if research_lvl > 0:
        r_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
        r_list.remove(type_list.index(gem_type))
        if random.random() <= research_lvl:
            r = random.choice(r_list)
            guessed_list.append(r)
            r_list.remove(r)
            crossed_out += 1
        if 1+random.random() <= research_lvl:
            r = random.choice(r_list)
            guessed_list.append(r)
            r_list.remove(r)
            crossed_out += 1
        if 2+random.random() <= research_lvl:
            r = random.choice(r_list)
            guessed_list.append(r)
            r_list.remove(r)
            crossed_out += 1
        print("List: " + str(r_list))
        print("Gem Type: "+ str(gem_type))
    log_history = []
    icons = []
    lenses = []
    for type in type_list:
        icons.append(load("p/"+type+"_ico.png"))
    for type in type_list:
        lenses.append(load("p/research/"+type+"_lens.png"))
    gem0 = load("p/research/Gem_0.png")
    gem1 = load("p/research/Gem_1.png")
    gem2 = load("p/research/Gem_2.png")
    log_ico = []
    log_ico.append(load("p/research/log0.png"))
    log_ico.append(load("p/research/log1.png"))
    log_ico.append(load("p/research/log2.png"))
    new_lens = True
    new_guess = True
    lens = n_lens
    gem = gem0
    choose = 0
    current_lens = 0
    switch_high = 0
    guess_high = 0
    current = P.font.render("Lens Type:",True,(20,50,20))
    quit = P.font.render("Quit",True,(20,50,20))
    log = P.font.render("Log",True,(20,50,20))
    switch = P.font.render("Switch",True,(20,50,20))
    guess = P.font.render("Guess",True,(20,50,20))
    end = True
    y1 = 0
    y2 = 0
    a = 0
    def guess_menu():
        P.surface.blit(gmenu,(540,510-abs(y2)))
        P.surface.blit(guess,(600,520-abs(y2)))
        xpos = 0
        ypos = 0
        for ic in range(len(icons)):
            P.surface.blit(icons[ic],(550+xpos,610+ypos-abs(y2)))
            if ic in guessed_list:
                P.surface.blit(icon_shad,(550+xpos,610+ypos-abs(y2)))
            if guess_high == ic:
                P.surface.blit(icon_high,(550+xpos,610+ypos-abs(y2)))
            if ypos == 360:
                ypos = 0
                xpos = 120
            else:
                ypos += 45
    def switch_menu():
        P.surface.blit(cmenu,(280,510-abs(y1)))
        P.surface.blit(switch,(328,520-abs(y1)))
        xpos = 0
        ypos = 0
        for ic in range(len(icons)):
            P.surface.blit(icons[ic],(290+xpos,610+ypos-abs(y1)))
            if ic in used_list:
                P.surface.blit(icon_shad,(290+xpos,610+ypos-abs(y1)))
            if switch_high == ic:
                P.surface.blit(icon_high,(290+xpos,610+ypos-abs(y1)))
            if ypos == 360:
                ypos = 0
                xpos = 120
            else:
                ypos += 45
    while end:
        P.surface.blit(back,(0,0))
        P.surface.blit(gem,(365,85))
        P.surface.blit(lens,(345,95))
        P.surface.blit(current,(367,20))
        P.surface.blit(log,(134,20))
        xpos = 0
        ypos = 0
        for logs in log_history:
            P.surface.blit(icons[logs[0]],(20+xpos,80+ypos))
            P.surface.blit(log_ico[logs[1]],(120+xpos,80+ypos))
            if ypos == 360:
                ypos = 0
                xpos = 160
            else:
                ypos += 45
        P.surface.blit(quit,(97,520))
        if lens != n_lens:
            P.surface.blit(icons[current_lens],(655,25))
        if y1 == 0:
            switch_menu()
        if y2 == 0:
            guess_menu()
        if (y1 > 20 or y1 < -20) or (y2 > 20 or y2 < -20):
            P.surface.blit(shadow,(0,0))
        if y1 != 0:
            switch_menu()
        if y2 != 0:
            guess_menu()
        if y1 == 0 and y2 == 0:
            P.surface.blit(high,(280+choose,510))
        for event in map_keys():
            if (event.type == KEYDOWN or P.buffer_talk) and a > 5:
                #Z
                if event.key == pygame.key.key_code(P.controls[4]):
                    if choose == 0 and y1 == 0:
                        switch_high = 0
                        y1 = 20
                    if choose == 260 and y2 == 0:
                        guess_high = 0
                        y2 = 20
                    if choose == -260 and y2 == 0:
                        new_txt(P)
                        write(P,"Are you sure you want to","leave? You'll lose all your","current progress.")
                        if choice(P):
                            gem_count = 1
                            points = [-1,False]
                            end = False
                        else:
                            a = 1
                    if y2 == 440:
                        if guess_high in guessed_list:
                            txt(P,"You've already guessed this", "type.")
                        else:
                            # current_lens = switch_high
                            # lens = lenses[switch_high]
                            guessed_list.append(guess_high)
                            y2 = -420
                    if y1 == 440:
                        if switch_high in used_list:
                            txt(P,"You've already used this lens.")
                        else:
                            current_lens = switch_high
                            lens = lenses[switch_high]
                            used_list.append(switch_high)
                            result = type_eff(type_list[current_lens],gem_type)
                            if result < 1:
                                gem = gem1
                            elif result > 1:
                                gem = gem2
                            else:
                                gem = gem0
                            y1 = -420
                #X
                if event.key == pygame.key.key_code(P.controls[5]):
                    if choose == 0 and y1 == 440:
                        y1 = -420
                        new_lens = False
                    if choose == 260 and y2 == 440:
                        y2 = -420
                        new_guess = False
                    if y1 == 0 and y2 == 0:
                        new_txt(P)
                        write(P,"Are you sure you want to","leave? You'll lose all your","current progress.")
                        if choice(P):
                            gem_count = 1
                            points = [-1,False]
                            end = False
                        else:
                            a = 1
                #up
                if event.key == pygame.key.key_code(P.controls[0]):
                    if switch_high != 0 and switch_high != 9 and y1 == 440:
                        switch_high -= 1
                    if guess_high != 0 and guess_high != 9 and y2 == 440:
                        guess_high -= 1
                #down
                if event.key == pygame.key.key_code(P.controls[1]):
                    if switch_high != 8 and switch_high != 17 and y1 == 440:
                        switch_high += 1
                    if guess_high != 8 and guess_high != 17 and y2 == 440:
                        guess_high += 1
                #left
                if event.key == pygame.key.key_code(P.controls[2]):
                    if choose != -260 and y1 == 0 and y2 == 0:
                        choose -= 260
                    if switch_high > 8 and y1 == 440:
                        switch_high -= 9
                    if guess_high > 8 and y2 == 440:
                        guess_high -= 9
                #right
                if event.key == pygame.key.key_code(P.controls[3]):
                    if choose != 260 and y1 == 0 and y2 == 0:
                        choose += 260
                    if switch_high < 9 and y1 == 440:
                        switch_high += 9
                    if guess_high < 9 and y2 == 440:
                        guess_high += 9
        if y2 > 0 and y2 < 440:
            y2 += 20
            if y2 == 440:
                a = 1
        if y2 < 0:
            y2 += 20
            if y2 == 0:
                a = 1
                if new_guess:
                    if type_list[guess_high] == gem_type:
                        txt(P,"Looks good to me!","One more "+type_list[guess_high]+" gem for the","collection!")
                        if gem_count == 2:
                            txt(P,"Alright, one more to go!")
                        elif gem_count != 1:
                            txt(P,"Give me a moment to get the","next gem set up for you.")
                        else:
                            txt(P,"That's all of them! Good work!")
                        end = False
                    else:
                        txt(P,"That doesn't seem right.","Maybe you should try a few","more lenses.")
                else:
                    new_guess = True
        if y1 > 0 and y1 < 440:
            y1 += 20
            if y1 == 440:
                a = 1
        if y1 < 0:
            y1 += 20
            if y1 == 0:
                a = 1
                if new_lens:
                    if gem == gem0:
                        txt(P,'The gem appears normal.')
                        log_history.append([switch_high,0])
                    elif gem == gem1:
                        txt(P,"The gem appears very dull.")
                        log_history.append([switch_high,1])
                    else:
                        txt(P,"The gem is glowing brightly!")
                        log_history.append([switch_high,2])
                else:
                    new_lens = True
        if a == 0:
            fade_in(P)
            txt(P,"It's all set up! Go ahead and","switch the lens when you're","ready!")
            if crossed_out > 0:
                txt(P,"You narrowed your options a","little based on your previous","experiences.")
        a += 1
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P)
    if points[0] == -1:
        return [-1,False]
    pt = 1000
    #lowest possible 35
    mod = 18
    for x in range(len(used_list)):
        pt -= 5+mod
        mod -= 1
    mod = 17
    for x in range(len(guessed_list)-1-crossed_out):
        pt -= 15+(3*mod)
        mod -= 1
    if len(guessed_list) != 18 and len(used_list) != 18 and points[1] == True:
        points[1] = False
    print(points[0]+pt)
    points[0] += pt
    if gem_count != 1:
        return research_game(P,gem_count-1,points)
    else:
        return points

def get_location(P,map = False,location = None):
    if location == None:
        location = P.loc
    if location in ["route_1",'beedrill']:
        return 'Route 1'
    elif location == "route_2":
        return 'Route 2'
    elif location == "echo_cave":
        return 'Echo Cave'
    elif location == "vigore":
        return 'Vigore Dam'
    elif location in ["cruise_1","cruise_2","dock_1","am_square","square_1"]:
        if map:
            return 'South Alto Mare'
        return 'Alto Mare'
    elif location in ["north_am","pc_am"]:
        if map:
            return 'North Alto Mare'
        return 'Alto Mare'
    elif location in ["egida","egida_under","egida_mine","egida_lab","pc_egida"]:
        return 'Egida City'
    elif location in ["egi_gym","egi_gym_l","egi_gym_r","egi_gym_b"]:
        if map:
            return 'Egida City'
        else:
            return 'Egida Gym'
    elif location in ["power_plant_1","power_plant_b","power_plant_2"]:
        if map:
            return 'Vigore Dam'
        else:
            return 'Power Plant'
    elif location == 'route_3':
        return 'Route 3'
    elif location in ['isola','pc_isola']:
        return 'Isola Town'
    elif location in ['verde','pc_verde']:
        return 'Verde City'
    elif location in ['scarab_l','scarab_r']:
        return 'Scarab Woods'
    elif location in ['fiore','pc_fiore','fiore_garden']:
        return 'Fiore Town'
    elif location in ['pianura','pc_pianura','pianura_nursery','pianura_bakery']:
        return 'Pianura City'
    elif location in ['pia_gym'] or location[:7] == "pia_gym":
        if map:
            return 'Pianura City'
        else:
            return 'Pianura Gym'
    elif location == 'mirror_cave':
        return 'Mirror Cave'
    elif location == 'route_4':
        return 'Route 4'
    elif location == 'route_5':
        return 'Route 5'
    elif location[:7] == "house_1":
        if int(location[8:]) == 1:
            if map:
                return 'North Alto Mare'
            return 'Alto Mare'
        elif int(location[8:]) < 9:
            return 'Egida City'
        elif int(location[8:]) < 12:
            return 'Fiore Town'
        else:
            return 'Pianura City'
    elif location[:8] == "house_21" or P.loc[:8] == "house_22":
        if int(location[9:]) <= 3:
            if map:
                if int(location[9:]) == 1:
                    return 'South Alto Mare'
                else:
                    return 'North Alto Mare'
            return 'Alto Mare'
        elif int(location[9:]) <= 5:
            return 'Pianura City'
        else:
            return 'Egida City'
    elif location[:7] == "house_3":
        if int(location[8:]) == 1:
            return 'Fiore Town'
        elif int(location[8:]) <= 4:
            return 'Isola Town'

def set_location(P):
    loc = get_location(P)
    if P.loc_in_txt:
        if loc != P.loc_in_txt:
            P.new_location = True
        else:
            P.new_location = False
    P.loc_in_txt = loc
    P.loc_txt = P.font.render(loc,True,(200,255,200))

def show_location(P,text,tim):
    if tim >= 170 or P.new_location == False:
        return
    tim -= 10
    gloc = 0
    rloc = 0
    tloc = 0
    if tim <= 30:
        gloc = tim*23
        rloc = tim*23
    elif tim <= 80:
        gloc = 690
        rloc = 690+((tim-30)*2)
    elif tim <= 130:
        gloc = 690
        rloc = 790-((tim-80))
    else:
        gloc = 690-((tim-130)*23)
        rloc = 690-((tim-130)*23)
    P.surface.blit(P.g_flair,(-800+gloc,10))
    P.surface.blit(P.r_flair,(-800+rloc,10))
    P.surface.blit(text,(-670+gloc,25))

def open_cpu(P) -> None:
    class Box:
        def __init__(self,box,num):
            self.box = box
            self.pokes = []
            count = 0
            if num != -1:
                for x in range(5):
                    l = []
                    for y in range(6):
                        thing = P.save_data.box[num][count]
                        if thing == 0:
                            l.append(0)
                        else:
                            l.append(poke.Poke(thing[0],thing[1]))
                        count += 1
                    self.pokes.append(l)
            else:
                l = []
                for x in P.party:
                    l.append(x)
                for x in range(6-len(P.party)):
                    l.append(0)
                self.pokes.append(l)
        def set_np(self,n,p):
            self.prev = p
            self.next = n
        def to_list(self):
            ans = []
            for x in range(5):
                for y in range(6):
                    if self.pokes[x][y] != 0:
                        ans.append([self.pokes[x][y].code,self.pokes[x][y].to_list()])
                    else:
                        ans.append(0)
            return ans
        def to_party(self):
            ans = []
            for x in range(6):
                if self.pokes[0][x] != 0:
                    ans.append(self.pokes[0][x])
            return ans
        def shift_party(self):
            l = []
            for y in self.pokes[0]:
                if y != 0:
                    l.append(y)
            while len(l) < 6:
                l.append(0)
            self.pokes[0] = l             
    pok = 0
    back = load("p/am/cpu_hud.png")
    box1 = load("p/am/box_1.png")
    box2 = load("p/am/box_2.png")
    box3 = load("p/am/box_3.png")
    arrow = load("p/pointer.png")
    txtbox = load("p/one_line_txt.png")
    cbox = load("p/5_box.png")
    guides = load("p/box_guides.png")
    party = load("p/am/party_box.png")
    move = P.font.render("Move",True,(0,0,0))
    summary = P.font.render("Summary",True,(0,0,0))
    item = P.font.render("Item",True,(0,0,0))
    release = P.font.render("Release",True,(0,0,0))
    cancel = P.font.render("Cancel",True,(0,0,0))
    mega = pygame.transform.scale(load("p/mega_symbol.png"),(30,30))
    nurse = pygame.transform.scale(load("p/nurse_icon.png"),(30,30))
    b1 = Box(box1,0)
    b2 = Box(box2,1)
    b3 = Box(box3,2)
    b4 = Box(box3,3)
    b5 = Box(box3,4)
    b6 = Box(box3,5)
    b7 = Box(box3,6)
    b8 = Box(box3,7)
    b9 = Box(box3,8)
    b10 = Box(box3,9)
    pbox = Box(box1,-1)
    b1.set_np(b2,b10)
    b2.set_np(b3,b1)
    b3.set_np(b4,b2)
    b4.set_np(b5,b3)
    b5.set_np(b6,b4)
    b6.set_np(b7,b5)
    b7.set_np(b8,b6)
    b8.set_np(b9,b7)
    b9.set_np(b10,b8)
    b10.set_np(b1,b9)
    b = b1
    P.surface.blit(back,(0,0))
    end = True
    a = 0
    tran = 0
    a_pos = 0
    a_x = 0
    a_y = 0
    ax = 0
    ay = 0
    ary = 270
    count = 0
    select = 0
    py = 0
    p_x = 0
    p_y = 0
    pp = 0
    P.surface.blit(b.box,(-20+tran,70))
    print_box(P,b.pokes,0+tran)
    P.surface.blit(back,(0,0))
    P.surface.blit(arrow,(220+ax,55+ay))
    fade_in(P)
    while end:
        P.surface.blit(b.box,(-20+tran,70))
        P.surface.blit(b.next.box,(480+tran,70))
        P.surface.blit(b.prev.box,(-520+tran,70))
        print_box(P,b.pokes,0+tran)
        print_box(P,b.next.pokes,500+tran)
        print_box(P,b.prev.pokes,-500+tran)
        P.surface.blit(back,(0,0))
        if select == 1:
            pok = spoke
        if pok != 0 and (a_pos != 0 or select == 1):
            name = P.font.render(pok.name,True,(255,255,255))
            name_size = P.font.size(pok.name)[0]
            lvl = P.font.render("Lv. "+str(pok.lvl),True,(255,255,255))
            abi = P.font_s.render(pok.ability,True,(255,255,255))
            abip = P.font_s.size(pok.ability)[0]
            if pok.item == None:
                it = P.font_s.render("No Item",True,(255,255,255))
                itp = P.font_s.size("No Item")[0]
            else:
                it = P.font_s.render(pok.item,True,(255,255,255))
                itp = P.font_s.size(pok.item)[0]
            ball = pygame.transform.scale(load("p/"+pok.ball+".png"),(30,30))
            full = pygame.transform.scale(load("p/poke/"+pok.code+"_full.png"),(250,250))
            if pok.gen == 0:
                gen_i = load("p/boy_ico.png")
            if pok.gen == 1:
                gen_i = load("p/girl_ico.png")
            if pok.gen == 2:
                gen_i = load("p/blank.png")
            type1 = load("p/"+pok.type[0]+"_ico.png")
            P.surface.blit(guides,(450,20))
            if pok.type[1] != None:
                type2 = load("p/"+pok.type[1]+"_ico.png")
                P.surface.blit(type1,(560,30))
                P.surface.blit(type2,(680,30))
            else:
                P.surface.blit(type1,(620,30))
            P.surface.blit(lvl,(620,93))
            P.surface.blit(abi,(790-abip,420))
            P.surface.blit(it,(790-itp,470))
            P.surface.blit(ball,(15,22))
            P.surface.blit(name,(60,15))
            if pok.code[:5] == 'Mega_':
                P.surface.blit(mega,(65+name_size,25))
            if pok.nurse:
                P.surface.blit(nurse,(65+name_size,25))
            P.surface.blit(gen_i,(360,15))
            P.surface.blit(full,(540,155))
        if py != 0:
            P.surface.blit(party,(100,600-abs(py)))
            if pbox.pokes[0][0] != 0:
                P.surface.blit(pbox.pokes[0][0].icon,(140,625-abs(py)))
            if pbox.pokes[0][1] != 0:
                P.surface.blit(pbox.pokes[0][1].icon,(250,655-abs(py)))
            if pbox.pokes[0][2] != 0:
                P.surface.blit(pbox.pokes[0][2].icon,(140,725-abs(py)))
            if pbox.pokes[0][3] != 0:
                P.surface.blit(pbox.pokes[0][3].icon,(250,755-abs(py)))
            if pbox.pokes[0][4] != 0:
                P.surface.blit(pbox.pokes[0][4].icon,(140,825-abs(py)))
            if pbox.pokes[0][5] != 0:
                P.surface.blit(pbox.pokes[0][5].icon,(250,855-abs(py)))
        if a_pos == 2:
            P.surface.blit(txtbox,(0,530))
            P.surface.blit(cbox,(550,260))
            P.surface.blit(txt0,(20,540))
            P.surface.blit(move,(600,270))
            P.surface.blit(summary,(600,320))
            P.surface.blit(item,(600,370))
            P.surface.blit(release,(600,420))
            P.surface.blit(cancel,(600,470))
            P.surface.blit(P.arrow,(550,ary))
        if select == 1:
            if a_pos == 0:
                P.surface.blit(spoke.icon,(200,65))
            if a_pos == 1 and py>= 0:
                P.surface.blit(spoke.icon,(20+a_x,130+a_y))
            if a_pos == 3 or (a_pos == 4 and py > 0 and py < 420):
                P.surface.blit(spoke.icon,(200,505))
            if (a_pos == 4 and py == 420) or py < 0 or (a_pos == 2 and py == 420):
                P.surface.blit(spoke.icon,(140+p_x,175+p_y))
        if a_pos == 0:
            P.surface.blit(arrow,(220+ax,55+ay))
        if (a_pos == 1 and py >= 0) or (a_pos == 2 and py == 0):
            P.surface.blit(arrow,(40+a_x+ax,130+a_y+ay))
        if a_pos == 3 or (a_pos == 4 and py > 0 and py < 420):
            P.surface.blit(arrow,(220+ax,505+ay))
        if (a_pos == 4 and py == 420) or py < 0 or (a_pos == 2 and py == 420):
            P.surface.blit(arrow,(160+p_x+ax,175+p_y+ay))
        for event in pygame.event.get(eventtype = KEYDOWN):
            if event.key == pygame.key.key_code(P.controls[5]) and a > 15:
                if select == 1:
                    if a_pos == 4:
                        py = -420
                        a_x = 0
                        a_y = 0
                        a_pos = 1
                    else:
                        select = 0
                        tbox.pokes[int(ty/70)][int(tx/70)] = spoke
                elif a_pos == 4:
                    a_pos = 1
                    py = -420
                    a_x = 0
                    a_y = 0
                elif a_pos == 2:
                    if py == 420:
                        a_pos = 4
                    else:
                        a_pos = 1
                else:
                    end = False
            if event.key == pygame.key.key_code(P.controls[3]) and a > 15 and tran == 0:
                if a_pos == 0:
                    tran = -1
                    a_x = 0
                if a_pos == 1 and a_x < 350:
                    a_x += 70
                if a_pos == 4 and p_x == 0:
                    p_x = 110
                    p_y += 30
                    pp += 1
            if event.key == pygame.key.key_code(P.controls[2]) and a > 15 and tran == 0:
                if a_pos == 0:
                    tran = 1
                    a_x = 0
                if a_pos == 1 and a_x > 0:
                    a_x -= 70
                if a_pos == 4 and p_x == 110:
                    p_x = 0
                    p_y -= 30
                    pp -= 1
            if event.key == pygame.key.key_code(P.controls[1]) and a > 15 and tran == 0:
                if a_pos == 0:
                    a_pos = 1
                elif a_pos == 1 and a_y == 280:
                    a_pos = 3
                elif a_pos == 1 and a_y < 280:
                    a_y += 70
                elif a_pos == 2 and ary < 470:
                    ary += 50
                elif a_pos == 4:
                    if pp < 4 and pp > -1:
                        p_y += 100
                        pp += 2
                    elif pp > 3:
                        p_x = 60
                        p_y = 330
                        pp = -1
            if event.key == pygame.key.key_code(P.controls[0]) and a > 15:
                if a_y == 0 and a_pos == 1:
                    a_pos = 0
                elif a_pos == 2 and ary > 270:
                    ary -= 50
                elif a_pos == 3:
                    a_pos = 1
                elif a_pos == 1:
                    a_y -= 70
                elif a_pos == 4:
                    if pp > 1:
                        p_y -= 100
                        pp -= 2
                    elif pp == -1:
                        p_x = 110
                        p_y = 230
                        pp = 5
            if event.key == pygame.key.key_code(P.controls[4]) and a > 15:
                if a_pos == 1:
                    if select == 1:
                        if b.pokes[int(a_y/70)][int(a_x/70)] != 0:
                            tbox.pokes[int(ty/70)][int(tx/70)] = b.pokes[int(a_y/70)][int(a_x/70)]
                        b.pokes[int(a_y/70)][int(a_x/70)] = spoke
                        pbox.shift_party()
                        select = 0
                    elif pok != 0:
                        txt0 = P.font.render(pok.name + " is selected.",True,(0,0,0))
                        t = P.surface.copy()
                        a_pos = 2
                elif a_pos == 4 and pp != -1:
                    if select == 1:
                        if pbox.pokes[0][pp] != 0:
                            tbox.pokes[int(ty/70)][int(tx/70)] = pbox.pokes[0][pp]
                        pbox.pokes[0][pp] = spoke
                        pbox.shift_party()
                        select = 0
                    elif pok != 0:
                        txt0 = P.font.render(pok.name + " is selected.",True,(0,0,0))
                        t = P.surface.copy()
                        a_pos = 2
                elif a_pos == 2:
                    if ary == 470:
                        if py == 420:
                            a_pos = 4
                        else:
                            a_pos = 1
                    if ary == 420:
                        if pbox.pokes[0][1] == 0 and py == 420:
                            P.surface.blit(txtbox,(0,530))
                            write(P,"","","That's your last Pokemon!")
                            cont(P)
                        elif pok.nurse:
                            P.surface.blit(txtbox,(0,530))
                            write(P,"","","You can't release "+pok.name+"!")
                            cont(P)
                        else:
                            P.surface.blit(t,(0,0))
                            new_txt(P)
                            write(P,"Release this Pokemon?")
                            if choice(P,reverse = True):
                                pass
                            else:
                                txt(P,pok.name+" was released.")
                                txt(P,"Bye-bye, "+pok.name+"!")
                                if py == 0:
                                    b.pokes[int(a_y/70)][int(a_x/70)] = 0
                                if py == 420:
                                    pbox.pokes[0][pp] = 0
                                pbox.shift_party()
                        if py == 420:
                            a_pos = 4
                        else:
                            a_pos = 1
                    if ary == 370:
                        if pok.item == None:
                            #t = P.surface.copy()
                            fade_out(P)
                            chose_item = bag(P,True)
                            P.surface.blit(t,(0,0))
                            fade_in(P)
                            if chose_item:
                                txt(P,pok.name + " was given the",chose_item+" to hold.")
                                pok.item = chose_item
                                add_item(P,chose_item,-1)
                        else:
                            P.surface.blit(t,(0,0))
                            new_txt(P)
                            write(P,"Take this "+pok.item+"?")
                            if choice(P):
                                txt(P,"Received the "+pok.item ,"from " + pok.name +".")
                                add_item(P,pok.item,1)
                                pok.item = None
                        a = 0
                        if py == 420:
                            a_pos = 4
                        else:
                            a_pos = 1
                    if ary == 320:
                        fade_out(P)
                        summ(P,pok)
                        P.surface.blit(t,(0,0))
                        fade_in(P)
                        a = 0
                        if py == 420:
                            a_pos = 4
                        else:
                            a_pos = 1
                    if ary == 270:
                        if pbox.pokes[0][1] == 0 and py == 420:
                            P.surface.blit(txtbox,(0,530))
                            write(P,"","","That's your last Pokemon!")
                            cont(P)
                            a_pos = 4
                        else:
                            if py == 420:
                                tbox = pbox
                                tx = pp*70
                                ty = 0
                                spoke = pok
                                select = 1
                                a_pos = 4
                                pbox.pokes[0][pp] = 0
                            else:
                                tbox = b
                                tx = a_x
                                ty = a_y
                                spoke = pok
                                select = 1
                                a_pos = 1
                                b.pokes[int(a_y/70)][int(a_x/70)] = 0
                elif a_pos == 3:
                    a_pos = 4
                    py = 1
                elif a_pos == 4 and p_x == 60 and p_y == 330:
                    a_pos = 1
                    py = -420
                    a_x = 0
                    a_y = 0
        if py == 0:
            pok = b.pokes[int(a_y/70)][int(a_x/70)]
        if py == 420:
            pok = pbox.pokes[0][pp]
        if a_pos != 2:
            ary = 270
        if tran < 0:
            if tran == -1:
                tran = -50
            elif tran == -500:
                tran = 0
                b = b.next
            else:
                tran -= 50
        if tran > 0:
            if tran == 1:
                tran = 50
            elif tran == 500:
                tran = 0
                b = b.prev
            else:
                tran += 50
        if count == 10:
            count = -10
        if a%3 == 0:
            count += 1
            ax = abs(count)
            ay = -abs(count)
        if select == 1:
            ax = 0
            ay = -20
        if py > 0 and py < 420:
            if py == 1:
                py = 20
            else:
                py += 20
        if py < 0:
            py += 20
            if py == 0:
                p_x = 0
                p_y = 0
                pp = 0
        a += 1
        P.clock.tick(P.ani_spd)
        update_screen(P)
    b_list = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10]
    for x in b_list:
        for y in range(5):
            for z in range(6):
                if x.pokes[y][z] != 0:
                    x.pokes[y][z].heal()
    P.save_data.box[0] = b1.to_list()
    P.save_data.box[1] = b2.to_list()
    P.save_data.box[2] = b3.to_list()
    P.save_data.box[3] = b4.to_list()
    P.save_data.box[4] = b5.to_list()
    P.save_data.box[5] = b6.to_list()
    P.save_data.box[6] = b7.to_list()
    P.save_data.box[7] = b8.to_list()
    P.save_data.box[8] = b9.to_list()
    P.save_data.box[9] = b10.to_list()
    P.party = pbox.to_party()
    fade_out(P)

def mart_sell(P, candy = False) -> None:
    box = load("p/bag_box.png")
    back = load("p/bag.png")
    i = load("p/item_ico.png")
    m = load("p/med_ico.png")
    b = load("p/balls_ico.png")
    t = load("p/tm_ico.png")
    k = load("p/key_ico.png")
    high = load("p/bag_high.png")
    sell_mod = 2
    if candy:
        sell_mod = 10
    ico = i
    ix = 0
    scroll = 0
    bag = 0
    a = 0
    curr = ['',0]
    su = False
    sd = False
    end = True
    while end:
        P.surface.blit(back,(0,0))
        P.surface.blit(ico,(ix,0))
        title = "ITEMS"
        if bag == 1:
            title = "MEDICINE"
        if bag == 2:
            title = "BALLS"
        if bag == 3:
            title = "TMs"
        if bag == 4:
            title = "KEY ITEMS"
        tle = P.font.render(title,True,(255,255,255))
        P.surface.blit(tle,((400-(P.font.size(title)[0]))/2,85))
        y = 0
        if scroll <= 280:
            s = 0
        elif scroll >= (((len(P.bag[bag])-1)*70)-210):
            if len(P.bag[bag]) < 8:
                s = (((len(P.bag[bag])-1)*70))-(70*(len(P.bag[bag])-1))
            else:
                s = (((len(P.bag[bag])-1)*70))-490
        else:
            s = scroll-280
        for z in P.bag[bag]:
            txt1 = P.font_s.render(z[0],True,(0,0,0))
            P.surface.blit(box,(420,20-s+y))
            P.surface.blit(txt1,(420+(360-(P.font_s.size(z[0])[0]))/2,35-s+y))
            if z == P.bag[bag][int(scroll/70)]:
                P.surface.blit(high,(420,20-s+y))
                curr = z
            y += 70
        if(curr != ['',0]):
            txt1 = P.font_s.render(curr[0],True,(0,0,0))
            txt2 = P.font_s.render(' x '+str(curr[1]),True,(0,0,0))
            P.surface.blit(txt1,((380-P.font_s.size(curr[0])[0])/2,150))
            P.surface.blit(txt2,(180,195))
            ic = pygame.transform.scale(load("p/item/"+curr[0]+".png"),(50,50))
            P.surface.blit(ic,(130,185))
            item = items.Item(curr[0])
            descr = []
            cngy = 0
            for x in item.desc:
                descr.append(P.font_s.render(x,True,(0,0,0)))
            for x in descr:
                P.surface.blit(x,(20,240+cngy))
                cngy += 34
        if a == 0:
            fade_in(P)
        for event in pygame.event.get(eventtype = KEYDOWN):
            if event.key == pygame.key.key_code(P.controls[4]) and a > 10 and curr != ['',0]:
                if items.Item(curr[0]).price == -1:
                    txt(P,curr[0]+"? Oh no.", "I can't buy that.")
                elif item_in_bag(P,curr[0]) == 1:
                    new_txt(P)
                    write(P,"I can pay $"+str(int(items.Item(curr[0]).price/sell_mod))+".","Would that be okay?")
                    if choice(P):
                        txt(P,"Turned over the "+curr[0],"and received $"+str(int(items.Item(curr[0]).price/sell_mod))+".")
                        add_item(P,curr[0],-1)
                        P.save_data.money += int(items.Item(curr[0]).price/sell_mod)
                else:
                    new_txt(P)
                    write(P,curr[0]+"?","How many would you like to", "sell?")
                    num = choose_num(P,item_in_bag(P,curr[0]))
                    if num > 0:
                        new_txt(P)
                        write(P,"I can pay $"+str(int(items.Item(curr[0]).price/sell_mod*num))+".","Would that be okay?")
                        if choice(P):
                            txt(P,"Turned over the "+curr[0],"and received $"+str(int(items.Item(curr[0]).price/sell_mod*num))+".")
                            add_item(P,curr[0],-1*num)
                            P.save_data.money += int(items.Item(curr[0]).price/sell_mod*num)
                if scroll/70 > (len(P.bag[bag])-1):
                    scroll -= 70
                if len(P.bag[bag]) == 0:
                    curr = ['',0]
            if event.key == pygame.key.key_code(P.controls[5]) and a > 10:
                end = False
            elif event.key == pygame.key.key_code(P.controls[2]) and a > 10:
                if bag != 0:
                    curr = ['',0]
                    scroll = 0
                    bag -= 1
                    ix -= 80
                    if bag == 0:
                        ico = i
                    if bag == 1:
                        ico = m
                    if bag == 2:
                        ico = b
                    if bag == 3:
                        ico = t
            elif event.key == pygame.key.key_code(P.controls[3]) and a > 10:
                if bag != 4:
                    curr = ['',0]
                    scroll = 0
                    bag += 1
                    ix += 80
                    if bag == 1:
                        ico = m
                    if bag == 2:
                        ico = b
                    if bag == 3:
                        ico = t
                    if bag == 4:
                        ico = k
        keys = pygame.key.get_pressed()
        if scroll%70 == 0:
            su = False
            sd = False
        if keys[pygame.key.key_code(P.controls[0])] and scroll > 0 and sd == False:
            su = True
        if keys[pygame.key.key_code(P.controls[1])] and scroll < (len(P.bag[bag])-1)*70 and su == False:
            sd = True
        if(su):
            scroll -= 10
        if(sd):
            scroll += 10
        a += 1
        P.clock.tick(P.ani_spd)
        update_screen(P)
    fade_out(P)


def poke_mart(P,back,candy = False,custom_shop = None, stock = None,price_mod = 1,diff_price = []):
    mart = load("p/pokemart.png")
    shelf = load("p/mart_shelf.png")
    wind = load("p/mart_window.png")
    if candy:
        price_mod = 5
        shop = ['Expired Candy','Old Candy']
        if P.prog[0] >= 48:
            shop.append('Common Candy')
        shop.append('Quit')
    elif custom_shop != None:
        shop = custom_shop
    elif P.loc == 'egida_mine':
        shop = ['Bug Gem','Dark Gem','Dragon Gem','Electric Gem','Fairy Gem','Fighting Gem','Fire Gem','Flying Gem','Ghost Gem','Grass Gem','Ground Gem','Ice Gem','Normal Gem','Poison Gem','Psychic Gem','Rock Gem','Steel Gem','Water Gem','Quit']
    elif P.loc == 'pianura_bakery':
        shop = ['Cinnamon Roll','Coffee','Cupcake','Jello','Lava Cake','Sundae','Poffin','Quit']
    else:
        shop = ['Poke Ball','Potion','Quit']
    box = load("p/mart_box.png")
    high = load("p/mart_high.png")
    text = load("p/mart_text.png")
    money = P.font.render("$" + str(P.save_data.money),True,(0,0,0))
    zero = P.font.render("0",True,(0,0,0))
    inbag = zero
    tim = 0
    my = 0
    by = 0
    s = 0
    curr = ''
    scroll = 0
    end = True
    while end:
        P.surface.blit(back,(0,0))
        P.surface.blit(mart,(0,-300+my))
        P.surface.blit(shelf,(410,633-by))
        if scroll <= 210:
            s = 0
        elif scroll >= (((len(shop)-1)*70)-140):
            if len(shop) < 6:
                s = (((len(shop)-1)*70))-(70*(len(shop)-1))
            else:
                s = (((len(shop)-1)*70))-350
        else:
            s = scroll-210
        inc = 0
        P.surface.set_clip((0,123,800,477))
        for i in shop:
            txt0 = P.font_s.render(i, True, (0, 0, 0))
            P.surface.blit(box, (420, 643 - by - s + inc))
            P.surface.blit(txt0, (420 + (360 - (P.font_s.size(i)[0])) / 2, 658 - s - by + inc))
            inc += 70
            if i == shop[int(scroll/70)] and tim > 30:
                P.surface.blit(high,(420,573 - by - s + inc))
                inbag = zero
                for x in P.bag:
                    for it in x:
                        if it[0] == i:
                            inbag = P.font.render(str(it[1]),True,(0,0,0))
                curr = i
        P.surface.set_clip((0,0,800,600))
        P.surface.blit(money,(160,-255+my))
        P.surface.blit(wind,(400,623-by))
        if tim > 30 and curr != 'Quit':
            P.surface.blit(text,(10,190))
            txt1 = P.font_s.render(curr, True, (0, 0, 0))
            if curr in diff_price:
                price = P.font_s.render("$"+str(int(items.Item(curr).price*diff_price[0])),True,(0,0,0))
            else:
                price = P.font_s.render("$"+str(int(items.Item(curr).price*price_mod)),True,(0,0,0))
            P.surface.blit(txt1, (200 - txt1.get_width()/2, 200))
            P.surface.blit(price,(190,245))
            icon = pygame.transform.scale(load("p/item/" + curr + ".png"), (50, 50))
            P.surface.blit(icon, (130, 235))
            descr = []
            cngy = 0
            for x in items.Item(curr).desc:
                descr.append(P.font_s.render(x, True, (0, 0, 0)))
            for x in descr:
                P.surface.blit(x, (20, 290 + cngy))
                cngy += 34
            P.surface.blit(inbag,(680-inbag.get_width()/2,45))
        for event in pygame.event.get(eventtype = KEYDOWN):
            if event.key == pygame.key.key_code(P.controls[4]) and tim > 40:
                if curr == 'Quit':
                    end = False
                else:
                    pr = items.Item(curr).price
                    if curr in diff_price:
                        pr = int(pr*diff_price[0])
                    else:
                        pr = int(pr*price_mod)
                    if pr > P.save_data.money:
                        new_txt(P)
                        write(P,"You don't have enough money.")
                        cont(P)
                    else:
                        new_txt(P)
                        if stock == None:
                            write(P,curr + "? Certainly.", "How many would you like?")
                            num = choose_num(P,math.floor(P.save_data.money/pr))
                        else:
                            if stock[curr] != 0:
                                write(P,curr + "? Certainly.", "How many would you like?","In stock: "+str(stock[curr]))
                                num = choose_num(P,min(math.floor(P.save_data.money/pr),stock[curr]))
                            else:
                                write(P,curr + "? Sorry, but","those are out of stock.")
                                cont(P)
                                break
                        new_txt(P)
                        if num > 1:
                            sss = "s"
                        elif num == 0:
                            sss = "!"
                        else:
                            sss = ""
                        if sss != "!":
                            cost = num*pr
                            write(P,"You want " + str(num) + " " + curr + sss + ".","That will be $" + str(cost) + ".", "Is that OK?")
                            if choice(P,550,600) == True:
                                new_txt(P)
                                write(P,"Here you go.","Thank you.")
                                cont(P)
                                new_txt(P)
                                write(P,"You put away the " + curr + sss, "in the " + items.Item(curr).type[1] + " Pocket.")
                                cont(P)
                                P.save_data.money -= cost
                                if stock:
                                    stock[curr] -= num
                                money = P.font.render("$" + str(P.save_data.money),True,(0,0,0))
                                add_item(P,curr,num)
                                if curr == 'Poke Ball' and num >= 10:
                                    txt(P,"You also get a Premier Ball","as an added bonus.")
                                    add_item(P,"Premier Ball",1)
            if event.key == pygame.key.key_code(P.controls[5]) and tim > 40:
                end = False
        keys = pygame.key.get_pressed()
        if scroll % 70 == 0:
            su = False
            sd = False
        if keys[pygame.key.key_code(P.controls[0])] and scroll > 0 and sd == False and tim > 40:
            su = True
        if keys[pygame.key.key_code(P.controls[1])] and scroll < (len(shop) - 1) * 70 and su == False and tim > 40:
            sd = True
        if (su):
            scroll -= 10
        if (sd):
            scroll += 10
        tim += 1
        if my < 300:
            my += 10
        if by < 500:
            by += 20
        update_screen(P)
        P.clock.tick(P.ani_spd)
    end = True
    while end:
        P.surface.blit(back, (0, 0))
        P.surface.blit(mart, (0, -300 + my))
        P.surface.blit(shelf, (410, 633 - by))
        inc = 0
        for i in shop:
            txt0 = P.font_s.render(i, True, (0, 0, 0))
            P.surface.blit(box, (420, 643 - by + s + inc))
            P.surface.blit(txt0, (420 + (360 - (P.font_s.size(i)[0])) / 2, 658 + s - by + inc))
            inc += 70
        P.surface.blit(money, (160, -255 + my))
        P.surface.blit(wind, (400, 623 - by))
        if my > 0:
            my -= 10
        if by > 0:
            by -= 20
        if my == 0:
            end = False
        update_screen(P)
        P.clock.tick(P.ani_spd)
    if stock:
        return stock

def update_locs(P):
    # if P.prog[7] == 0 and P.loc == 'north_am':
    #     P.prog[7] += 1
    if P.prog[7] == 1 and P.loc == 'route_1':
        P.prog[7] += 1
    elif P.prog[7] == 2 and P.loc == 'egida':
        P.prog[7] += 1
    elif P.prog[7] == 3 and P.loc == 'route_2':
        P.prog[7] += 1
    elif P.prog[7] == 4 and P.loc == 'echo_cave':
        P.prog[7] += 1
    elif P.prog[7] == 5 and P.loc == 'vigore':
        P.prog[7] += 1
    elif P.prog[7] == 6 and P.loc == 'route_3':
        P.prog[7] += 1
    elif P.prog[7] == 7 and P.loc == 'scarab_l':
        P.prog[7] += 1
    elif P.prog[7] == 8 and P.loc == 'fiore':
        P.prog[7] += 1
    elif P.prog[7] == 9 and P.loc == 'scarab_r':
        P.prog[7] += 1
    elif P.prog[7] == 10 and P.loc == 'pianura':
        P.prog[7] += 1
    elif P.prog[7] == 11 and P.loc == 'mirror_cave':
        P.prog[7] += 1
    elif P.prog[7] == 12 and P.loc == 'route_4':
        P.prog[7] += 1
    elif P.prog[7] == 13 and P.loc == 'isola':
        P.prog[7] += 1
    elif P.prog[7] == 14 and P.loc == 'route_5':
        P.prog[7] += 1
    elif P.prog[7] == 15 and P.loc == 'verde':
        P.prog[7] += 1

def get_gondo(P,loc):
    if loc == 'South Alto Mare':
        P.loc = 'square_1'
        P.px = -875
        P.py = 1175
        P.p = P.l1
    if loc == 'North Alto Mare':
        P.loc = 'north_am'
        P.px = 25
        P.py = 1225
        P.p = P.r1
    if loc == 'Egida City':
        P.loc = 'egida_under'
        P.px = -1425
        P.py = 275
        P.p = P.r1
    if loc == 'Fiore Town':
        P.loc = 'fiore'
        P.px = -825
        P.py = 275
        P.p = P.r1
    if loc == 'Pianura City':
        P.loc = 'pianura'
        P.px = -525
        P.py = -525
        P.p = P.r1
    if loc == 'Isola Town':
        P.loc = 'isola'
        P.px = -1175
        P.py = 25
        P.p = P.l1
    if loc == 'Verde City':
        P.loc = 'verde'
        P.px = -1025
        P.py = 875
        P.p = P.l1

def gondolier(P):
    loc = get_location(P,True)
    cop = P.surface.copy()
    new_txt(P)
    write(P,f'Hi, I\'m the {loc}', "gondolier. Where would you", "like to go?")
    cont(P)
    fade_out(P)
    l = open_map(P)
    P.surface.blit(cop,(0,0))
    fade_in(P)
    if l != "":
        return l
    else:
        new_txt(P)
        write(P,"Let me know if you want to", "travel anywhere.")
        cont(P)
        return loc

def gondo_locs(P):
    list = ["South Alto Mare","North Alto Mare"]
    if P.prog[0] >= 48:
        list.append("Egida City")
    if P.prog[7] >= 9:
        list.append("Fiore Town")
    if P.prog[7] >= 11:
        list.append("Pianura City")
    if P.prog[7] >= 14:
        list.append("Isola Town")
    if P.prog[7] >= 16:
        list.append("Verde City")
    return list

def open_map(P,from_bag = False) -> None:
    pmap = load("p/map_1.png")
    if P.prog[7] >= 14:
        pmap = load("p/map_2.png")
    amn = load("p/am_n_mico.png")
    ams = load("p/am_s_mico.png")
    city_high = load("p/city_high.png")
    town_high = load("p/town_high.png")
    land_high = load("p/landmark_high.png")
    city_cover = load("p/city_cover.png")
    town_cover = load("p/town_cover.png")
    land_cover = load("p/landmark_cover.png")
    half_cover = load("p/half_cover.png")
    pointer = load("p/pointer.png")
    pox = 400
    poy = 300
    px = 0
    py = 0
    count = 0
    loc = get_location(P,True)
    l = loc
    loc_txt = P.font.render("Current: "+loc,True,(255,255,255))
    txtpos = P.font.size("Current: "+loc)
    if loc == "South Alto Mare":
        pox = 295
        poy = 510
    elif loc == "North Alto Mare":
        pox = 295
        poy = 490
    elif loc == 'Egida City':
        pox = 395
        poy = 415
    elif loc == 'Route 1':
        pox = 350
        poy = 452
    elif loc == 'Echo Cave':
        pox = 345
        poy = 365
    elif loc == 'Route 2':
        pox = 370
        poy = 390
    elif loc == 'Route 3':
        pox = 485
        poy = 412
    elif loc == 'Vigore Dam':
        pox = 375
        poy = 345
    elif loc == 'Scarab Woods':
        if P.loc == 'scarab_l':
            pox = 465
            poy = 435
        else:
            pox = 515
            poy = 430
        #add right side
    elif loc == 'Fiore Town':
        pox = 490
        poy = 455
    elif loc == 'Pianura City':
        pox = 580
        poy = 410
    elif loc == 'Mirror Cave':
        pox = 620
        poy = 390
    elif loc == 'Route 4':
        pox = 660
        poy = 340
    elif loc == 'Isola Town':
        pox = 700
        poy = 290
    elif loc == 'Route 5':
        pox = 675
        poy = 250
    elif loc == 'Verde City':
        pox = 640
        poy = 210
    P.surface.blit(pmap,(0,0))
    if P.prog[7] < 3:
        P.surface.blit(city_cover,(397,455))
    if P.prog[7] < 11:
        P.surface.blit(city_cover,(584,448))
    if P.prog[7] < 16:
        P.surface.blit(city_cover,(641,249))
    if P.prog[7] < 9:
        P.surface.blit(town_cover,(491,496))
    if P.prog[7] < 14:
        P.surface.blit(town_cover,(703,332))
    if P.prog[7] < 5:
        P.surface.blit(land_cover,(354,411))
    if P.prog[7] < 6:
        P.surface.blit(land_cover,(383,388))
    if P.prog[7] < 1:
        P.surface.blit(half_cover,(296,536))
    if P.prog[7] < 12:
        P.surface.blit(land_cover,(627,433))
    P.surface.blit(pointer,(pox,poy))
    fade_in(P)
    end = True
    a = 0
    while end:
        #print(pox,poy)
        P.surface.blit(pmap,(0,0))
        if pox > 275 and pox < 315 and poy > 470 and poy < 500 and P.prog[7] >= 1:
            P.surface.blit(amn,(296,536))
            l = "North Alto Mare"
        elif pox > 275 and pox < 315 and poy >= 500 and poy < 540:
            P.surface.blit(ams,(296,553))
            l = "South Alto Mare"
        elif pox > 375 and pox < 415 and poy >= 395 and poy < 435:
            if P.prog[7] >= 3:
                P.surface.blit(city_high,(397,455))
                l = "Egida City"
        elif pox > 555 and pox < 595 and poy >= 390 and poy < 430:
            if P.prog[7] >= 11:
                P.surface.blit(city_high,(584,448))
                l = "Pianura City"
        elif pox > 615 and pox < 655 and poy >= 190 and poy < 230:
            if P.prog[7] >= 16:
                P.surface.blit(city_high,(641,249))
                l = "Verde City"
        elif pox > 475 and pox < 505 and poy >= 440 and poy < 470:
            if P.prog[7] >= 9:
                P.surface.blit(town_high,(491,496))
                l = "Fiore Town"
        elif pox > 685 and pox < 715 and poy >= 275 and poy < 305:
            if P.prog[7] >= 14:
                P.surface.blit(town_high,(703,332))
                l = "Isola Town"
        elif pox > 605 and pox < 635 and poy >= 375 and poy < 405:
            if P.prog[7] >= 12:
                P.surface.blit(land_high,(627,433))
                l = "Mirror Cave"
        elif pox > 330 and pox < 360 and poy >= 350 and poy < 380:
            if P.prog[7] >= 5:
                P.surface.blit(land_high,(354,411))
                l = "Echo Cave"
        elif pox > 295 and pox < 395 and poy > 415 and poy < 490 and abs((0.75*(pox-295)) - ((800-poy)-310)) < 20 and P.prog[7] >= 2:
            l = "Route 1"
        elif pox > 345 and pox < 395 and poy > 365 and poy < 415 and abs((-1*(pox-390)) - ((800-poy)-385)) < 20 and P.prog[7] >= 4:
            l = "Route 2"
        elif pox > 395 and pox < 575 and poy < 425 and poy > 400 and abs((0.14*(pox-575)) - ((800-poy)-400)) < 20 and P.prog[7] >= 7:
            l = "Route 3"
        elif pox > 620 and pox < 700 and poy > 290 and poy < 390 and abs((1.25*(pox-620)) - ((800-poy)-410)) < 20 and P.prog[7] >= 13:
            l = "Route 4"
        elif pox > 640 and pox < 700 and poy > 210 and poy < 290 and abs((-1.3*(pox-700)) - ((800-poy)-510)) < 20 and P.prog[7] >= 15:
            l = "Route 5"
        elif pox > 440 and pox < 490 and poy > 420 and poy < 455 and abs((-0.7*(pox-490)) - ((800-poy)-345)) < 20 and P.prog[7] >= 8:
            l = "Scarab Woods"
        elif pox > 490 and pox < 525 and poy > 405 and poy < 455 and abs((1.4*(pox-490)) - ((800-poy)-345)) < 20 and P.prog[7] >= 10:
            l = "Scarab Woods"
        elif pox > 360 and pox < 390 and poy >= 330 and poy < 360 and P.prog[7] >= 6:
            P.surface.blit(land_high,(383,388))
            l = "Vigore Dam"
        else:
            l = ""
        if P.prog[7] < 1:
            P.surface.blit(half_cover,(296,536))
        if P.prog[7] < 3:
            P.surface.blit(city_cover,(397,455))
        if P.prog[7] < 11:
            P.surface.blit(city_cover,(584,448))
        if P.prog[7] < 16:
            P.surface.blit(city_cover,(641,249))
        if P.prog[7] < 9:
            P.surface.blit(town_cover,(491,496))
        if P.prog[7] < 14:
            P.surface.blit(town_cover,(703,332))
        if P.prog[7] < 5:
            P.surface.blit(land_cover,(354,411))
        if P.prog[7] < 6:
            P.surface.blit(land_cover,(383,388))
        if P.prog[7] < 12:
            P.surface.blit(land_cover,(627,433))
        if l == loc:
            if l == 'Scarab Woods':
                if (pox > 490 and P.loc == 'scarab_l') or (pox < 490 and P.loc == 'scarab_r'):
                    loc_txt = P.font.render(l,True,(255,255,255))
                    txtpos = P.font.size(l)
                else:
                    loc_txt = P.font.render("Current: "+l,True,(255,255,255))
                    txtpos = P.font.size("Current: "+l)
            else:
                loc_txt = P.font.render("Current: "+l,True,(255,255,255))
                txtpos = P.font.size("Current: "+l)
        else:
            loc_txt = P.font.render(l,True,(255,255,255))
            txtpos = P.font.size(l)
        P.surface.blit(pointer,(pox+px,poy+py))
        P.surface.blit(loc_txt,((800-txtpos[0])/2,5))
        for event in pygame.event.get(eventtype = KEYDOWN):
            if event.key == pygame.key.key_code(P.controls[4]) and a > 15 and from_bag == False:
                if l == loc:
                    txt(P,"You're already here!")
                elif l == "":
                    pass
                elif l not in gondo_locs(P):
                    txt(P,"You can't travel here!")
                else:
                    fade_out(P)
                    return l
            if event.key == pygame.key.key_code(P.controls[5]) and a > 15:
                fade_out(P)
                return ""
        keys = pygame.key.get_pressed()
        if keys[pygame.key.key_code(P.controls[3])] and a > 15 and pox < 730:
            pox += 4
        if keys[pygame.key.key_code(P.controls[2])] and a > 15 and pox > -5:
            pox -= 4
        if keys[pygame.key.key_code(P.controls[0])] and a > 15 and poy > 30:
            poy -= 4
        if keys[pygame.key.key_code(P.controls[1])] and a > 15 and poy < 540:
            poy += 4
        a += 1
        if count == 10:
            count = -10
        if a%3 == 0:
            count += 1
            px = abs(count)
            py = -abs(count)
        P.clock.tick(P.ani_spd)
        update_screen(P)
    fade_out(P)        

def play_music(P,song,repeat = -1):
    P.song = song
    pygame.mixer.music.load(P.song)
    set_mixer_volume(P,P.vol,P.song)
    pygame.mixer.music.play(repeat)

def draw_lamps(P,temppx,temppy,listx,listy,bf = "f"):
    iter = 0
    for x in range(len(listx)):
        if (bf == "f" and temppy+listy[iter]-275 > -120) or bf == "b":
            P.surface.blit(P.lamp,(temppx+listx[iter],temppy+listy[iter]))
        iter += 1
    if bf == "f":
        set_sky(P)
        if ((get_time() > 19 or get_time() < 6) or P.lighting == 'Night') and P.lighting != 'Day':
            iter = 0
            for x in range(len(listx)):
                P.surface.blit(P.light,(temppx+listx[iter]-30,temppy+listy[iter]))
                iter += 1

def draw_falls(P,fall,x,y,h):
    P.surface.set_clip((P.px+x,P.py+y,150,h))
    P.surface.blit(P.falls,(P.px+x,P.py+y+fall-150))
    P.surface.blit(P.falls,(P.px+x,P.py+y+fall))
    P.surface.blit(P.falls,(P.px+x,P.py+y+fall+150))
    P.surface.blit(P.falls,(P.px+x,P.py+y+fall+300))
    P.surface.set_clip((0,0,800,600))

def draw_waves(P,wx,wy):
    if P.graphic == 1:
        P.surface.fill((abs(P.ocean)+20,abs(P.ocean)+80,abs(P.ocean)+190))
    x = int(math.ceil((-P.px-800)/400)*400)
    y = int(math.ceil((-P.py-800)/400)*400)
    if P.graphic == 1:
        a = 400-wx
        b = 400-wy
        while a+x <= -400-P.px:
            a += 400
        while b+y <= -400-P.py:
            b += 400
        P.surface.blit(P.wave,(P.px+a+x,P.py+b+y+abs(P.foam)))
    a = wx
    b = wy
    while a+x <= -400-P.px:
        a += 400
    while b+y <= -400-P.py:
        b += 400
    P.surface.blit(P.wave,(P.px+a+x,P.py+b+y))

def draw_grass(P,px,py,x,y,w,h,temp = None,ignore = [],modx = 0,mody = 0,dark = False):
    a = x
    b = y
    if temp != None:
        temppx = px
        temppy = py
        px = 375-px
        py = 275-py
    while b > (y-h):
        while a > (x-w):
            if (py-b) < 50 and (py-b) >= 0 and (a,b) not in ignore:
                if((px-a < 50) and (px-a > -50)):
                    if temp != None:
                        if dark:
                            P.surface.blit(P.dark_grass,(px-a+temppx+temp[0]+modx,py-b+temppy+temp[1]-10+mody))
                        else:
                            P.surface.blit(P.grass,(px-a+temppx+temp[0]+modx,py-b+temppy+temp[1]-10+mody))
                    else:
                        if dark:
                            P.surface.blit(P.dark_grass,(px-a+375+modx,py-b+265+mody))
                        else:
                            P.surface.blit(P.grass,(px-a+375+modx,py-b+265+mody))
            a -= 50
        a = x
        b -= 50
    
def rect_draw(P,rects):
    for x in rects:
        pygame.draw.rect(P.surface,(60,60,60),x)

def load(image):
    return pygame.image.load(image).convert_alpha()

# def load_notrans(image):
#     return pygame.image.load(image).convert()

def get_time():
    #night
    #return 20
    #day
    #return 12
    return datetime.datetime.now().hour


def set_sky(P):
    hr = get_time()
    a = 0
    if P.lighting == 'Day':
        hr = 12
    if P.lighting == 'Night':
        hr = 21
    if hr < 9:
        for x in range(9-hr):
            if a < 150:
                a += 25
    elif hr > 16:
        for x in range(abs(16-hr)):
            if a < 150:
                a += 25
    if P.loc in ['egida_under','scarab_l','scarab_r','beedrill']:
        a += (200-a)/2
    if P.prog[0] >= 71 and P.prog[0] <= 74 and P.px >= -5000:
        mod = False
        if a < 100:
            mod = True
        a += (5000+min(P.px,-3925))/(7 + (a/15))
        if mod:
            if a < 100:
                a += 10+(5000+P.px)/40
            else:
                a += 25
    trans = pygame.Surface((800,600))
    trans.set_alpha(a)
    trans.fill((0,0,20))
    P.surface.blit(trans,(0,0))

def fade_in(P) -> None:
    P.surface.set_clip((0,0,800,600))
    temp = P.surface.copy()
    a = 256
    while a >= -10:
        trans = pygame.Surface((800,600))
        trans.set_alpha(a)
        trans.fill((0,0,0))
        P.surface.blit(temp,(0,0))
        P.surface.blit(trans,(0,0))
        a -= 10
        update_screen(P)
        P.clock.tick(P.ani_spd)
    pygame.event.clear()
        
def fade_out(P,song = None) -> None:
    P.surface.set_clip((0,0,800,600))
    temp = P.surface.copy()
    a = 0
    vol = P.vol
    while a <= 256:
        if song != None:
            set_mixer_volume(P,vol)
        trans = pygame.Surface((800,600))
        trans.set_alpha(a)
        trans.fill((0,0,0))
        P.surface.blit(temp,(0,0))
        P.surface.blit(trans,(0,0))
        vol -= P.vol/26
        a += 10
        update_screen(P)
        P.clock.tick(P.ani_spd)
    pygame.event.clear()

def npc_x_dist(P,npc):
    return npc.x + P.px - 375

def npc_y_dist(P,npc):
    return npc.y + P.py - 275

def load_rival(P) -> None:
    if P.save_data.gen == 1:
        txt = 'b'
    else:
        txt = 'g'
    P.nr1 = pygame.transform.scale(load("p/spr/rival_"+txt+"r1.png"),(50,60))
    P.nr2 = pygame.transform.scale(load("p/spr/rival_"+txt+"r2.png"),(50,60))
    P.nr3 = pygame.transform.scale(load("p/spr/rival_"+txt+"r3.png"),(50,60))
    P.nl1 = pygame.transform.scale(load("p/spr/rival_"+txt+"l1.png"),(50,60))
    P.nl2 = pygame.transform.scale(load("p/spr/rival_"+txt+"l2.png"),(50,60))
    P.nl3 = pygame.transform.scale(load("p/spr/rival_"+txt+"l3.png"),(50,60))
    P.nu1 = pygame.transform.scale(load("p/spr/rival_"+txt+"u1.png"),(50,60))
    P.nu2 = pygame.transform.scale(load("p/spr/rival_"+txt+"u2.png"),(50,60))
    P.nu3 = pygame.transform.scale(load("p/spr/rival_"+txt+"u3.png"),(50,60))
    P.nd1 = pygame.transform.scale(load("p/spr/rival_"+txt+"d1.png"),(50,60))
    P.nd2 = pygame.transform.scale(load("p/spr/rival_"+txt+"d2.png"),(50,60))
    P.nd3 = pygame.transform.scale(load("p/spr/rival_"+txt+"d3.png"),(50,60))

def load_npc(P,code) -> None:
    P.ncode = code
    P.nr1 = pygame.transform.scale(load("p/spr/"+code+"r1.png"),(50,60))
    P.nr2 = pygame.transform.scale(load("p/spr/"+code+"r2.png"),(50,60))
    P.nr3 = pygame.transform.scale(load("p/spr/"+code+"r3.png"),(50,60))
    P.nl1 = pygame.transform.scale(load("p/spr/"+code+"l1.png"),(50,60))
    P.nl2 = pygame.transform.scale(load("p/spr/"+code+"l2.png"),(50,60))
    P.nl3 = pygame.transform.scale(load("p/spr/"+code+"l3.png"),(50,60))
    P.nu1 = pygame.transform.scale(load("p/spr/"+code+"u1.png"),(50,60))
    P.nu2 = pygame.transform.scale(load("p/spr/"+code+"u2.png"),(50,60))
    P.nu3 = pygame.transform.scale(load("p/spr/"+code+"u3.png"),(50,60))
    P.nd1 = pygame.transform.scale(load("p/spr/"+code+"d1.png"),(50,60))
    P.nd2 = pygame.transform.scale(load("p/spr/"+code+"d2.png"),(50,60))
    P.nd3 = pygame.transform.scale(load("p/spr/"+code+"d3.png"),(50,60))

def next_to(P,x,y):
    return (P.py + y == 275 and ((P.px + x == 325 and face_l(P)) or (P.px + x == 425 and face_r(P)))) or (P.px + x == 375 and ((P.py + y == 225 and face_u(P)) or (P.py + y == 325 and face_d(P))))

def item_fight(P,music,num,lvl,moves,pokes,message = None):
    pp = []
    for m in moves:
        if m == None:
            pp.append(None)
        else:
            pp.append(-1)
    te = P.surface.copy()
    if message != None:
        txt(P,message)
    P.song = "music/wild_battle.wav"
    pygame.mixer.music.load(P.song)
    set_mixer_volume(P,P.vol)
    pygame.mixer.music.play(0)
    gen = random.randint(0,1)
    if pokes == 'Voltorb':
        gen = 2
    battle(P,[poke.Poke(pokes,[lvl,gen,334,moves[0],pp[0],moves[1],pp[1],moves[2],pp[2],moves[3],pp[3],None,None,0,"Poke Ball"])])
    P.prog[6][num] = 1
    play_music(P,music)
    P.surface.blit(te,(0,0))
    fade_in(P)

def face_r(P) -> bool:
    if P.p == P.r1 or P.p == P.r2 or P.p == P.r3:
        return True
    return False

def face_l(P) -> bool:
    if P.p == P.l1 or P.p == P.l2 or P.p == P.l3:
        return True
    return False

def face_u(P) -> bool:
    if P.p == P.u1 or P.p == P.u2 or P.p == P.u3:
        return True
    return False

def face_d(P) -> bool:
    if P.p == P.d1 or P.p == P.d2 or P.p == P.d3:
        return True
    return False

def in_party(P,name,live = False) -> bool:
    for x in P.party:
        if x.code_nos() == name and (live == False or x.status != 'Faint'):
            return True
    return False

def heal_party(P):
    for x in P.party:
        x.heal()        

def use_hs(P,poke):
    back = load("p/hs_back.png")
    if poke.code[-2:] == '_S':
        back = load("p/hs_back_S.png")
    front = load("p/hs_front.png")
    ball = pygame.transform.scale(load("p/"+poke.ball+".png"),(30,30))
    box = load("p/hs_move.png")
    name = P.font.render(poke.name,True,(255,255,255))
    name_size = P.font.size(poke.name)[0]
    mega = pygame.transform.scale(load("p/mega_symbol.png"),(30,30))
    nurse = pygame.transform.scale(load("p/nurse_icon.png"),(30,30))
    exp = load("p/summ_exp.png")
    high = load("p/high_move.png")
    desc = load("p/move_desc.png")
    use = False
    if poke.gen == 0:
        gen_i = load("p/boy_ico.png")
    if poke.gen == 1:
        gen_i = load("p/girl_ico.png")
    if poke.gen == 2:
        gen_i = load("p/blank.png")
    lvl = P.font.render("Lv."+str(poke.lvl),True,(255,255,255))
    type1 = load("p/"+poke.type[0]+"_ico.png")
    if poke.type[1] != None:
        type2 = load("p/"+poke.type[1]+"_ico.png")
    move_list = []
    for l in poke.moveset:
        if l == 1:
            for mve in poke.moveset[l]:
                move_list.append(mve)
        else:
            if poke.lvl >= l and poke.moveset[l] not in move_list:
                move_list.append(poke.moveset[l])
    scroll = 0
    scroll_spd = 10
    scroll_mod = 0
    a = 0
    end = True
    while end:
        P.surface.blit(back,(0,0))
        if poke.lvl != 100:
            P.surface.fill((0,0,255), Rect(64,110,int(320*(poke.exp/poke.get_exp())),10))
        else:
            P.surface.fill((0,0,255), Rect(64,110,320,10))
        P.surface.blit(exp,(10,105))
        P.surface.blit(ball,(18,18))
        P.surface.blit(name,(60,10))
        if poke.code[:5] == 'Mega_':
            P.surface.blit(mega,(65+name_size,20))
        if poke.nurse:
            P.surface.blit(nurse,(65+name_size,20))
        P.surface.blit(gen_i,(350,10))
        P.surface.blit(lvl,(20,50))
        # P.surface.blit(m4,(430,400))
        # P.surface.blit(mt4,(425,440))
        # P.surface.blit(mp4,(550,435))
        P.surface.blit(type1,(170,55))
        if poke.type[1] != None:
            P.surface.blit(type2,(280,55))
        y = 0
        if scroll <= 200:
            s = 0
        elif scroll >= (((len(move_list)-1)*100)-200):
            if len(move_list) < 6:
                s = 0
            else:
                s = (((len(move_list)-1)*100))-400
        else:
            s = scroll-200
        for mve in move_list:
            text = P.font.render(str(mve),True,(0,0,0))
            type = pygame.image.load("p/"+moves.Move(mve).type+"_ico.png")
            pp = P.font.render("PP "+str(moves.Move(mve).pp),True,(0,0,0))
            P.surface.blit(box,(410,50-s+y))
            P.surface.blit(text,(430,50-s+y))
            P.surface.blit(type,(425,95-s+y))
            P.surface.blit(pp,(550,90-s+y))
            #txt = P.font_s.render(z[0],True,(0,0,0))
            #P.surface.blit(text,(420+(360-(P.font_s.size(str(mve))[0]))/2,35-s+y))
            if mve == move_list[int(scroll/100)]:
                P.surface.blit(high,(410,50-s+y))
                curr = moves.Move(mve)
            y += 100
        P.surface.blit(front,(400,0))
        P.surface.blit(desc,(5,130))
        if curr.cat == '0':
            cat_ico = pygame.image.load("p/phy_ico.png")
        elif curr.cat == '1':
            cat_ico = pygame.image.load("p/spe_ico.png")
        else:
            cat_ico = pygame.image.load("p/sta_ico.png")
        cat = P.font.render("Category",True,(0,0,0))
        power = P.font.render("Power     "+curr.pow,True,(0,0,0))
        if int(float(curr.acc)*100) > 100:
            acc = P.font.render("Accuracy  ---",True,(0,0,0))
        else:
            acc = P.font.render("Accuracy  "+str(int(float(curr.acc)*100)),True,(0,0,0))
        descr = []
        cngy = 0
        for x in curr.desc:
            descr.append(P.font_s.render(x,True,(0,0,0)))
        for x in descr:
            P.surface.blit(x,(20,285+cngy))
            cngy += 34
        P.surface.blit(cat,(20,135))
        P.surface.blit(cat_ico,(270,140))
        P.surface.blit(power,(20,185))
        P.surface.blit(acc,(20,235))
        if scroll%100 == 0:
            for event in pygame.event.get(eventtype = KEYDOWN):
                if event.key == pygame.key.key_code(P.controls[4]) and a > 10:
                    new_txt(P)
                    write(P,'Teach ' + curr.name+"?")
                    if choice(P):
                        res = poke.learn(P,curr,False)
                        if res == True:
                            use = True
                            end = False
                        elif res == -1:
                            txt(P,poke.name+" already knows",curr.name+"!")
                            a = 1
                        else:
                            a = 1
                    else:
                        a = 1
                if event.key == pygame.key.key_code(P.controls[5]) and a > 10:
                    end = False
        keys = pygame.key.get_pressed()
        if scroll%100 == 0:
            su = False
            sd = False
        if keys[pygame.key.key_code(P.controls[0])] and scroll > 0 and sd == False:
            su = True
        if keys[pygame.key.key_code(P.controls[1])] and scroll < (len(move_list)-1)*100 and su == False:
            sd = True
        if(su):
            if scroll_mod > 50 and scroll_spd == 10:
                if scroll%100 == 0:
                    scroll_spd = 25
            if scroll_mod <= 50 and scroll_spd == 25:
                if scroll%100 == 0:
                    scroll_spd = 10
            scroll -= scroll_spd
            scroll_mod += 1
        elif(sd):
            if scroll_mod > 50 and scroll_spd == 10:
                if scroll%100 == 0:
                    scroll_spd = 25
            if scroll_mod <= 50 and scroll_spd == 25:
                if scroll%70 == 0:
                    scroll_spd = 10
            scroll += scroll_spd
            scroll_mod += 1
        else:
            scroll_mod = 0
        if a == 0:
            fade_in(P)
        a += 1
        P.clock.tick(P.ani_spd)
        update_screen(P)
    fade_out(P)
    return use

def wild_grass(P,x,y,w,h,pmod = 1,ignore = [],all = False) -> bool:
    #print(P.grass_prob)
    prob = P.grass_prob
    if P.party[0].item == 'Pure Incense':
        prob = P.grass_prob/3
    if P.moving and ((P.px <= x and P.px > x-w and P.py <= y and P.py > y-h) or all) and abs(P.px-25)%50 == 0 and abs(P.py-25)%50 == 0 and (P.px,P.py) not in ignore:
        if random.random() < prob*pmod:
            return True
        else:
            P.grass_prob += 0.002
    return False

def party_fainted(P):
    all_dead = True
    for x in P.party:
        if x.status != 'Faint':
            all_dead = False
    return all_dead

def reset_move_stat(P,poke):
    if poke.yawn == 1:
        poke.yawn = 2
    if poke.chrg == 1:
        poke.chrg = 2
    if poke.chrg == 2:
        poke.chrg = 0
    poke.can_sucker = False
    poke.child_hit = False
    if poke.cont_move != [None,0]:
        poke.cont_move[1] -= 1
        if poke.cont_move[1] == 0:
            if poke.cont_move[0] == 'Uproar':
                new_battle_txt(P)
                battle_write(P,poke.get_name()+" calmed","down.")
                P.clock.tick(P.bat_spd)
            poke.cont_move = [None,0]
        else:
            if poke.cont_move[0] == 'Uproar':
                new_battle_txt(P)
                battle_write(P,poke.get_name()+" is making","an uproar!")
                P.clock.tick(P.bat_spd)
    if poke.magic_coat:
        poke.magic_coat = False
    if poke.magnet_rise > 0:
        poke.magnet_rise -= 1
        if poke.magnet_rise == 0:
            new_battle_txt(P)
            battle_write(P,poke.get_name() + "'s","electromagnetism wore off!")
            P.clock.tick(P.bat_spd)
    poke.turn_count += 1
    poke.flinch = False
    poke.protect = False
    poke.spikyshield = False
    poke.endure = False
    if poke.roost == 1:
        poke.type[0] = 'Flying'
    if poke.roost == 2:
        poke.type[1] = 'Flying'
    poke.roost = 0
    poke.damage_taken = 0
    return poke

def blit_infobox(P,pokes,pokee):
    pokesname = P.font_s.render(pokes.name,True,(255,255,255))
    sname_size = P.font_s.size(pokes.name)[0]
    pokeename = P.font_s.render(pokee.name,True,(255,255,255))
    ename_size = P.font_s.size(pokee.name)[0]
    pokeslvl = P.font_s.render("Lv."+str(pokes.lvl),True,(255,255,255))
    pokeelvl = P.font_s.render("Lv."+str(pokee.lvl),True,(255,255,255))
    mega = pygame.transform.scale(load("p/mega_symbol.png"),(30,30))
    nurse = pygame.transform.scale(load("p/nurse_icon.png"),(30,30))
    boy = load("p/boy_ico.png")
    girl = load("p/girl_ico.png")
    expbar = load("p/summ_exp.png")
    infoboxs = load("p/battle_info_boxs.png")
    if pokes.code[-2:] == '_S':
        infoboxs = load("p/battle_info_boxs_S.png")
    infoboxe = load("p/battle_info_boxe.png")
    if pokee.code[-2:] == '_S':
        infoboxe = load("p/battle_info_boxe_S.png")
    P.surface.blit(infoboxs,(800-P.infospos,300))
    if pokes.gen == 0:
        P.surface.blit(boy,(855-P.infospos,310))
    elif pokes.gen == 1:
        P.surface.blit(girl,(855-P.infospos,310))
    P.surface.blit(pokesname,(900-P.infospos,315))
    if pokes.code[:5] == 'Mega_':
        P.surface.blit(mega,(905-P.infospos+sname_size,317))
    if pokes.nurse:
        P.surface.blit(nurse,(905-P.infospos+sname_size,317))
    P.surface.blit(pokeslvl,(830-P.infospos,380))
    P.surface.fill((255,255,255),Rect(850-P.infospos,425,350,10))
    if pokes.lvl != 100:
        P.surface.fill((0,0,255), Rect(874-P.infospos,425,int(320*(pokes.exp/pokes.get_exp())),10))
    else:
        P.surface.fill((0,0,255), Rect(874-P.infospos,425,320,10))
    P.surface.blit(expbar,(820-P.infospos,420))
    P.surface.blit(infoboxe,(-400+P.infoepos,100))
    if pokee.gen == 0:
        P.surface.blit(boy,(-395+P.infoepos,110))
    elif pokee.gen == 1:
        P.surface.blit(girl,(-395+P.infoepos,110))
    P.surface.blit(pokeename,(-350+P.infoepos,115))
    if pokee.code[:5] == 'Mega_':
        P.surface.blit(mega,(-345+P.infoepos+ename_size,117))
        ename_size += 30
    if pokee.code_nos() in P.save_data.pokedex and P.save_data.pokedex[pokee.code_nos()][0] == 1:
        P.surface.blit(P.caught_icon,(-340+P.infoepos+ename_size,120))
    P.surface.blit(pokeelvl,(-390+P.infoepos,155))

def blit_stat(P,pokes,pokee):
    xmod = 0
    if pokes.status != None:
        if pokes.code[:5] == 'Mega_' or pokes.nurse:
            xmod += 30
        sta = load("p/"+pokes.status+"_ico.png")
        sta = pygame.transform.scale(sta,(50,20))
        szn = P.font_s.size(pokes.name)
        P.surface.blit(sta,(910-P.infospos+szn[0]+xmod,322))
    if pokee.status != None:
        if pokee.code[:5] == 'Mega_':
            xmod += 30
        if pokee.code_nos() in P.save_data.pokedex and P.save_data.pokedex[pokee.code_nos()][0] == 1:
            xmod += 40
        sta = load("p/"+pokee.status+"_ico.png")
        sta = pygame.transform.scale(sta,(50,20))
        szn = P.font_s.size(pokee.name)
        P.surface.blit(sta,(-340+P.infoepos+szn[0]+xmod,122))

def blit_hp(P,pokes,pokee,main = False):
    hpbar = load("p/team_hp.png")
    hps = P.font_s.render(str(pokes.ch) + "/" + str(pokes.hp),True,(255,255,255))
    hpsze = P.font_s.size(str(pokes.ch) + "/" + str(pokes.hp))
    P.surface.blit(hps,(1120-P.infospos-hpsze[0],380))
    if pokes.ch/pokes.hp >= 0.5:
        P.surface.fill((0,255,0), Rect(984-P.infospos,365,int(200*(pokes.ch/pokes.hp)),10))
    elif pokes.ch/pokes.hp >= 0.25:
        P.surface.fill((255,255,0), Rect(984-P.infospos,365,int(200*(pokes.ch/pokes.hp)),10))
    else:
        P.surface.fill((255,50,0), Rect(984-P.infospos,365,int(200*(pokes.ch/pokes.hp)),10))
    P.surface.blit(hpbar,(940-P.infospos,360))
    if main == False:
        if pokee.ch/pokee.hp >= 0.5:
            P.surface.fill((0,255,0), Rect(-236+P.infoepos,165,int(200*(pokee.ch/pokee.hp)),10))
        elif pokee.ch/pokee.hp >= 0.25:
            P.surface.fill((255,255,0), Rect(-236+P.infoepos,165,int(200*(pokee.ch/pokee.hp)),10))
        else:
            P.surface.fill((255,50,0), Rect(-236+P.infoepos,165,int(200*(pokee.ch/pokee.hp)),10))
        P.surface.blit(hpbar,(-280+P.infoepos,160))

def battle_music_loop(P):
    if P.song == "music/trainer_battle.wav" and (pygame.mixer.music.get_pos() > 2680 or pygame.mixer.music.get_busy() == False):
        P.song = "music/trainer_battle_loop.wav"
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.play(-1)
    if P.song == "music/wild_battle.wav" and (pygame.mixer.music.get_pos() > 2650 or pygame.mixer.music.get_busy() == False):
        P.song = "music/wild_battle_loop.wav"
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.play(-1)
    if P.song == "music/steven_battle.wav" and (pygame.mixer.music.get_pos() > 2650 or pygame.mixer.music.get_busy() == False):
        P.song = "music/steven_battle_loop.wav"
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.play(-1)
    if P.song == "music/colress_battle.wav" and (pygame.mixer.music.get_pos() > 4696 or pygame.mixer.music.get_busy() == False):
        P.song = "music/colress_battle_loop.wav"
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.play(-1)
    if P.song == "music/fon_battle.wav" and (pygame.mixer.music.get_pos() > 2900 or pygame.mixer.music.get_busy() == False):
        P.song = "music/fon_battle_loop.wav"
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.play(-1)
    if P.song == "music/cheryl_battle.wav" and (pygame.mixer.music.get_pos() > 3450 or pygame.mixer.music.get_busy() == False):
        P.song = "music/cheryl_battle_loop.wav"
        pygame.mixer.music.load(P.song)
        pygame.mixer.music.play(-1)

def trainer_cutin(P,trainer):
    t_img = load("p/spr/"+trainer+"_battle.png")
    end = True
    tim = 0
    t = P.surface.copy()
    x_pos = 0
    while end:
        P.surface.blit(t,(0,0))
        P.surface.blit(t_img,(902-x_pos,0))
        if tim == 70:
            new_battle_txt(P)
            if trainer == 'Colress':
                battle_write(P,"Did you know certain Pokemon","can undergo unique evolutions?")
            elif trainer == 'Cheryl':
                battle_write(P,"I may be on my last Pokemon","but I'm far from finished!")
            P.clock.tick(P.bat_spd/2)
            end = False
        if tim < 65:
            x_pos += 6
        tim += 1
        P.clock.tick(P.ani_spd)
        update_screen(P)
    return x_pos

def has_shiny(pokes):
    if pokes.code+'_S_full.png' in os.listdir("p/poke"):
        return True
    return False
        

def battle(P,opp,no_pc = False) -> None:
    P.battle_weather = None
    P.battle_terrain = None
    if P.prog[0] == 75:
        P.battle_terrain = ['Electric',-1,load("p/terrain/Electric_Terrain.png")]
        P.battle_weather = ['Rain',-1]
    terrain_print = 0
    weather_print = 0
    #spikes toxic stealth sticky
    P.self_traps = [0,0,0,0]
    P.enemy_traps = [0,0,0,0]
    P.echoed = [0,0]
    P.grass_prob = 0.01
    P.turn_count = 0
    P.opponent = opp
    battle_type = 0
    if len(opp) > 1:
        #0 = wild, 1 = trainer
        battle_type = 1
    loop = 0
    t = P.surface.copy()
    end = True
    a = 0
    e = 0
    while end:
        while a <= 256 and e < 3:
            trans = pygame.Surface((800,600))
            trans.set_alpha(a)
            trans.fill((0,0,0))
            P.surface.blit(t,(0,0))
            P.surface.blit(trans,(0,0))
            a += 40
            P.clock.tick(P.ani_spd)
            update_screen(P)
        while a >= 0 and e < 3:
            trans = pygame.Surface((800,600))
            trans.set_alpha(a)
            trans.fill((0,0,0))
            P.surface.blit(t,(0,0))
            P.surface.blit(trans,(0,0))
            a -= 40
            P.clock.tick(P.ani_spd)
            update_screen(P)
        e += 1
        if e == 30:
            end = False
        P.clock.tick(P.ani_spd)
    P.surface.blit(t,(0,0))
    fade_out(P)
    fight = P.font.render("FIGHT",True,(0,0,0))
    bag = P.font.render("BAG",True,(0,0,0))
    pokemon = P.font.render("POKEMON",True,(0,0,0))
    run = P.font.render("RUN",True,(0,0,0))
    if P.habitat != None:
        day_night = ""
        if P.habitat in ['grass','forest','dock','road','path','beach','mount_grass','mount']:
            if ((get_time() > 19 or get_time() < 6) or P.lighting == 'Night') and P.lighting != 'Day':
                day_night = '_night'
            else:
                day_night = '_day'
        back = load("p/terrain/"+P.habitat+day_night+".png")
        plate = load("p/terrain/enemy_"+P.habitat+day_night+".png")
        plats = load("p/terrain/self_"+P.habitat+day_night+".png")
    else:
        back = load("p/terrain/indoor.png")
        plate = load("p/terrain/enemy_indoor.png")
        plats = load("p/terrain/self_indoor.png")
    if battle_type == 1:
        try:
            trainame = opp[0][:opp[0].index(' ')]
        except:
            if opp[0] == 'Steven':
                trainame = opp[0]
        if trainame == 'Leader':
            trainame = opp[0][7:]
        if trainame == 'Battle':
            trainame = 'Battle Girl'
        if trainame == 'Hex':
            trainame = 'Hex Maniac'
        elif trainame == 'Bug':
            trainame = opp[0][0:11]
        elif trainame == 'Rich':
            trainame = opp[0][0:8]
        elif trainame == 'Ace':
            trainame = opp[0][0:12]
            opp[0] = 'Ace Trainer' + opp[0][12:]
        elif trainame[0:6] == 'Expert':
            opp[0] = 'Expert' + opp[0][7:]
        elif opp[0] == 'Rival Hugh':
            trainame = 'Rivalb'
            opp[0] = 'Trainer Hugh'
        elif trainame == 'Team':
            trainame = opp[0][0:12]
            opp[0] = 'Team Rocket Grunt'
        elif trainame == 'Rocket':
            trainame = opp[0]+opp[1]
            opp[0] = 'Rocket Admin'
        elif opp[0] == 'Rival May':
            trainame = 'Rivalg'
            opp[0] = 'Trainer May'
        opp_ts = load("p/spr/"+trainame+"_battle.png")
        if trainame == 'Preschoolerb' or trainame == 'Preschoolerg':
            opp[0] = 'Preschooler' + opp[0][12:]
        if trainame == 'Scientistm' or trainame == 'Scientistf':
            opp[0] = 'Scientist' + opp[0][10:]
    box = load("p/battle_box.png")
    bare = load("p/team_list_bare.png")
    bars = load("p/team_list_bars.png")
    poke_ico = load("p/battle_poke_ico.png")
    poke_icof = load("p/battle_poke_icof.png")
    poke_icoe = load("p/battle_poke_icoe.png")
    cbox = load("p/battle_cbox.png")
    obox = load("p/battle_obox.png")
    hobox = load("p/battle_obox_high.png")
    oboxl = [hobox,obox,obox,obox]
    if P.save_data.gen == 0:
        ts1 = load("p/spr/boy_battle_1.png")
        ts2 = load("p/spr/boy_battle_2.png")
        ts3 = load("p/spr/boy_battle_3.png")
        ts = ts1
    if P.save_data.gen == 1:
        ts1 = load("p/spr/girl_battle_1.png")
        ts2 = load("p/spr/girl_battle_2.png")
        ts3 = load("p/spr/girl_battle_3.png")
        ts = ts1
    if battle_type == 1:
        pokee = opp[1]
        if pokee.code_nos() not in P.save_data.pokedex:
            P.save_data.pokedex[pokee.code_nos()] = [0,[]]
        pokemone = load("p/poke/"+pokee.code+"_bfw.png")
    else:
        pokee = opp[0]
        if battle_type == 0 and P.legendary_battle == False and P.tourney_battle == False and has_shiny(pokee) and random.random() < 0.02:
            pokee.code += '_S'
        loc = P.loc
        if P.loc == 'route_3' and P.habitat[:5] == 'beach':
            loc = "route_3b"
        if P.loc == 'route_5' and P.habitat[:5] == 'beach':
            loc = "route_5b"
        print(loc)
        if pokee.code_nos() not in P.save_data.pokedex:
            P.save_data.pokedex[pokee.code_nos()] = [0,[loc]]
        elif loc not in P.save_data.pokedex[pokee.code_nos()][1]:
            P.save_data.pokedex[pokee.code_nos()][1].append(loc)
        pokemone = load("p/poke/"+pokee.code+"_bf.png")
        pokemone = pygame.transform.scale(pokemone,(290,290))
    balle1 = load("p/spr/enemy_"+pokee.ball+"_1.png")
    balle2 = load("p/spr/enemy_"+pokee.ball+"_2.png")
    balle = balle1
    for x in P.party:
        if x.status != 'Faint':
            pokes = x
            break
    pokemons = load("p/poke/"+pokes.code+"_bbw.png")
    hpbar = load("p/team_hp.png")
    balls = load("p/spr/self_"+pokes.ball+".png")
    balls2 = balls
    opp_ball = []
    self_ball = []
    for x in opp:
        if type(x) != str:
            if x.status != 'Faint':
                opp_ball.append(poke_ico)
            else:
                opp_ball.append(poke_icof)
    for x in P.party:
        if x.status != 'Faint':
            self_ball.append(poke_ico)
        else:
            self_ball.append(poke_icof)
    while 0 < 6-len(opp_ball):
        opp_ball.append(poke_icoe)
    while 0 < 6-len(self_ball):
        self_ball.append(poke_icoe)
    P.surface.blit(back,(0,0))
    if P.battle_terrain != None:
        P.surface.blit(P.battle_terrain[2],(0,0))
    P.surface.blit(box,(0,460))
    fade_in(P)
    end = True
    spx = 0
    epx = 0
    barx = 0
    while end:
        battle_music_loop(P)
        P.surface.blit(back,(0,0))
        P.surface.blit(plate,(802-epx,200))
        P.surface.blit(plats,(-603+spx,360))
        if P.battle_terrain != None:
            P.surface.blit(P.battle_terrain[2],(0,0))
        P.surface.blit(ts,(-503+spx,260))
        P.surface.blit(box,(0,460))
        if battle_type == 1:
            P.surface.blit(opp_ts,(902-epx,0))
            P.surface.blit(bare,(-400+barx,200))
        else:
            P.surface.blit(pokemone,(857-epx,-36))
        P.surface.blit(bars,(800-barx,400))
        ballpos = 0
        if battle_type == 1:
            for x in opp_ball:
                P.surface.blit(x,(-60-ballpos+barx,140))
                ballpos += 60
        ballpos = 0
        for x in self_ball:
            P.surface.blit(x,(810+ballpos-barx,340))
            ballpos += 60
        if barx < 400:
            barx += 10
        if spx < 603:
            spx += 9
        else:
            end = False
        if epx < 402:
            epx += 6
        P.clock.tick(P.ani_spd/1.1)
        update_screen(P)
    end = True
    new_battle_txt(P)
    if P.legendary_battle:
        battle_write(P,f"{pokee.name} appeared!")
    elif battle_type == 1:
        battle_write(P,opp[0]+" would", "like to battle!")
    else:
        battle_write(P,f"A wild {pokee.name} appeared!")
    P.clock.tick(P.bat_spd)
    a = 0
    throws = -70
    throws2 = 280
    throwe = 0
    ex = epx
    sx = spx
    ballx = 0
    bally = 0
    ballx2 = 0
    bally2 = 0
    tourney_print = False
    sizee = 50
    sizes = 50
    whitepokemone = load("p/poke/"+pokee.code+"_bfw.png")
    origpokemone = pokemone
    origpokemons = pokemons
    high = 0
    ballsp = balls.get_rect()
    ballsp2 = balls2.get_rect()
    click = 0
    P.infospos = 0
    P.infoepos = 0
    new = pokes
    newe = pokee
    mvnum = 0
    turn = 0
    strug = moves.Move('Struggle')
    fainteds = 0
    faintede = 0
    turns1 = 1
    turne1 = 1
    trainer_cut = False
    barex = barx
    showbar = 0
    oppswcmv = None
    was_in = []
    P.poke_m = [1,-5]
    shakes = 0
    pokes.turn_count = 0
    pokee.turn_count = 0
    if P.legendary_battle:
        battle_type = 1
    while end:
        battle_music_loop(P)
        if a % 5 == 0:
            for x in range(2):
                if P.poke_m[x] > 0 and P.poke_m[x] < 5:
                    P.poke_m[x] += 1
                elif P.poke_m[x] < -1:
                    P.poke_m[x] += 1
                if P.poke_m[x] == 5:
                    P.poke_m[x] = -5
                if (x == 0 and a%100 == 0) or (x == 1 and (a-25) % 100 == 0):
                    if P.poke_m[x] == -1:
                        P.poke_m[x] = 1
        P.surface.blit(back,(0,0))
        P.surface.blit(plate,(802-epx,200))
        P.surface.blit(plats,(-603+spx,360))
        if P.battle_terrain != None:
            P.surface.blit(P.battle_terrain[2],(0,0))
        if battle_type == 1 and P.legendary_battle == False:
            P.surface.blit(opp_ts,(902-ex,0))
            P.surface.blit(bare,(-400+barex,200))
            ballpos = 360
            for x in opp_ball:
                P.surface.blit(x,(300-ballpos+barex,140))
                ballpos += 60
        elif throwe <= 40 and a<40:
            P.surface.blit(pokemone,(455,-36))
        P.surface.blit(ts,(-503+sx,260))
        P.surface.blit(bars,(800-barx,400))
        blit_infobox(P,pokes,pokee)
        ballpos = 360
        for x in self_ball:
            P.surface.blit(x,(450+ballpos-barx,340))
            ballpos += 60
        if throwe > 0 and throwe < 60 and battle_type == 1 and P.legendary_battle == False:
            P.surface.blit(balle,(575,155))
        P.animate_back = P.surface.copy()
        if throwe > -45 and throwe < 0:
            if sizee > 50:
                sizee -= 12
                pokemone = pygame.transform.scale(origpokemone,(sizee,sizee))
                P.surface.blit(pokemone,(600-(sizee/2),250-sizee))
        if throwe >= 40:
            if battle_type == 1 and P.legendary_battle == False:
                if sizee < 290:
                    sizee += 12
                    pokemone = pygame.transform.scale(origpokemone,(sizee,sizee))
                    if sizee > 289:
                        pokemone = pygame.transform.scale(load("p/poke/"+pokee.code+"_bf.png"),(sizee,sizee))
            elif throwe == 40:
                sizee = 290
            if (throws2 > 60 and throws2 < 80) and battle_type == 0:
                sizee -= 12
                pokemone = pygame.transform.scale(whitepokemone,(sizee,sizee))
            if (throws2 > 259 and throws2 < 279) and battle_type == 0:
                sizee += 12
                pokemone = pygame.transform.scale(whitepokemone,(sizee,sizee))
                if sizee > 289:
                    pokemone = pygame.transform.scale(load("p/poke/"+pokee.code+"_bf.png"),(sizee,sizee))
            if (battle_type == 1) or (battle_type == 0 and (throws2 <= 60 or throws2 >= 260)):
                P.surface.blit(pokemone,(600-(sizee/2),255-sizee-abs(P.poke_m[0])))
            elif throws2 <= 80:
                P.surface.blit(pokemone,(600-(sizee/2),110-(sizee/2)-abs(P.poke_m[0])))
        move_back = P.surface.copy()
        blit_stat(P,pokes,pokee)
        if P.infoepos <= 236:
            P.infoeposx = 0
        else:
            P.infoeposx = -236+P.infoepos
        if P.infoepos <= 236:
            P.infoeposs = (P.infoepos - 36)-(200-int(200*(pokee.ch/pokee.hp)))
        else:
            P.infoeposs = int(200*(pokee.ch/pokee.hp))
        blit_hp(P,pokes,pokee,True)
        if pokee.ch/pokee.hp >= 0.5:
            P.surface.fill((0,255,0), Rect(P.infoeposx,165,P.infoeposs,10))
        elif pokee.ch/pokee.hp >= 0.25:
            P.surface.fill((255,255,0), Rect(P.infoeposx,165,P.infoeposs,10))
        else:
            P.surface.fill((255,50,0), Rect(P.infoeposx,165,P.infoeposs,10))
        P.surface.blit(hpbar,(-280+P.infoepos,160))
        if throws > -60 and throws < -15:
            if sizes > 50:
                sizes -= 18
                pokemons = pygame.transform.scale(origpokemons,(sizes,sizes))
                P.surface.blit(pokemons,(200-(sizes/2),480-sizes))
        if throws > 45:
            if sizes < 410:
                sizes += 18
                pokemons = pygame.transform.scale(origpokemons,(sizes,sizes))
                if sizes > 409:
                    pokemons = pygame.transform.scale(load("p/poke/"+pokes.code+"_bb.png"),(sizes,sizes))
            P.surface.blit(pokemons,(200-(sizes/2),485-sizes-abs(P.poke_m[1])))
        if throws > 0 and throws < 40:
            P.surface.blit(balls,(90+ballx+ballsp[0],260+bally+ballsp[1]))
        if throws2 > 0 and (throws2 < 40 or (throws2 < 60 and battle_type == 1)):
            P.surface.blit(balls2,(-60+ballx2+ballsp2[0],265+bally2+ballsp2[1]))
        elif throws2 < 278 and battle_type == 0:
            P.surface.blit(balls2,(-55+ballx2+ballsp2[0],240+bally2+ballsp2[1]))
        #start of turn
        if P.infospos == 400 and throws == 50 and throwe == 70 and ((throws2 >= 65 and battle_type == 1) or (throws2 == 280 and battle_type == 0)):
            if pokee.ball == 'Nursery Ball' and pokee.code_nos() == 'Metapod' and P.turn_count == 3:
                P.turn_count += 1
                P.surface.set_clip((0,0,800,600))
                pokes.reset_stats()
                fade_out(P)
                return
            if pokee.ability == 'Dodge' and P.turn_count == 5:
                P.surface.set_clip((0,0,800,600))
                pokes.reset_stats()
                fade_out(P)
                return
            pokes.damage_taken = 0
            pokee.damage_taken = 0
            if turns1 == 1:
                use_ability1(P,pokes,pokee,1,move_back)
                turns1 = 0
            if turne1 == 1:
                use_ability1(P,pokee,pokes,0,move_back)
                turne1 = 0
            P.surface.set_clip((0,0,800,600))
            P.surface.blit(box,(0,460))
            P.surface.blit(cbox,(0,460))
            whatwill = P.font.render("What will",True,(0,0,0))
            xdo = P.font.render(pokes.name+" do?",True,(0,0,0))
            P.surface.blit(whatwill,(20,480))
            P.surface.blit(xdo,(20,530))
            P.surface.set_clip((0,0,800,460))
        #player fainted
        if throws == -15 and fainteds == 1:
            all_dead = party_fainted(P)
            opp_dead = True
            for x in opp:
                if type(x) != str and x.status != 'Faint':
                    opp_dead = False
            if all_dead == False:
                if opp_dead == False:
                    turns1 = 1
                    if battle_type == 0:
                        new_battle_txt(P)
                        battle_write(P,"Choose next Pokemon?")
                    new = choose_nxtpoke(P,pokes,battle_type,True,pokee)
                    if new == 1:
                        fade_out(P)
                        evo_check(P)
                        return 0
                    click = 0
                    fainteds = 0
            else:
                if not (pokee.code == 'Kangaskhan' and P.legendary_battle):
                    new_battle_txt(P)
                    battle_write(P,P.save_data.name + " is out of","Pokemon!")
                    P.clock.tick(P.bat_spd)
                    if battle_type == 0 or P.legendary_battle:
                        if no_pc == False:
                            new_battle_txt(P)
                            battle_write(P,P.save_data.name + " panicked and","dropped $"+str(calc_lost_money(P))+"!")
                            P.save_data.money -= calc_lost_money(P)
                            P.clock.tick(P.bat_spd)
                    else:
                        new_battle_txt(P)
                        battle_write(P,P.save_data.name + " lost against",opp[0]+"!")
                        P.clock.tick(P.bat_spd)
                        new_battle_txt(P)
                        if no_pc == False:
                            battle_write(P,P.save_data.name + " gave $"+str(calc_lost_money(P)),"to the winner!")
                            P.save_data.money -= calc_lost_money(P)
                            P.clock.tick(P.bat_spd)
                    new_battle_txt(P)
                    battle_write(P,P.save_data.name + " blacked out!")
                    P.clock.tick(P.bat_spd)
                fade_out(P,P.song)
                evo_check(P)
                P.double_money = False
                if no_pc:
                    return 0
                else:
                    print_blackout(P)
                    P.px = 125
                    P.py = -125
                    P.loc = P.save_data.pc
                    P.switch_locations()
        #opponent fainted
        if throwe == 0 and faintede == 1:
            all_dead = True
            gain_exp(P,pokes,pokee,was_in,battle_type)
            was_in = []
            pokeslvl = P.font_s.render("Lv."+str(pokes.lvl),True,(255,255,255))
            for x in opp:
                if type(x) != str:
                    if x.status != 'Faint':
                        newe = x
                        turne1 = 1
                        temp = pokes.copy()
                        if pokes.status != 'Faint':
                            if pokes.bide[0] > 0 or pokes.charge != None or pokes.rollcount > 0:
                                new = pokes
                            else:
                                new_battle_txt(P)
                                battle_write(P,opp[0] + " is about", "to send in " + newe.name + '!')
                                P.clock.tick(P.bat_spd)
                                new_battle_txt(P)
                                battle_write(P,"Will " + P.save_data.name + " change", "Pokemon?")
                                new = choose_nxtpoke(P,pokes,1.5)
                        faintede = 0
                        if new.equals(temp) == False:
                            new.turn_count = -1
                            pokes.reset_stats()
                            if pokes.ch != 0:
                                if temp.status != pokes.status and pokes.ability == 'Natural Cure':
                                    new_battle_txt(P)
                                    battle_write(P,pokes.get_name() + " cured", "itself of status effects!")
                                    show_ability(P,'Natural Cure',1)
                                new_battle_txt(P)
                                battle_write(P,pokes.get_name() + ', that\'s', 'enough!')
                                P.clock.tick(P.bat_spd)
                            oboxl[high] = obox
                            turns1 = 1
                            high = 0
                            oboxl[0] = hobox
                            mvnum = 0
                            throws = -60
                            ballx = 0
                            bally = 0
                            throwe = -150
                        showbar = 0
                        all_dead = False
                        break
            if (all_dead):
                temp = pokes.copy()
                pokes.reset_stats()
                if temp.status != pokes.status and pokes.ability == 'Natural Cure':
                    new_battle_txt(P)
                    battle_write(P,pokes.get_name() + " cured", "itself of status effects!")
                    show_ability(P,'Natural Cure',1)
                if battle_type == 1 and P.legendary_battle == False:
                    new_battle_txt(P)
                    battle_write(P,P.save_data.name + " defeated",opp[0]+"!")
                    P.clock.tick(P.bat_spd)
                    new_battle_txt(P)
                    battle_write(P,opp[0] + " paid $" + str(calc_prize(P,opp)), "as the prize money!")
                    P.clock.tick(P.bat_spd)
                    P.save_data.money += calc_prize(P,opp)
                fade_out(P,P.song)
                evo_check(P)
                P.double_money = False
                return 0
        #top part battle
        if P.infospos == 400 and throws == 50 and throwe == 70 and ((throws2 >= 65 and battle_type == 1) or (throws2 == 280 and battle_type == 0)):
            if P.turn_count == 0 and P.tourney_battle and tourney_print == False:
                new_battle_txt(P)
                battle_write(P,"The battle is looking intense!")
                P.clock.tick(P.bat_spd)
                tourney_print = True
            if weather_print == P.turn_count:
                if P.battle_weather != None and P.battle_weather[0] == 'Rain':
                    P.battle_weather[1] -= 1
                    new_battle_txt(P)
                    if P.battle_weather[1] == 0:
                        battle_write(P,"The rain stopped.")
                        P.clock.tick(P.bat_spd)
                        P.battle_weather = None
                    elif weather_print == 0:
                        battle_write(P,"It is raining!")
                    else:
                        battle_write(P,"Rain continues to fall.")
                    if P.battle_weather != None:
                        if P.ani_on:
                            rain_temp = P.surface.copy()
                            rain_val = 0
                            for r in range(60):
                                P.surface.blit(rain_temp,(0,0))
                                blit_rain(P,rain_val)
                                update_screen(P)
                                P.clock.tick(P.ani_spd)
                                rain_val += 1
                                if rain_val == 40:
                                    rain_val = -20
                        else:
                            P.clock.tick(P.bat_spd)
                weather_print += 1
            if terrain_print == P.turn_count:
                if P.battle_terrain != None and P.battle_terrain[0] == 'Electric':
                    P.battle_terrain[1] -= 1
                    new_battle_txt(P)
                    if P.battle_terrain[1] == 0:
                        battle_write(P,"The electricity disappeared", "from the battlefield!")
                        P.battle_terrain = None
                    else:
                        battle_write(P,"An electric current is running","across the battlefield!")
                    P.clock.tick(P.bat_spd)
                terrain_print += 1
            if turn == 1:
                orige = pokee.copy()
                origs = pokes.copy()
                if oppswcmv == strug and pokee.bide == [0,0] and pokee.rollcount == 0 and pokee.charge == False:
                    new_battle_txt(P)
                    battle_write(P,pokee.get_name() +" is out of", "moves!")
                    P.clock.tick(P.bat_spd)
                eff = oppswcmv.cast(P,pokee,pokes,choose)
                battle_move_use(P,origs,orige,pokes,pokee,move_back,eff,1)
                count = eff[4]
                if oppswcmv.name == 'Metronome':
                    oppswcmv = moves.Move(P.metronome)
                for x in range(count):
                    if pokes.ch == 0 or pokee.ch == 0:
                        break
                    eff = oppswcmv.use(P,pokee,pokes,1)
                    battle_move_use(P,origs,orige,pokes,pokee,move_back,eff,x+2)
                if count != 0 and pokes.ch != 0 and pokee.ch != 0:
                    new_battle_txt(P)
                    battle_write(P,"Hit " + str(count+1) + " times!")
                    P.clock.tick(P.bat_spd)
                P.gem_active = False
                EOT_effects(P,pokes,pokee,0,move_back)
                EOT_effects(P,pokee,pokes,1,move_back)
                P.turn_count += 1
                pokes = reset_move_stat(P,pokes)
                pokee = reset_move_stat(P,pokee)
                if P.echoed[1] == 1:
                    P.echoed = [0,0]
                if P.echoed[1] != 0:
                    P.echoed[1] -= 1
                if pokes.status == 'Faint':
                    oboxl[high] = obox
                    high = 0
                    oboxl[0] = hobox
                    mvnum = 0
                    throws = -60
                    ballsp = balls.get_rect()
                    ballx = 0
                    bally = 0
                    fainteds = 1
                if pokee.status == 'Faint':
                    all_dead = True
                    for x in opp:
                        if type(x) != str:
                            if x.status != 'Faint':
                                all_dead = False
                    if all_dead == False:
                        opp_ball = []
                        for x in opp:
                            if type(x) != str:
                                if x.status != 'Faint':
                                    opp_ball.append(poke_ico)
                                else:
                                    opp_ball.append(poke_icof)
                        while 0 < 6-len(opp_ball):
                            opp_ball.append(poke_icoe)
                        showbar = 1
                    throwe = -45
                    balle = balle1
                    faintede = 1
                turn = 0
            else:
                use_move = False
                if pokes.bide[0] > 0:
                    use_x(P,pokes,pokee,move_back,moves.Move('Bide'))
                    use_move = True
                elif pokes.charge != None:
                    use_x(P,pokes,pokee,move_back,moves.Move(pokes.charge))
                    use_move = True
                elif pokes.rollcount > 0:
                    use_x(P,pokes,pokee,move_back,moves.Move('Rollout'))
                    use_move = True
                elif pokes.cont_move[1] > 0:
                    use_x(P,pokes,pokee,move_back,moves.Move(pokes.cont_move[0]))
                    use_move = True
                if use_move:
                    click = 0
                    if pokes.status == 'Faint':
                        oboxl[high] = obox
                        high = 0
                        oboxl[0] = hobox
                        mvnum = 0
                        throws = -60
                        ballsp = balls.get_rect()
                        ballx = 0
                        bally = 0
                        fainteds = 1
                    if pokee.status == 'Faint':
                        all_dead = True
                        for x in opp:
                            if type(x) != str:
                                if x.status != 'Faint':
                                    all_dead = False
                        if all_dead == False:
                            opp_ball = []
                            for x in opp:
                                if type(x) != str:
                                    if x.status != 'Faint':
                                        opp_ball.append(poke_ico)
                                    else:
                                        opp_ball.append(poke_icof)
                            while 0 < 6-len(opp_ball):
                                opp_ball.append(poke_icoe)
                            showbar = 1
                        throwe = -45
                        balle = balle1
                        faintede = 1
                else:
                    P.surface.set_clip((400,460,400,140))
                    P.surface.blit(box,(0,460))
                    P.surface.blit(oboxl[0],(400,460))
                    P.surface.blit(oboxl[1],(600,460))
                    P.surface.blit(oboxl[2],(400,530))
                    P.surface.blit(oboxl[3],(600,530))
                    P.surface.blit(fight,(440,473))
                    P.surface.blit(bag,(664,473))
                    P.surface.blit(pokemon,(415,543))
                    P.surface.blit(run,(664,543))
                    P.surface.set_clip((0,0,800,460))
                #key presses
                for event in map_keys():
                    if event.type == KEYDOWN and click > 15:
                        if event.key == pygame.key.key_code(P.controls[4]):
                            #battle
                            if high == 0:
                                #use struggle
                                if (pokes.p1 == 0 or pokes.p1 == None or (moves.Move(pokes.m1).cat == '2' and pokes.taunt != 0)) and (pokes.p2 == 0 or pokes.p2 == None or (moves.Move(pokes.m2).cat == '2' and pokes.taunt != 0)) and (pokes.p3 == 0 or pokes.p3 == None or (moves.Move(pokes.m3).cat == '2' and pokes.taunt != 0)) and (pokes.p4 == 0 or pokes.p4 == None or (moves.Move(pokes.m4).cat == '2' and pokes.taunt != 0)):
                                    use_x(P,pokes,pokee,move_back,strug)
                                    click = 0
                                #use other moves
                                else:
                                    #pick move
                                    pm_ret = pick_move(P,pokes,pokee,mvnum,move_back,pokemone,pokemons,sizes,sizee,a)
                                    mvnum = pm_ret[0]
                                    a = pm_ret[1]
                                    click = 0
                                if pokes.status == 'Faint':
                                    oboxl[high] = obox
                                    high = 0
                                    oboxl[0] = hobox
                                    mvnum = 0
                                    throws = -60
                                    ballsp = balls.get_rect()
                                    ballx = 0
                                    bally = 0
                                    fainteds = 1
                                if pokee.status == 'Faint':
                                    all_dead = True
                                    for x in opp:
                                        if type(x) != str:
                                            if x.status != 'Faint':
                                                all_dead = False
                                    if all_dead == False:
                                        opp_ball = []
                                        for x in opp:
                                            if type(x) != str:
                                                if x.status != 'Faint':
                                                    opp_ball.append(poke_ico)
                                                else:
                                                    opp_ball.append(poke_icof)
                                        while 0 < 6-len(opp_ball):
                                            opp_ball.append(poke_icoe)
                                        showbar = 1
                                    throwe = -45
                                    balle = balle1
                                    faintede = 1
                                click = 0
                            #bag
                            if high == 1:
                                if P.tourney_battle:
                                    new_battle_txt(P)
                                    battle_write(P,"You can't use items!")
                                    cont(P)
                                else:
                                    P.surface.set_clip((0,0,800,600))
                                    t = P.surface.copy()
                                    fade_out(P)
                                    ittar = battle_bag(P)
                                    click = 0
                                    it = ittar[0]
                                    tar = ittar[1]
                                    P.surface.blit(t,(0,0))
                                    fade_in(P)
                                    if it != '':
                                        item = items.Item(it)
                                        if item.type[0] == 'Ball':
                                            if battle_type == 0:
                                                add_item(P,item.name,-1)
                                            balls2 = load("p/spr/self_"+item.name+".png")
                                            ballsp2 = balls2.get_rect()
                                            ballx2 = 0
                                            bally2 = 0
                                            throws2 = 0
                                            click = 0
                                            new_battle_txt(P)
                                            battle_write(P,P.save_data.name + " used "+item.aan(), item.name + '!')
                                            P.surface.set_clip((0,0,800,460))
                                        if item.type[0] == 'Potion' or item.name == 'Sitrus Berry' or item.name == 'Oran Berry':
                                            new_battle_txt(P)
                                            battle_write(P,P.save_data.name + " used "+item.aan(), item.name + '!')
                                            P.clock.tick(P.bat_spd)
                                            new_battle_txt(P)
                                            battle_write(P,tar.name + "'s HP was", 'restored!')
                                            P.clock.tick(P.bat_spd)
                                            add_item(P,item.name,-1)
                                            print(pokes.same(tar))
                                            if pokes.same(tar):
                                                ori = pokes.copy()
                                                heal = item.mod()
                                                if item.name == 'Sitrus Berry':
                                                    heal = int(pokes.hp/4)
                                                pokes.ch += heal
                                                if pokes.ch > pokes.hp:
                                                    pokes.ch = pokes.hp
                                                hp_change(P,ori,pokee,pokes,pokee,move_back)
                                            else:
                                                heal = item.mod()
                                                if item.name == 'Sitrus Berry':
                                                    heal = int(tar.hp/4)
                                                tar.ch += heal
                                                if tar.ch > tar.hp:
                                                    tar.ch = tar.hp
                                            use_x(P,pokes,pokee,move_back,1)
                                        if item.type[0] == 'Battle Berry' and (type(item.mod()) == list and tar.status in item.mod()[0]) or ((item.name == 'Lum Berry' or item.name == 'Persim Berry') and tar.cfs > 0):
                                            new_battle_txt(P)
                                            battle_write(P,P.save_data.name + " used "+item.aan(), item.name + '!')
                                            P.clock.tick(P.bat_spd)
                                            add_item(P,item.name,-1)
                                            new_battle_txt(P)
                                            s = item.mod()[0][0]
                                            if item.name == 'Lum Berry':
                                                if tar.cfs > 0:
                                                    tar.cfs = 0
                                                    battle_write(P,tar.name + " was cured", "of confusion!")
                                                    if tar.status != None:
                                                        P.clock.tick(P.bat_spd)
                                                        new_battle_txt(P)
                                                s = tar.status
                                            if s == None:
                                                pass
                                            elif s == 'Slp':
                                                battle_write(P,tar.name + " woke up!")
                                            elif s == 'Frz':
                                                battle_write(P,tar.name + " thawed","out!")
                                            elif s == 'Brn':
                                                battle_write(P,tar.name + " burn was","healed!")
                                            else:
                                                sta = item.mod()[1]
                                                if item.name == 'Lum Berry':
                                                    if s == 'Par':
                                                        sta = 'Paralysis'
                                                    else:
                                                        sta = 'Poisoning'
                                                battle_write(P,tar.name + " was cured", "of "+sta+"!")
                                            P.clock.tick(P.bat_spd)
                                            if item.name == 'Persim Berry':
                                                tar.cfs = 0
                                            else:
                                                tar.status = None
                                            use_x(P,pokes,pokee,move_back,1)
                            #pokemon
                            if high == 2:
                                P.surface.set_clip((0,0,800,600))
                                t = P.surface.copy()
                                fade_out(P)
                                new = battle_team(P,pokes,0,pokee)
                                click = 0
                                temp = pokes.copy()
                                if new != pokes:
                                    new.turn_count = -1
                                    balls = load("p/spr/self_"+new.ball+".png")
                                    ballsp = balls.get_rect()
                                    if pokes not in was_in:
                                        if pokes.item == 'Luck Incense':
                                            P.double_money = True
                                        was_in.append(pokes)
                                    pokes.reset_stats()
                                    oboxl[high] = obox
                                    high = 0
                                    oboxl[0] = hobox
                                    mvnum = 0
                                    throws = -60
                                    ballx = 0
                                    bally = 0
                                    turns1 = 1
                                    P.surface.blit(t,(0,0))
                                    fade_in(P)
                                    if pokes.ch != 0:
                                        if temp.status != pokes.status and pokes.ability == 'Natural Cure':
                                            new_battle_txt(P)
                                            battle_write(P,pokes.name + " cured itself", "of status effects!")
                                            show_ability(P,'Natural Cure',1)
                                        new_battle_txt(P)
                                        battle_write(P,pokes.name+", that\'s enough!")
                                        P.clock.tick(P.bat_spd)
                                    move_l = []
                                    if pokee.m1 != None and pokee.p1 > 0:
                                        if pokee.taunt == 0 or moves.Move(pokee.m1).cat != '2':
                                            move_l.append(moves.Move(pokee.m1))
                                    if pokee.m2 != None and pokee.p2 > 0:
                                        if pokee.taunt == 0 or moves.Move(pokee.m2).cat != '2':
                                            move_l.append(moves.Move(pokee.m2))
                                    if pokee.m3 != None and pokee.p3 > 0:
                                        if pokee.taunt == 0 or moves.Move(pokee.m3).cat != '2':
                                            move_l.append(moves.Move(pokee.m3))
                                    if pokee.m4 != None and pokee.p4 > 0:
                                        if pokee.taunt == 0 or moves.Move(pokee.m4).cat != '2':
                                            move_l.append(moves.Move(pokee.m4))
                                    if len(move_l) == 0:
                                        choose = -1
                                        oppswcmv = strug
                                    else:
                                        choose = random.randint(0,len(move_l)-1)
                                        oppswcmv = move_l[choose]
                                    orige = pokee.copy()
                                    origs = pokes.copy()
                                    if oppswcmv.name == 'Pursuit':
                                        pokee.pursuit = True
                                        eff = oppswcmv.cast(P,pokee,pokes,choose)
                                        battle_move_use(P,origs,orige,pokes,pokee,move_back,eff)
                                        pokee.pursuit = False
                                    else:
                                        turn = 1
                                    click = 0
                                else:
                                    P.surface.blit(t,(0,0))
                                    fade_in(P)
                                    P.surface.set_clip((0,0,800,460))
                            #run
                            if high == 3:
                                if P.legendary_battle:
                                    new_battle_txt(P)
                                    battle_write(P,"Your escape route has been", "cut off!")
                                    cont(P)
                                elif battle_type == 1:
                                    new_battle_txt(P)
                                    battle_write(P,"There's no running from a", "Trainer battle!")
                                    cont(P)
                                elif ((pokee.ability == 'Shadow Tag' and pokes.ability != 'Shadow Tag' and 'Ghost' not in pokes.type) or (pokee.ability == 'Arena Trap' and pokes.ability != 'Levitate' and pokes.magnet_rise == 0 and 'Flying' not in pokes.type) or (pokee.ability == 'Magnet Pull' and 'Steel' in pokes.type) or (pokes.trapped[1] != 0)) and (pokes.ability != 'Run Away' or 'Ghost' in pokes.type):
                                    new_battle_txt(P)
                                    battle_write(P,pokes.name + " is trapped!")
                                    show_ability(P,pokee.ability,0)
                                    cont(P)
                                elif battle_type == 0:
                                    if use_x(P,pokes,pokee,move_back,0) == 1:
                                        temp = pokes.copy()
                                        pokes.reset_stats()
                                        if temp.status != pokes.status and pokes.ability == 'Natural Cure':
                                            new_battle_txt(P)
                                            battle_write(P,pokes.name + " cured itself", "of status effects!")
                                            show_ability(P,'Natural Cure',1)
                                        fade_out(P)
                                        evo_check(P)
                                        return 0
                                    click = 0
                                    if pokes.status == 'Faint':
                                        oboxl[high] = obox
                                        high = 0
                                        oboxl[0] = hobox
                                        mvnum = 0
                                        throws = -60
                                        ballsp = balls.get_rect()
                                        ballx = 0
                                        bally = 0
                                        fainteds = 1
                                    if pokee.status == 'Faint':
                                        all_dead = True
                                        for x in opp:
                                            if type(x) != str:
                                                if x.status != 'Faint':
                                                    all_dead = False
                                        if all_dead == False:
                                            opp_ball = []
                                            for x in opp:
                                                if type(x) != str:
                                                    if x.status != 'Faint':
                                                        opp_ball.append(poke_ico)
                                                    else:
                                                        opp_ball.append(poke_icof)
                                            while 0 < 6-len(opp_ball):
                                                opp_ball.append(poke_icoe)
                                            showbar = 1
                                        throwe = -45
                                        balle = balle1
                                        faintede = 1
                        elif event.key == pygame.key.key_code(P.controls[0]) and high > 1:
                            high -= 2
                            oboxl[high+2] = obox
                            oboxl[high] = hobox
                        elif event.key == pygame.key.key_code(P.controls[1]) and high < 2:
                            high += 2
                            oboxl[high-2] = obox
                            oboxl[high] = hobox
                        elif event.key == pygame.key.key_code(P.controls[2]) and high%2 == 1:
                            high -= 1
                            oboxl[high+1] = obox
                            oboxl[high] = hobox
                        elif event.key == pygame.key.key_code(P.controls[3]) and high%2 == 0:
                            high += 1
                            oboxl[high-1] = obox
                            oboxl[high] = hobox
            click += 1
        #bottom part battle
        if throwe == 40:
            balle = balle2
        if a == 50:
            ts = ts2
        #enemy send pokemon
        if throwe == 0 and battle_type == 1 and P.legendary_battle == False:
            if newe.code_nos() not in P.save_data.pokedex:
                P.save_data.pokedex[newe.code_nos()] = [0,[]]
            if newe.code_nos() == "Mega_Mawile" and opp[0] == "Leader Colress":
                ex = trainer_cutin(P,"Colress")
                trainer_cut = True
            if newe.code_nos() == "Mega_Audino" and opp[0] == "Leader Cheryl":
                ex = trainer_cutin(P,"Cheryl")
                trainer_cut = True
            pokee = newe
            pokeelvl = P.font_s.render("Lv."+str(pokee.lvl),True,(255,255,255))
            pokeename = P.font_s.render(pokee.name,True,(255,255,255))
            pokemone = load("p/poke/"+pokee.code+"_bfw.png")
            balle1 = load("p/spr/enemy_"+pokee.ball+"_1.png")
            balle2 = load("p/spr/enemy_"+pokee.ball+"_2.png")
            balle = balle1
            origpokemone = pokemone
            P.surface.set_clip((0,0,800,600))
            new_battle_txt(P)
            battle_write(P,opp[0] + " sent out ", pokee.name+"!")
            P.clock.tick(P.bat_spd)
        if throws == -15:
            pokes = new
            pokeslvl = P.font_s.render("Lv."+str(pokes.lvl),True,(255,255,255))
            pokesname = P.font_s.render(pokes.name,True,(255,255,255))
            pokemons = load("p/poke/"+pokes.code+"_bbw.png")
            balls = load("p/spr/self_"+pokes.ball+".png")
            ballsp = balls.get_rect()
            origpokemons = pokemons
            P.surface.set_clip((0,0,800,600))
            new_battle_txt(P)
            battle_write(P,"Go "+pokes.name+"!")
        if a == 70:
            ts = ts3
        if throwe < 70:
            throwe += 1
        if throws < 50:
            throws += 1
        if throws2 < 280:
            throws2 += 1
        if throws2 == 255 and battle_type == 0:
            new_battle_txt(P)
            battle_write(P,"Gotcha! " + pokee.name + " was caught!")
            P.clock.tick(P.bat_spd)
            pokee.ball = item.name
            get_poke(P,pokee)
            gain_exp(P,pokes,pokee,was_in,battle_type)
            temp = pokes.copy()
            pokes.reset_stats()
            if temp.status != pokes.status and pokes.ability == 'Natural Cure':
                new_battle_txt(P)
                battle_write(P,pokes.name + " cured itself", "of status effects!")
                show_ability(P,'Natural Cure',1)
            fade_out(P)
            evo_check(P)
            return 0
        if (throws2 == 61 and battle_type == 1) or (throws2 == 279 and battle_type == 0):
            new_battle_txt(P)
            if P.legendary_battle:
                battle_write(P,pokee.get_name()+" blocked", "your Poke Ball!")
                cont(P)
            elif battle_type == 1:
                battle_write(P,"The trainer blocked your Poke", "Ball!")
                cont(P)
                new_battle_txt(P)
                battle_write(P,"Dont\'t be a thief!")
                cont(P)
            elif battle_type == 0:
                if shakes == 0:
                    battle_write(P,"Oh no! The Pokemon broke free!")
                elif shakes == 1:
                    battle_write(P,"Aww! It appeared to be caught!")
                elif shakes == 2:
                    battle_write(P,"Aargh! Almost had it!")
                else:
                    battle_write(P,"Gah! It was so close, too!")
                cont(P)
            use_x(P,pokes,pokee,move_back,1)
            click = 0
            if pokes.status == 'Faint':
                oboxl[high] = obox
                high = 0
                oboxl[0] = hobox
                mvnum = 0
                throws = -60
                ballsp = balls.get_rect()
                ballx = 0
                bally = 0
                fainteds = 1
            if pokee.status == 'Faint':
                all_dead = True
                for x in opp:
                    if type(x) != str:
                        if x.status != 'Faint':
                            all_dead = False
                if all_dead == False:
                    opp_ball = []
                    for x in opp:
                        if type(x) != str:
                            if x.status != 'Faint':
                                opp_ball.append(poke_ico)
                            else:
                                opp_ball.append(poke_icof)
                    while 0 < 6-len(opp_ball):
                        opp_ball.append(poke_icoe)
                    showbar = 1
                throwe = -45
                balle = balle1
                faintede = 1
        if throws >= 5 and throws <= 45:
            if throws%5 == 0:
                balls = pygame.transform.rotate(balls,45)
                ballsp = balls.get_rect(center = ballsp.center)
        if throws2 >= 5 and throws2 <= 40:
            if throws2%5 == 0:
                balls2 = pygame.transform.rotate(balls2,45)
                ballsp2 = balls2.get_rect(center = ballsp2.center)
        if (throws2 == 40 or throws2 == 80) and battle_type == 0:
            balls2 = load("p/spr/enemy_"+item.name+"_1.png")
            ballsp2 = balls2.get_rect(center = ballsp2.center)
            origballs2 = load("p/spr/enemy_"+item.name+"_1.png")
            ang = 0
        if (throws2 == 60 or throws2 == 260) and battle_type == 0:
            balls2 = load("p/spr/enemy_"+item.name+"_2.png")
            ballsp2 = balls2.get_rect(center = ballsp2.center)
        if throws2 == 251 and battle_type == 0:
            balls2 = load("p/spr/enemy_"+item.name+"_3.png")
            ballsp2 = balls2.get_rect(center = ballsp2.center)
        a += 1
        if barx > 0:
            barx -= 10
        if barex > 0 and showbar == 0:
            barex -= 10
        if showbar == 1 and barex < 400:
            barex += 10
        if throws > 0 and throws <= 10:
            ballx += 3
            bally -= 4
        if throws > 10 and throws <= 35:
            ballx += 3
            bally += 10
        if throws2 > 0 and throws2 <= 30:
            ballx2 += 16
            bally2 -= (12-(throws2/3))
        if throws2 > 30 and throws2 <= 40:
            ballx2 += 15
            bally2 += (throws2/5)
        if throws2 > 40 and battle_type == 1:
            ballx2 -= 25
            bally2 -= 15
        if battle_type == 0:
            if throws2 >= 80 and throws2 < 90:
                bally2 += 8
            if throws2 >= 90 and throws2 < 95:
                bally2 -= 4
            if throws2 >= 95 and throws2 < 100:
                bally2 += 4
            if (throws2 >= 130 and throws2 < 135) or (throws2 >= 170 and throws2 < 175) or (throws2 >= 210 and throws2 < 215):
                ang -= 5
                balls2 = pygame.transform.rotate(origballs2,ang)
            if (throws2 >= 135 and throws2 < 140) or (throws2 >= 175 and throws2 < 180) or (throws2 >= 215 and throws2 < 220):
                ang += 5
                balls2 = pygame.transform.rotate(origballs2,ang)
            if throws2 == 129 or throws2 == 169 or throws2 == 209 or throws2 == 249:
                if throws2 == 129:
                    shakes = 0
                elif throws2 == 169:
                    shakes = 1
                elif throws2 == 209:
                    shakes = 2
                else:
                    shakes = 3
                if random.randint(1,255) <= catch_check(P,pokee,pokes,item):
                    throws2 = 256
        if (a > 0 and a < 100) or (trainer_cut and ex > 0):
            ex -= 4
            if ex == 0:
                trainer_cut = False
        if a > 50 and a < 150:
            sx -= 6
        if throwe > 40:
            if P.infoepos < 400:
                P.infoepos += 16
        if throws > -60 and throws < -15:
            if P.infospos > 0:
                P.infospos -= 16
        if throwe > -60 and throwe < -15:
            if P.infoepos > 0:
                P.infoepos -= 16
        if throws > 45:
            if P.infospos < 400:
                P.infospos += 16
        P.clock.tick(P.ani_spd)
        update_screen(P)
    P.surface.set_clip((0,0,800,600))
    fade_out(P)

def get_poke(P,poke,show_pokedex = True) -> None:
    ret = pygame.transform.scale(load("p/return.png"),(25,25))
    enter = P.font.render("[ENTER]",True,(0,0,0))
    esc = P.font.render("[ESC]",True,(0,0,0))
    if poke.ball == 'Friend Ball':
        poke.friend = 200
    new_poke = False
    if poke.code_nos() not in P.save_data.pokedex:
        if poke.nurse:
            P.save_data.pokedex[poke.code_nos()] = [0,[]]
        else:
            P.save_data.pokedex[poke.code_nos()] = [1,[]]
            new_poke = True
    elif P.save_data.pokedex[poke.code_nos()][0] == 0:
        P.save_data.pokedex[poke.code_nos()][0] = 1
        new_poke = True
    if show_pokedex and new_poke:
        new_battle_txt(P)
        battle_write(P,poke.name+"'s data was added", "to the Pokedex.")
        cont(P)
        t = P.surface.copy()
        fade_out(P)
        dex_entry(P,poke.code_nos(),True,False)
        P.surface.blit(t,(0,0))
        fade_in(P)
    if show_pokedex:
        new_battle_txt(P)
        battle_write(P,"Give a nickname to",poke.name+"?")
        if choice(P,ymod = 10):
            new_battle_txt(P)
            battle_write(P,poke.name+"'s nickname?")
            P.surface.set_clip((0,0,800,600))
            name = ""
            temp = P.surface.copy()
            end = True
            a = 0
            while end:
                for event in pygame.event.get(eventtype = KEYDOWN):
                    if event.type == pygame.KEYDOWN:
                        if len(name) < 9:
                            if (pygame.K_a <= event.key <= pygame.key.key_code(P.controls[4])) or (pygame.K_0 <= event.key <= pygame.K_9):
                                name += event.unicode
                            if event.key == K_SPACE:
                                name += " "
                        if event.key == K_ESCAPE:
                            new_battle_txt(P)
                            battle_write(P,"Don't give "+poke.name + " a","nickname?")
                            if choice(P,ymod = 10):
                                end = False
                            else:
                                new_battle_txt(P)
                                battle_write(P,poke.name+"'s nickname?")
                                P.surface.set_clip((0,0,800,600))
                                name = ""
                                temp = P.surface.copy()
                        if event.key == K_BACKSPACE:
                            name = name[:-1]
                        if event.key == K_RETURN:
                            onlyspc = True
                            for let in name:
                                if let != ' ':
                                    onlyspc = False
                            if onlyspc:
                                new_battle_txt(P)
                                battle_write(P,"That name doesn't seem very","good...")
                                cont(P)
                                new_battle_txt(P)
                                battle_write(P,poke.name+"'s nickname?")
                                P.surface.set_clip((0,0,800,600))
                                temp = P.surface.copy()
                            else:
                                poke.name = name
                                end = False
                P.surface.blit(temp,(0,0))
                if len(name) == 9 or int(a/20)%2 == 1:
                    txt0 = P.font.render(name,True,(0,0,0))
                else:
                    txt0 = P.font.render(name+"_",True,(0,0,0))
                a += 1
                if len(name) == 9:
                    P.surface.blit(ret,(250,543))
                P.surface.blit(esc,(650,480))
                P.surface.blit(enter,(625,530))
                P.surface.blit(txt0,(20,530))
                P.clock.tick(P.ani_spd)
                update_screen(P)
    poke.player = True
    if len(P.party) < 6:
        P.party.append(poke)
    else:
        poke.heal()
        for x in range(10):
            for y in range(30):
                if P.save_data.box[x][y] == 0:
                    P.save_data.box[x][y] = [poke.code,poke.to_list()]
                    if show_pokedex:
                        new_battle_txt(P)
                        battle_write(P,poke.name+" was sent to Box " + str(x+1)+".")
                        cont(P)
                    else:
                        txt(P,poke.name+" was sent to Box " + str(x+1)+".")
                    return

def catch_check(P, poke, self_poke, ball) -> bool:
    lvl_mod = 1
    if poke.lvl <= 50:
        lvl_mod = 1+(50-poke.lvl)/100
    a = (((4*poke.hp) - (3*poke.ch))*poke.cr*lvl_mod)/(3*poke.hp)
    if a < 1:
        a = 1
    mod = ball.mod()
    if mod == -1:
        if ball.name == 'Fast Ball':
            f = open("poke/"+poke.code_nos()+".txt","r")
            data = f.readlines()
            if ast.literal_eval(data[1])[5] >= 2:
                mod = 4
            else:
                mod = 1
            f.close()
        elif ball.name == 'Level Ball':
            if self_poke.lvl <= poke.lvl:
                mod = 1
            elif self_poke.lvl <= 2*poke.lvl:
                mod = 2
            elif self_poke.lvl <= 4*poke.lvl:
                mod = 4
            else:
                mod = 8
        elif ball.name == 'Nest Ball':
            if poke.lvl <= 29:
                mod = (41-poke.lvl)/10
            else:
                mod = 1
        elif ball.name == 'Net Ball':
            if 'Water' in poke.type or 'Bug' in poke.type:
                mod = 3.5
            else:
                mod = 1
        elif ball.name == 'Quick Ball':
            if P.turn_count == 0:
                mod = 5
            else:
                mod = 1
        elif ball.name == 'Timer Ball':
            if P.turn_count <= 10:
                mod = (1+P.turn_count)*1229/4096
            else:
                mod = 4
    a *= mod
    if poke.status != None:
        a *= 2
    if a > 255:
        a = 255
    #print(a)
    a = 255-a
    a = ((a/255)**4)*255
    print(a/255*100)
    return a

def evo_check(P) -> None:
    for y in range(len(P.party)):
        if y >= len(P.party) or P.party[y].item == "Everstone" or P.party[y].nurse:
            pass
        elif P.party[y].evo != [] and type(P.party[y].evo[0]) == str:
            if P.party[y].evo[0] == 'friend' and P.party[y].friend >= 300 and P.party[y] in P.leveled_up and (P.party[y].code_nos() not in ['Chingling'] or get_time() > 19 or get_time() < 6) and (P.party[y].code_nos() not in ['Budew'] or (get_time() >= 6 and get_time() <= 19)):
                x = P.party[y]
                temp = x
                P.party[y] = poke.Poke(x.evo[1],[x.lvl,x.gen,x.ch,x.m1,x.p1,x.m2,x.p2,x.m3,x.p3,x.m4,x.p4,x.item,x.status,x.exp,x.ball,x.friend,x.ability,True])
                t = P.surface.copy()
                evolve(P,temp,P.party[y])
                P.surface.blit(t,(0,0))
            elif P.party[y].evo[0] == 'move' and P.party[y] in P.leveled_up:
                if P.party[y].code_nos() in ['Mime Jr','Bonsly'] and P.party[y].has_move('Mimic'):
                    x = P.party[y]
                    temp = x
                    P.party[y] = poke.Poke(x.evo[1],[x.lvl,x.gen,x.ch,x.m1,x.p1,x.m2,x.p2,x.m3,x.p3,x.m4,x.p4,x.item,x.status,x.exp,x.ball,x.friend,x.ability,True])
                    t = P.surface.copy()
                    evolve(P,temp,P.party[y])
                    P.surface.blit(t,(0,0))
        elif P.party[y].evo != [] and type(P.party[y].evo[0]) == int and P.party[y] in P.leveled_up:
            z = None
            x = P.party[y]
            if x.lvl >= x.evo[0]:
                evo = False
                if x.code_nos() == 'Karrablast':
                    for p in range(len(P.party)):
                        if P.party[p].code_nos() == 'Shelmet' and P.party[p].lvl >= 30 and P.party[p].item != 'Everstone':
                            z = p
                            evo = True
                            break
                elif x.code_nos() == 'Shelmet':
                    for p in range(len(P.party)):
                        if P.party[p].code_nos() == 'Karrablast' and P.party[p].lvl >= 30 and P.party[p].item != 'Everstone':
                            z = p
                            evo = True
                            break
                elif x.code_nos() == 'Happiny':
                    if get_time() >= 6 and get_time() <= 19 and x.item == 'Oval Stone':
                        evo = True
                elif x.code_nos() == 'Slowpoke':
                    for p in range(len(P.party)):
                        if P.party[p].code_nos() == 'Shellder':
                            z = p
                            evo = True
                            break
                elif x.code_nos() == 'Mantyke':
                    for p in range(len(P.party)):
                        if P.party[p].code_nos() == 'Remoraid':
                            z = p
                            evo = True
                            break
                elif x.code_nos() == 'Magneton':
                    if P.loc == 'vigore':
                        evo = True
                else:
                    evo = True
                if evo:
                    temp = x
                    P.party[y] = poke.Poke(x.evo[1],[x.lvl,x.gen,x.ch,x.m1,x.p1,x.m2,x.p2,x.m3,x.p3,x.m4,x.p4,x.item,x.status,x.exp,x.ball,x.friend,x.ability,True])
                    t = P.surface.copy()
                    evolve(P,temp,P.party[y])
                    P.surface.blit(t,(0,0))
                    if x.code_nos() in ['Karrablast','Shelmet']:
                        x = P.party[z]
                        temp = P.party[z]
                        P.party[z] = poke.Poke(x.evo[1],[x.lvl,x.gen,x.ch,x.m1,x.p1,x.m2,x.p2,x.m3,x.p3,x.m4,x.p4,x.item,x.status,x.exp,x.ball,x.friend,x.ability,True])
                        t = P.surface.copy()
                        evolve(P,temp,P.party[z])
                        P.surface.blit(t,(0,0))
                    elif x.code_nos() in ['Slowpoke','Mantyke']:
                        P.party.remove(P.party[z])
    P.leveled_up = []

def blit_alpha(P,img, xy, alp):
        x = xy[0]
        y = xy[1]
        temp = pygame.Surface((img.get_width(), img.get_height())).convert()
        temp.blit(P.surface, (-x, -y))
        temp.blit(img, (0, 0))
        temp.set_alpha(alp)        
        P.surface.blit(temp, xy)
        
def evolve(P,pokeo,poken) -> None:
    pygame.mixer.stop()
    set_channel_volume(P,P.sfx_vol,1)
    pygame.mixer.Channel(1).play(pygame.mixer.Sound('music/sfx/evo_click.wav'))
    if pokeo.name != pokeo.actual_name:
        poken.name = pokeo.name
    if pokeo.code[-2:] == '_S':
        poken.code += '_S'
        poken.icon = pygame.transform.scale(pygame.image.load("p/poke/"+poken.code+"_ico.png"),(70,70))
    back = load("p/evo_back.png")
    lighti = load("p/evo_light.png")
    light = pygame.transform.scale(lighti,(1,1))
    poke_1 = pygame.transform.scale(load("p/poke/"+pokeo.code+"_bf.png"),(400,400))
    poke_1wi = load("p/poke/"+pokeo.code+"_bfw.png")
    poke_1w = pygame.transform.scale(poke_1wi,(400,400))
    poke_2 = pygame.transform.scale(load("p/poke/"+poken.code+"_bf.png"),(400,400))
    P.surface.blit(back,(0,0))
    P.surface.blit(poke_1,(200,50))
    fade_in(P)
    end = True
    a = 0
    size = 400
    sizel = 1
    alp = 0
    rotate = 0
    count = 1
    while end:
        if a == 0:
            txt(P,"What?",pokeo.name+" is evolving!")
            P.song = "music/evo.wav"
            pygame.mixer.music.load(P.song)
            set_mixer_volume(P,P.vol)
            pygame.mixer.music.play(-1)
        P.surface.blit(back,(0,0))
        if a < 200:
            alp += 6
        elif a < 335:
            alp += 12
        else:
            alp -= 8
        if a < 50:
            P.surface.blit(poke_1,(200,50))
            blit_alpha(P,poke_1w,(400-(size/2),250-(size/2)),alp)
        if a >= 50 and a < 100:
            P.surface.blit(poke_1w,(400-(size/2),250-(size/2)))
            size -= 8
        if a > 335:
            P.surface.blit(poke_2,(200,50))
        poke_1w = pygame.transform.scale(poke_1wi,(size,size))
        if a > 100 and a < 340:
            P.surface.blit(light,(400-(light.get_width()/2),250-(light.get_height()/2)))
            if a < 200:
                sizel += 12
                rotate -= 1
            elif a < 400:
                count += 0.05
                rotate -= count
            if a > 300 and a < 340:
                sizel += 40
        if a == 310:
            alp = 0
        if a > 310:
            trans = pygame.Surface((800,600))
            trans.set_alpha(alp)
            trans.fill((255,255,255))
            P.surface.blit(trans,(0,0))
        light = pygame.transform.rotate(pygame.transform.scale(lighti,(sizel,sizel)),rotate)
        a += 1
        if a == 370:
            state = "Your "+pokeo.name
            if pokeo.name != pokeo.actual_name:
                state = pokeo.name
            if poken.code[:5] == 'Mega_':
                txt(P,"Congratulations! ", state + " evolved", "into its Mega form!")
            else:
                txt(P,"Congratulations! ", state + " evolved", "into " + poken.actual_name+"!")
        if a == 371:
            if len(pokeo.evo) == 3:
                poken.learn(P,moves.Move(pokeo.evo[2]),False)
            if len(pokeo.evo) == 4:
                poken.learn(P,moves.Move(pokeo.evo[2]),False)
                poken.learn(P,moves.Move(pokeo.evo[3]),False)
        if a == 375:
            end = False
        pygame.event.pump()
        P.clock.tick(P.ani_spd)
        update_screen(P)
    if poken.code_nos() not in P.save_data.pokedex:
        P.save_data.pokedex[poken.code_nos()] = [1,[]]
    elif P.save_data.pokedex[poken.code_nos()][0] == 0:
        P.save_data.pokedex[poken.code_nos()][0] = 1
    if poken.ch != 0:
        poken.ch += poken.hp-pokeo.hp
    fade_out(P,P.song)

def EOT_effects(P,pokes,pokee,turn,move_back):
    op = pokes.copy()
    oe = pokee.copy()
    if pokes.status == None and pokes.yawn == 2:
        if pokes.ability == 'Insomnia':
            new_battle_txt(P)
            battle_write(P,pokes.get_name()+" didn't", "fall asleep!")
            show_ability(P,'Insomnia',abs(turn-1))
        elif P.battle_terrain != None and P.battle_terrain[0] == 'Electric' and pokes.grounded():
            new_battle_txt(P)
            battle_write(P,pokes.get_name()+" didn't", "fall asleep!")
            P.clock.tick(P.bat_spd)
        else:
            pokes.status = 'Slp'
            pokes.slptim = random.randint(1,4)
            if pokes.ability == 'Early Bird':
                pokes.slptim = int(pokes.slptim/2)
            new_battle_txt(P)
            battle_write(P,pokes.get_name()+" fell", "asleep!")
            P.clock.tick(P.bat_spd)
        pokes.yawn = 0
    if pokes.ability == 'Shed Skin' and random.random() <= .3 and pokes.status != None and pokes.status != 'Faint':
        pokes.status = None
        new_battle_txt(P)
        battle_write(P,pokes.get_name()+" shed its", "skin!")
        show_ability(P,'Shed Skin',abs(turn-1))
    if pokes.ability == 'Healer' and random.random() <= .3 and pokes.status != None and pokes.status != 'Faint':
        pokes.status = None
        new_battle_txt(P)
        battle_write(P,pokes.get_name()+" healed its", "condition!")
        show_ability(P,'Healer',abs(turn-1))
    if pokes.ability == 'Hydration' and P.battle_weather != None and P.battle_weather[0] == 'Rain' and pokes.status != None and pokes.status != 'Faint':
        pokes.status = None
        new_battle_txt(P)
        battle_write(P,pokes.get_name()+"'s status", "was cured!")
        show_ability(P,'Hydration',abs(turn-1))
    if pokes.item != None and items.Item(pokes.item).type[0] == 'Battle Berry' and type(items.Item(pokes.item).mod()) == list:
        if pokes.status in items.Item(pokes.item).mod()[0] or ((items.Item(pokes.item).name == 'Lum Berry' or items.Item(pokes.item).name == 'Persim Berry') and pokes.cfs > 0):
            new_battle_txt(P)
            battle_write(P,pokes.get_name() + " ate its", pokes.item+"!")
            P.clock.tick(P.bat_spd)
            new_battle_txt(P)
            s = items.Item(pokes.item).mod()[0][0]
            if items.Item(pokes.item).name == 'Lum Berry':
                if pokes.cfs > 0:
                    pokes.cfs = 0
                    battle_write(P,pokes.name + " was cured", "of confusion!")
                    if pokes.status != None:
                        P.clock.tick(P.bat_spd)
                        new_battle_txt(P)
                s = pokes.status
            if s == None:
                pass
            elif s == 'Slp':
                battle_write(P,pokes.name + " woke up!")
            elif s == 'Frz':
                battle_write(P,pokes.name + " thawed","out!")
            elif s == 'Brn':
                battle_write(P,pokes.name + " burn was","healed!")
            else:
                sta = items.Item(pokes.item).mod()[1]
                if items.Item(pokes.item).name == 'Lum Berry':
                    if s == 'Par':
                        sta = 'Paralysis'
                    else:
                        sta = 'Poisoning'
                battle_write(P,pokes.name + " was cured", "of "+sta+"!")
            P.clock.tick(P.bat_spd)
            if items.Item(pokes.item).name == 'Persim Berry':
                pokes.cfs = 0
            else:
                pokes.status = None
            pokes.item = None
    P.surface.set_clip((0,0,800,460))
    tempp = pokes.copy()
    tempe = pokee.copy()
    if pokes.trapped[1] > 0:
        pokes.trapped[1] -= 1
        if pokes.trapped[1] == 0:
            new_battle_txt(P)
            battle_write(P,pokes.get_name()+" was freed","from "+pokes.trapped[0]+"!")
            P.clock.tick(P.bat_spd)
            pokes.trapped = [None,0]
        else:
            new_battle_txt(P)
            battle_write(P,pokes.get_name()+" is hurt by", pokes.trapped[0]+"!")
            P.clock.tick(P.bat_spd)
            tempp.take_damage(P,int(tempp.hp/8))
            # tempp.ch -= int(tempp.hp/8)
            # if tempp.ch < 0:
            #     tempp.ch = 0
            if turn == 0:
                hp_change(P,pokes,pokee,tempp,tempe,move_back)
            else:
                hp_change(P,pokee,pokes,tempe,tempp,move_back)
            if pokes.ch == 0:
                poke_faint(P,pokes)
                pokee.trapped = [None,0]
                P.ion_deluge = False
                return pokes
    if pokes.status == 'Brn':
        new_battle_txt(P)
        battle_write(P,pokes.get_name()+" was hurt", "by its burn!")
        P.clock.tick(P.bat_spd)
        # tempp.ch -= int(tempp.hp/16)
        tempp.take_damage(P,int(tempp.hp/16))
    if pokes.status == 'Psn':
        new_battle_txt(P)
        battle_write(P,pokes.get_name()+" was hurt", "by poison!")
        P.clock.tick(P.bat_spd)
        #tempp.ch -= int(tempp.hp/8)
        tempp.take_damage(P,int(tempp.hp/8))
    if pokes.status == 'BPs':
        new_battle_txt(P)
        battle_write(P,pokes.get_name()+" was hurt", "by poison!")
        P.clock.tick(P.bat_spd)
        # tempp.ch -= int(tempp.hp*tempp.bps/16)
        tempp.take_damage(P,int(tempp.hp*tempp.bps/16))
        pokes.bps += 1
    if pokes.nightmare:
        if pokes.status != 'Slp':
            pokes.nightmare = False
        else:
            new_battle_txt(P)
            battle_write(P,pokes.get_name()+" is locked", "in a nightmare!")
            P.clock.tick(P.bat_spd)
            tempp.take_damage(P,int(tempp.hp/4))
    if pokes.taunt > 0:
        pokes.taunt -= 1
        if pokes.taunt == 0:
            new_battle_txt(P)
            battle_write(P,pokes.get_name()+" shook off", "the taunt!")
            P.clock.tick(P.bat_spd)
    if tempp.ch < 0:
        tempp.ch = 0
    if turn == 0:
        hp_change(P,pokes,pokee,tempp,tempe,move_back)
    else:
        hp_change(P,pokee,pokes,tempe,tempp,move_back)
    P.ion_deluge = False
    if pokes.ch == 0:
        poke_faint(P,pokes)
        pokee.trapped = [None,0]
    return pokes

def poke_max(P,poke):
    lvl = 15
    if P.prog[0] >= 48:
        lvl = 25
    if P.prog[0] >= 86:
        lvl = 35
    if poke == None:
        return lvl
    if poke.lvl == lvl and poke.exp == poke.get_exp():
        return True
    return False

def gain_exp(P,pokes,pokee,was_in,battle_type) -> None:
    expbar = load("p/summ_exp.png")
    hpbar = load('p/team_hp.png')
    infoboxs = load("p/battle_info_boxs.png")
    if pokes.code[-2:] == '_S':
        infoboxs = load("p/battle_info_boxs_S.png")
    tempok = pokee.copy()
    tempok.lvl = 100
    tempok.get_stats()
    stattot = tempok.ak+tempok.sak+tempok.df+tempok.sdf+tempok.spd+tempok.hp
    exp = int(pokee.get_exp()*stattot/2000*((200-pokes.lvl)/300))+6
    if exp == 0:
        exp = 1
    if battle_type == 1:
        if (pokee.name in ['Scizor','Steelix','Ferrothorn'] and pokee.item == 'Metal Coat' and pokee.lvl == 40) or ((pokee.name == 'Nidorina' or pokee.name == 'Nidorino') and pokee.item == 'Eviolite' and pokee.lvl == 16):
            exp *= 0.5
        elif P.legendary_battle == False:
            exp *= 1.5
    exp = int(2*exp)
    otherexp = exp
    if pokes.lvl != 100 and pokes.status != 'Faint' and poke_max(P,pokes) == False:
        new_battle_txt(P)
        battle_write(P,pokes.name+" gained " + str(int(exp)),"Exp. Points!")
        P.clock.tick(P.bat_spd)
        end = True
        while end:
            for x in range(1+int(pokes.get_exp()/50)):
                if pokes.exp == pokes.get_exp():
                    break
                pokes.exp += 1
                exp -= 1
                if exp == 0:
                    end = False
                    break
            P.surface.fill((255,255,255), Rect(474,425,320,10))
            P.surface.fill((0,0,255), Rect(474,425,int(320*(pokes.exp/pokes.get_exp())),10))
            P.surface.blit(expbar,(420,420))
            if poke_max(P,pokes):
                break
            if pokes.exp == pokes.get_exp():
                new_battle_txt(P)
                P.surface.set_clip((425,384,120,25))
                P.surface.blit(infoboxs,(400,300))
                P.surface.set_clip((0,0,800,600))
                P.surface.blit(P.font_s.render("Lv."+str(pokes.lvl+1),True,(255,255,255)),(430,380))
                battle_write(P,pokes.name + " leveled up!")
                P.surface.fill((255,255,255), Rect(474,425,320,10))
                P.surface.blit(expbar,(420,420))
                P.clock.tick(P.bat_spd)
                # thp = pokes.hp
                pokes.lvlup(P)
                # pokes.ch += pokes.hp-thp
                hps = P.font_s.render(str(pokes.ch) + "/" + str(pokes.hp),True,(255,255,255))
                hpsze = P.font_s.size(str(pokes.ch) + "/" + str(pokes.hp))
                P.surface.set_clip((540,360,250,50))
                P.surface.blit(infoboxs,(400,300))
                P.surface.set_clip((0,0,800,600))
                P.surface.blit(hps,(720-hpsze[0],380))
                if pokes.ch/pokes.hp >= 0.5:
                    P.surface.fill((0,255,0), Rect(584,365,int(200*(pokes.ch/pokes.hp)),10))
                elif pokes.ch/pokes.hp >= 0.25:
                    P.surface.fill((255,255,0), Rect(584,365,int(200*(pokes.ch/pokes.hp)),10))
                else:
                    P.surface.fill((255,50,0), Rect(584,365,int(200*(pokes.ch/pokes.hp)),10))
                P.surface.blit(hpbar,(540,360))
                if pokes.lvl == 100:
                    exp = 0
                P.leveled_up.append(pokes)
            P.clock.tick(P.ani_spd)
            update_screen(P)
    for x in range(len(was_in)):
        if was_in[x].equals(pokes):
            del was_in[x]
            break
    for y in was_in:
        exp = int(1.5*(otherexp)/(len(was_in)+1))
        if y.lvl != 100 and y.status != 'Faint' and poke_max(P,y) == False:
            new_battle_txt(P)
            battle_write(P,y.name+" gained " + str(int(exp)),"Exp. Points!")
            P.clock.tick(P.bat_spd)
            end = True
            while end:
                for x in range(1+int(y.get_exp()/50)):
                    if y.exp == y.get_exp():
                        break
                    y.exp += 1
                    exp -= 1
                    if exp == 0:
                        end = False
                        break
                if poke_max(P,y):
                    break
                if y.exp == y.get_exp():
                    new_battle_txt(P)
                    battle_write(P,y.name + " leveled up!")
                    P.clock.tick(P.bat_spd)
                    # thp = y.hp
                    y.lvlup(P)
                    # y.ch += y.hp-thp
                    P.leveled_up.append(y)
        
def calc_prize(P,opp) -> int:
    lvl = 0
    mod = 1.1
    for poke in opp:
        if mod <= 1:
            lvl += poke.lvl*mod
        mod -= .1
    lvl = int(lvl)
    if P.double_money:
        lvl *= 2
    pos = 0
    try:
        while opp[0][pos] != ' ':
            pos += 1
    except:
        pos = -1
    if opp[0][0:pos] == 'Steven':
        return int(20*lvl)
    if opp[0][0:pos] == 'Leader':
        return int(30*lvl)
    if opp[0][0:pos] == 'Professor':
        return int(50*lvl)
    if opp[0][0:pos] in ['Lass','Youngster','Bug']:
        return int(8*lvl)
    if opp[0][0:pos] in ['Gentleman','Rich','Beauty']:
        return int(18*lvl)
    if opp[0][0:pos] in ['Trainer','Expert','Ace']:
        return int(13*lvl)
    if opp[0][0:pos] in ['Hiker','Triathelete','Battle','Team','Psychic','Hex','Fisherman']:
        return int(10*lvl)
    if opp[0][0:pos] == 'Preschooler':
        return int(5*lvl)

def show_ability(P,ability,turn):
    tim = 0
    end = True
    text = P.font_s.render(ability,True,(150, 255, 150))
    size = text.get_width()
    if turn == 1:
        x = -(size+30)
        x2 = x
        y = 400
    else:
        x = 830
        x2 = x
        y = 240
    temp = P.surface.copy()
    while end:
        P.surface.blit(temp,(0,0))
        if turn == 1:
            pygame.draw.rect(P.surface,(20, 130, 50),Rect(x2-10,y-20,size+40,50))
            pygame.draw.rect(P.surface,(255, 40, 40),Rect(x - 20, y-10,size+40, 50))
        else:
            pygame.draw.rect(P.surface, (20, 130, 50), Rect(x2 - 20, y - 20, size+40, 50))
            pygame.draw.rect(P.surface, (255, 40, 40), Rect(x - 10, y-10, size+40, 50))
        P.surface.blit(text,(x,y))
        if turn == 1:
            if tim < 5:
                x2 += (size / 5) + 8
            elif tim < 10:
                x += (size / 5) + 8
            if tim > 65:
                x2 -= (size / 5) + 8
            elif tim > 60:
                x -= (size / 5) + 8
        else:
            if tim < 5:
                x2 -= (size / 5) + 8
            elif tim < 10:
                x -= (size / 5) + 8
            if tim > 65:
                x2 += (size / 5) + 8
            elif tim > 60:
                x += (size / 5) + 8
        if tim == 71:
            end = False
        tim += 1
        P.clock.tick(P.ani_spd)
        update_screen(P)

def use_ability1(P,pokes,pokee,turn,move_back) -> None:
    if pokee.inf == True:
        pokee.inf = False
    if pokee.trapped[1] != 0:
        pokee.trapped = [None,0]
    if pokes.ability == 'Intimidate':
        show_ability(P,'Intimidate',turn)
        if pokee.ability == 'Hyper Cutter':
            new_battle_txt(P)
            battle_write(P,pokee.get_name() + "'s attack", "can't be lowered!")
            show_ability(P,'Hyper Cutter',abs(turn-1))
        elif pokee.ability == 'Clear Body':
            new_battle_txt(P)
            battle_write(P,pokee.get_name() + "'s attack", "can't be lowered!")
            show_ability(P,'Clear Body',abs(turn-1))
        elif pokee.akm == -6:
            new_battle_txt(P)
            battle_write(P, pokee.get_name() + "'s attack", "won't go any lower!")
            P.clock.tick(P.bat_spd)
        else:
            new_battle_txt(P)
            battle_write(P, pokee.get_name() + "'s attack", "fell!")
            P.clock.tick(P.bat_spd)
            pokee.akm -= 1
    if turn == 1:
        if pokes.ability == 'Forewarn':
            new_battle_txt(P)
            power = 0
            mvs = [pokee.m1,pokee.m2,pokee.m3,pokee.m4]
            move_list = []
            for m in mvs:
                if m != None:
                    mov = moves.Move(m)
                    if mov.pow in ['---',"???"]:
                        if mov.cat != '2':
                            if mov.name in ['Stored Power','Power Trip']:
                                if power <= 20:
                                    if power < 20:
                                        move_list = []
                                    power = 20
                                    move_list.append(mov)
                            elif mov.name in ['Counter','Metal Burst','Mirror Coat']:
                                if power <= 120:
                                    if power < 120:
                                        move_list = []
                                    power = 120
                                    move_list.append(mov)
                            elif mov.name in ['Eruption', 'Water Spout', 'Fissure', 'Guillotine', 'Horn Drill', 'Sheer Cold']:
                                if power <= 150:
                                    if power < 150:
                                        move_list = []
                                    power = 150
                                    move_list.append(mov)
                        else:
                            if power == 0:
                                move_list.append(mov)
                    elif int(mov.pow) >= power:
                        if power < int(mov.pow):
                            move_list = []
                        power = int(mov.pow)
                        move_list.append(mov)
            battle_write(P,pokee.name + "'s", move_list[random.randint(0,len(move_list)-1)].name+" was revealed!")
            show_ability(P,'Forewarn',turn)
        if pokes.ability == 'Frisk':
            if pokee.item != None:
                new_battle_txt(P)
                aan = 'a '
                if pokee.item[0] in ['A','E','I','O','U']:
                    aan = 'an '
                battle_write(P,pokes.name + " frisked the foe", "and found " + aan + pokee.item+"!")
                show_ability(P,'Frisk',turn)
    if pokes.grounded():
        if ((turn == 0 and P.enemy_traps[0] > 0) or (turn == 1 and P.self_traps[0] > 0)):
            tempp = pokes.copy()
            tempe = pokee.copy()
            layers = P.self_traps[0]
            if turn == 0:
                layers = P.enemy_traps[0]
            if layers == 1:
                damage = 0.125
            elif layers == 2:
                damage = 0.1666
            else:
                damage = 0.25
            new_battle_txt(P)
            battle_write(P,pokes.get_name()+" was hurt","by the spikes!")
            P.clock.tick(P.bat_spd)
            damage = int(damage*pokes.hp)
            tempp.take_damage(P,damage)
            if turn == 1:
                hp_change(P,pokes,pokee,tempp,tempe,move_back)
            else:
                hp_change(P,pokee,pokes,tempe,tempp,move_back)
            if pokes.ch == 0:
                poke_faint(P,pokes)
                pokee.trapped = [None,0]
        if ((turn == 0 and P.enemy_traps[1] > 0) or (turn == 1 and P.self_traps[1] > 0)) and pokes.status == None:
            if (turn == 0 and P.enemy_traps[1] == 1) or (turn == 1 and P.self_traps[1] == 1):
                new_battle_txt(P)
                battle_write(P,pokes.get_name() + " was", "poisoned!")
                P.clock.tick(P.bat_spd)
                pokes.status = 'Psn'
            else:
                new_battle_txt(P)
                battle_write(P,pokes.get_name() + " was badly", "poisoned!")
                P.clock.tick(P.bat_spd)
                pokes.status = 'BPs'
        if ((turn == 0 and P.enemy_traps[2] > 0) or (turn == 1 and P.self_traps[2] > 0)):
            tempp = pokes.copy()
            tempe = pokee.copy()
            new_battle_txt(P)
            battle_write(P,"Pointed stones dug into",pokes.get_name(True)+"!")
            P.clock.tick(P.bat_spd)
            rock_move = moves.Move('Rock Throw')
            damage = (0.125*rock_move.eff_no_print(P,pokes)*pokes.hp)
            tempp.take_damage(P,damage)
            if turn == 1:
                hp_change(P,pokes,pokee,tempp,tempe,move_back)
            else:
                hp_change(P,pokee,pokes,tempe,tempp,move_back)
            if pokes.ch == 0:
                poke_faint(P,pokes)
                pokee.trapped = [None,0]
        if (turn == 0 and P.enemy_traps[3] > 0) or (turn == 1 and P.self_traps[3] > 0):
            new_battle_txt(P)
            battle_write(P,pokes.get_name()+" was caught", "in a sticky web!")
            P.clock.tick(P.bat_spd)
            new_battle_txt(P)
            battle_write(P,pokes.get_name() + "'s speed", "fell!")
            P.clock.tick(P.bat_spd)
            pokes.spdm -= 1
    P.ion_deluge = False

def choose_nxtpoke(P,pokes,battle_type,ans = True,pokee = 0) -> None:
    if battle_type == 1:
        P.surface.set_clip((0,0,800,600))
        t = P.surface.copy()
        fade_out(P)
        ans = battle_team(P,pokes,battle_type)
        P.surface.blit(t,(0,0))
        fade_in(P)
        return ans
    elif (choice(P,550,600,ans)):
        P.surface.set_clip((0,0,800,600))
        t = P.surface.copy()
        fade_out(P)
        if battle_type == 0:
            battle_type = 2
        ans = battle_team(P,pokes,battle_type)
        P.surface.blit(t,(0,0))
        fade_in(P)
        return ans
    elif battle_type == 1.5:
        return pokes
    elif battle_type == 0:
        if random.random()<(pokes.spd/pokee.spd) or pokes.ability == 'Run Away' or 'Ghost' in pokes.type:
            new_battle_txt(P)
            battle_write(P,"You got away safely!")
            P.clock.tick(P.bat_spd)
            return 1
        else:
            new_battle_txt(P)
            battle_write(P,"You couldn\'t get away!")
            P.clock.tick(P.bat_spd)
            P.surface.set_clip((0,0,800,600))
            t = P.surface.copy()
            fade_out(P)
            ans = battle_team(P,pokes,2)
            P.surface.blit(t,(0,0))
            fade_in(P)
            return ans

def acc_mod(stage) -> float:
    if stage >= 0:
        return 1+(stage*0.3)
    elif stage == -1:
        return 0.77
    elif stage == -2:
        return 0.63
    elif stage == -3:
        return 0.53
    elif stage == -4:
        return 0.45
    elif stage == -5:
        return 0.4
    return 0.36

def crit_mod(stage) -> float:
    if stage == 0:
        return 0.042
    elif stage == 1:
        return .125
    elif stage == 2:
        return 0.5
    return 1


def modifier(stage) -> float:
    if stage >= 0:
        return 1+(stage*0.5)
    elif stage == -1:
        return 0.67
    elif stage == -2:
        return 0.5
    elif stage == -3:
        return 0.4
    elif stage == -4:
        return 0.33
    elif stage == -5:
        return 0.29
    return 0.25

def opp_effect(move):
    #return true if it has an effect that effects the opponent
    if move.eff == {}:
        return False
    for key,items in move.eff.items():
        eff = items[0]
        break
    print("effect: " + eff)
    return eff == "Trp" or eff == "Inf" or eff == "Brn" or eff == "Frz" or eff == "Par" or eff == "Psn" or eff == "BPs" or eff == "Slp" or eff == "Bnd" or eff == "Cfs" or eff == "Fln" or eff == "AD" or eff == "SAD" or eff == "DD" or eff == "SDD" or eff == "SD" or eff == "AcD" or eff == "EvD" or eff == "Idf" or eff == "CD"

def poke_strength(pokes):
    ak = modifier(pokes.akm)*pokes.ak
    sak = modifier(pokes.sakm)*pokes.sak
    df = modifier(pokes.dfm)*pokes.df
    sdf = modifier(pokes.sdfm)*pokes.sdf
    spd = modifier(pokes.spdm)*pokes.spd
    total = ak + sak + df + sdf + spd + pokes.hp
    acc = acc_mod(pokes.accm)*total/6
    eva = acc_mod(-1 * pokes.evam)*total/6
    crit = crit_mod(pokes.critm)*total/6
    total += acc
    total += eva
    total += crit
    if pokes.status != None:
        total *= .8
    return total


def opp_AI(P,pokee,pokes,moves):
    #0 self buff
    #1 opp buff
    #2 attack
    move_options = {"ss":[],"os":[],"a":[]}
    for move in moves:
        print(move.cat)
        if move.cat == '2':
            if opp_effect(move):
                move_options["os"].append(move)
            else:
                move_options["ss"].append(move)
        else:
            move_options["a"].append(move)
    print("move_options: "+str(move_options))
    pokestot = poke_strength(pokes)
    pokeetot = poke_strength(pokee)
    if pokeetot > pokestot:
        move_prob = [0.75*(pokeetot/pokestot)*pokee.ch*pokee.ch/pokee.hp/pokee.hp,max(0,(1.5-pokeetot/pokestot)),1]
    else:
        move_prob = [max(0,(2-pokestot/pokeetot)),0.75*(pokestot/pokeetot)*pokes.ch*pokes.ch/pokes.hp/pokes.hp,1]
    if move_options["ss"] == []:
        move_prob[0] = 0
    if move_options["os"] == []:
        move_prob[1] = 0
    if move_options["a"] == []:
        move_prob[2] = 0
    print("move_prob: "+str(move_prob))
    randtot = 0
    for prob in move_prob:
        randtot += prob
    choose = random.uniform(0,randtot)
    print("choose: "+str(choose))
    if choose < move_prob[0]:
        pick = "ss"
    elif choose < move_prob[0]+move_prob[1]:
        pick = "os"
    else:
        pick = "a"
    print("pick: "+str(pick))
    if pick == "a" and len(move_options[pick]) == 1:
        if move_options[pick][0].eff_no_print(P,pokes) != 0:
            final_move = move_options[pick][0]
        else:
            final_move = None
    elif pick == "a":
        power = []
        for move in move_options[pick]:
            try:
                if move.name == 'Spit Up':
                    power.append(int(100*pokee.stockpile[0])*move.eff_no_print(P,pokes))
                elif move.name in ['Overheat','Draco Meteor','Leaf Storm','Fleur Cannon']:
                    power.append((int(move.pow)-(70*pokes.ch/pokes.hp))*move.eff_no_print(P,pokes))
                elif move.name == 'Return':
                    power.append(int(int(pokee.friend/4)*move.eff_no_print(P,pokes)))
                elif move.name in ['Self-Destruct','Explosion']:
                    power.append(40+(int(move.pow)*move.eff_no_print(P,pokes)*((pokee.hp-pokee.ch)/pokee.hp)))
                elif move.name == 'Fury Cutter':
                    power.append((int(move.pow)*(pokee.fury_count+1))*move.eff_no_print(P,pokes))
                elif move.name == 'Flail':
                    power.append((150*(((pokee.hp-pokee.ch)/pokee.hp)**2))*move.eff_no_print(P,pokes))
                elif move.name == 'Hex' and pokes.status != None:
                    power.append(int(move.pow)*move.eff_no_print(P,pokes)*2)
                elif move.name == 'Dream Eater' and pokes.status != 'Slp':
                    power.append(0)
                elif move.name == 'Fake Out':
                    num = 0
                    if move.eff_no_print(P,pokes) != 0 and pokee.turn_count == 0:
                        num = 200
                    power.append(num)
                else:
                    power.append(int(move.pow)*move.eff_no_print(P,pokes)*min(move.acc+max(((pokestot/pokeetot)-1)*0.6,0),1))
            except:
                power.append(60*move.eff_no_print(P,pokes))
        print("power: " + str(power))
        if len(power) > 0:
            strongest = max(power)
            move_probs = []
            for pow in power:
                if pow == strongest:
                    move_probs.append(1)
                else:
                    move_probs.append(0)
            counter = 0
            for move in move_options[pick]:
                if move.eff != {}:
                    if pokeetot < pokestot:
                        move_probs[counter] += 1-pokeetot/pokestot
                counter += 1
            randtot = 0
            for prob in move_probs:
                randtot += prob
            choose = random.uniform(0,randtot)
            print("choose: "+str(choose))
            lb = 0
            ub = move_probs[0]
            counter = 0
            final_move = move_options[pick][len(move_options[pick])-1]
            for x in range(len(move_probs)):
                if choose >= lb and choose < ub:
                    final_move = move_options[pick][counter]
                    break
                counter += 1
                lb = ub
                if counter < len(move_probs):
                    ub = move_probs[counter]
            if final_move.eff_no_print(P,pokes) == 0:
                final_move = None
        else:
            final_move = None
    else:
        no_eff = []
        final_list = move_options[pick]
        for move in final_list:
            if (move.name == 'Swallow' and (pokee.stockpile[0] == 0 or pokee.ch/pokee.hp > 1-(0.2*pokee.stockpile[0]))) or (move.name == 'Stockpile' and pokee.stockpile[0] == 3):
                no_eff.append(move)
            if move.name == 'Nightmare' and pokes.status != 'Slp':
                no_eff.append(move)
        if len(no_eff) > 0:
            for move in no_eff:
                final_list.remove(move)
        if len(final_list) > 0:
            final_move = final_list[random.randint(0,len(final_list)-1)]
        else:
            final_move = None
    for x in range(len(moves)):
        if final_move == moves[x]:
            return x
    move_copy = []
    for move in moves:
        if move.eff_no_print(P,pokes) != 0 or (move.cat == '2' and opp_effect(move) == False):
            move_copy.append(move)
    print(len(move_copy))
    if len(move_copy) > 0:
        choose = random.randint(0,len(move_copy)-1)
        final_move = move_copy[choose]
        for x in range(len(moves)):
            if final_move == moves[x]:
                return x
    return random.randint(0,len(moves)-1)

def use_x(P,pokes,pokee,move_back,movex):
    if type(movex) != int and movex.cat != '2':
        pokes.can_sucker = True
    strug = moves.Move('Struggle')
    hpbar = load("p/team_hp.png")
    move_l = []
    if pokee.m1 != None and pokee.p1 > 0:
        if pokee.taunt == 0 or moves.Move(pokee.m1).cat != '2':
            move_l.append(moves.Move(pokee.m1))
    if pokee.m2 != None and pokee.p2 > 0:
        if pokee.taunt == 0 or moves.Move(pokee.m2).cat != '2':
            move_l.append(moves.Move(pokee.m2))
    if pokee.m3 != None and pokee.p3 > 0:
        if pokee.taunt == 0 or moves.Move(pokee.m3).cat != '2':
            move_l.append(moves.Move(pokee.m3))
    if pokee.m4 != None and pokee.p4 > 0:
        if pokee.taunt == 0 or moves.Move(pokee.m4).cat != '2':
            move_l.append(moves.Move(pokee.m4))
    if len(move_l) == 0:
        choose = -1
        movee = strug
    else:
        # choose = random.randint(0,len(move_l)-1)
        choose = opp_AI(P,pokee,pokes,move_l)
        print(choose)
        movee = move_l[choose]
    if movee.cat != '2' or pokee.cont_move != [None,0] or pokee.rollcount != 0 or pokee.bide != [0,0] or pokee.charge != None:
        pokee.can_sucker = True
    spds = pokes.get_spd(P)
    spde = pokee.get_spd(P)
    if movex == 0:
        if random.random()<(pokes.spd/pokee.spd) or pokes.ability == 'Run Away' or 'Ghost' in pokes.type:
            new_battle_txt(P)
            battle_write(P,"You got away safely!")
            cont(P)
            return 1
        else:
            opp = 1
            new_battle_txt(P)
            battle_write(P,"You couldn\'t get away!")
            cont(P)
    elif movex == 1:
        opp = 1
    else:
        priox = movex.priority
        prioe = movee.priority
        if pokes.ability == 'Prankster' and movex.cat == '2':
            priox += 1
        if pokee.ability == 'Prankster' and movee.cat == '2':
            prioe += 1
        if priox > prioe or (pokee.item == 'Full Incense' or pokee.ability == 'Stall'):
            spds = 1
            spde = 0
        elif priox < prioe or (pokes.item == 'Full Incense' or pokes.ability == 'Stall'):
            spde = 1
            spds = 0
        if spde > spds:
            opp_move(P,pokes,pokee,movee,move_back,strug,choose)
            opp = 0
        else:
            opp = 1
        if pokes.status != 'Faint':
            orige = pokee.copy()
            origs = pokes.copy()
            if movex.name == 'Struggle':
                new_battle_txt(P)
                battle_write(P,pokes.name+" is out of moves!")
                P.clock.tick(P.bat_spd)
            eff = movex.cast(P,pokes,pokee,4,0)
            battle_move_use(P,origs,orige,pokes,pokee,move_back,eff,1)
            count = eff[4]
            if movex.name == 'Metronome':
                movex = moves.Move(P.metronome)
            for x in range(count):
                if pokee.ch == 0 or pokes.ch == 0:
                    break
                eff = movex.use(P,pokes,pokee,0)
                battle_move_use(P,origs,orige,pokes,pokee,move_back,eff,x+2)
            if count != 0 and pokes.ch != 0 and pokee.ch != 0:
                new_battle_txt(P)
                battle_write(P,"Hit " + str(count+1) + " times!")
                P.clock.tick(P.bat_spd)
            P.gem_active = False
    if opp == 1 and pokee.status != 'Faint':
        opp_move(P,pokes,pokee,movee,move_back,strug,choose)
    EOT_effects(P,pokes,pokee,0,move_back)
    EOT_effects(P,pokee,pokes,1,move_back)
    pokes = reset_move_stat(P,pokes)
    pokee = reset_move_stat(P,pokee)
    if P.echoed[1] == 1:
        P.echoed = [0,0]
    if P.echoed[1] != 0:
        P.echoed[1] -= 1
    return 0

def opp_move(P,pokes,pokee,movee,move_back,strug,choose):
    orige = pokee.copy()
    origs = pokes.copy()
    if movee == strug and pokee.bide == [0,0] and pokee.rollcount == 0 and pokee.charge == False:
        new_battle_txt(P)
        battle_write(P,pokee.get_name()+" is out of", "moves!")
        P.clock.tick(P.bat_spd)
    if pokee.bide[0] > 0:
        eff = moves.Move('Bide').cast(P,pokee,pokes,4)
        battle_move_use(P,origs,orige,pokes,pokee,move_back,eff)
    elif pokee.charge != None:
        eff = moves.Move(pokee.charge).cast(P,pokee,pokes,4)
        battle_move_use(P,origs,orige,pokes,pokee,move_back,eff)
    elif pokee.rollcount > 0:
        eff = moves.Move('Rollout').cast(P,pokee,pokes,4)
        battle_move_use(P,origs,orige,pokes,pokee,move_back,eff)
    elif pokee.cont_move[1] > 0:
        eff = moves.Move(pokee.cont_move[0]).cast(P,pokee,pokes,4)
        battle_move_use(P,origs,orige,pokes,pokee,move_back,eff)
    else:
        eff = movee.cast(P,pokee,pokes,choose)
        battle_move_use(P,origs,orige,pokes,pokee,move_back,eff,1)
        count = eff[4]
        if movee.name == 'Metronome':
            movee = moves.Move(P.metronome)
        for x in range(count):
            if pokes.ch == 0 or pokee.ch == 0:
                break
            eff = movee.use(P,pokee,pokes,1)
            battle_move_use(P,origs,orige,pokes,pokee,move_back,eff,x+2)
        if count != 0 and pokes.ch != 0 and pokee.ch != 0:
            new_battle_txt(P)
            battle_write(P,"Hit " + str(count+1) + " times!")
            P.clock.tick(P.bat_spd)
        P.gem_active = False

def pick_move(P, pokes, pokee, mvnum, move_back,pokemone,pokemons,sizes,sizee,a) -> list:
    P.surface.set_clip((0,0,800,600))
    strug = moves.Move('Struggle')
    back = load("p/battle_box.png")
    mvinfo = load("p/move_info_box.png")
    move_boxes = []
    move_box1 = load("p/move_box_1.png")
    move_box2 = load("p/move_box_2.png")
    for x in range(4):
        move_boxes.append(move_box1)
    move_boxes[mvnum] = move_box2
    movesl = []
    if pokes.m1 != None:
        movesl.append(moves.Move(pokes.m1))
        move1 = P.font_s.render(pokes.m1,True,(0,0,0))
        sz1 = P.font_s.size(pokes.m1)
    if pokes.m2 != None:
        movesl.append(moves.Move(pokes.m2))
        move2 = P.font_s.render(pokes.m2,True,(0,0,0))
        sz2 = P.font_s.size(pokes.m2)
    if pokes.m3 != None:
        movesl.append(moves.Move(pokes.m3))
        move3 = P.font_s.render(pokes.m3,True,(0,0,0))
        sz3 = P.font_s.size(pokes.m3)
    if pokes.m4 != None:
        movesl.append(moves.Move(pokes.m4))
        move4 = P.font_s.render(pokes.m4,True,(0,0,0))
        sz4 = P.font_s.size(pokes.m4)
    move_col = []
    for x in movesl:
        if x.type == 'Normal':
            move_col.append((255,250,230))
        elif x.type == 'Fighting':
            move_col.append((240,160,160))
        elif x.type == 'Flying':
            move_col.append((220,200,255))
        elif x.type == 'Poison':
            move_col.append((200,150,230))
        elif x.type == 'Ground':
            move_col.append((230,210,130))
        elif x.type == 'Rock':
            move_col.append((200,170,100))
        elif x.type == 'Bug':
            move_col.append((200,230,110))
        elif x.type == 'Ghost':
            move_col.append((160,140,190))
        elif x.type == 'Steel':
            move_col.append((200,200,200))
        elif x.type == 'Fire':
            move_col.append((255,190,130))
        elif x.type == 'Water':
            move_col.append((150,190,255))
        elif x.type == 'Grass':
            move_col.append((140,255,140))
        elif x.type == 'Electric':
            move_col.append((255,255,130))
        elif x.type == 'Psychic':
            move_col.append((255,150,200))
        elif x.type == 'Ice':
            move_col.append((200,250,255))
        elif x.type == 'Dragon':
            move_col.append((170,150,255))
        elif x.type == 'Dark':
            move_col.append((140,130,120))
        elif x.type == 'Fairy':
            move_col.append((255,200,255))
    while len(move_col) < 4:
        move_col.append((100,100,100))
    hpbar = load("p/team_hp.png")
    end = True
    move_l = []
    if pokee.m1 != None and pokee.p1 > 0:
        if pokee.taunt == 0 or moves.Move(pokee.m1).cat != '2':
            move_l.append(moves.Move(pokee.m1))
    if pokee.m2 != None and pokee.p2 > 0:
        if pokee.taunt == 0 or moves.Move(pokee.m2).cat != '2':
            move_l.append(moves.Move(pokee.m2))
    if pokee.m3 != None and pokee.p3 > 0:
        if pokee.taunt == 0 or moves.Move(pokee.m3).cat != '2':
            move_l.append(moves.Move(pokee.m3))
    if pokee.m4 != None and pokee.p4 > 0:
        if pokee.taunt == 0 or moves.Move(pokee.m4).cat != '2':
            move_l.append(moves.Move(pokee.m4))
    mv = mvnum
    while end:
        if a % 5 == 0:
            for x in range(2):
                if P.poke_m[x] > 0 and P.poke_m[x] < 5:
                    P.poke_m[x] += 1
                elif P.poke_m[x] < -1:
                    P.poke_m[x] += 1
                if P.poke_m[x] == 5:
                    P.poke_m[x] = -5
                if (x == 0 and a%100 == 0) or (x == 1 and (a-25) % 100 == 0):
                    if P.poke_m[x] == -1:
                        P.poke_m[x] = 1
        type_ico = load("p/"+movesl[mv].type+"_ico.png")
        P.surface.blit(P.animate_back,(0,0))
        P.surface.blit(pokemone,(600-(sizee/2),255-sizee-abs(P.poke_m[0])))
        blit_stat(P,pokes,pokee)
        blit_hp(P,pokes,pokee)
        P.surface.blit(pokemons, (200 - (sizes / 2), 485 - sizes - abs(P.poke_m[1])))
        P.surface.blit(back,(0,460))
        P.surface.fill(move_col[0],Rect(5,465,320,60))
        P.surface.fill(move_col[1],Rect(335,465,320,60))
        P.surface.fill(move_col[2],Rect(5,535,320,60))
        P.surface.fill(move_col[3],Rect(335,535,320,60))
        P.surface.blit(move_boxes[0],(0,460))
        P.surface.blit(move_boxes[1],(330,460))
        P.surface.blit(move_boxes[2],(0,530))
        P.surface.blit(move_boxes[3],(330,530))
        P.surface.blit(mvinfo,(660,460))
        P.surface.blit(type_ico,(680,480))
        P.surface.blit(P.font_s.render("PP",True,(0,0,0)),(710,520))
        if mv == 0:
            ppl = P.font_s.render(str(pokes.p1)+"/"+str(movesl[mv].pp),True,(0,0,0))
            ppsz = P.font_s.size(str(pokes.p1)+"/"+str(movesl[mv].pp))
        if mv == 1:
            ppl = P.font_s.render(str(pokes.p2)+"/"+str(movesl[mv].pp),True,(0,0,0))
            ppsz = P.font_s.size(str(pokes.p2)+"/"+str(movesl[mv].pp))
        if mv == 2:
            ppl = P.font_s.render(str(pokes.p3)+"/"+str(movesl[mv].pp),True,(0,0,0))
            ppsz = P.font_s.size(str(pokes.p3)+"/"+str(movesl[mv].pp))
        if mv == 3:
            ppl = P.font_s.render(str(pokes.p4)+"/"+str(movesl[mv].pp),True,(0,0,0))
            ppsz = P.font_s.size(str(pokes.p4)+"/"+str(movesl[mv].pp))
        P.surface.blit(ppl,(730-ppsz[0]/2,550))
        if pokes.m1 != None:
            P.surface.blit(move1,(165-sz1[0]/2,480))
        if pokes.m2 != None:
            P.surface.blit(move2,(495-sz2[0]/2,480))
        if pokes.m3 != None:
            P.surface.blit(move3,(165-sz3[0]/2,550))
        if pokes.m4 != None:
            P.surface.blit(move4,(495-sz4[0]/2,550))
        for event in pygame.event.get(eventtype = KEYDOWN):
            if event.key == pygame.key.key_code(P.controls[4]):
                out_pp = 0
                cat = 0
                if mv == 0:
                    if pokes.p1 == 0:
                        out_pp = 1
                    cat = moves.Move(pokes.m1).cat
                elif mv == 1:
                    if pokes.p2 == 0:
                        out_pp = 1
                    cat = moves.Move(pokes.m2).cat
                elif mv == 2:
                    if pokes.p3 == 0:
                        out_pp = 1
                    cat = moves.Move(pokes.m3).cat
                else:
                    if pokes.p4 == 0:
                        out_pp = 1
                    cat = moves.Move(pokes.m4).cat
                if out_pp == 1:
                    t = P.surface.copy()
                    new_battle_txt(P)
                    battle_write(P,movesl[mv].name + " is out of PP!")
                    cont(P)
                    P.surface.set_clip(0,0,800,600)
                    P.surface.blit(t,(0,0))
                elif cat == '2' and pokes.taunt != 0:
                    t = P.surface.copy()
                    new_battle_txt(P)
                    battle_write(P,pokes.name + " is taunted!")
                    cont(P)
                    P.surface.set_clip(0,0,800,600)
                    P.surface.blit(t,(0,0))
                else:
                    if movesl[mv].cat != '2':
                        pokes.can_sucker = True
                    if len(move_l) == 0:
                        choose = -1
                        movee = strug
                    else:
                        #choose = random.randint(0,len(move_l)-1)
                        choose = opp_AI(P,pokee,pokes,move_l)
                        movee = move_l[choose]
                    if movee.cat != '2' or pokee.cont_move != [None,0] or pokee.rollcount != 0 or pokee.bide != [0,0] or pokee.charge != None:
                        pokee.can_sucker = True
                    spds = pokes.get_spd(P)
                    spde = pokee.get_spd(P)
                    priox = movesl[mv].priority
                    prioe = movee.priority
                    if pokes.ability == 'Prankster' and movesl[mv].cat == '2':
                        priox += 1
                    if pokee.ability == 'Prankster' and movee.cat == '2':
                        prioe += 1
                    if priox > prioe or (pokee.item == 'Full Incense' or pokee.ability == 'Stall'):
                        spds = 1
                        spde = 0
                    elif priox < prioe or (pokes.item == 'Full Incense' or pokes.ability == 'Stall'):
                        spde = 1
                        spds = 0
                    if spde > spds:
                        opp_move(P,pokes,pokee,movee,move_back,strug,choose)
                        opp = 0
                    else:
                        opp = 1
                    if pokes.status != 'Faint':
                        orige = pokee.copy()
                        origs = pokes.copy()
                        eff = movesl[mv].cast(P,pokes,pokee,mv,0)
                        battle_move_use(P,origs,orige,pokes,pokee,move_back,eff,1)
                        count = eff[4]
                        if movesl[mv].name == 'Metronome':
                            movesl[mv] = moves.Move(P.metronome)
                        for x in range(count):
                            if pokee.ch == 0 or pokes.ch == 0:
                                break
                            eff = movesl[mv].use(P,pokes,pokee,0)
                            battle_move_use(P,origs,orige,pokes,pokee,move_back,eff,x+2)
                        if count != 0 and pokes.ch != 0 and pokee.ch != 0:
                            new_battle_txt(P)
                            battle_write(P,"Hit " + str(count+1) + " times!")
                            P.clock.tick(P.bat_spd)
                        P.gem_active = False
                    end = False
            if event.key == pygame.key.key_code(P.controls[5]):
                opp = 0
                return [mv,a]
            if event.key == pygame.key.key_code(P.controls[0]) and mv > 1:
                mv -= 2
                move_boxes[mv] = move_box2
                move_boxes[mv+2] = move_box1
            if event.key == pygame.key.key_code(P.controls[1]) and mv < 2 and mv+2 < len(movesl):
                mv += 2
                move_boxes[mv] = move_box2
                move_boxes[mv-2] = move_box1
            if event.key == pygame.key.key_code(P.controls[2]) and mv%2 == 1:
                mv -= 1
                move_boxes[mv] = move_box2
                move_boxes[mv+1] = move_box1
            if event.key == pygame.key.key_code(P.controls[3]) and mv%2 == 0 and mv+1 < len(movesl):
                mv += 1
                move_boxes[mv] = move_box2
                move_boxes[mv-1] = move_box1
        a += 1
        P.clock.tick(P.ani_spd)
        update_screen(P)
    if opp == 1 and pokee.status != 'Faint':
        opp_move(P,pokes,pokee,movee,move_back,strug,choose)
    P.surface.set_clip((0,0,800,460))
    EOT_effects(P,pokes,pokee,0,move_back)
    EOT_effects(P,pokee,pokes,1,move_back)
    P.turn_count += 1
    pokes = reset_move_stat(P,pokes)
    pokee = reset_move_stat(P,pokee)
    if P.echoed[1] == 1:
        P.echoed = [0,0]
    if P.echoed[1] != 0:
        P.echoed[1] -= 1
    return (mv,a)

def poke_faint(P,poke) -> None:
    if poke.status != 'Faint':
        new_battle_txt(P)
        battle_write(P,poke.get_name() + " fainted!")
        P.clock.tick(P.bat_spd)
        poke.status = 'Faint'
        poke.friend -= int(poke.friend*0.1)
        poke.reset_stats()
        if poke.code == 'Kangaskhan_M':
            P.party[1].status = 'Faint'
            P.party[1].ch = 0

def battle_move_draw(P,origs,orige,pokes,pokee,move_back):
    pokemons = pygame.transform.scale(load('p/poke/'+pokes.code+"_bb.png"),(410,410))
    P.surface.blit(move_back,(0,0))
    blit_hp(P,origs,orige)
    blit_stat(P,origs,orige)
    P.surface.blit(pokemons, (-5, 75 - abs(P.poke_m[1])))
    update_screen(P)

def hp_change(P,op,oe,poke,pokee,move_back):
    if op.ch != poke.ch:
        pok = poke
        o = op
    else:
        pok = pokee
        o = oe
    end = True
    while end:
        for x in range(1+int(pok.hp/100)):
            if pok.ch < o.ch:
                o.ch -= 1
            elif pok.ch > o.ch:
                o.ch += 1
            else:
                end = False
        battle_move_draw(P,op,oe,poke,pokee,move_back)
        P.clock.tick(P.ani_spd)
    if pok.item != None and items.Item(pok.item).type[0] == 'Battle Berry' and pok.bugbite:
        if o == op:
            e = pokee
            eo = oe
        else:
            e = poke
            eo = op
        new_battle_txt(P)
        battle_write(P,e.get_name() + " stole and", "ate the "+pok.item+"!")
        P.clock.tick(P.bat_spd)
        if pok.item in ['Sitrus Berry','Oran Berry']:
            if e.ch != e.hp:
                new_battle_txt(P)
                battle_write(P,e.get_name() + " restored", "HP using its "+pok.item+"!")
                P.clock.tick(P.bat_spd)
            if pok.item == 'Sitrus Berry':
                e.ch += int(e.hp/4)
            else:
                e.ch += 10
            if e.ch > e.hp:
                e.ch = e.hp
            if o == op:
                hp_change(P,o,oe,pok,e,move_back)
            else:
                hp_change(P,op,o,e,pok,move_back)
        else:
            if e.status in items.Item(pok.item).mod()[0] or ((items.Item(pok.item).name == 'Lum Berry' or items.Item(pok.item).name == 'Persim Berry') and e.cfs > 0):
                new_battle_txt(P)
                battle_write(P,e.get_name() + " ate its", pok.item+"!")
                P.clock.tick(P.bat_spd)
                new_battle_txt(P)
                s = items.Item(pok.item).mod()[0][0]
                if items.Item(pok.item).name == 'Lum Berry':
                    if e.cfs > 0:
                        e.cfs = 0
                        eo.cfs = 0
                        battle_write(P,e.name + " was cured", "of confusion!")
                        if e.status != None:
                            P.clock.tick(P.bat_spd)
                            new_battle_txt(P)
                    s = e.status
                if s == None:
                    pass
                elif s == 'Slp':
                    battle_write(P,e.name + " woke up!")
                elif s == 'Frz':
                    battle_write(P,e.name + " thawed","out!")
                elif s == 'Brn':
                    battle_write(P,e.name + " burn was","healed!")
                else:
                    sta = items.Item(pok.item).mod()[1]
                    if items.Item(pok.item).name == 'Lum Berry':
                        if s == 'Par':
                            sta = 'Paralysis'
                        else:
                            sta = 'Poisoning'
                    battle_write(P,e.name + " was cured", "of "+sta+"!")
                P.clock.tick(P.bat_spd)
                if items.Item(pok.item).name == 'Persim Berry':
                    e.cfs = 0
                    eo.cfs = 0
                else:
                    e.status = None
                    eo.status = None
        pok.item = None
        pok.bugbite = False
    if o.item == 'Sitrus Berry' and o.ch/o.hp < 0.5 and o.ch != 0:
        new_battle_txt(P)
        battle_write(P,o.get_name() + " ate its", "Sitrus Berry!")
        P.clock.tick(P.bat_spd)
        new_battle_txt(P)
        battle_write(P,o.get_name() + " restored", "HP using its Sitrus Berry!")
        P.clock.tick(P.bat_spd)
        pok.ch += int(pok.hp/4)
        if o == op:
            hp_change(P,o,oe,pok,pokee,move_back)
        else:
            hp_change(P,op,o,poke,pok,move_back)
        pok.item = None
    elif o.item == 'Oran Berry' and o.ch/o.hp < 0.5 and o.ch != 0:
        new_battle_txt(P)
        battle_write(P,o.get_name() + " ate its", "Oran Berry!")
        P.clock.tick(P.bat_spd)
        new_battle_txt(P)
        battle_write(P,o.get_name() + " restored", "HP using its Oran Berry!")
        P.clock.tick(P.bat_spd)
        pok.ch += 10
        if pok.ch > pok.hp:
            pok.ch = pok.hp
        if o == op:
            hp_change(P,o,oe,pok,pokee,move_back)
        else:
            hp_change(P,op,o,poke,pok,move_back)
        pok.item = None

def take_damage(P,op,oe,poke,pokee,move_back,eff):
    turn = 0
    if not op.equals(poke):
        turn = 1
    hp_change(P,op,oe,poke,pokee,move_back)
    op.ch = poke.ch
    oe.ch = pokee.ch
    if eff[1] == True:
        new_battle_txt(P)
        battle_write(P,"It was a critical hit!")
        P.clock.tick(P.bat_spd)
    if eff[0] == 1:
        new_battle_txt(P)
        battle_write(P,"It's not very effective...")
        P.clock.tick(P.bat_spd)
    elif eff[0] == 2:
        new_battle_txt(P)
        battle_write(P,"It's super effective!")
        P.clock.tick(P.bat_spd)
    if eff[2] != 0:
        if turn == 0 and not poke.explode:
            new_battle_txt(P)
            battle_write(P,poke.get_name() + " was", "damaged by the recoil!")
            P.clock.tick(P.bat_spd)
        elif turn == 1 and not pokee.explode:
            new_battle_txt(P)
            battle_write(P,pokee.get_name() + " was", "damaged by the recoil!")
            P.clock.tick(P.bat_spd)
        if turn == 0:
            poke.take_damage(P,eff[2])
            #poke.ch -= eff[2]
        else:
            pokee.take_damage(P,eff[2])
            #pokee.ch -= eff[2]
        hp_change(P,op,oe,poke,pokee,move_back)
        op.ch = poke.ch
        oe.ch = pokee.ch
    for pos,xy in enumerate(eff[3]):
        if xy[0] == 5:
            new_battle_txt(P)
            battle_write(P,xy[2] + " was hurt!")
            if xy[3] == 0:
                show_ability(P,"Rough Skin",turn)
            else:
                show_ability(P,"Iron Barbs",turn)
            P.clock.tick(P.bat_spd)
            if turn == 0:
                poke.take_damage(P,xy[1])
                #poke.ch -= xy[1]
            else:
                pokee.take_damage(P,xy[1])
                # pokee.ch -= xy[1]
            hp_change(P,op,oe,poke,pokee,move_back)
            op.ch = poke.ch
            oe.ch = pokee.ch
            del eff[3][pos]
    if eff[5] != 0:
        new_battle_txt(P)
        if turn == 0:
            battle_write(P,pokee.get_name() + " had its", "energy drained!")
        else:
            battle_write(P,poke.get_name() + " had its", "energy drained!")
        P.clock.tick(P.bat_spd)
        if turn == 0:
            poke.ch += eff[5]
        else:
            pokee.ch += eff[5]
        hp_change(P,op,oe,poke,pokee,move_back)
        op.ch = poke.ch
        oe.ch = pokee.ch

def give_status_eff(P,poke,orig):
    if poke.ch == 0:
        return
    if orig.cfs == 0 and poke.cfs > 0 and poke.ch != 0:
        orig.cfs = poke.cfs
        new_battle_txt(P)
        battle_write(P,poke.get_name()+" became", "confused!")
        P.clock.tick(P.bat_spd)
    if orig.inf == False and poke.inf == True and poke.ch != 0:
        orig.inf = poke.inf
        new_battle_txt(P)
        battle_write(P,poke.get_name()+" fell in", "love!")
        P.clock.tick(P.bat_spd)
    if poke.idf != orig.idf and poke.ch != 0:
        new_battle_txt(P)
        battle_write(P,poke.get_name()+" was", "identified!")
        P.clock.tick(P.bat_spd)
        orig.idf = poke.idf
    if orig.status != poke.status and poke.ch != 0:
        orig.status = poke.status
        if poke.status == 'Psn':
            new_battle_txt(P)
            battle_write(P,poke.get_name()+" was", "poisoned!")
            P.clock.tick(P.bat_spd)
        if poke.status == 'Brn':
            new_battle_txt(P)
            battle_write(P,poke.get_name()+" was", "burned!")
            P.clock.tick(P.bat_spd)
        if poke.status == 'BPs':
            new_battle_txt(P)
            battle_write(P,poke.get_name()+" was badly", "poisoned!")
            P.clock.tick(P.bat_spd)
        if poke.status == 'Par':
            new_battle_txt(P)
            battle_write(P,poke.get_name()+" was", "paralyzed!")
            P.clock.tick(P.bat_spd)
        if poke.status == 'Slp':
            if poke.rest:
                poke.rest = False
            else:
                new_battle_txt(P)
                battle_write(P,poke.get_name()+" fell", "asleep!")
                P.clock.tick(P.bat_spd)
        if poke.status == 'Frz':
            new_battle_txt(P)
            battle_write(P,poke.get_name()+" was", "frozen!")
            P.clock.tick(P.bat_spd)
    if poke.item != None and items.Item(poke.item).type[0] == 'Battle Berry' and type(items.Item(poke.item).mod()) == list:
        if poke.status in items.Item(poke.item).mod()[0] or ((items.Item(poke.item).name == 'Lum Berry' or items.Item(poke.item).name == 'Persim Berry') and poke.cfs > 0):
            new_battle_txt(P)
            battle_write(P,poke.get_name() + " ate its", poke.item+"!")
            P.clock.tick(P.bat_spd)
            new_battle_txt(P)
            s = items.Item(poke.item).mod()[0][0]
            if items.Item(poke.item).name == 'Lum Berry':
                if poke.cfs > 0:
                    poke.cfs = 0
                    orig.cfs = 0
                    battle_write(P,poke.name + " was cured", "of confusion!")
                    if poke.status != None:
                        P.clock.tick(P.bat_spd)
                        new_battle_txt(P)
                s = poke.status
            if s == None:
                pass
            elif s == 'Slp':
                battle_write(P,poke.name + " woke up!")
            elif s == 'Frz':
                battle_write(P,poke.name + " thawed","out!")
            elif s == 'Brn':
                battle_write(P,poke.name + " burn was","healed!")
            else:
                sta = items.Item(poke.item).mod()[1]
                if items.Item(poke.item).name == 'Lum Berry':
                    if s == 'Par':
                        sta = 'Paralysis'
                    else:
                        sta = 'Poisoning'
                battle_write(P,poke.name + " was cured", "of "+sta+"!")
            P.clock.tick(P.bat_spd)
            if items.Item(poke.item).name == 'Persim Berry':
                poke.cfs = 0
                orig.cfs = 0
            else:
                poke.status = None
                orig.status = None
            poke.item = None
            orig.item = None

def stat_write(P,name,poke,orig,stat):
    new_battle_txt(P)
    word = ''
    stat1 = stat
    stat2 = ''
    if ' ' in stat:
        stat1 = stat[:stat.find(' ')]
        stat2 = stat[stat.find(' ')+1:]+' '
    if poke - orig == -1:
        word = 'fell!'
        if stat == 'evasion':
            word = 'rose!'
    elif poke - orig == 1:
        word = 'rose!'
        if stat == 'evasion':
            word = 'fell!'
    elif poke - orig < -1:
        word = 'harshly fell!'
        if stat == 'evasion':
            word = 'sharply rose!'
    elif poke - orig > 1:
        word = 'sharply rose!'
        if stat == 'evasion':
            word = 'harshly fell!'
    battle_write(P,name+"'s "+stat1, stat2 + word)
    P.clock.tick(P.bat_spd)

def stat_message(P,poke,orig):
    if P.haze_active > 0:
        P.haze_active -= 1
        return
    if poke.ch == 0 or poke.bellydrum:
        poke.bellydrum = False
        return
    if poke.dfm != orig.dfm:
        stat_write(P,poke.get_name(),poke.dfm,orig.dfm,'defense')
        orig.dfm = poke.dfm
    if poke.sdfm != orig.sdfm:
        stat_write(P,poke.get_name(),poke.sdfm,orig.sdfm,'special defense')
        orig.sdfm = poke.sdfm
    if poke.akm != orig.akm:
        stat_write(P,poke.get_name(),poke.akm,orig.akm,'attack')
        orig.akm = poke.akm
    if poke.sakm != orig.sakm:
        stat_write(P,poke.get_name(),poke.sakm,orig.sakm,'special attack')
        orig.sakm = poke.sakm
    if poke.spdm != orig.spdm:
        stat_write(P,poke.get_name(),poke.spdm,orig.spdm,'speed')
        orig.spdm = poke.spdm
    if poke.accm != orig.accm:
        stat_write(P,poke.get_name(),poke.accm,orig.accm,'accuracy')
        orig.accm = poke.accm
    if poke.evam != orig.evam:
        stat_write(P,poke.get_name(),poke.evam,orig.evam,'evasion')
        orig.evam = poke.evam

def battle_move_use(P,origs,orige,poke,pokee,move_back,eff,repeat = 0) -> None:
    P.surface.set_clip((0,0,800,460))
    origs.p1 = poke.p1
    origs.p2 = poke.p2
    origs.p3 = poke.p3
    origs.p4 = poke.p4
    orige.p1 = pokee.p1
    orige.p2 = pokee.p2
    orige.p3 = pokee.p3
    orige.p4 = pokee.p4
    for pos,xy in enumerate(eff[3]):
        if xy[0] == 6:
            new_battle_txt(P)
            battle_write(P,xy[2] + " was", 'damaged by the Spiky Shield!')
            P.clock.tick(P.bat_spd)
            if poke.spikyshield:
                pokee.take_damage(P,xy[1])
                #pokee.ch -= xy[1]
                hp_change(P,origs,orige,origs,pokee,move_back)
            else:
                poke.take_damage(P,xy[1])
                #poke.ch -= xy[1]
                hp_change(P,origs,orige,poke,orige,move_back)
                # origs.ch = poke.ch
            del eff[3][pos]
    if pokee.equals(orige) and poke.equals(origs):
        #return
        pass
    if poke.ch != origs.ch:
        take_damage(P,origs,orige,poke,pokee,move_back,eff)
        # origs.ch = poke.ch
    give_status_eff(P,poke,origs)
    give_status_eff(P,pokee,orige)
    battle_move_draw(P,origs,orige,poke,pokee,move_back)
    if pokee.ch != orige.ch:
        take_damage(P,origs,orige,poke,pokee,move_back,eff)
        # orige.ch = pokee.ch
    give_status_eff(P,poke,origs)
    give_status_eff(P,pokee,orige)
    battle_move_draw(P,origs,orige,poke,pokee,move_back)
    stat_message(P,poke,origs)
    stat_message(P,pokee,orige)
    for pos,xy in enumerate(eff[3]):
        if xy[0] == 1:
            xy[3].status = xy[4]
            new_battle_txt(P)
            if xy[4] == 'Slp':
                battle_write(P,xy[3].get_name()+" fell", xy[5])
            else:
                battle_write(P,xy[3].get_name()+" was", xy[5])
            show_ability(P,xy[1],xy[2])
            if xy[3].item != None and items.Item(xy[3].item).type[0] == 'Battle Berry' and type(items.Item(xy[3].item).mod()) == list:
                if xy[3].status in items.Item(xy[3].item).mod()[0] or ((items.Item(xy[3].item).name == 'Lum Berry' or items.Item(xy[3].item).name == 'Persim Berry') and xy[3].cfs > 0):
                    new_battle_txt(P)
                    battle_write(P,xy[3].get_name() + " ate its", xy[3].item+"!")
                    P.clock.tick(P.bat_spd)
                    new_battle_txt(P)
                    s = items.Item(xy[3].item).mod()[0][0]
                    if items.Item(xy[3].item).name == 'Lum Berry':
                        if xy[3].cfs > 0:
                            xy[3].cfs = 0
                            battle_write(P,xy[3].name + " was cured", "of confusion!")
                            if xy[3].status != None:
                                P.clock.tick(P.bat_spd)
                                new_battle_txt(P)
                        s = xy[3].status
                    if s == None:
                        pass
                    elif s == 'Slp':
                        battle_write(P,xy[3].name + " woke up!")
                    elif s == 'Frz':
                        battle_write(P,xy[3].name + " thawed","out!")
                    elif s == 'Brn':
                        battle_write(P,xy[3].name + " burn was","healed!")
                    else:
                        sta = items.Item(xy[3].item).mod()[1]
                        if items.Item(xy[3].item).name == 'Lum Berry':
                            if s == 'Par':
                                sta = 'Paralysis'
                            else:
                                sta = 'Poisoning'
                        battle_write(P,xy[3].name + " was cured", "of "+sta+"!")
                    P.clock.tick(P.bat_spd)
                    if items.Item(xy[3].item).name == 'Persim Berry':
                        xy[3].cfs = 0
                    else:
                        xy[3].status = None
                    xy[3].item = None
        if xy[0] == 2:
            if xy[1][0] != "":
                new_battle_txt(P)
                battle_write(P,xy[1][0],xy[1][1])
            show_ability(P,xy[2],xy[3])
        if xy[0] == 3:
            stat1 = xy[2]
            stat2 = ''
            if ' ' in xy[2]:
                stat1 = xy[2][:xy[2].find(' ')]
                stat2 = xy[2][xy[2].find(' ')+1:]+' '
            new_battle_txt(P)
            battle_write(P,xy[1] + "'s " + stat1, stat2 + "won't go any higher!")
            P.clock.tick(P.bat_spd)
        if xy[0] == 4:
            stat1 = xy[2]
            stat2 = ''
            if ' ' in xy[2]:
                stat1 = xy[2][:xy[2].find(' ')]
                stat2 = xy[2][xy[2].find(' ')+1:]+' '
            new_battle_txt(P)
            battle_write(P,xy[1] + "'s " + stat1, stat2 + "won't go any lower!")
            P.clock.tick(P.bat_spd)
        if xy[0] == 7:
            new_battle_txt(P)
            if len(xy) == 2:
                battle_write(P,xy[1])
            else:
                battle_write(P,xy[1],xy[2])
            P.clock.tick(P.bat_spd)
        if xy[0] == 8:
            xy[1].inf = True
            new_battle_txt(P)
            battle_write(P,xy[1].get_name() +" fell in", "love!")
            show_ability(P,'Cute Charm',xy[2])
        if xy[0] == 9:
            if xy[1] == poke:
                origs.akm += 1
            else:
                orige.akm += 1
            xy[1].akm += 1
            if xy[1].ch != 0:
                new_battle_txt(P)
                battle_write(P,xy[1].get_name() +"'s attack","rose!")
                show_ability(P,'Moxie',xy[2])
        del eff[3][pos]
    if poke.ch == 0:
        if eff[4] != 0:
            new_battle_txt(P)
            battle_write(P,"Hit " + str(repeat) + " times!")
            P.clock.tick(P.bat_spd)
        pokee.trapped = [None,0]
        poke_faint(P,poke)
    if pokee.ch == 0:
        if eff[4] != 0:
            new_battle_txt(P)
            battle_write(P,"Hit " + str(repeat) + " times!")
            P.clock.tick(P.bat_spd)
        poke.trapped = [None,0]
        poke_faint(P,pokee)
        

def mem(P) -> None:
    save = open("save_files/" + P.save_data.name + ".txt", "w")
    save.write("['"+P.save_data.name + "','"+P.save_data.starter+"']\n")
    save.write(str(P.save_data.gen) + "\n")
    save.write(str(P.px) + "\n")
    save.write(str(P.py) + "\n")
    if P.p == P.r1 or P.p == P.r2 or P.p == P.r3:
        save.write("r\n")
    elif P.p == P.l1 or P.p == P.l2 or P.p == P.l3:
        save.write("l\n")
    elif P.p == P.u1 or P.p == P.u2 or P.p == P.u3:
        save.write("u\n")
    else:
        save.write("d\n")
    save.write(str([P.loc,P.save_data.pc])+"\n")
    save.write(str(P.prog)+"\n")
    save.write(str(poke_party_to_list(P.party))+"\n")
    save.write(str(P.save_data.money)+'\n')
    save.write(str(P.bag)+'\n')
    save.write(str(P.save_data.box)+'\n')
    update_time(P)
    save.write(str(P.save_data.time)+'\n')
    save.write(str(P.save_data.register)+'\n')
    save.write(str(P.save_data.pokedex)+'\n')

def update_time(P):
    temptime = P.save_data.start_time
    P.save_data.start_time = datetime.datetime.now()
    diff = P.save_data.start_time-temptime
    sec = int(diff.total_seconds()%60)
    rem = int((diff.total_seconds()-sec)/60)
    min = int(rem%60)
    hour = int((rem-min)/60)
    print(hour,min,sec)
    P.save_data.time[2] += sec
    if P.save_data.time[2] >= 60:
        P.save_data.time[2] -= 60
        min += 1
    P.save_data.time[1] += min
    if P.save_data.time[1] >= 60:
        P.save_data.time[1] -= 60
        hour += 1
    P.save_data.time[0] += hour

def load_trainer(P) -> None:
    if P.save_data.gen == 0:
        let = 'b'
    else:
        let = 'g'
    P.r1 = pygame.transform.scale(load("p/spr/"+let+"r1.png"),(50,60))
    P.r2 = pygame.transform.scale(load("p/spr/"+let+"r2.png"),(50,60))
    P.r3 = pygame.transform.scale(load("p/spr/"+let+"r3.png"),(50,60))
    P.l1 = pygame.transform.scale(load("p/spr/"+let+"l1.png"),(50,60))
    P.l2 = pygame.transform.scale(load("p/spr/"+let+"l2.png"),(50,60))
    P.l3 = pygame.transform.scale(load("p/spr/"+let+"l3.png"),(50,60))
    P.u1 = pygame.transform.scale(load("p/spr/"+let+"u1.png"),(50,60))
    P.u2 = pygame.transform.scale(load("p/spr/"+let+"u2.png"),(50,60))
    P.u3 = pygame.transform.scale(load("p/spr/"+let+"u3.png"),(50,60))
    P.d1 = pygame.transform.scale(load("p/spr/"+let+"d1.png"),(50,60))
    P.d2 = pygame.transform.scale(load("p/spr/"+let+"d2.png"),(50,60))
    P.d3 = pygame.transform.scale(load("p/spr/"+let+"d3.png"),(50,60))
    if P.save_data.dir == "r\n":
        P.p = P.r1
    elif P.save_data.dir == "l\n":
        P.p = P.l1
    elif P.save_data.dir == "u\n":
        P.p = P.u1
    else:
        P.p = P.d1
            
def npc_move(P, move = [0,0,0,0], xy = []) -> None:
    #right left up down
    if xy == []:
        xy = [P.px,P.py]
    P.surface.blit(P.n,(P.nx+xy[0],P.ny+xy[1]))
    if move[0] == 1 and P.npcy == 0:
        if P.npcx == 0:
            P.n = P.nr2
        P.npcx = 1
    elif move[1] == 1 and P.npcy == 0:
        if P.npcx == 0:
            P.n = P.nl2
        P.npcx = -1
    else:
        P.npcx = 0
    if move[2] == 1 and P.npcx == 0:
        if P.npcy == 0:
            P.n = P.nu2
        P.npcy = 1
    elif move[3] == 1 and P.npcx == 0:
        if P.npcy == 0:
            P.n = P.nd2
        P.npcy = -1
    else:
        P.npcy = 0
    if (P.npcx == 1 or P.nxr != 0):
        P.nx += 5
        P.nxr += 5
        if P.nx % 25 == 0:
            if P.n == P.nr2:
                P.n = P.nr3
            else:
                P.n = P.nr2
    if (P.npcx == -1 or P.nxl != 0):
        P.nx -= 5
        P.nxl += 5
        if P.nx % 25 == 0:
            if P.n == P.nl2:
                P.n = P.nl3
            else:
                P.n = P.nl2
    if (P.npcy == 1 or P.nyu != 0):
        P.ny -= 5
        P.nyu += 5
        if P.ny % 25 == 0:
            if P.n == P.nu2:
                P.n = P.nu3
            else:
                P.n = P.nu2
    if (P.npcy == -1 or P.nyd != 0):
        P.ny += 5
        P.nyd += 5
        if P.ny % 25 == 0:
            if P.n == P.nd2:
                P.n = P.nd3
            else:
                P.n = P.nd2
    if P.nxr == 50:
        P.nxr = 0
    if P.nxl == 50:
        P.nxl = 0
    if P.nyu == 50:
        P.nyu = 0
    if P.nyd == 50:
        P.nyd = 0
    if P.npcx == 0 and P.nxr == 0:
        if P.n == P.nr2 or P.n == P.nr3:
            P.n = P.nr1
    if P.npcx == 0 and P.nxl == 0:
        if P.n == P.nl2 or P.n == P.nl3:
            P.n = P.nl1
    if P.npcy == 0 and P.nyu == 0:
        if P.n == P.nu2 or P.n == P.nu3:
            P.n = P.nu1
    if P.npcy == 0 and P.nyd == 0:
        if P.n == P.nd2 or P.n == P.nd3:
            P.n= P.nd1
    pygame.event.pump()

def add_item(P,item,number) -> None:
    i = items.Item(item)
    found = False
    if i.type[1] == 'Item':
        for a in P.bag[0]:
            if a[0] == item:
                found = True
                a[1] += number
                if a[1] == 0:
                    P.bag[0].remove(a)
        if found == False:
            P.bag[0].append([item,number])
    if i.type[1] == 'Medicine':
        for a in P.bag[1]:
            if a[0] == item:
                found = True
                a[1] += number
                if a[1] == 0:
                    P.bag[1].remove(a)
        if found == False:
            P.bag[1].append([item,number])
    if i.type[1] == 'Ball':
        for a in P.bag[2]:
            if a[0] == item:
                found = True
                a[1] += number
                if a[1] == 0:
                    P.bag[2].remove(a)
        if found == False:
            P.bag[2].append([item,number])
    if i.type[1] == 'TM':
        for a in P.bag[3]:
            if a[0] == item:
                found = True
                a[1] += number
                if a[1] == 0:
                    P.bag[3].remove(a)
        if found == False:
            P.bag[3].append([item,number])
    if i.type[1] == 'Key':
        for a in P.bag[4]:
            if a[0] == item:
                found = True
                a[1] += number
                if a[1] == 0:
                    P.bag[4].remove(a)
        if found == False:
            P.bag[4].append([item,number])
    #order bag
    for cat in P.bag:
        cat.sort()

def battle_bag(P) -> list:
    box = load("p/bag_box.png")
    back = load("p/bag.png")
    i = load("p/item_ico.png")
    m = load("p/med_ico.png")
    b = load("p/balls_ico.png")
    t = load("p/tm_ico.png")
    k = load("p/key_ico.png")
    high = load("p/bag_high.png")
    ico = i
    ix = 0
    scroll = 0
    scroll_spd = 10
    scroll_mod = 0
    bag = 0
    a = 0
    curr = ['',0]
    su = False
    sd = False
    end = True
    while end:
        P.surface.blit(back,(0,0))
        P.surface.blit(ico,(ix,0))
        title = "ITEMS"
        if bag == 1:
            title = "MEDICINE"
        if bag == 2:
            title = "BALLS"
        if bag == 3:
            title = "TMs"
        if bag == 4:
            title = "KEY ITEMS"
        tle = P.font.render(title,True,(255,255,255))
        P.surface.blit(tle,((400-(P.font.size(title)[0]))/2,85))
        y = 0
        if scroll <= 280:
            s = 0
        elif scroll >= (((len(P.bag[bag])-1)*70)-210):
            if len(P.bag[bag]) < 8:
                s = 0
            else:
                s = (((len(P.bag[bag])-1)*70))-490
        else:
            s = scroll-280
        for z in P.bag[bag]:
            txt = P.font_s.render(z[0],True,(0,0,0))
            size_x = (360-(P.font_s.size(z[0])[0]))/2
            if z[0] in P.save_data.register:
                txt = P.font_s.render("???"+z[0]+"???",True,(0,0,0))
                size_x = (360-(P.font_s.size("???"+z[0]+"???")[0]))/2
            P.surface.blit(box,(420,20-s+y))
            P.surface.blit(txt,(420+size_x,35-s+y))
            if z == P.bag[bag][int(scroll/70)]:
                P.surface.blit(high,(420,20-s+y))
                curr = z
            y += 70
        if(curr != ['',0]):
            txt = P.font_s.render(curr[0],True,(0,0,0))
            txt2 = P.font_s.render(' x '+str(curr[1]),True,(0,0,0))
            P.surface.blit(txt,((380-P.font_s.size(curr[0])[0])/2,150))
            P.surface.blit(txt2,(180,195))
            ic = pygame.transform.scale(load("p/item/"+curr[0]+".png"),(50,50))
            P.surface.blit(ic,(130,185))
            item = items.Item(curr[0])
            descr = []
            cngy = 0
            for x in item.desc:
                descr.append(P.font_s.render(x,True,(0,0,0)))
            for x in descr:
                P.surface.blit(x,(20,240+cngy))
                cngy += 34
        temp = P.surface.copy()
        if a == 0:
            fade_in(P)
        if scroll%70 == 0:
            for event in pygame.event.get(eventtype = KEYDOWN):
                if event.key == pygame.key.key_code(P.controls[4]) and a>10 and curr != ['',0]:
                    it = items.Item(curr[0]).battle_menu(P,curr[1])
                    a = 0
                    if it != '':
                        if items.Item(it).type[0] == 'Ball':
                            fade_out(P)
                            return [it,None]
                        elif items.Item(it).type[0] == 'Potion' or items.Item(it).type[0] == 'Battle Berry':
                            fade_out(P)
                            target = items.Item(it).use_item(P,True)
                            if target:
                                return [it,target]
                            else:
                                P.surface.blit(temp,(0,0))
                                fade_in(P)
                if event.key == pygame.key.key_code(P.controls[5]) and a > 10:
                    fade_out(P)
                    return ['',None]
                elif event.key == pygame.key.key_code(P.controls[2]) and a > 10:
                    if bag != 0:
                        curr = ['',0]
                        scroll = 0
                        bag -= 1
                        ix -= 80
                        if bag == 0:
                            ico = i
                        if bag == 1:
                            ico = m
                        if bag == 2:
                            ico = b
                        if bag == 3:
                            ico = t
                elif event.key == pygame.key.key_code(P.controls[3]) and a > 10:
                    if bag != 4:
                        curr = ['',0]
                        scroll = 0
                        bag += 1
                        ix += 80
                        if bag == 1:
                            ico = m
                        if bag == 2:
                            ico = b
                        if bag == 3:
                            ico = t
                        if bag == 4:
                            ico = k
        keys = pygame.key.get_pressed()
        if scroll%70 == 0:
            su = False
            sd = False
        if keys[pygame.key.key_code(P.controls[0])] and scroll > 0 and sd == False:
            su = True
        if keys[pygame.key.key_code(P.controls[1])] and scroll < (len(P.bag[bag])-1)*70 and su == False:
            sd = True
        if(su):
            if scroll_mod > 50 and scroll_spd == 10:
                if scroll%70 == 0:
                    scroll_spd = 35
            if scroll_mod <= 50 and scroll_spd == 35:
                if scroll%70 == 0:
                    scroll_spd = 10
            scroll -= scroll_spd
            scroll_mod += 1
        elif(sd):
            if scroll_mod > 50 and scroll_spd == 10:
                if scroll%70 == 0:
                    scroll_spd = 35
            if scroll_mod <= 50 and scroll_spd == 35:
                if scroll%70 == 0:
                    scroll_spd = 10
            scroll += scroll_spd
            scroll_mod += 1
        else:
            scroll_mod = 0
        a += 1
        P.clock.tick(P.ani_spd)
        update_screen(P)
    fade_out(P)

def item_in_bag(P,item):
    if items.Item(item).type[1] == 'Item':
        pos = 0
    elif items.Item(item).type[1] == 'Medicine':
        pos = 1
    elif items.Item(item).type[1] == 'Ball':
        pos = 2
    elif items.Item(item).type[1] == 'TM':
        pos = 3
    else:
        pos = 4
    for i in P.bag[pos]:
        if i[0] == item:
            return i[1]
    return 0

def dex_entry(P,pokes,fade,from_dex = True):
    back2 = load("p/Dex_Info.png")
    if from_dex == False:
        back2 = load("p/Dex_Info_2.png")
    back0 = load("p/Dex_Info_0.png")
    back1 = load("p/Dex_Info_1.png")
    back = back2
    mega = pygame.transform.scale(load("p/mega_symbol.png"),(30,30))
    grass_ico = pygame.transform.scale(load("p/grass_icon.png"),(20,20))
    cave_ico = pygame.transform.scale(load("p/cave_icon.png"),(22,22))
    beach_ico = pygame.transform.scale(load("p/beach_icon.png"),(22,22))
    caught = P.save_data.pokedex[pokes][0]
    if caught == 0:
        box = load("p/dex_box0.png")
    else:
        box = load("p/dex_box1.png")
    f = open("poke/"+pokes+".txt")
    data = f.readlines()
    dex = int(data[8])
    num = ""
    if dex < 10:
        num += "0"
    if dex < 100:
        num += "0"
    num += str(dex)
    if pokes[:5] == 'Mega_':
        txt0 = P.font.render(num+" "+pokes[5:],True,(0,0,0))
    elif pokes[-2:] == '_M':
        txt0 = P.font.render(num+" "+pokes[:-2]+"???",True,(0,0,0))
    elif pokes[-2:] == '_F':
        txt0 = P.font.render(num+" "+pokes[:-2]+"???",True,(0,0,0))
    elif pokes == 'Mime Jr':
        txt0 = P.font.render(num+" "+"Mime Jr.",True,(0,0,0))
    elif pokes == 'Mr Mime':
        txt0 = P.font.render(num+" "+"Mr. Mime",True,(0,0,0))
    elif pokes[:10] == 'Pineapple_':
        txt0 = P.font.render(num+" "+pokes[10:],True,(0,0,0))
    else:
        txt0 = P.font.render(num+" "+pokes,True,(0,0,0))
    type = P.font_s.render("Type:",True,(0,0,0))
    ft = int(int((data[7]))/12)
    inchi = int((data[7]))-(ft*12)
    inch = ""
    if inchi < 10:
        inch += "0"
    inch += str(inchi)
    locations = []
    if caught == 1:
        cat = P.font_s.render(ast.literal_eval(data[10])[0]+" Pokemon",True,(0,0,0))
        desc = []
        d = ast.literal_eval(data[10])
        for entry in range(len(d)):
            if entry != 0:
                desc.append(P.font_s.render(d[entry],True,(80,25,0)))
        height = P.font_s.render("Height: "+str(ft)+"'"+inch+'"',True,(0,0,0))
        weight = P.font_s.render("Weight: "+str(round(float(data[6])*2.20462,1))+" lbs.",True,(0,0,0))
        type1 = load("p/"+ast.literal_eval(data[2])[0]+"_ico.png")
        if ast.literal_eval(data[2])[1] != None:
            type2 = load("p/"+ast.literal_eval(data[2])[1]+"_ico.png")
        else:
            type2 = None
        if ast.literal_eval(data[9]) == []:
            locations.append([P.font_vs.render("Unknown",True,(0,0,0)),None])
        else:
            for x in ast.literal_eval(data[9]):
                if x not in P.save_data.pokedex[pokes][1]:
                    locations.append([P.font_vs.render("Unknown",True,(0,0,0)),None])
                else:
                    if x == 'echo_cave' or x == 'mirror_cave':
                        locations.append([P.font_vs.render(get_location(P,location = x),True,(0,0,0)),cave_ico])
                    elif x in ['route_3b','route_5b']:
                        locations.append([P.font_vs.render(get_location(P,location = x[:-1]),True,(0,0,0)),beach_ico])
                    else:
                        locations.append([P.font_vs.render(get_location(P,location = x),True,(0,0,0)),grass_ico])
    else:
        desc = []
        cat = P.font_s.render("????? Pokemon",True,(0,0,0))
        height = P.font_s.render("Height: ?????",True,(0,0,0))
        weight = P.font_s.render("Weight: ?????",True,(0,0,0))
        type1 = P.font.render("---",True,(0,0,0))
        type2 = None
        if ast.literal_eval(data[9]) == []:
            locations.append([P.font_vs.render("?????",True,(0,0,0)),None])
        else:
            for x in ast.literal_eval(data[9]):
                locations.append([P.font_vs.render("?????",True,(0,0,0)),None])
    locs = P.font_s.render("Habitats: ",True,(0,0,0))
    full = pygame.transform.scale(load("p/poke/"+pokes+"_full.png"),(260,260))
    f.close()
    end = True
    a = 0
    if not fade:
        a += 1
    while end:
        P.surface.blit(back,(0,0))
        P.surface.blit(box,(320,0))
        if a >= -1:
            P.surface.blit(full,(25,87))
            if pokes[:5] == 'Mega_':
                P.surface.blit(mega,(420+P.font.size(num+" "+pokes[5:])[0],35))
            P.surface.blit(txt0,(410,27))
            P.surface.blit(cat,(335,110))
            P.surface.blit(type,(335,150))
            P.surface.blit(type1,(440,147))
            if type2 != None:
                P.surface.blit(type2,(560,147))
            P.surface.blit(height,(335,190))
            P.surface.blit(weight,(335,230))
            P.surface.blit(locs,(335,270))
            y = 0
            x = 0
            for l in locations:
                P.surface.blit(l[0],(335+x,307+y))
                if l[1] != None:
                    P.surface.blit(l[1],(345+x+l[0].get_width(),307+y))
                y += 30
                if y == 120:
                    y = 0
                    x = 230
            y = 0
            for entry in desc:
                P.surface.blit(entry,(10,447+y))
                y += 30
        for event in pygame.event.get(eventtype = KEYDOWN):
            if event.key == pygame.key.key_code(P.controls[0]) and a>10 and from_dex:
                back = back0
                a = -10
            if event.key == pygame.key.key_code(P.controls[1]) and a>10 and from_dex:
                back = back1
                a = -10
            if event.key == pygame.key.key_code(P.controls[5]) and a>10:
                end = False
            if event.key == pygame.key.key_code(P.controls[4]) and a>10 and from_dex == False:
                end = False
        if a == 0:
            fade_in(P)
        if a == -5:
            if back == back0:
                return 0
            else:
                return 1
        a += 1
        P.clock.tick(P.ani_spd)
        update_screen(P)
    fade_out(P)
    return -1


def pokedex(P):
    back = load("p/Pokedex.png")
    sort_bar = load("p/Pokedex_sort.png")
    sortf = load("p/Pokedex_sortf.png")
    sort_high = load("p/sort_high.png")
    front = load("p/Pokedex_f.png")
    outline = load("p/Pokedex_borders.png")
    mega = pygame.transform.scale(load("p/mega_symbol.png"),(30,30))
    box0 = load("p/dex_box0.png")
    box1 = load("p/dex_box1.png")
    box2 = load("p/dex_box2.png")
    # box3 = load("p/dex_box3.png")
    # box3 = load("p/dex_box4.png")
    # box3 = load("p/dex_box4.png")
    sort0 = P.font_s.render("By Number",True,(0,0,0))
    sort1 = P.font_s.render("A-Z",True,(0,0,0))
    sort2 = P.font_s.render("Heavy-Light",True,(0,0,0))
    sort3 = P.font_s.render("Light-Heavy",True,(0,0,0))
    sort4 = P.font_s.render("Tall-Short",True,(0,0,0))
    sort5 = P.font_s.render("Short-Tall",True,(0,0,0))
    sort = sort0
    press_sort = P.font_s.render("Press "+P.controls[6]+" to sort",True,(255,255,255))
    ps_len = P.font_s.size("Press "+P.controls[6]+" to sort")[0]/2
    caught_count = 0
    uncaught_count = 0
    orig_dex = {}
    for file in os.listdir("poke"):
        if file.endswith(".txt") and file.startswith("OUTLINE") == False:
            lst = []
            name = file[:-4]
            f = open("poke/"+file)
            data = f.readlines()
            if name == 'Thundurus_T':
                print(data[8])
            if len(data) > 8 and data[8] != '-1\n':
                if name not in P.save_data.pokedex:
                    # P.save_data.pokedex[name] = [1,[]]
                    lst.append(pygame.transform.scale(load("p/Question_full.png"),(220,220)))
                    uncaught_count += 1
                else:
                    if P.save_data.pokedex[name][0] == 1:
                        caught_count += 1
                    else:
                        uncaught_count += 1
                    lst.append(pygame.transform.scale(load("p/poke/"+name+"_full.png"),(220,220)))
                #dex weight height
                lst.append(int(data[8]))
                lst.append(float(data[6]))
                lst.append(int(data[7]))
                orig_dex[name] = lst
            f.close()
    dex = sorted(orig_dex.items(),key = lambda x:x[1][1])
    caught = P.font_s.render(str(caught_count),True,(255,255,255))
    uncaught = P.font_s.render(str(uncaught_count),True,(255,255,255))
    #print(dex)
    scroll = 0
    scroll_mod = 0
    scroll_spd = 10
    sorty = 0
    sort_pick = 0
    curr_sort = 0
    scroll_size = 4/(len(dex)+3)*502
    scroll_inc = (1/(len(dex)+3))*502
    a = 0
    end = True
    while end:
        P.surface.blit(back,(0,0))
        #blit pokemon
        y = 0
        for x in dex:
            if 190-(scroll/8*28)+y > -280 and 190-(scroll/8*28)+y < 880:
                P.surface.blit(x[1][0],(50,190-(scroll/8*28)+y))
            y += 280
        P.surface.blit(front,(0,0))
        #blit boxes
        y = 0
        for x in dex:
            if 277-scroll+y > -80 and 277-scroll+y < 680:
                box = box2
                if x[0] in P.save_data.pokedex and P.save_data.pokedex[x[0]][0] == 1:
                    box = box1
                if x[0] in P.save_data.pokedex and P.save_data.pokedex[x[0]][0] == 0:
                    box = box0
                P.surface.blit(box,(320,250-scroll+y))
                num = ""
                if x[1][1] < 10:
                    num += "0"
                if x[1][1] < 100:
                    num += "0"
                num += str(x[1][1])
                if box == box2:
                    #change?
                    txt0 = P.font.render(num+" ?????",True,(0,0,0))
                else:
                    if x[0][:5] == 'Mega_':
                        txt0 = P.font.render(num+" "+x[0][5:],True,(0,0,0))
                        P.surface.blit(mega,(420+P.font.size(num+" "+x[0][5:])[0],285-scroll+y))
                    elif x[0][-2:] == '_M':
                        txt0 = P.font.render(num+" "+x[0][:-2]+"???",True,(0,0,0))
                    elif x[0][-2:] == '_F':
                        txt0 = P.font.render(num+" "+x[0][:-2]+"???",True,(0,0,0))
                    elif x == 'Mime Jr':
                        txt0 = P.font.render(num+" "+"Mime Jr.",True,(0,0,0))
                    elif x == 'Mr Mime':
                        txt0 = P.font.render(num+" "+"Mr. Mime",True,(0,0,0))
                    elif x[0][:10] == 'Pineapple_':
                        txt0 = P.font.render(num+" "+x[0][10:],True,(0,0,0))
                    else:
                        txt0 = P.font.render(num+" "+x[0],True,(0,0,0))
                P.surface.blit(txt0,(410,277-scroll+y))
            y += 80
        P.surface.blit(outline,(0,0))
        P.surface.blit(caught,(365,8))
        P.surface.blit(uncaught,(465,8))
        P.surface.fill((201,240,255), Rect(785,48+(int(scroll/80)*scroll_inc),15,scroll_size))
        P.surface.blit(sort_bar,(0,250-abs(sorty)))
        P.surface.blit(sort_high,(335,605+sort_pick-abs(sorty)))
        P.surface.blit(sortf,(0,250-abs(sorty)))
        P.surface.blit(sort0,(489,610-abs(sorty)))
        P.surface.blit(sort1,(542,650-abs(sorty)))
        P.surface.blit(sort2,(471,690-abs(sorty)))
        P.surface.blit(sort3,(471,730-abs(sorty)))
        P.surface.blit(sort4,(480,770-abs(sorty)))
        P.surface.blit(sort5,(480,810-abs(sorty)))
        P.surface.blit(sort,(565,8))
        P.surface.blit(press_sort,(560-ps_len,558-abs(sorty)))
        if scroll%80 == 0:
            for event in pygame.event.get(eventtype = KEYDOWN):
                if a > 10 and sorty%250 == 0:
                    if event.key == pygame.key.key_code(P.controls[4]):
                        if sorty == 250:
                            if sort_pick != curr_sort:
                                curr_sort = sort_pick
                                if sort_pick == 0:
                                    dex = sorted(orig_dex.items(),key = lambda x:x[1][1])
                                    sort = sort0
                                elif sort_pick == 40:
                                    dex1 = orig_dex.copy()
                                    for pok in orig_dex:
                                        if pok not in P.save_data.pokedex:
                                            dex1.pop(pok)
                                    dex = dex1.copy()
                                    change_list = []
                                    for pok in dex1:
                                        if pok[:5] == "Mega_":
                                            change_list.append(pok[5:]+"_M")
                                            dex[pok[5:]+"_M"] = dex.pop(pok)
                                        if pok[:10] == "Pineapple_":
                                            change_list.append(pok[10:]+"_P")
                                            dex[pok[10:]+"_P"] = dex.pop(pok)
                                    dex = sorted(dex.items(),key = lambda x:x[0])
                                    for pok in range(len(dex)):
                                        if dex[pok][0] in change_list and dex[pok][0][-2:] == '_M':
                                            dex[pok] = list(dex[pok])
                                            dex[pok][0] = 'Mega_'+dex[pok][0][:-2]
                                        if dex[pok][0] in change_list and dex[pok][0][-2:] == '_P':
                                            dex[pok] = list(dex[pok])
                                            dex[pok][0] = 'Pineapple_'+dex[pok][0][:-2]
                                    sort = sort1
                                else:
                                    dex = orig_dex.copy()
                                    for pok in orig_dex:
                                        if pok not in P.save_data.pokedex:
                                            dex.pop(pok)
                                        elif P.save_data.pokedex[pok][0] == 0:
                                            dex.pop(pok)
                                    if sort_pick == 80:
                                        dex = sorted(dex.items(),key = lambda x:x[1][2],reverse = True)
                                        sort = sort2
                                    elif sort_pick == 120:
                                        dex = sorted(dex.items(),key = lambda x:x[1][2])
                                        sort = sort3
                                    elif sort_pick == 160:
                                        dex = sorted(dex.items(),key = lambda x:x[1][3],reverse = True)
                                        sort = sort4
                                    else:
                                        dex = sorted(dex.items(),key = lambda x:x[1][3])
                                        sort = sort5
                                sorty = -225
                                scroll = 0
                                scroll_size = 4/(len(dex)+3)*502
                                scroll_inc = (1/(len(dex)+3))*502
                        elif len(dex) != 0:
                            if dex[int(scroll/80)][0] in P.save_data.pokedex:
                                fade_out(P)
                                finish = True
                                fade = True
                                while finish:
                                    ans = dex_entry(P,dex[int(scroll/80)][0],fade)
                                    if ans == -1:
                                        a = -1
                                        finish = False
                                    elif ans == 1:
                                        finish2 = True
                                        while finish2:
                                            if scroll < (len(dex)-1)*80:
                                                scroll += 80
                                            else:
                                                scroll = 0
                                            if dex[int(scroll/80)][0] in P.save_data.pokedex:
                                                finish2 = False
                                        fade = False
                                    elif ans == 0:
                                        finish2 = True
                                        while finish2:
                                            if scroll > 0:
                                                scroll -= 80
                                            else:
                                                scroll = (len(dex)-1)*80
                                            if dex[int(scroll/80)][0] in P.save_data.pokedex:
                                                finish2 = False
                                        fade = False
                    if event.key == pygame.key.key_code(P.controls[5]):
                        if sorty == 250:
                            sort_pick = curr_sort
                            sorty = -225
                        else:
                            end = False
                    if event.key == pygame.key.key_code(P.controls[6]):
                        if sorty == 250:
                            sorty = -225
                        else:
                            sorty = 25
                    if event.key == pygame.key.key_code(P.controls[0]) and sorty == 250:
                        if sort_pick != 0:
                            sort_pick -= 40
                    if event.key == pygame.key.key_code(P.controls[1]) and sorty == 250:
                        if sort_pick != 200:
                            sort_pick += 40
        keys = pygame.key.get_pressed()
        if scroll%80 == 0:
            su = False
            sd = False
        if keys[pygame.key.key_code(P.controls[0])] and scroll > 0 and sd == False and sorty == 0:
            su = True
        if keys[pygame.key.key_code(P.controls[1])] and scroll < (len(dex)-1)*80 and su == False and sorty == 0:
            sd = True
        if(su):
            if scroll_mod > 150 and scroll_spd == 20:
                if scroll%80 == 0:
                    scroll_spd = 40
            elif scroll_mod > 50 and scroll_spd == 10:
                if scroll%80 == 0:
                    scroll_spd = 20
            if scroll_mod <= 50 and scroll_spd >= 20:
                if scroll%80 == 0:
                    scroll_spd = 10
            scroll -= scroll_spd
            scroll_mod += 1
        elif(sd):
            if scroll_mod > 150 and scroll_spd == 20:
                if scroll%80 == 0:
                    scroll_spd = 40
            if scroll_mod > 50 and scroll_spd == 10:
                if scroll%80 == 0:
                    scroll_spd = 20
            if scroll_mod <= 50 and scroll_spd >= 20:
                if scroll%80 == 0:
                    scroll_spd = 10
            scroll += scroll_spd
            scroll_mod += 1
        else:
            scroll_mod = 0
        if a == 0:
            fade_in(P)
        if sorty > 0 and sorty < 250:
            sorty += 25
        if sorty < 0 and sorty > -250:
            sorty += 25
        a += 1
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P)

def bag(P,pick_item = False) -> None:
    box = load("p/bag_box.png")
    back = load("p/bag.png")
    i = load("p/item_ico.png")
    m = load("p/med_ico.png")
    b = load("p/balls_ico.png")
    t = load("p/tm_ico.png")
    k = load("p/key_ico.png")
    high = load("p/bag_high.png")
    ico = i
    ix = 0
    bag = 0
    a = 0
    curr = ['',0]
    chose_item = ''
    scroll = 0
    scroll_mod = 0
    scroll_spd = 10
    su = False
    sd = False
    end = True
    while end:
        P.surface.blit(back,(0,0))
        P.surface.blit(ico,(ix,0))
        title = "ITEMS"
        if bag == 1:
            title = "MEDICINE"
        if bag == 2:
            title = "BALLS"
        if bag == 3:
            title = "TMs"
        if bag == 4:
            title = "KEY ITEMS"
        tle = P.font.render(title,True,(255,255,255))
        P.surface.blit(tle,((400-(P.font.size(title)[0]))/2,85))
        y = 0
        if scroll <= 280:
            s = 0
        elif scroll >= (((len(P.bag[bag])-1)*70)-210):
            if len(P.bag[bag]) < 8:
                s = 0
            else:
                s = (((len(P.bag[bag])-1)*70))-490
        else:
            s = scroll-280
        for z in P.bag[bag]:
            txt = P.font_s.render(z[0],True,(0,0,0))
            size_x = (360-(P.font_s.size(z[0])[0]))/2
            if z[0] in P.save_data.register:
                txt = P.font_s.render("???"+z[0]+"???",True,(0,0,0))
                size_x = (360-(P.font_s.size("???"+z[0]+"???")[0]))/2
            P.surface.blit(box,(420,20-s+y))
            P.surface.blit(txt,(420+size_x,35-s+y))
            if z == P.bag[bag][int(scroll/70)]:
                P.surface.blit(high,(420,20-s+y))
                curr = z
            y += 70
        if(curr != ['',0]):
            txt = P.font_s.render(curr[0],True,(0,0,0))
            txt2 = P.font_s.render(' x '+str(curr[1]),True,(0,0,0))
            P.surface.blit(txt,((380-P.font_s.size(curr[0])[0])/2,150))
            P.surface.blit(txt2,(180,195))
            ic = pygame.transform.scale(load("p/item/"+curr[0]+".png"),(50,50))
            P.surface.blit(ic,(130,185))
            item = items.Item(curr[0])
            descr = []
            cngy = 0
            for x in item.desc:
                descr.append(P.font_s.render(x,True,(0,0,0)))
            for x in descr:
                P.surface.blit(x,(20,240+cngy))
                cngy += 34
        if a == 0:
            fade_in(P)
        if scroll%70 == 0:
            for event in pygame.event.get(eventtype = KEYDOWN):
                if event.key == pygame.key.key_code(P.controls[4]) and a>10 and curr != ['',0]:
                    if pick_item:
                        if items.Item(curr[0]).price == -1:
                            new_txt(P)
                            write(P,"The "+curr[0],"can't be held.")
                            cont(P)
                        else:
                            chose_item = curr[0]
                            end = False
                    else:
                        if items.Item(curr[0]).menu(P,curr[1]):
                            a = -1
                        else:
                            if P.use_key_item != None:
                                end = False
                            a = 0
                    if scroll/70 > (len(P.bag[bag])-1):
                        scroll -= 70
                    if len(P.bag[bag]) == 0:
                        curr = ['',0]
                if event.key == pygame.key.key_code(P.controls[5]) and a > 10:
                    end = False
                elif event.key == pygame.key.key_code(P.controls[2]) and a > 10:
                    if bag != 0:
                        curr = ['',0]
                        scroll = 0
                        bag -= 1
                        ix -= 80
                        if bag == 0:
                            ico = i
                        if bag == 1:
                            ico = m
                        if bag == 2:
                            ico = b
                        if bag == 3:
                            ico = t
                elif event.key == pygame.key.key_code(P.controls[3]) and a > 10:
                    if bag != 4:
                        curr = ['',0]
                        scroll = 0
                        bag += 1
                        ix += 80
                        if bag == 1:
                            ico = m
                        if bag == 2:
                            ico = b
                        if bag == 3:
                            ico = t
                        if bag == 4:
                            ico = k
        keys = pygame.key.get_pressed()
        if scroll%70 == 0:
            su = False
            sd = False
        if keys[pygame.key.key_code(P.controls[0])] and scroll > 0 and sd == False:
            su = True
        if keys[pygame.key.key_code(P.controls[1])] and scroll < (len(P.bag[bag])-1)*70 and su == False:
            sd = True
        if(su):
            if scroll_mod > 50 and scroll_spd == 10:
                if scroll%70 == 0:
                    scroll_spd = 35
            if scroll_mod <= 50 and scroll_spd == 35:
                if scroll%70 == 0:
                    scroll_spd = 10
            scroll -= scroll_spd
            scroll_mod += 1
        elif(sd):
            if scroll_mod > 50 and scroll_spd == 10:
                if scroll%70 == 0:
                    scroll_spd = 35
            if scroll_mod <= 50 and scroll_spd == 35:
                if scroll%70 == 0:
                    scroll_spd = 10
            scroll += scroll_spd
            scroll_mod += 1
        else:
            scroll_mod = 0
        a += 1
        P.clock.tick(P.ani_spd)
        update_screen(P)
    if pick_item and chose_item != '' and items.Item(chose_item).type[0] == 'Evo':
        return chose_item
    else:
        fade_out(P)
    if pick_item:
        return chose_item
    else:
        return None

def set_channel_volume(P,volume,num):
    #if volume >= 1:
        #volume = volume**2
    pygame.mixer.Channel(num).set_volume(volume)

def set_mixer_volume(P,volume,song = None,sat = False):
    if sat:
        fes_vol = 0
        dist = math.sqrt(P.ams_npc2.y_dist()**2+P.ams_npc2.x_dist()**2)
        if dist < 500:
            fes_vol = volume-(volume*dist/500)
        volume = volume-(fes_vol)
        #if fes_vol >= 1:
            #fes_vol = fes_vol**2
        pygame.mixer.Channel(0).set_volume(fes_vol)
    if P.prog[0] >= 70 and P.prog[0] <= 74 and P.px >= -5000:
        v = volume*((5000+P.px)/50)/30
        volume = volume - v
        pygame.mixer.Channel(0).set_volume(P.sfx_vol*2)
    #if volume >= 1:
        #volume = volume**2
    if P.song in ["music/echoing_cave.wav","music/isola.wav"] or song == "music/load.wav":
        volume *= 1.5
    if P.song == 'music/fon_battle.wav' or "music/cheryl_battle.wav" or "music/cheryl_battle_loop.wav":
        volume *= 2
    if P.loc[:5] == 'house' or P.loc in ['egida_mine','egida_lab','fiore_garden','pianura_nursery','pianura_bakery']:
        volume *= 0.6
    pygame.mixer.music.set_volume(volume)

def rebind_controls(P):
    copy = P.surface.copy()
    over1 = load("p/rebind_menu.png")
    over2 = load("p/rebind_menu_2.png")
    over = over1
    high = load("p/controls_high.png")
    up = P.font_s.render("Up",True,(240,230,230))
    up1 = P.font_s.render(P.controls[0].upper(),True,(255,255,255))
    down = P.font_s.render("Down",True,(240,230,230))
    down1 = P.font_s.render(P.controls[1].upper(),True,(0,0,0))
    left = P.font_s.render("Left",True,(240,230,230))
    left1 = P.font_s.render(P.controls[2].upper(),True,(0,0,0))
    right = P.font_s.render("Right",True,(240,230,230))
    right1 = P.font_s.render(P.controls[3].upper(),True,(0,0,0))
    select = P.font_s.render("Select",True,(240,230,230))
    select1 = P.font_s.render(P.controls[4].upper(),True,(0,0,0))
    back = P.font_s.render("Back",True,(240,230,230))
    back1 = P.font_s.render(P.controls[5].upper(),True,(0,0,0))
    menu = P.font_s.render("Menu",True,(240,230,230))
    menu1 = P.font_s.render(P.controls[6].upper(),True,(0,0,0))
    hot = P.font_s.render("Quick Use",True,(240,230,230))
    hot1 = P.font_s.render(P.controls[7].upper(),True,(0,0,0))
    new_key = P.font_s.render("Press New Key",True,(255,255,255))
    reset = P.font_s.render("Reset Default",True,(0,0,0))
    y = 0
    new = -1
    end = True
    while end:
        P.surface.blit(copy,(0,0))
        P.surface.blit(over,(95,85))
        if y != 8:
            P.surface.blit(high,(402,110+(45*y)))
        P.surface.blit(up,(257,115))
        if up1 == new_key:
            P.surface.blit(up1,(408,115))
        else:
            P.surface.blit(up1,(525-(P.font_s.size(P.controls[0].upper())[0]/2),115))
        P.surface.blit(down,(239,160))
        if down1 == new_key:
            P.surface.blit(down1,(408,160))
        else:
            P.surface.blit(down1,(525-(P.font_s.size(P.controls[1].upper())[0]/2),160))
        P.surface.blit(left,(239,205))
        if left1 == new_key:
            P.surface.blit(left1,(408,205))
        else:
            P.surface.blit(left1,(525-(P.font_s.size(P.controls[2].upper())[0]/2),205))
        P.surface.blit(right,(230,250))
        if right1 == new_key:
            P.surface.blit(right1,(408,250))
        else:
            P.surface.blit(right1,(525-(P.font_s.size(P.controls[3].upper())[0]/2),250))
        P.surface.blit(select,(221,295))
        if select1 == new_key:
            P.surface.blit(select1,(408,295))
        else:
            P.surface.blit(select1,(525-(P.font_s.size(P.controls[4].upper())[0]/2),295))
        P.surface.blit(back,(239,340))
        if back1 == new_key:
            P.surface.blit(back1,(408,340))
        else:
            P.surface.blit(back1,(525-(P.font_s.size(P.controls[5].upper())[0]/2),340))
        P.surface.blit(menu,(239,385))
        if menu1 == new_key:
            P.surface.blit(menu1,(408,385))
        else:
            P.surface.blit(menu1,(525-(P.font_s.size(P.controls[6].upper())[0]/2),385))
        P.surface.blit(hot,(194,430))
        if hot1 == new_key:
            P.surface.blit(hot1,(408,430))
        else:
            P.surface.blit(hot1,(525-(P.font_s.size(P.controls[7].upper())[0]/2),430))
        P.surface.blit(reset,(283,485))
        for event in pygame.event.get(eventtype = KEYDOWN):
            if new != -1:
                if pygame.key.name(event.key) not in P.controls or pygame.key.name(event.key) == P.controls[new]:
                    try:
                        print(pygame.key.key_code(pygame.key.name(event.key)))
                        P.controls[new] = pygame.key.name(event.key)
                        if new == 0:
                            up1 = P.font_s.render(P.controls[new].upper(),True,(255,255,255))
                        if new == 1:
                            down1 = P.font_s.render(P.controls[new].upper(),True,(255,255,255))
                        if new == 2:
                            left1 = P.font_s.render(P.controls[new].upper(),True,(255,255,255))
                        if new == 3:
                            right1 = P.font_s.render(P.controls[new].upper(),True,(255,255,255))
                        if new == 4:
                            select1 = P.font_s.render(P.controls[new].upper(),True,(255,255,255))
                        if new == 5:
                            back1 = P.font_s.render(P.controls[new].upper(),True,(255,255,255))
                        if new == 6:
                            menu1 = P.font_s.render(P.controls[new].upper(),True,(255,255,255))
                        if new == 7:
                            hot1 = P.font_s.render(P.controls[new].upper(),True,(255,255,255))
                        new = -1
                    except:
                        txt(P,"The "+pygame.key.name(event.key)+" key can't be", "bound.")
                else:
                    txt(P,"The "+pygame.key.name(event.key)+" key is already","binded to another command.")
            elif event.key == pygame.key.key_code(P.controls[4]):
                if y == 8:
                    P.controls = ['up','down','left','right','z','x','c','v']
                    up1 = P.font_s.render(P.controls[0].upper(),True,(0,0,0))
                    down1 = P.font_s.render(P.controls[1].upper(),True,(0,0,0))
                    left1 = P.font_s.render(P.controls[2].upper(),True,(0,0,0))
                    right1 = P.font_s.render(P.controls[3].upper(),True,(0,0,0))
                    select1 = P.font_s.render(P.controls[4].upper(),True,(0,0,0))
                    back1 = P.font_s.render(P.controls[5].upper(),True,(0,0,0))
                    menu1 = P.font_s.render(P.controls[6].upper(),True,(0,0,0))
                    hot1 = P.font_s.render(P.controls[7].upper(),True,(0,0,0))
                else:
                    new = y
                    if y == 0:
                        up1 = new_key
                    if y == 1:
                        down1 = new_key
                    if y == 2:
                        left1 = new_key
                    if y == 3:
                        right1 = new_key
                    if y == 4:
                        select1 = new_key
                    if y == 5:
                        back1 = new_key
                    if y == 6:
                        menu1 = new_key
                    if y == 7:
                        hot1 = new_key
            elif event.key == pygame.key.key_code(P.controls[5]):
                end = False
            elif event.key == pygame.key.key_code(P.controls[1]) and y < 8:
                y += 1
                if y == 1:
                    up1 = P.font_s.render(P.controls[0].upper(),True,(0,0,0))
                    down1 = P.font_s.render(P.controls[1].upper(),True,(255,255,255))
                if y == 2:
                    down1 = P.font_s.render(P.controls[1].upper(),True,(0,0,0))
                    left1 = P.font_s.render(P.controls[2].upper(),True,(255,255,255))
                if y == 3:
                    left1 = P.font_s.render(P.controls[2].upper(),True,(0,0,0))
                    right1 = P.font_s.render(P.controls[3].upper(),True,(255,255,255))
                if y == 4:
                    right1 = P.font_s.render(P.controls[3].upper(),True,(0,0,0))
                    select1 = P.font_s.render(P.controls[4].upper(),True,(255,255,255))
                if y == 5:
                    select1 = P.font_s.render(P.controls[4].upper(),True,(0,0,0))
                    back1 = P.font_s.render(P.controls[5].upper(),True,(255,255,255))
                if y == 6:
                    back1 = P.font_s.render(P.controls[5].upper(),True,(0,0,0))
                    menu1 = P.font_s.render(P.controls[6].upper(),True,(255,255,255))
                if y == 7:
                    menu1 = P.font_s.render(P.controls[6].upper(),True,(0,0,0))
                    hot1 = P.font_s.render(P.controls[7].upper(),True,(255,255,255))
                if y == 8:
                    over = over2
                    hot1 = P.font_s.render(P.controls[7].upper(),True,(0,0,0))
                    reset = P.font_s.render("Reset Default",True,(255,255,255))
            elif event.key == pygame.key.key_code(P.controls[0]) and y > 0:
                y -= 1
                if y == 0:
                    down1 = P.font_s.render(P.controls[1].upper(),True,(0,0,0))
                    up1 = P.font_s.render(P.controls[0].upper(),True,(255,255,255))
                if y == 1:
                    left1 = P.font_s.render(P.controls[2].upper(),True,(0,0,0))
                    down1 = P.font_s.render(P.controls[1].upper(),True,(255,255,255))
                if y == 2:
                    right1 = P.font_s.render(P.controls[3].upper(),True,(0,0,0))
                    left1 = P.font_s.render(P.controls[2].upper(),True,(255,255,255))
                if y == 3:
                    select1 = P.font_s.render(P.controls[4].upper(),True,(0,0,0))
                    right1 = P.font_s.render(P.controls[3].upper(),True,(255,255,255))
                if y == 4:
                    back1 = P.font_s.render(P.controls[5].upper(),True,(0,0,0))
                    select1 = P.font_s.render(P.controls[4].upper(),True,(255,255,255))
                if y == 5:
                    menu1 = P.font_s.render(P.controls[6].upper(),True,(0,0,0))
                    back1 = P.font_s.render(P.controls[5].upper(),True,(255,255,255))
                if y == 6:
                    hot1 = P.font_s.render(P.controls[7].upper(),True,(0,0,0))
                    menu1 = P.font_s.render(P.controls[6].upper(),True,(255,255,255))
                if y == 7:
                    hot1 = P.font_s.render(P.controls[7].upper(),True,(255,255,255))
                    over = over1
                    reset = P.font_s.render("Reset Default",True,(0,0,0))
        update_screen(P)
        P.clock.tick(P.ani_spd)

def save_settings(P):
    set = open("save_files/Sett!ngs.txt","w")
    set.write(str(P.txt_spd)+"\n")
    set.write(str(P.ani_on)+"\n")
    set.write(str(P.walk_spd)+"\n")
    set.write(str(P.graphic)+"\n")
    set.write(str(P.lighting)+"\n")
    set.write(str(P.vol)+"\n")
    set.write(str(P.sfx_vol)+"\n")
    set.write(str(P.controls)+"\n")
    set.close()

def settings(P,saturday = False):
    back1 = load("p/Settings.png")
    back2 = load("p/Settings_2.png")
    back = back1
    over1 = load("p/settings_overlay_1.png")
    over2 = load("p/settings_overlay_2.png")
    over = over1
    highlight = load("p/options_highlight.png")
    options = P.font_l.render("OPTIONS",True,(80,0,0))
    off_color = (150,150,150)
    on_color = (0,0,0)
    on_color_high = (255,255,255)
    #text speed
    txtspd = P.font_s.render("Text Speed",True,(240,230,230))
    slo = P.font_s.render("Slow",True,off_color)
    norm = P.font_s.render("Normal",True,off_color)
    fast = P.font_s.render("Fast",True,off_color)
    if P.txt_spd == 20:
        slo = P.font_s.render("Slow",True,on_color_high)
    if P.txt_spd == 40:
        norm = P.font_s.render("Normal",True,on_color_high)
    if P.txt_spd == 60:
        fast = P.font_s.render("Fast",True,on_color_high)
    #battle animations
    batani = P.font_s.render("Battle Animations",True,(240,230,230))
    on = P.font_s.render("On",True,off_color)
    off = P.font_s.render("Off",True,off_color)
    if P.ani_on == True:
        on = P.font_s.render("On",True,on_color)
    if P.ani_on == False:
        off = P.font_s.render("Off",True,on_color)
    #move speed
    mvspd = P.font_s.render("Walking Speed",True,(240,230,230))
    normm = P.font_s.render("Normal",True,off_color)
    fastm = P.font_s.render("Fast",True,off_color)
    if P.walk_spd == 5:
        normm = P.font_s.render("Normal",True,on_color)
    if P.walk_spd == 7:
        fastm = P.font_s.render("Fast",True,on_color)
    #graphics
    graphics = P.font_s.render("Graphics",True,(240,230,230))
    low = P.font_s.render("Low",True,off_color)
    high = P.font_s.render("High",True,off_color)
    if P.graphic == 0:
        low = P.font_s.render("Low",True,on_color)
    if P.graphic == 1:
        high = P.font_s.render("High",True,on_color)
    #lighting
    light = P.font_s.render("Lighting",True,(240,230,230))
    day = P.font_s.render("Day",True,off_color)
    dyn = P.font_s.render("Dynamic",True,off_color)
    nite = P.font_s.render("Night",True,off_color)
    if P.lighting == 'Day':
        day = P.font_s.render("Day",True,on_color)
    if P.lighting == 'Dynamic':
        dyn = P.font_s.render("Dynamic",True,on_color)
    if P.lighting == 'Night':
        nite = P.font_s.render("Night",True,on_color)
    #bgm
    bgm = P.font_s.render("Background Music",True,(240,230,230))
    vol = P.font_s.render(str(int(P.vol*200)),True,on_color)
    #sfx
    sfx = P.font_s.render("Sound Effects",True,(240,230,230))
    sfx_vol = P.font_s.render(str(int(P.sfx_vol*200)),True,on_color)
    #rebind
    rebind = P.font.render("Controls",True,on_color)
    save = P.font_l.render("SAVE CHANGES",True,on_color)
    bar = load("p/vol_bar.png")
    white = load("p/vol_white.png")
    black = load("p/vol_black.png")
    bgm_but = black
    sfx_but = black
    old_set = []
    old_set.append(P.txt_spd)
    old_set.append(P.ani_on)
    old_set.append(P.walk_spd)
    old_set.append(P.graphic)
    old_set.append(P.lighting)
    old_set.append(P.vol)
    old_set.append(P.sfx_vol)
    old_set.append(P.controls.copy())
    end = True
    a = 0
    y = 0
    fade_in(P)
    while end:
        P.surface.blit(back,(0,0))
        P.surface.blit(highlight,(330,95+(45*y)))
        P.surface.blit(options,(400-P.font_l.size("OPTIONS")[0]/2,5))
        P.surface.blit(txtspd,(10,100))
        P.surface.blit(slo,(400,100))
        P.surface.blit(norm,(510,100))
        P.surface.blit(fast,(660,100))
        P.surface.blit(batani,(10,145))
        P.surface.blit(off,(470,145))
        P.surface.blit(on,(650,145))
        P.surface.blit(mvspd,(10,190))
        P.surface.blit(normm,(440,190))
        P.surface.blit(fastm,(640,190))
        P.surface.blit(graphics,(10,235))
        P.surface.blit(low,(460,235))
        P.surface.blit(high,(640,235))
        P.surface.blit(light,(10,280))
        P.surface.blit(day,(400,280))
        P.surface.blit(dyn,(500,280))
        P.surface.blit(nite,(670,280))
        P.surface.blit(bgm,(10,325))
        P.surface.blit(vol,(720,325))
        P.surface.blit(sfx,(10,370))
        P.surface.blit(sfx_vol,(720,370))
        P.surface.blit(bar,(400,335))
        P.surface.blit(bar,(400,380))
        P.surface.fill((255,150,150), Rect(400,335,P.vol*600,10))
        P.surface.fill((255,150,150), Rect(400,380,P.sfx_vol*600,10))
        P.surface.blit(bgm_but,(388+P.vol*600,328))
        P.surface.blit(sfx_but,(388+P.sfx_vol*600,373))
        P.surface.blit(over,(0,405))
        P.surface.blit(rebind,(304,427))
        P.surface.blit(save,(220,525))
        for event in pygame.event.get(eventtype = KEYDOWN):
            if a > 10:
                if event.key == pygame.key.key_code(P.controls[4]):
                    if y == 7:
                        rebind_controls(P)
                    if y == 8:
                        save_settings(P)
                        end = False
                if event.key == pygame.key.key_code(P.controls[5]):
                    if old_set[0] == P.txt_spd and old_set[1] == P.ani_on and old_set[2] == P.walk_spd and old_set[3] == P.graphic and old_set[4] == P.lighting and old_set[5] == P.vol and old_set[6] == P.sfx_vol and old_set[7] == P.controls:
                        end = False
                    else:
                        new_txt(P)
                        write(P,"Save changes?")
                        if choice(P):
                            save_settings(P)
                            end = False
                        else:
                            P.txt_spd = old_set[0]
                            P.ani_on = old_set[1]
                            P.walk_spd = old_set[2]
                            P.graphic = old_set[3]
                            P.lighting = old_set[4]
                            P.vol = old_set[5]
                            P.sfx_vol = old_set[6]
                            P.controls = old_set[7]
                            end = False
                if event.key == pygame.key.key_code(P.controls[1]) and y < 8:
                    y += 1
                    if y == 1:
                        if P.txt_spd == 20:
                            slo = P.font_s.render("Slow",True,on_color)
                        if P.txt_spd == 40:
                            norm = P.font_s.render("Normal",True,on_color)
                        if P.txt_spd == 60:
                            fast = P.font_s.render("Fast",True,on_color)
                        if P.ani_on:
                            on = P.font_s.render("On",True,on_color_high)
                        if P.ani_on == False:
                            off = P.font_s.render("Off",True,on_color_high)
                    if y == 2:
                        if P.ani_on:
                            on = P.font_s.render("On",True,on_color)
                        if P.ani_on == False:
                            off = P.font_s.render("Off",True,on_color)
                        if P.walk_spd == 5:
                            normm = P.font_s.render("Normal",True,on_color_high)
                        if P.walk_spd == 7:
                            fastm = P.font_s.render("Fast",True,on_color_high)
                    if y == 3:
                        if P.walk_spd == 5:
                            normm = P.font_s.render("Normal",True,on_color)
                        if P.walk_spd == 7:
                            fastm = P.font_s.render("Fast",True,on_color)
                        if P.graphic == 0:
                            low = P.font_s.render("Low",True,on_color_high)
                        if P.graphic == 1:
                            high = P.font_s.render("High",True,on_color_high)
                    if y == 4:
                        if P.graphic == 0:
                            low = P.font_s.render("Low",True,on_color)
                        if P.graphic == 1:
                            high = P.font_s.render("High",True,on_color)
                        if P.lighting == 'Day':
                            day = P.font_s.render("Day",True,on_color_high)
                        if P.lighting == 'Dynamic':
                            dyn = P.font_s.render("Dynamic",True,on_color_high)
                        if P.lighting == 'Night':
                            nite = P.font_s.render("Night",True,on_color_high)
                    if y == 5:
                        if P.lighting == 'Day':
                            day = P.font_s.render("Day",True,on_color)
                        if P.lighting == 'Dynamic':
                            dyn = P.font_s.render("Dynamic",True,on_color)
                        if P.lighting == 'Night':
                            nite = P.font_s.render("Night",True,on_color)
                        bgm_but = white
                        vol = P.font_s.render(str(int(P.vol*200)),True,on_color_high)
                    if y == 6:
                        bgm_but = black
                        vol = P.font_s.render(str(int(P.vol*200)),True,on_color)
                        sfx_but = white
                        sfx_vol = P.font_s.render(str(int(P.sfx_vol*200)),True,on_color_high)
                    if y == 7:
                        sfx_but = black
                        sfx_vol = P.font_s.render(str(int(P.sfx_vol*200)),True,on_color)
                        over = over2
                        rebind = P.font.render("Controls",True,on_color_high)
                    if y == 8:
                        over = over1
                        rebind = P.font.render("Controls",True,on_color)
                        back = back2
                        save = P.font_l.render("SAVE CHANGES",True,(250,180,180))
                if event.key == pygame.key.key_code(P.controls[0]) and y > 0:
                    y -= 1
                    if y == 0:
                        if P.txt_spd == 20:
                            slo = P.font_s.render("Slow",True,on_color_high)
                        if P.txt_spd == 40:
                            norm = P.font_s.render("Normal",True,on_color_high)
                        if P.txt_spd == 60:
                            fast = P.font_s.render("Fast",True,on_color_high)
                        if P.ani_on:
                            on = P.font_s.render("On",True,on_color)
                        if P.ani_on == False:
                            off = P.font_s.render("Off",True,on_color)
                    if y == 1:
                        if P.ani_on:
                            on = P.font_s.render("On",True,on_color_high)
                        if P.ani_on == False:
                            off = P.font_s.render("Off",True,on_color_high)
                        if P.walk_spd == 5:
                            normm = P.font_s.render("Normal",True,on_color)
                        if P.walk_spd == 7:
                            fastm = P.font_s.render("Fast",True,on_color)
                    if y == 2:
                        if P.walk_spd == 5:
                            normm = P.font_s.render("Normal",True,on_color_high)
                        if P.walk_spd == 7:
                            fastm = P.font_s.render("Fast",True,on_color_high)
                        if P.graphic == 0:
                            low = P.font_s.render("Low",True,on_color)
                        if P.graphic == 1:
                            high = P.font_s.render("High",True,on_color)
                    if y == 3:
                        if P.graphic == 0:
                            low = P.font_s.render("Low",True,on_color_high)
                        if P.graphic == 1:
                            high = P.font_s.render("High",True,on_color_high)
                        if P.lighting == 'Day':
                            day = P.font_s.render("Day",True,on_color)
                        if P.lighting == 'Dynamic':
                            dyn = P.font_s.render("Dynamic",True,on_color)
                        if P.lighting == 'Night':
                            nite = P.font_s.render("Night",True,on_color)
                    if y == 4:
                        bgm_but = black
                        vol = P.font_s.render(str(int(P.vol*200)),True,on_color)
                        if P.lighting == 'Day':
                            day = P.font_s.render("Day",True,on_color_high)
                        if P.lighting == 'Dynamic':
                            dyn = P.font_s.render("Dynamic",True,on_color_high)
                        if P.lighting == 'Night':
                            nite = P.font_s.render("Night",True,on_color_high)
                    if y == 5:
                        sfx_but = black
                        sfx_vol = P.font_s.render(str(int(P.sfx_vol*200)),True,on_color)
                        bgm_but = white
                        vol = P.font_s.render(str(int(P.vol*200)),True,on_color_high)
                    if y == 6:
                        sfx_but = white
                        sfx_vol = P.font_s.render(str(int(P.sfx_vol*200)),True,on_color_high)
                        over = over1
                        rebind = P.font.render("Controls",True,on_color)
                    if y == 7:
                        over = over2
                        rebind = P.font.render("Controls",True,on_color_high)
                        back = back1
                        save = P.font_l.render("SAVE CHANGES",True,on_color)
                if event.key == pygame.key.key_code(P.controls[3]):
                    if y == 0 and P.txt_spd != 60:
                        P.txt_spd += 20
                        if P.txt_spd == 40:
                            slo = P.font_s.render("Slow",True,off_color)
                            norm = P.font_s.render("Normal",True,on_color_high)
                        else:
                            norm = P.font_s.render("Normal",True,off_color)
                            fast = P.font_s.render("Fast",True,on_color_high)
                    if y == 1 and P.ani_on == False:
                        off = P.font_s.render("Off",True,off_color)
                        on = P.font_s.render("On",True,on_color_high)
                        P.ani_on = True
                    if y == 2 and P.walk_spd == 5:
                        normm = P.font_s.render("Normal",True,off_color)
                        fastm = P.font_s.render("Fast",True,on_color_high)
                        P.walk_spd = 7
                    if y == 3 and P.graphic == 0:
                        low = P.font_s.render("Low",True,off_color)
                        high = P.font_s.render("High",True,on_color_high)
                        P.graphic = 1
                    if y == 4 and P.lighting != 'Night':
                        if P.lighting == 'Day':
                            day = P.font_s.render("Day",True,off_color)
                            dyn = P.font_s.render("Dynamic",True,on_color_high)
                            P.lighting = 'Dynamic'
                        elif P.lighting == 'Dynamic':
                            dyn = P.font_s.render("Dynamic",True,off_color)
                            nite = P.font_s.render("Night",True,on_color_high)
                            P.lighting = 'Night'
                if event.key == pygame.key.key_code(P.controls[2]):
                    if y == 0 and P.txt_spd != 20:
                        P.txt_spd -= 20
                        if P.txt_spd == 40:
                            fast = P.font_s.render("Fast",True,off_color)
                            norm = P.font_s.render("Normal",True,on_color_high)
                        else:
                            norm = P.font_s.render("Normal",True,off_color)
                            slo = P.font_s.render("Slow",True,on_color_high)
                    if y == 1 and P.ani_on:
                        off = P.font_s.render("Off",True,on_color_high)
                        on = P.font_s.render("On",True,off_color)
                        P.ani_on = False
                    if y == 2 and P.walk_spd == 7:
                        normm = P.font_s.render("Normal",True,on_color_high)
                        fastm = P.font_s.render("Fast",True,off_color)
                        P.walk_spd = 5
                    if y == 3 and P.graphic == 1:
                        low = P.font_s.render("Low",True,on_color_high)
                        high = P.font_s.render("High",True,off_color)
                        P.graphic = 0
                    if y == 4 and P.lighting != 'Day':
                        if P.lighting == 'Dynamic':
                            day = P.font_s.render("Day",True,on_color_high)
                            dyn = P.font_s.render("Dynamic",True,off_color)
                            P.lighting = 'Day'
                        elif P.lighting == 'Night':
                            dyn = P.font_s.render("Dynamic",True,on_color_high)
                            nite = P.font_s.render("Night",True,off_color)
                            P.lighting = 'Dynamic'
        keys = pygame.key.get_pressed()
        if y == 5 and P.vol < 0.5 and keys[pygame.key.key_code(P.controls[3])]:
            P.vol += 0.005
            vol = P.font_s.render(str(int(P.vol*200)),True,on_color_high)
            set_mixer_volume(P,P.vol,sat = saturday)
        if y == 5 and P.vol > 0 and keys[pygame.key.key_code(P.controls[2])]:
            P.vol -= 0.005
            vol = P.font_s.render(str(int(P.vol*200)),True,on_color_high)
            if int(P.vol*200) == 0:
                P.vol = 0
            set_mixer_volume(P,P.vol,sat = saturday)
        if y == 6 and P.sfx_vol < 0.5 and keys[pygame.key.key_code(P.controls[3])]:
            P.sfx_vol += 0.005
            sfx_vol = P.font_s.render(str(int(P.sfx_vol*200)),True,on_color_high)
        if y == 6 and P.sfx_vol > 0 and keys[pygame.key.key_code(P.controls[2])]:
            P.sfx_vol -= 0.005
            sfx_vol = P.font_s.render(str(int(P.sfx_vol*200)),True,on_color_high)
            if int(P.sfx_vol*200) == 0:
                P.sfx_vol = 0
        if a == 0:
            fade_in(P)
        a += 1
        update_screen(P)
        P.clock.tick(P.ani_spd)
    fade_out(P)
    P.load_images(True)

def profile(P):
    if P.save_data.gen == 0:
        back1 = load("p/profile_boy_1.png")
        back2 = load("p/profile_boy_2.png")
    else:
        back1 = load("p/profile_girl_1.png")
        back2 = load("p/profile_girl_2.png")
    txtbox = load("p/profile_textbox.png")
    name = P.font_s.render("Name:   "+P.save_data.name,True,(255,255,255))
    money = P.font_s.render("Money:   $"+str(P.save_data.money),True,(255,255,255))
    max = P.font_s.render("Max Level:   "+str(poke_max(P,None)),True,(255,255,255))
    update_time(P)
    time_str = ""
    if P.save_data.time[0] < 10:
        time_str += '0'
    time_str += str(P.save_data.time[0])
    if P.save_data.time[1] < 10:
        time_str += ':0'
    else:
        time_str += ':'
    time_str += str(P.save_data.time[1])
    time = P.font_s.render("Play Time:   "+time_str,True,(255,255,255))
    dex_count = 0
    for pok in P.save_data.pokedex:
        if P.save_data.pokedex[pok][0] == 1:
            dex_count += 1
    dex = P.font_s.render("Pokedex:   "+str(dex_count)+"/187",True,(255,255,255))
    analytic1 = load("p/analytic_1.png")
    analytic2 = load("p/analytic_2.png")
    analytic = analytic1
    affinity1 = load("p/affinity_1.png")
    affinity2 = load("p/affinity_2.png")
    affinity = affinity1
    job_list = []
    research0 = load("p/research_icon_0.png")
    research1 = load("p/research_icon_1.png")
    research2 = load("p/research_icon_2.png")
    research = research0
    nursing0 = load("p/nursing_icon_0.png")
    nursing1 = load("p/nursing_icon_1.png")
    nursing2 = load("p/nursing_icon_2.png")
    nursing = nursing0
    job_curr = 0
    gym_curr = 0
    rlvl = None
    nlvl = None
    if P.prog[8][0][0] != -1:
        research = research1
        job_list.append("Research")
        rlvl = P.font_s.render(str(P.prog[8][0][0]),True,(0,0,0))
        rlength = P.font_s.size(str(P.prog[8][0][0]))[0]/2
    if P.prog[8][1][0] != -1:
        nursing = nursing1
        job_list.append("Nursing")
        nlvl = P.font_s.render(str(P.prog[8][1][0]),True,(0,0,0))
        nlength = P.font_s.size(str(P.prog[8][1][0]))[0]/2
    gym_list = []
    if P.prog[0] >= 48:
        gym_list.append("Analytic Badge")
    if P.prog[0] >= 86:
        gym_list.append("Affinity Badge")
    titletxt = P.font.render("",True,(255,255,255))
    titlex = 0
    info = 0
    back = back1
    end = True
    a = 0
    P.surface.blit(back,(0,0))
    if len(gym_list) > 0:
        P.surface.blit(analytic,(-6,235))
    if len(gym_list) > 1:
        P.surface.blit(affinity,(164,235))
    P.surface.blit(name,(230,30))
    P.surface.blit(money,(230,70))
    P.surface.blit(max,(230,110))
    P.surface.blit(time,(230,150))
    P.surface.blit(dex,(230,190))
    fade_in(P)
    tab = 0
    while end:
        P.surface.blit(back,(0,0))
        P.surface.blit(name,(230,30))
        P.surface.blit(money,(230,70))
        P.surface.blit(max,(230,110))
        P.surface.blit(time,(230,150))
        P.surface.blit(dex,(230,190))
        if tab == 0:
            if len(gym_list) > 0:
                P.surface.blit(analytic,(-6,235))
            if len(gym_list) > 1:
                P.surface.blit(affinity,(164,235))
        if tab == 1:
            if 'Research' in job_list:
                P.surface.fill((100,190,240), Rect(21,395-(P.prog[8][0][1]*1.2),150,P.prog[8][0][1]*1.2))
            P.surface.blit(research,(16,262))
            if rlvl:
                P.surface.blit(rlvl,(95-rlength,382))
            if 'Nursing' in job_list:
                P.surface.fill((255,246,233), Rect(191,395-(P.prog[8][1][1]*1.2),150,P.prog[8][1][1]*1.2))
            P.surface.blit(nursing,(186,262))
            if nlvl:
                P.surface.blit(nlvl,(265-rlength,382))
        if info == 1:
            P.surface.blit(txtbox,(0,180))
            P.surface.blit(titletxt,(400-titlex,195))
        for event in pygame.event.get(eventtype = KEYDOWN):
            if a > 10:
                if event.key == pygame.key.key_code(P.controls[4]) and info == 0 and len(gym_list) > 0:
                    if tab == 0:
                        titletxt = P.font.render("Analytic Badge",True,(255,255,255))
                        titlex = P.font.size("Analytic Badge")[0]/2
                        analytic = analytic2
                        info = 1
                        gym_curr = 0
                    if tab == 1:
                        if "Research" in job_list:
                            titletxt = P.font.render("Research",True,(255,255,255))
                            titlex = P.font.size("Research")[0]/2
                            research = research2
                            info = 1
                            job_curr = 0
                if event.key == pygame.key.key_code(P.controls[5]):
                    if info == 0:
                        end = False
                    else:
                        if research == research2:
                            research = research1
                        elif nursing == nursing2:
                            nursing = nursing1
                        analytic = analytic1
                        affinity = affinity1
                        info = 0
                if event.key == pygame.key.key_code(P.controls[1]) and tab == 0 and info == 0:
                    tab = 1
                    back = back2
                if event.key == pygame.key.key_code(P.controls[0]) and tab == 1 and info == 0:
                    tab = 0
                    back = back1
                if event.key == pygame.key.key_code(P.controls[2]) and info == 1:
                    if tab == 1:
                        if job_curr > 0:
                            job_curr -= 1
                            titletxt = P.font.render(job_list[job_curr],True,(255,255,255))
                            titlex = P.font.size(job_list[job_curr])[0]/2
                            research = research2
                            nursing = nursing1
                    else:
                        if gym_curr > 0:
                            gym_curr -= 1
                            titletxt = P.font.render(gym_list[gym_curr],True,(255,255,255))
                            titlex = P.font.size(gym_list[gym_curr])[0]/2
                            affinity = affinity1
                            analytic = analytic2
                if event.key == pygame.key.key_code(P.controls[3]) and info == 1:
                    if tab == 1:
                        if job_curr < len(job_list)-1:
                            job_curr += 1
                            titletxt = P.font.render(job_list[job_curr],True,(255,255,255))
                            titlex = P.font.size(job_list[job_curr])[0]/2
                            research = research1
                            nursing = nursing2
                    else:
                        if gym_curr < len(gym_list)-1:
                            gym_curr += 1
                            titletxt = P.font.render(gym_list[gym_curr],True,(255,255,255))
                            titlex = P.font.size(gym_list[gym_curr])[0]/2
                            affinity = affinity2
                            analytic = analytic1
                
        a += 1
        P.clock.tick(P.ani_spd)
        update_screen(P)
    fade_out(P)


def team(P) -> None:
    box = load("p/team_box_1.png")
    back = load("p/load_back.png")
    tbox = load("p/4_box.png")
    hp_b = load("p/team_hp.png")
    item_ico = pygame.transform.scale(load("p/item_icon.png"),(20,25))
    mega = pygame.transform.scale(load("p/mega_symbol.png"),(30,30))
    nurse = pygame.transform.scale(load("p/nurse_icon.png"),(30,30))
    end = True
    current = 0
    a = 0
    swc = 10
    while end:
        pos = 0
        x = 0
        y = 0
        P.surface.blit(back,(0,0))
        for p in P.party:
            if pos == current:
                box = load("p/team_box_2.png")
                if p.code[-2:] == '_S':
                    box = load("p/team_box_2_S.png")
            else:
                box = load("p/team_box_1.png")
                if p.code[-2:] == '_S':
                    box = load("p/team_box_1_S.png")
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
                status = load("p/"+p.status+"_ico.png")
                status = pygame.transform.scale(status,(50,20))
                P.surface.blit(status,(x+145,y+95))
            if p.item != None:
                P.surface.blit(item_ico,(x+70,y+70))
            pos += 1
        temp = P.surface.copy()
        for event in pygame.event.get(eventtype = KEYDOWN):
            if event.key == pygame.key.key_code(P.controls[5]) and a > 10:
                if swc < 10:
                    swc = 10
                    a = 1
                else:
                    end = False
            elif event.key == pygame.key.key_code(P.controls[0]) and current > 1:
                current -= 2
            elif event.key == pygame.key.key_code(P.controls[1]) and current < 4 and current+2 < len(P.party):
                current += 2
            elif event.key == pygame.key.key_code(P.controls[3]) and current % 2 == 0 and current+1 < len(P.party):
                current += 1
            elif event.key == pygame.key.key_code(P.controls[2]) and current % 2 != 0:
                current -= 1
            elif event.key == pygame.key.key_code(P.controls[4]) and swc < 10:
                if current != swc:
                    temporary = P.party[swc]
                    P.party[swc] = P.party[current]
                    P.party[current] = temporary
                swc = 10
                a = 1
            elif event.key == pygame.key.key_code(P.controls[4]) and a > 10 and swc == 10:
                P.surface.set_clip(Rect(0,0,800,600))
                new_txt(P)
                write(P,"Do what with "+P.party[current].name+"?")
                P.surface.blit(tbox,(550,230))
                summary = P.font.render("Summary",True,(0,0,0))
                switch = P.font.render("Switch",True,(0,0,0))
                item = P.font.render("Item",True,(0,0,0))
                cancel = P.font.render("Cancel",True,(0,0,0))
                P.clock.tick(5)
                ay = 240
                P.surface.blit(summary,(600,240))
                P.surface.blit(switch,(600,290))
                P.surface.blit(item,(600,340))
                P.surface.blit(cancel,(600,390))
                temp3 = P.surface.copy()
                P.surface.blit(P.arrow,(550,ay))
                update_screen(P)
                ans = 0
                tim = 0
                end1 = True
                while end1:
                    for event in pygame.event.get(eventtype = KEYDOWN):
                        if event.key == pygame.key.key_code(P.controls[4]) and tim > 10:
                            if ans == 0:
                                P.surface.set_clip(Rect(0,0,800,450))
                                P.surface.blit(temp,(0,0))
                                P.surface.set_clip(Rect(0,0,800,600))
                                update_screen(P)
                                temp4 = P.surface.copy()
                                fade_out(P)
                                summ(P,P.party[current])
                                P.surface.blit(temp4,(0,0))
                                fade_in(P)
                                endl = False
                                a = 1
                            if ans == 1:
                                P.surface.set_clip(Rect(0,0,800,450))
                                P.surface.blit(temp,(0,0))
                                P.surface.set_clip(Rect(0,0,800,600))
                                new_txt(P)
                                write(P,"Switch with who?")
                                swc = current
                                end1 = False
                            elif ans == 2:
                                P.surface.set_clip(Rect(0,0,800,450))
                                P.surface.blit(temp,(0,0))
                                P.surface.set_clip(Rect(0,0,800,600))
                                new_txt(P)
                                write(P,"Do what with an item?")
                                choic = multi_choice(P,4,temp,"Use","Give","Take","Cancel")
                                if choic == 0:
                                    t = P.surface.copy()
                                    fade_out(P)
                                    chose_item = bag(P,True)
                                    if chose_item == '' or items.Item(chose_item).type[0] != 'Evo':
                                        P.surface.blit(t,(0,0))
                                    if chose_item == '':
                                        fade_in(P)
                                    elif (items.Item(chose_item).type[0] == 'Potion' or items.Item(chose_item).name == 'Oran Berry') and P.party[current].ch < P.party[current].hp and P.party[current].status != 'Faint':
                                        fade_in(P)
                                        heal = items.Item(chose_item).mod()
                                        P.party[current].ch += heal
                                        if P.party[current].ch > P.party[current].hp:
                                            heal -= P.party[current].ch - P.party[current].hp
                                            P.party[current].ch = P.party[current].hp
                                        txt(P,P.party[current].name+"'s HP was restored","by "+str(heal)+" points!")
                                        add_item(P,chose_item,-1)
                                    elif items.Item(chose_item).type[0] == 'Food' and P.party[current].friend != 400:
                                        if items.Item(chose_item).mod()[1] == 'All' or items.Item(chose_item).mod()[1] in P.party[current].type:
                                            P.party[current].gain_friend(items.Item(chose_item).mod()[0])
                                            txt(P,P.party[current].name+" eagerly ate the",chose_item + " and grew", "friendlier!")
                                            add_item(P,chose_item,-1)
                                        else:
                                            P.party[current].gain_friend(items.Item(chose_item).mod()[0]/2)
                                            txt(P,P.party[current].name+" ate the",chose_item + " and grew", "friendlier!")
                                            add_item(P,chose_item,-1)
                                    elif items.Item(chose_item).name == 'Sitrus Berry' and P.party[current].ch < P.party[current].hp and P.party[current].status != 'Faint':
                                        fade_in(P)
                                        heal = int(P.party[current].hp/4)
                                        P.party[current].ch += heal
                                        if P.party[current].ch > P.party[current].hp:
                                            heal -= P.party[current].ch - P.party[current].hp
                                            P.party[current].ch = P.party[current].hp
                                        txt(P,P.party[current].name+"'s HP was restored","by "+str(heal)+" points!")
                                        add_item(P,chose_item,-1)
                                    elif items.Item(chose_item).type[0] == 'Battle Berry' and (type(items.Item(chose_item).mod()) == list and P.party[current].status in items.Item(chose_item).mod()[0]) or ((items.Item(chose_item).name == 'Lum Berry' or items.Item(chose_item).name == 'Persim Berry') and P.party[current].cfs > 0):
                                        fade_in(P)
                                        P.party[current].status = None
                                        s = items.Item(chose_item).mod()[0][0]
                                        if items.Item(chose_item).name == 'Lum Berry':
                                            if P.party[current].cfs > 0:
                                                P.party[current].cfs = 0
                                                txt(P,P.party[current].name + " was cured", "of confusion!")
                                            s = P.party[current].status
                                        if s == None:
                                            pass
                                        elif s == 'Slp':
                                            txt(P,P.party[current].name + " woke up!")
                                        elif s == 'Frz':
                                            txt(P,P.party[current].name + " thawed","out!")
                                        elif s == 'Brn':
                                            txt(P,P.party[current].name + " burn was","healed!")
                                        else:
                                            sta = items.Item(chose_item).mod()[1]
                                            if items.Item(chose_item).name == 'Lum Berry':
                                                if s == 'Par':
                                                    sta = 'Paralysis'
                                                else:
                                                    sta = 'Poisoning'
                                            txt(P,P.party[current].name + " was cured", "of "+sta+"!")
                                        if items.Item(chose_item).name == 'Persim Berry':
                                            P.party[current].cfs = 0
                                        else:
                                            P.party[current].status = None
                                        add_item(P,chose_item,-1)
                                    elif items.Item(chose_item).type[0] == 'Candy' and (poke_max(P,P.party[current]) == False or (chose_item == 'Expired Candy' and P.party[current].lvl > 1)):
                                        fade_in(P)
                                        if chose_item == 'Expired Candy':
                                            txt(P,P.party[current].name + "'s level dropped!")
                                            perc = P.party[current].exp/P.party[current].get_exp()
                                            P.party[current].lvl -= 1
                                            P.party[current].exp = perc*P.party[current].get_exp()
                                            P.party[current].update_stats()
                                            box = load("p/team_box_2.png")
                                            if P.party[current].code[-2:] == '_S':
                                                box = load("p/team_box_2_S.png")
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
                                                status = load("p/"+P.party[current].status+"_ico.png")
                                                status = pygame.transform.scale(status,(50,20))
                                                P.surface.blit(status,(x+145,y+95))
                                            if P.party[current].item != None:
                                                P.surface.blit(item_ico,(x+70,y+70))
                                        else:
                                            txt(P,P.party[current].name + " gained "+str(items.Item(chose_item).mod()),"Exp. Points!")
                                            ende = True
                                            exp = items.Item(chose_item).mod()
                                            while ende:
                                                P.party[current].exp += exp
                                                if P.party[current].exp >= P.party[current].get_exp():
                                                    exp = P.party[current].exp - P.party[current].get_exp()
                                                    P.party[current].exp = P.party[current].get_exp()
                                                else:
                                                    exp = 0
                                                    ende = False
                                                if poke_max(P,P.party[current]):
                                                    break
                                                if P.party[current].exp == P.party[current].get_exp():
                                                    txt(P,P.party[current].name + " leveled up!")
                                                    # thp = P.party[current].hp
                                                    P.party[current].lvlup(P,False,True)
                                                    # if P.party[current].status != 'Faint':
                                                    #     P.party[current].ch += P.party[current].hp-thp
                                                    box = load("p/team_box_2.png")
                                                    if P.party[current].code[-2:] == '_S':
                                                        box = load("p/team_box_2_S.png")
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
                                                        status = load("p/"+P.party[current].status+"_ico.png")
                                                        status = pygame.transform.scale(status,(50,20))
                                                        P.surface.blit(status,(x+145,y+95))
                                                    if P.party[current].item != None:
                                                        P.surface.blit(item_ico,(x+70,y+70))
                                        add_item(P,chose_item,-1)
                                    elif items.Item(chose_item).type[0] == 'Heart Scale' and items.Item(chose_item).can_hs(P.party[current]):
                                        if use_hs(P,P.party[current]):
                                            add_item(P,'Heart Scale',-1)
                                        else:
                                            pass
                                        P.surface.blit(t,(0,0))
                                        fade_in(P)
                                    elif items.Item(chose_item).type[0] == 'Evo':
                                        if P.party[current].evo != [] and P.party[current].evo[0] == chose_item:
                                            song = P.song
                                            fade_out(P,P.song)
                                            copy = P.party[current].copy()
                                            P.party[current] = poke.Poke(copy.evo[1],[copy.lvl,copy.gen,copy.ch,copy.m1,copy.p1,copy.m2,copy.p2,copy.m3,copy.p3,copy.m4,copy.p4,copy.item,copy.status,copy.exp,copy.ball,copy.friend,copy.ability,True])
                                            evolve(P,copy,P.party[current])
                                            P.surface.set_clip(Rect(0,0,800,600))
                                            play_music(P,song)
                                            add_item(P,chose_item,-1)
                                            a = -1
                                        elif P.party[current].code_nos() == 'Clamperl' and chose_item in ['Deep Sea Scale','Deep Sea Tooth']:
                                            song = P.song
                                            fade_out(P,P.song)
                                            copy = P.party[current].copy()
                                            ev = 'Huntail'
                                            if chose_item == 'Deep Sea Scale':
                                                ev = 'Gorebyss'
                                            P.party[current] = poke.Poke(ev,[copy.lvl,copy.gen,copy.ch,copy.m1,copy.p1,copy.m2,copy.p2,copy.m3,copy.p3,copy.m4,copy.p4,copy.item,copy.status,copy.exp,copy.ball,copy.friend,copy.ability,True])
                                            evolve(P,copy,P.party[current])
                                            P.surface.set_clip(Rect(0,0,800,600))
                                            play_music(P,song)
                                            add_item(P,chose_item,-1)
                                            a = -1
                                        else:
                                            fade_out(P)
                                            P.surface.blit(t,(0,0))
                                            fade_in(P)
                                            txt(P,"It won't have any effect.")
                                    elif items.Item(chose_item).type[0] == 'Balm Mushroom' and has_shiny(P.party[current]):
                                        fade_in(P)
                                        P.party[current].code += '_S'
                                        P.party[current].icon = pygame.transform.scale(pygame.image.load("p/poke/"+P.party[current].code+"_ico.png"),(70,70))
                                        txt(P,"Something strange happened","to "+P.party[current].name+"!")
                                        add_item(P,'Balm Mushroom',-1)
                                    else:
                                        fade_in(P)
                                        txt(P,"It won't have any effect.")
                                    if a != -1:
                                        a = 1
                                    end1 = False
                                elif choic == 1:
                                    t = P.surface.copy()
                                    fade_out(P)
                                    chose_item = bag(P,True)
                                    P.surface.blit(t,(0,0))
                                    fade_in(P)
                                    if chose_item:
                                        if P.party[current].item == None:
                                            txt(P,P.party[current].name + " was given the",chose_item+" to hold.")
                                            P.party[current].item = chose_item
                                            add_item(P,chose_item,-1)
                                        else:
                                            aan = "a "
                                            if P.party[current].item[0] in ['A','E','I','O','U']:
                                                aan = "an "
                                            txt(P,P.party[current].name + " is already holding",aan +P.party[current].item+".")
                                            new_txt(P)
                                            write(P,"Would you like to switch the","two items?")
                                            if choice(P,550,600):
                                                txt(P,"The "+P.party[current].item + " was taken and","replaced with the "+chose_item+".")
                                                add_item(P,P.party[current].item,1)
                                                P.party[current].item = chose_item
                                                add_item(P,chose_item,-1)
                                            else:
                                                pass
                                        end1 = False
                                        a = 1
                                    else:
                                        end1 = False
                                        a = 1
                                elif choic == 2:
                                    if P.party[current].item == None:
                                        txt(P,P.party[current].name+" isn't holding","anything!")
                                    else:
                                        txt(P,"Received the "+P.party[current].item ,"from " + P.party[current].name +".")
                                        add_item(P,P.party[current].item,1)
                                        P.party[current].item = None
                                    end1 = False
                                    a = 1
                                else:
                                    end1 = False
                                    a = 1
                            else:
                                end1 = False
                                a = 1
                        elif event.key == pygame.key.key_code(P.controls[5]) and tim > 10:
                            end1 = False
                            a = 1
                        elif event.key == pygame.key.key_code(P.controls[0]) and ans != 0:
                            ans -= 1
                            ay -= 50
                            P.surface.blit(temp3,(0,0))
                            P.surface.blit(P.arrow,(550,ay))
                        elif event.key == pygame.key.key_code(P.controls[1]) and ans != 3:
                            ans += 1;
                            ay += 50
                            P.surface.blit(temp3,(0,0))
                            P.surface.blit(P.arrow,(550,ay))
                    update_screen(P)
                    P.clock.tick(P.ani_spd)
                    tim += 1
                if a != -1:
                    P.surface.set_clip(Rect(0,0,800,450))
        if a == 0:
            fade_in(P)
        if a == 2:
            P.surface.set_clip(Rect(0,0,800,600))
            new_txt(P)
            write(P,"Choose a Pokemon.")
            P.surface.set_clip(Rect(0,0,800,450))
        a += 1
        P.clock.tick(P.ani_spd)
        update_screen(P)
    P.surface.set_clip(Rect(0,0,800,600))
    fade_out(P) 

def has_mega_stone(P,p,name = False):
    if p == 'Beedrill' and item_in_bag(P,"Beedrillite"):
        if name:
            return 'Beedrillite'
        return True
    elif p == 'Manectric' and item_in_bag(P,"Manectite"):
        if name:
            return 'Manectite'
        return True
    elif p == 'Heracross' and item_in_bag(P,"Heracronite"):
        if name:
            return 'Heracronite'
        return True
    elif p == 'Pinsir' and item_in_bag(P,"Pinsirite"):
        if name:
            return 'Pinsirite'
        return True
    elif p == 'Lopunny' and item_in_bag(P,"Lopunnite"):
        if name:
            return 'Lopunnite'
        return True
    elif p == 'Sableye' and item_in_bag(P,"Sablenite"):
        if name:
            return 'Sablenite'
        return True
    elif p == 'Steelix' and item_in_bag(P,"Steelixite"):
        if name:
            return 'Steelixite'
        return True
    elif p == 'Kangaskhan' and item_in_bag(P,"Kangaskhanite"):
        if name:
            return 'Kangaskhanite'
        return True
    else:
        return False

def trade_poke(P,poke_code,pick_poke = False,name_hater = False, nurse_poke = False, return_nurse = False, mega_poke = False,massage_poke = False):
    box = load("p/team_box_1.png")
    back = load("p/load_back.png")
    hp_b = load("p/team_hp.png")
    item_ico = pygame.transform.scale(load("p/item_icon.png"),(20,25))
    mega = pygame.transform.scale(load("p/mega_symbol.png"),(30,30))
    nurse = pygame.transform.scale(load("p/nurse_icon.png"),(30,30))
    able = P.font.render("ABLE",True,(255,255,255))
    notable = P.font.render("NOT ABLE",True,(255,255,255))
    end = True
    result = None
    current = 0
    a = 0
    while end:
        pos = 0
        x = 0
        y = 0
        P.surface.blit(back,(0,0))
        for p in P.party:
            if pos == current:
                box = load("p/team_box_2.png")
            else:
                box = load("p/team_box_1.png")
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
            if (p.code_nos() == poke_code and p.nurse == False) or (pick_poke and (massage_poke == False or p.friend < 400) and (mega_poke == False or has_mega_stone(P,p.code_nos())) and (name_hater == False or p.name != p.actual_name) and (nurse_poke == False or p.friend != 400) and (((p.nurse == False or massage_poke) and return_nurse == False) or (return_nurse and p.friend == 400 and p.nurse))):
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
                if (P.party[current].code_nos() == poke_code and P.party[current].nurse == False) or (pick_poke and (massage_poke == False or P.party[current].friend < 400) and (mega_poke == False or has_mega_stone(P,P.party[current].code_nos())) and (name_hater == False or P.party[current].name != P.party[current].actual_name) and (nurse_poke == False or P.party[current].friend != 400) and (((P.party[current].nurse == False or massage_poke) and return_nurse == False) or (return_nurse and P.party[current].friend == 400 and P.party[current].nurse))):
                    if P.party[current].item != None and (pick_poke == False or nurse_poke):
                        txt(P,P.party[current].name+" is holding an",'item.')
                        new_txt(P)
                        write(P,'Are you sure you want to',"select it?")
                        if choice(P):
                            result = P.party[current]
                            end = False
                        else:
                            a = 1
                    else:
                        result = P.party[current]
                        end = False
                else:
                    if return_nurse and P.party[current].nurse:
                        txt(P,P.party[current].name+"'s friendship isn't","maxed out yet!")
                    elif massage_poke:
                        txt(P,P.party[current].name+"'s friendship is","already maxed out!")
                    elif P.party[current].nurse:
                        if nurse_poke:
                            txt(P,"This would probably be a bad","idea...")
                        else:
                            txt(P,P.party[current].name+" is a nursing","Pokemon!")
                    elif name_hater:
                        txt(P,P.party[current].name+"'s name doesn't","need any changing!")
                    elif nurse_poke:
                        txt(P,P.party[current].name+"'s friendship is","already maxed out!")
                    elif mega_poke:
                        txt(P,"You don't have a stone for","this Pokemon!")
                    else:
                        txt(P,"That's not the right Pokemon!")
                    a = 1
        if a == 0:
            fade_in(P)
        if a == 2:
            P.surface.set_clip(Rect(0,0,800,600))
            new_txt(P)
            write(P,"Choose a Pokemon.")
            P.surface.set_clip(Rect(0,0,800,450))
        a += 1
        P.clock.tick(P.ani_spd)
        update_screen(P)
    P.surface.set_clip(Rect(0,0,800,600))
    fade_out(P)
    return result

def summ(P,poke) -> None:
    back = load("p/summary_1.png")
    if poke.code[-2:] == '_S':
        back = load("p/summary_1_S.png")
    friend = load("p/Friendship_f.png")
    ball = pygame.transform.scale(load("p/"+poke.ball+".png"),(30,30))
    full = pygame.transform.scale(load("p/poke/"+poke.code+"_full.png"),(340,340))
    name = P.font.render(poke.name,True,(255,255,255))
    name_size = P.font.size(poke.name)[0]
    mega = pygame.transform.scale(load("p/mega_symbol.png"),(30,30))
    nurse = pygame.transform.scale(load("p/nurse_icon.png"),(30,30))
    exp = load("p/summ_exp.png")
    next_exp = P.font_s.render("Next Level: "+str(poke.get_exp()-poke.exp),True,(255,255,255))
    if poke.lvl == 100:
        next_exp = P.font_s.render("Next Level: 0",True,(255,255,255))
    high = load("p/high_move.png")
    desc = load("p/move_desc.png")
    if poke.gen == 0:
        gen_i = load("p/boy_ico.png")
    if poke.gen == 1:
        gen_i = load("p/girl_ico.png")
    if poke.gen == 2:
        gen_i = load("p/blank.png")
    lvl = P.font.render("Lv."+str(poke.lvl),True,(255,255,255))
    item = P.font.render("Item     "+str(poke.item),True,(0,0,0))
    ability = P.font.render("Ability    "+poke.ability,True,(0,0,0))
    hp = P.font.render("HP       "+str(poke.hp),True,(0,0,0))
    atk = P.font.render("Attack   "+str(poke.ak),True,(0,0,0))
    satk = P.font.render("Sp.Atk   "+str(poke.sak),True,(0,0,0))
    df = P.font.render("Defense  "+str(poke.df),True,(0,0,0))
    sdf = P.font.render("Sp.Def   "+str(poke.sdf),True,(0,0,0))
    spd = P.font.render("Speed    "+str(poke.spd),True,(0,0,0))
    num_m = 0
    h = 0
    mn = 1
    if poke.m1 != None:
        num_m += 1
        m1 = P.font.render(str(poke.m1),True,(0,0,0))
        mt1 = load("p/"+moves.Move(poke.m1).type+"_ico.png")
        mp1 = P.font.render("PP "+str(poke.p1)+"/"+str(moves.Move(poke.m1).pp),True,(0,0,0))
    if poke.m2 != None:
        num_m += 1
        m2 = P.font.render(str(poke.m2),True,(0,0,0))
        mt2 = load("p/"+moves.Move(poke.m2).type+"_ico.png")
        mp2 = P.font.render("PP "+str(poke.p2)+"/"+str(moves.Move(poke.m2).pp),True,(0,0,0))
    if poke.m3 != None:
        num_m += 1
        m3 = P.font.render(str(poke.m3),True,(0,0,0))
        mt3 = load("p/"+moves.Move(poke.m3).type+"_ico.png")
        mp3 = P.font.render("PP "+str(poke.p3)+"/"+str(moves.Move(poke.m3).pp),True,(0,0,0))
    if poke.m4 != None:
        num_m += 1
        m4 = P.font.render(str(poke.m4),True,(0,0,0))
        mt4 = load("p/"+moves.Move(poke.m4).type+"_ico.png")
        mp4 = P.font.render("PP "+str(poke.p4)+"/"+str(moves.Move(poke.m4).pp),True,(0,0,0))
    type1 = load("p/"+poke.type[0]+"_ico.png")
    if poke.type[1] != None:
        type2 = load("p/"+poke.type[1]+"_ico.png")
    P.surface.blit(back,(0,0))
    if poke.lvl != 100:
        P.surface.fill((0,0,255), Rect(64,110,int(320*(poke.exp/poke.get_exp())),10))
    else:
        P.surface.fill((0,0,255), Rect(64,110,320,10))
    P.surface.blit(exp,(10,105))
    P.surface.blit(next_exp,(10,130))
    P.surface.blit(full,(30,162))
    P.surface.blit(ball,(18,18))
    P.surface.blit(name,(60,10))
    if poke.code[:5] == 'Mega_':
        P.surface.blit(mega,(65+name_size,20))
    if poke.nurse:
        P.surface.blit(nurse,(65+name_size,20))
    P.surface.blit(gen_i,(350,10))
    P.surface.blit(lvl,(20,50))
    P.surface.blit(item,(210,506))
    P.surface.blit(ability,(160,547))
    if poke.friend >= 0:
        P.surface.fill((255,120,180), Rect(17,505,min(26,poke.friend/100*26),40))
    if poke.friend >= 100:
        P.surface.fill((255,120,180), Rect(52,505,min(26,(poke.friend-100)/100*26),40))
    if poke.friend >= 200:
        P.surface.fill((255,120,180), Rect(87,505,min(26,(poke.friend-200)/100*26),40))
    if poke.friend >= 300:
        if poke.friend == 400:
            color = (255,240,0)
        else:
            color = (220,0,0)
        P.surface.fill(color, Rect(122,505,min(26,(poke.friend-300)/100*26),40))
    P.surface.blit(friend,(10,500))
    if poke.m1 != None:
        P.surface.blit(m1,(430,115))
        P.surface.blit(mt1,(425,155))
        P.surface.blit(mp1,(550,150))
    if poke.m2 != None:
        P.surface.blit(m2,(430,210))
        P.surface.blit(mt2,(425,250))
        P.surface.blit(mp2,(550,245))
    if poke.m3 != None:
        P.surface.blit(m3,(430,305))
        P.surface.blit(mt3,(425,345))
        P.surface.blit(mp3,(550,340))
    if poke.m4 != None:
        P.surface.blit(m4,(430,400))
        P.surface.blit(mt4,(425,440))
        P.surface.blit(mp4,(550,435))
    P.surface.blit(type1,(170,55))
    if poke.type[1] != None:
        P.surface.blit(type2,(280,55))
    fade_in(P)
    a = 0
    pos = 0
    end = True
    while end:
        if mn == 1:
            mv = moves.Move(poke.m1)
        if mn == 2:
            mv = moves.Move(poke.m2)
        if mn == 3:
            mv = moves.Move(poke.m3)
        if mn == 4:
            mv = moves.Move(poke.m4)
        P.surface.blit(back,(0,0))
        if poke.lvl != 100:
            P.surface.fill((0,0,255), Rect(64,110,int(320*(poke.exp/poke.get_exp())),10))
        else:
            P.surface.fill((0,0,255), Rect(64,110,320,10))
        P.surface.blit(exp,(10,105))
        P.surface.blit(next_exp,(10,130))
        P.surface.blit(full,(30,162))
        P.surface.blit(ball,(18,18))
        P.surface.blit(name,(60,10))
        if poke.code[:5] == 'Mega_':
            P.surface.blit(mega,(65+name_size,20))
        if poke.nurse:
            P.surface.blit(nurse,(65+name_size,20))
        P.surface.blit(gen_i,(350,10))
        P.surface.blit(lvl,(20,50))
        P.surface.blit(item,(210,506))
        P.surface.blit(ability,(160,547))
        if poke.friend >= 0:
            P.surface.fill((255,120,180), Rect(17,505,min(26,poke.friend/100*26),40))
        if poke.friend >= 100:
            P.surface.fill((255,120,180), Rect(52,505,min(26,(poke.friend-100)/100*26),40))
        if poke.friend >= 200:
            P.surface.fill((255,120,180), Rect(87,505,min(26,(poke.friend-200)/100*26),40))
        if poke.friend >= 300:
            if poke.friend == 400:
                color = (255,240,0)
            else:
                color = (220,0,0)
            P.surface.fill(color, Rect(122,505,min(26,(poke.friend-300)/100*26),40))
        P.surface.blit(friend,(10,500))
        if h == 1:
            if mv.cat == '0':
                cat_ico = load("p/phy_ico.png")
            elif mv.cat == '1':
                cat_ico = load("p/spe_ico.png")
            else:
                cat_ico = load("p/sta_ico.png")
            P.surface.blit(high,(410,15+(95*mn)))
            P.surface.blit(desc,(5,130))
            cat = P.font.render("Category",True,(0,0,0))
            power = P.font.render("Power     "+mv.pow,True,(0,0,0))
            if int(float(mv.acc)*100) > 100:
                acc = P.font.render("Accuracy  ---",True,(0,0,0))
            else:
                acc = P.font.render("Accuracy  "+str(int(float(mv.acc)*100)),True,(0,0,0))
            descr = []
            cngy = 0
            for x in mv.desc:
                descr.append(P.font_s.render(x,True,(0,0,0)))
            for x in descr:
                P.surface.blit(x,(20,285+cngy))
                cngy += 34
            P.surface.blit(cat,(20,135))
            P.surface.blit(cat_ico,(270,140))
            P.surface.blit(power,(20,185))
            P.surface.blit(acc,(20,235))
        if pos == 0:
            if poke.m1 != None:
                P.surface.blit(m1,(430,115))
                P.surface.blit(mt1,(425,155))
                P.surface.blit(mp1,(550,150))
            if poke.m2 != None:
                P.surface.blit(m2,(430,210))
                P.surface.blit(mt2,(425,250))
                P.surface.blit(mp2,(550,245))
            if poke.m3 != None:
                P.surface.blit(m3,(430,305))
                P.surface.blit(mt3,(425,345))
                P.surface.blit(mp3,(550,340))
            if poke.m4 != None:
                P.surface.blit(m4,(430,400))
                P.surface.blit(mt4,(425,440))
                P.surface.blit(mp4,(550,435))
        if pos == 1:
            P.surface.blit(hp,(420,116))
            P.surface.blit(atk,(420,181))
            P.surface.blit(satk,(420,245))
            P.surface.blit(df,(420,309))
            P.surface.blit(sdf,(420,373))
            P.surface.blit(spd,(420,437))
        P.surface.blit(type1,(170,55))
        if poke.type[1] != None:
            P.surface.blit(type2,(280,55))
        for event in pygame.event.get(eventtype = KEYDOWN):
            if event.key == pygame.key.key_code(P.controls[3]) and h == 0:
                if pos == 0:
                    back = load("p/summary_2.png")
                    if poke.code[-2:] == '_S':
                        back = load("p/summary_2_S.png")
                    pos = 1
            elif event.key == pygame.key.key_code(P.controls[2]):
                if pos == 1:
                    back = load("p/summary_1.png")
                    if poke.code[-2:] == '_S':
                        back = load("p/summary_1_S.png")
                    pos = 0
            elif event.key == pygame.key.key_code(P.controls[5]) and a>20:
                if h == 1:
                    h = 0
                else:
                    end = False
            elif event.key == pygame.key.key_code(P.controls[4]) and a>20 and pos == 0:
                h = 1
                mn = 1
            elif event.key == pygame.key.key_code(P.controls[0]) and h == 1:
                if mn > 1:
                    mn -= 1
            elif event.key == pygame.key.key_code(P.controls[1]) and h == 1:
                if mn < num_m:
                    mn += 1
        a += 1
        P.clock.tick(P.ani_spd)
        update_screen(P)
    fade_out(P)
    
def poke_party_to_list(party) -> dict:
    ans = []
    for x in party:
        ans.append([x.code,x.to_list()])
    return ans

def menu(P,saturday = False) -> None:
    t = P.surface.copy()
    poke_ico_1 = load("p/poke_ico_1.png")
    poke_ico_2 = load("p/poke_ico_2.png")
    save_ico_1 = load("p/save_ico_1.png")
    save_ico_2 = load("p/save_ico_2.png")
    exit_ico_1 = load("p/exit_ico_1.png")
    exit_ico_2 = load("p/exit_ico_2.png")
    bag_ico_1 =  load("p/bag_ico_1.png")
    bag_ico_2 =  load("p/bag_ico_2.png")
    dex_ico_1 =  load("p/dex_ico_1.png")
    dex_ico_2 =  load("p/dex_ico_2.png")
    set_ico_1 =  load("p/settings_ico_1.png")
    set_ico_2 =  load("p/settings_ico_2.png")
    prof_ico_1 =  load("p/profile_ico_1.png")
    prof_ico_2 =  load("p/profile_ico_2.png")
    back_1 = load("p/menu_back_1.png")
    back_2 = load("p/menu_back_2.png")
    trans = load("p/menu_trans.png")
    p = poke_ico_1
    s = save_ico_1
    e = exit_ico_1
    b = bag_ico_1
    d = dex_ico_1
    se = set_ico_1
    pr = prof_ico_1
    py = 0
    sy = 0
    ey = 0
    by = 0
    dy = 0
    sey = 0
    pry = 0
    end = True
    pos = 1
    tim = 0
    while end:
        P.surface.blit(t,(0,0))
        P.surface.blit(trans,(0,0))
        P.surface.blit(back_2,(0,-290+py*1.5))
        P.surface.blit(back_1,(0,-195+py))
        P.surface.blit(p,(10,-145+py))
        P.surface.blit(d,(120,-145+dy))
        P.surface.blit(b,(230,-145+by))
        P.surface.blit(pr,(340,-145+pry))
        P.surface.blit(se,(450,-145+sey))
        P.surface.blit(s,(560,-145+sy))
        P.surface.blit(e,(670,-145+ey))
        for event in map_keys():
            if event.type == KEYDOWN and tim > 10:
                if event.key == pygame.key.key_code(P.controls[2]):
                    if pos != 1:
                        pos -= 1
                        if pos == 1:
                            p = poke_ico_2
                            d = dex_ico_1
                        if pos == 2:
                            d = dex_ico_2
                            b = bag_ico_1
                        if pos == 3:
                            b = bag_ico_2
                            pr = prof_ico_1
                        if pos == 4:
                            pr = prof_ico_2
                            se = set_ico_1
                        if pos == 5:
                            se = set_ico_2
                            s = save_ico_1
                        if pos == 6:
                            s = save_ico_2
                            e = exit_ico_1
                if event.key == pygame.key.key_code(P.controls[3]):
                    if pos != 7:
                        pos += 1
                        if pos == 2:
                            d = dex_ico_2
                            p = poke_ico_1
                        if pos == 3:
                            b = bag_ico_2
                            d = dex_ico_1
                        if pos == 4:
                            pr = prof_ico_2
                            b = bag_ico_1
                        if pos == 5:
                            se = set_ico_2
                            pr = prof_ico_1
                        if pos == 6:
                            s = save_ico_2
                            se = set_ico_1
                        if pos == 7:
                            e = exit_ico_2
                            s = save_ico_1
                if event.key == pygame.key.key_code(P.controls[4]):
                    tim = 0
                    if pos == 1:
                        tem = P.surface.copy()
                        fade_out(P)
                        team(P)
                        P.surface.blit(tem,(0,0))
                        fade_in(P)
                    if pos == 2:
                        tem = P.surface.copy()
                        fade_out(P)
                        pokedex(P)
                        P.surface.blit(tem,(0,0))
                        fade_in(P)
                    if pos == 3:
                        tem = P.surface.copy()
                        fade_out(P)
                        bag(P)
                        if P.use_key_item != None:
                            P.surface.blit(t,(0,0))
                            fade_in(P)
                            end = False
                        else:
                            P.surface.blit(tem,(0,0))
                            fade_in(P)
                    if pos == 4:
                        tem = P.surface.copy()
                        fade_out(P)
                        profile(P)
                        P.surface.blit(tem,(0,0))
                        fade_in(P)
                    if pos == 5:
                        tem = P.surface.copy()
                        fade_out(P)
                        settings(P,saturday)
                        P.surface.blit(tem,(0,0))
                        fade_in(P)
                    if pos == 6:
                        mem(P)
                        new_txt(P)
                        write(P,"Saved.")
                        cont(P)
                    if pos == 7:
                        new_txt(P)
                        write(P,"Are you sure you want to exit?")
                        if choice(P):
                            P.running = False
                        # pygame.quit()
                        # sys.exit()
                if event.key == pygame.key.key_code(P.controls[5]):
                    end = False
                if event.key == pygame.key.key_code(P.controls[6]):
                    end = False
        if py < 150:
            py += 5
        if sy < 150:
            sy += 5
        if ey < 150:
            ey += 5
        if by < 150:
            by += 5
        if pry < 150:
            pry += 5
        if sey < 150:
            sey += 5
        if dy < 150:
            dy += 5
        if py == 150 and pos == 1:
            p = poke_ico_2
        if py == 150:
            tim += 1
        P.clock.tick(P.ani_spd)
        update_screen(P)
    end = True
    if P.use_key_item != None:
        end = False
    p = poke_ico_1
    s = save_ico_1
    e = exit_ico_1
    b = bag_ico_1
    d = dex_ico_1
    pr = prof_ico_1
    se = set_ico_1
    while end:
        P.surface.blit(t,(0,0))
        P.surface.blit(back_2,(0,-290+py*1.5))
        P.surface.blit(back_1,(0,-195+py))
        P.surface.blit(p,(10,-145+py))
        P.surface.blit(d,(120,-145+dy))
        P.surface.blit(b,(230,-145+by))
        P.surface.blit(pr,(340,-145+pry))
        P.surface.blit(se,(450,-145+sey))
        P.surface.blit(s,(560,-145+sy))
        P.surface.blit(e,(670,-145+ey))
        py -= 5
        sy -= 5
        ey -= 5
        by -= 5
        pry -= 5
        sey -= 5
        dy -= 5
        if py == 0:
            end = False
        P.clock.tick(P.ani_spd)
        update_screen(P)
    if P.use_key_item != None:
        use_keyitem(P,P.use_key_item)
        P.use_key_item = None

def use_keyitem(P,item):
    if item == 'Map':
        t = P.surface.copy()
        fade_out(P)
        l = open_map(P,True)
        P.surface.blit(t,(0,0))
        fade_in(P)
    if item == 'Felling Axe':
        if P.loc == 'scarab_l':
            if next_to(P,P.sl_tree1.x,P.sl_tree1.y):
                P.sl_tree1.cut(True)
            elif next_to(P,P.sl_tree2.x,P.sl_tree2.y):
                P.sl_tree2.cut(True)
            elif next_to(P,P.sl_tree3.x,P.sl_tree3.y):
                P.sl_tree3.cut(True)
            elif next_to(P,P.sl_tree4.x,P.sl_tree4.y):
                P.sl_tree4.cut(True)
            elif next_to(P,P.sl_tree5.x,P.sl_tree5.y):
                P.sl_tree5.cut(True)
            else:
                txt(P,"There's no tree to cut down!")
        elif P.loc == 'fiore':
            if next_to(P,P.fio_tree1.x,P.fio_tree1.y):
                P.fio_tree1.cut(True)
            elif next_to(P,P.fio_tree2.x,P.fio_tree2.y):
                P.fio_tree2.cut(True)
            elif next_to(P,P.fio_tree3.x,P.fio_tree3.y):
                P.fio_tree3.cut(True)
            else:
                txt(P,"There's no tree to cut down!")
        elif P.loc == 'route_2':
            if next_to(P,P.r2_tree1.x,P.r2_tree1.y):
                P.r2_tree1.cut(True)
            else:
                txt(P,"There's no tree to cut down!")
        elif P.loc == 'scarab_r':
            if next_to(P,P.sr_tree1.x,P.sr_tree1.y):
                P.sr_tree1.cut(True)
            elif next_to(P,P.sr_tree2.x,P.sr_tree2.y):
                P.sr_tree2.cut(True)
            elif next_to(P,P.sr_tree3.x,P.sr_tree3.y):
                P.sr_tree3.cut(True)
            elif next_to(P,P.sr_tree4.x,P.sr_tree4.y):
                P.sr_tree4.cut(True)
            elif next_to(P,P.sr_tree5.x,P.sr_tree5.y):
                P.sr_tree5.cut(True)
            elif next_to(P,P.sr_tree6.x,P.sr_tree6.y):
                P.sr_tree6.cut(True)
            elif next_to(P,P.sr_tree7.x,P.sr_tree7.y):
                P.sr_tree7.cut(True)
            elif next_to(P,P.sr_tree8.x,P.sr_tree8.y):
                P.sr_tree8.cut(True)
            else:
                txt(P,"There's no tree to cut down!")
        elif P.loc == 'route_4':
            if next_to(P,P.r4_tree1.x,P.r4_tree1.y):
                P.r4_tree1.cut(True)
            elif next_to(P,P.r4_tree2.x,P.r4_tree2.y):
                P.r4_tree2.cut(True)
            else:
                txt(P,"There's no tree to cut down!")
        elif P.loc == 'route_5':
            if next_to(P,P.r5_tree1.x,P.r5_tree1.y):
                P.r5_tree1.cut(True)
            elif next_to(P,P.r5_tree2.x,P.r5_tree2.y):
                P.r5_tree2.cut(True)
            elif next_to(P,P.r5_tree3.x,P.r5_tree3.y):
                P.r5_tree3.cut(True)
            else:
                txt(P,"There's no tree to cut down!")
        else:
            txt(P,"There's no tree to cut down!")
    elif item == 'Lantern':
        if P.loc == 'mirror_cave':
            if P.mc_dark == P.mc_darkness:
                txt(P,"The lantern shone brightly!")
                P.mc_dark = P.mc_light
            else:
                txt(P,"You put the lantern away.")
                P.mc_dark = P.mc_darkness
        else:
            txt(P,"There's no need to use the","lantern here!")

def register(P):
    t = P.surface.copy()
    reg = load("p/register.png")
    regl = load("p/register_l.png")
    regu = load("p/register_u.png")
    regd = load("p/register_d.png")
    regr = load("p/register_r.png")
    back = reg
    if P.save_data.register[0] != None:
        up = pygame.transform.scale(load("p/item/"+P.save_data.register[0]+".png"),(40,40))
    else:
        up = load("p/blank.png")
    if P.save_data.register[1] != None:
        right = pygame.transform.scale(load("p/item/"+P.save_data.register[1]+".png"),(40,40))
    else:
        right = load("p/blank.png")
    if P.save_data.register[2] != None:
        down = pygame.transform.scale(load("p/item/"+P.save_data.register[2]+".png"),(40,40))
    else:
        down = load("p/blank.png")
    if P.save_data.register[3] != None:
        left = pygame.transform.scale(load("p/item/"+P.save_data.register[3]+".png"),(40,40))
    else:
        left = load("p/blank.png")
    end = True
    choose = None
    tim = 0
    while end:
        P.surface.blit(t,(0,0))
        P.surface.blit(back,(275,175))
        P.surface.blit(up,(380,220))
        P.surface.blit(right,(435,275))
        P.surface.blit(down,(380,330))
        P.surface.blit(left,(325,275))
        for event in map_keys():
            if event.type == KEYDOWN and tim > 10:
                if event.key == pygame.key.key_code(P.controls[0]):
                    back = regu
                    tim = -20
                    choose = P.save_data.register[0]
                if event.key == pygame.key.key_code(P.controls[1]):
                    back = regd
                    tim = -20
                    choose = P.save_data.register[2]
                if event.key == pygame.key.key_code(P.controls[2]):
                    back = regl
                    tim = -20
                    choose = P.save_data.register[3]
                if event.key == pygame.key.key_code(P.controls[3]):
                    back = regr
                    tim = -20
                    choose = P.save_data.register[1]
                if event.key == pygame.key.key_code(P.controls[4]):
                    pass
                if event.key == pygame.key.key_code(P.controls[5]):
                    end = False
                if event.key == pygame.key.key_code(P.controls[7]):
                    end = False
        tim += 1
        if tim == -1:
            end = False
        P.clock.tick(P.ani_spd)
        update_screen(P)
    if choose != None:
        P.surface.blit(t,(0,0))
        use_keyitem(P,choose)

def update_screen(P):
    if P.running == False:
        pygame.quit()
        sys.exit()
    #P.screen.blit(P.surface,(0,0))
    pygame.display.update()

def no_move(P) -> bool:
    return P.xr == 0 and P.xl == 0 and P.yu == 0 and P.yd == 0

def blit_reverse_player(P,dir,val,sableye = 0):
    sprites = [P.u1,P.u2,P.u3,P.d1,P.d2,P.d3,P.l1,P.l2,P.l3,P.r1,P.r2,P.r3]
    if in_party(P,'Sableye',True) and P.prog[15][0] != 0 and P.prog[0] >= 89 and P.prog[15][9] != sableye and P.prog[15][9] != 6 and sableye != 0:
        new_sprites = [P.sableye_u1,P.sableye_u2,P.sableye_u3,P.sableye_d1,P.sableye_d2,P.sableye_d3,P.sableye_l1,P.sableye_l2,P.sableye_l3,P.sableye_r1,P.sableye_r2,P.sableye_r3]
    else:
        new_sprites = [P.u1,P.u2,P.u3,P.d1,P.d2,P.d3,P.l1,P.l2,P.l3,P.r1,P.r2,P.r3]
    pos = sprites.index(P.p)
    if dir == 'u':
        if pos < 3:
            pos += 3
        elif pos < 6:
            pos -= 3
    else:
        if pos > 8:
            pos -= 3
        elif pos > 5:
            pos += 3
    if dir == 'u':
        x = 0
        y = -50+(1.8*(P.py-val))
    if dir == 'r':
        x = 50+(1.8*(P.px-val))
        y = 0
    P.surface.blit(P.char_shad,(376+x,288+y))
    P.surface.blit(new_sprites[pos],(375+x,265+y))

def player_move(P, rects = [],rs = [],ls = [], manual_input = None,mod = 0,modx = 0,spd = None) -> None:
    if P.move_out_dir != None:
        manual_input = P.move_out_dir
        P.move_out_dir = None
    keys = pygame.key.get_pressed()
    if keys[pygame.key.key_code(P.controls[5])] and manual_input == None:
        times = P.walk_spd+3
    else:
        times = P.walk_spd
    if spd != None:
        times = spd
    plx = 375
    ply = 265
    if ((keys[pygame.key.key_code(P.controls[0])] and manual_input == None) or manual_input == 'u') and P.x == 0 and no_move(P):
        if P.y == 0:
            P.p = P.u1
        P.y = -1
    elif ((keys[pygame.key.key_code(P.controls[1])] and manual_input == None) or manual_input == 'd') and P.x == 0 and no_move(P):
        if P.y == 0:
            P.p = P.d1
        P.y = 1
    else:
        P.y = 0
    if ((keys[pygame.key.key_code(P.controls[3])] and manual_input == None) or manual_input == 'r') and P.y == 0 and no_move(P):
        if P.x == 0:
            P.p = P.r1
        P.x = -1
    elif ((keys[pygame.key.key_code(P.controls[2])] and manual_input == None) or manual_input == 'l') and P.y == 0 and no_move(P):
        if P.x == 0:
            P.p = P.l1
        P.x = 1
    else:
        P.x = 0
        P.moving = False
    for x in range(times):
        if (P.x == -1 or P.xr != 0):
            m = True
            for x in rects:
                if pygame.Rect(plx+1,ply,50,60).colliderect(x):
                    m = False
                    P.moving = False
            if m:
                P.moving = True
                P.px -= 1
                plx += 1
                P.xr += 1
                for rect in rs:
                    if rect.collidepoint(plx+24,ply+50):
                        P.py += 1
                        ply -= 1
                for rect in ls:
                    if rect.collidepoint(plx+24,ply+50):
                        P.py -= 1
                        ply += 1
                if P.px % 50 == 0:
                    if P.px % 100 >= 50:
                        P.p = P.r2
                    else:
                        P.p = P.r3
                elif P.px % 25 == 0:
                    P.p = P.r1
                    # if P.p == P.r2:
                    #     P.p = P.r3
                    # else:
                    #     P.p = P.r2
        if (P.x == 1 or P.xl != 0):
            m = True
            for x in rects:
                if pygame.Rect(plx-1,ply,50,60).colliderect(x):
                    m = False
                    P.moving = False
            if m:
                P.moving = True
                P.px += 1
                plx -= 1
                P.xl += 1
                for rect in rs:
                    if rect.collidepoint(plx+25,ply+50):
                        P.py -= 1
                        ply += 1
                for rect in ls:
                    if rect.collidepoint(plx+25,ply+50):
                        P.py += 1
                        ply -= 1
                if P.px % 50 == 0:
                    if P.px % 100 >= 50:
                        P.p = P.l2
                    else:
                        P.p = P.l3
                elif P.px % 25 == 0:
                    P.p = P.l1
                # if P.px % 25 == 0:
                #     if P.p == P.l2:
                #         P.p = P.l3
                #     else:
                #         P.p = P.l2
        if (P.y == -1 or P.yu != 0):
            m = True
            modif = 0
            for rect in rs:
                if rect.collidepoint(plx+25,ply+50):
                    modif = 25
            for rect in ls:
                if rect.collidepoint(plx+25,ply+50):
                    modif = 25
            for x in rects:
                if pygame.Rect(plx,ply-1,50,60).colliderect(x):
                    m = False
                    P.moving = False
            if m:
                P.moving = True
                P.py += 1
                ply -= 1
                P.yu += 1
                if (P.py+modif) % 50 == 0:
                    if (P.py+modif) % 100 >= 50:
                        P.p = P.u2
                    else:
                        P.p = P.u3
                elif (P.py+modif) % 25 == 0:
                    P.p = P.u1
                # if P.py % 25 == 0:
                #     if P.p == P.u2:
                #         P.p = P.u3
                #     else:
                #         P.p = P.u2
        if (P.y == 1 or P.yd != 0):
            m = True
            modif = 0
            for rect in rs:
                if rect.collidepoint(plx+25,ply+50):
                    modif = 25
            for rect in ls:
                if rect.collidepoint(plx+25,ply+50):
                    modif = 25
            for x in rects:
                if pygame.Rect(plx,ply+1,50,60).colliderect(x):
                    m = False
                    P.moving = False
            if m:
                P.moving = True
                P.py -= 1
                ply += 1
                P.yd += 1
                if (P.py+modif)  % 50== 0:
                    if (P.py+modif)  % 100 >= 50:
                        P.p = P.d2
                    else:
                        P.p = P.d3
                elif (P.py+modif) % 25 == 0:
                    P.p = P.d1
                # if P.py % 25 == 0:
                #     if P.p == P.d2:
                #         P.p = P.d3
                #     else:
                #         P.p = P.d2
        if P.xr == 50:
            friend_walk_gain(P)
            P.xr = 0
        if P.xl == 50:
            friend_walk_gain(P)
            P.xl = 0
        if P.yu == 50:
            friend_walk_gain(P)
            P.yu = 0
        if P.yd == 50:
            friend_walk_gain(P)
            P.yd = 0
        pygame.event.pump()
    if manual_input != None:
        P.moving = False
    P.surface.blit(P.char_shad,(376+modx,288+mod))
    P.surface.blit(P.p,(375+modx,265+P.ledge+mod))

def friend_walk_gain(P):
    for p in P.party:
        if p.status != 'Faint':
            p.gain_friend(.01,P)

def blit_player(P,mod = 0,modx = 0):
    P.surface.blit(P.char_shad,(376+modx,288+mod))
    P.surface.blit(P.p,(375+modx,265+mod))
                
def title_screen(P) -> None:
    P.song = "music/title.wav"
    pygame.mixer.music.load(P.song)
    set_mixer_volume(P,P.vol)
    pygame.mixer.music.play(-1)
    logo = load("p/rose_logo.png")
    back = load("p/title_back.png")
    as1 = load("p/latias1.png")
    as2 = load("p/latias2.png")
    os1 = load("p/latios1.png")
    os2 = load("p/latios2.png")
    start = load("p/z_to_start.png")
    P.surface.fill((255,255,255))
    P.surface.blit(back,(-100,0))
    a = -550
    b = 40
    c = -100
    d = 0
    e = -60
    f = -60
    g = 0
    back_c = 0
    end = True
    fade_in(P)
    while end:
        if back_c == 0:
            P.surface.blit(back,(-100-g,0-0.25*g))
        if back_c == 1:
            P.surface.blit(back,(-700+g,-150-0.25*g))
        if back_c == 2:
            P.surface.blit(back,(-100-g,-300-0.25*g))
        if back_c == 3:
            P.surface.blit(back,(-700+g,-450+0.25*g))
        if back_c == 4:
            P.surface.blit(back,(-100-g,-300+0.25*g))
        if back_c == 5:
            P.surface.blit(back,(-700+g,-150+0.25*g))
        if c <= 200:
            P.surface.blit(as1,(2000-15*c,1000-8*c))
        if e <= 0:
            P.surface.blit(os2,(280,50-e*10))
        if e > 0 and e <= 50:
            P.surface.blit(os2,(280,50-e))
        if e > 50 and e <= 100:
            P.surface.blit(os2,(280,0+(e-50)))
        if e > 100:
            P.surface.blit(os2,(280,50))
        P.surface.blit(logo,(0,a))
        if f <= 0:
            P.surface.blit(as2,(-20,300+f*10))
        if f > 0 and f <= 50:
            P.surface.blit(as2,(-20,300-f))
        if f > 50 and f <= 100:
            P.surface.blit(as2,(-20,250+(f-50)))
        if f > 100:
            P.surface.blit(as2,(-20,300))
        if d <= 250:
            P.surface.blit(os1,(-1800+15*d,300-1*d))
        if a < 0:
            a += 8
        if b >= 15:
            P.surface.blit(start,(150,450))
        if b == 0:
            b = 40
        if e == 120:
            e = 0
        if f == 125:
            f = 0
        if g == 600:
            g = 0
            back_c += 1
            if back_c == 6:
                back_c = 0
        if a > 0:
            for event in pygame.event.get(eventtype = KEYDOWN):
                if event.key == pygame.key.key_code(P.controls[4]):
                    end = False
        update_screen(P)
        P.clock.tick(P.ani_spd)
        b -= 1
        g += 1
        if a >= 0:
            c += 1
        if c > 250:
            d += 1
        if d > 300:
            e += 1
        if e >= 0:
            f += 1
    fade_out(P,P.song)

def load_save(save_files, P,position = -1, fade = True) -> None:
    if P.song != "music/load.wav":
        P.song = "music/load.wav"
        pygame.mixer.music.load(P.song)
        set_mixer_volume(P,P.vol,P.song)
        pygame.mixer.music.play(-1)
    back = load("p/load_back_real.png")
    P.surface.blit(back,(0,0))
    save_b = load("p/save_box.png")
    counter = 0
    txt_color = (99,50,57)
    for x in save_files:
        P.surface.blit(save_b,(0,0+counter*90))
        text = P.font.render(x[:-1],True,(59,20,27))
        P.surface.blit(text,(60, 7+counter*90))
        f = open("save_files/"+x[:-1]+".txt","r")
        data = f.readlines()
        data_temp = save.Save(data)
        P.loc = data_temp.loc
        if data_temp.prog[0] < 8:
            text2 = P.font_s.render("Ferry",True,txt_color)
        else:
            text2 = P.font_s.render(get_location(P),True,txt_color)
        #textlen = P.font_s.size("Location: "+get_location(P))[0]
        P.surface.blit(text2,(60, 47+counter*90))
        badges = 0
        if data_temp.prog[0] >= 47:
            badges += 1
        if data_temp.prog[0] >= 86:
            badges += 1
        text3 = P.font_s.render("Badges: "+str(badges),True,txt_color)
        P.surface.blit(text3,(350, 15+counter*90))
        dex_count = 0
        for pok in data_temp.pokedex:
            if data_temp.pokedex[pok][0] == 1:
                dex_count += 1
        text5 = P.font_s.render("Pokedex: "+str(dex_count),True,txt_color)
        P.surface.blit(text5,(550, 15+counter*90))
        time_str = ""
        if data_temp.time[0] < 10:
            time_str += '0'
        time_str += str(data_temp.time[0])
        if data_temp.time[1] < 10:
            time_str += ':0'
        else:
            time_str += ':'
        time_str += str(data_temp.time[1])
        text4 = P.font_s.render("Play Time: "+time_str,True,txt_color)
        P.surface.blit(text4,(350, 47+counter*90))
        counter+=1
        f.close()
    if counter < 6:
        P.surface.blit(save_b,(0,450))
        text = P.font.render("New Save",True,(59,20,27))
        P.surface.blit(text,(60,473))
    del_text = P.font_s.render("Press "+P.controls[6]+" to delete a save",True,txt_color)
    del_len = P.font_s.size("Press "+P.controls[6]+" to delete a save")[0]/2
    P.surface.blit(del_text,(400-del_len,557))
    temp = P.surface.copy()
    if position == -1:
        fade_in(P)
        pos = 1
        a = 0
    else:
        pos = position
        a = 15
    P.surface.blit(P.arrow,(10,-65+90*pos))
    end = True
    while end:
        for event in pygame.event.get(eventtype = KEYDOWN):
            if a == 0:
                P.surface.blit(temp,(0,0))
                P.surface.blit(P.arrow,(10,25))
            if a > 20:
                if event.key == pygame.key.key_code(P.controls[0]):
                    if pos != 1:
                        if pos == 6 and counter < 5:
                            if len(save_files) == 0:
                                pass
                            else:
                                P.surface.blit(temp,(0,0))
                                P.surface.blit(P.arrow,(10,-65+90*counter))
                                pos = counter
                        else:
                            P.surface.blit(temp,(0,0))
                            pos -= 1
                            P.surface.blit(P.arrow,(10,-65+90*pos))
                if event.key == pygame.key.key_code(P.controls[1]):
                    if pos != 6:
                        if pos == counter and counter < 5:
                            P.surface.blit(temp,(0,0))
                            P.surface.blit(P.arrow,(10,475))
                            pos = 6
                        else:
                            P.surface.blit(temp,(0,0))
                            pos += 1
                            P.surface.blit(P.arrow,(10,-65+90*pos))
                if event.key == pygame.key.key_code(P.controls[4]):
                    if pos == 6 and counter < 6:
                        fade_out(P)
                        new_save(P)
                        end = False
                    else:
                        file = save_files[pos-1]
                        f = open("save_files/"+file[:-1]+".txt","r")
                        data = f.readlines()
                        P.save_data = save.Save(data)
                        load_data(P)
                        end = False
                if event.key == pygame.key.key_code(P.controls[5]):
                    P.state = 1
                    end = False
                if event.key == pygame.key.key_code(P.controls[6]) and (pos != 6 or len(save_files) == 6):
                    new_txt(P)
                    write(P,"Delete "+save_files[pos-1][:-1]+"'s save file?")
                    if choice(P):
                        new_txt(P)
                        write(P,"Are you sure you want to","permanently delete this file?","(You can't undo this action.)")
                        if choice(P):
                            txt(P,"Deleted "+save_files[pos-1][:-1]+"'s save file.")
                            os.remove("save_files/"+save_files[pos-1][:-1]+".txt")
                            f1 = open("save_files/S@ves.txt","r")
                            dat = f1.readlines()
                            f1.close()
                            f = open("save_files/S@ves.txt","w")
                            for line in dat:
                                if line != save_files[pos-1]:
                                    f.write(line)
                            f.close()
                            del save_files[pos-1]
                            if len(save_files) < pos:
                                pos -= 1
                                if len(save_files) == 0:
                                    pos = 6
                    load_save(save_files,P,pos,fade = False)
                    end = False
        a += 1
        update_screen(P)
        P.clock.tick(P.ani_spd)
    if fade:
        fade_out(P,P.song)
                
def new_save(P) -> None:
    P.song = "music/intro.wav"
    pygame.mixer.music.load(P.song)
    set_mixer_volume(P,P.vol)
    pygame.mixer.music.play(-1)
    gen = 0
    back = load("p/start_back.png")
    girl = load("p/spr/girl_full.png")
    boy = load("p/spr/boy_full.png")
    girl_b = load("p/girl_banner.png")
    boy_b = load("p/boy_banner.png")
    prof = load("p/spr/prof_full.png")
    ret = pygame.transform.scale(load("p/return.png"),(25,25))
    enter = P.font.render("[ENTER]",True,(0,0,0))
    P.surface.fill((255,255,255))
    P.surface.blit(prof,(250,50))
    P.surface.blit(back,(0,0))
    fade_in(P)
    new_txt(P)
    write(P,"Hi, my name is Professor", "Burnet.")
    cont(P)
    new_txt(P)
    write(P,"I've been researching Pokemon", "at the island we're heading","to, Alto Mare.")
    cont(P)
    new_txt(P)
    write(P,"Well that's enough from me...", "Could you tell me about","yourself?")
    cont(P)
    P.surface.set_clip(Rect(0,0,800,450))
    a = 0
    P.surface.fill((255,255,255))
    while a <= 256:
        trans = pygame.Surface((800,600))
        trans.set_alpha(a)
        trans.fill((255,255,255))
        P.surface.fill((255,255,255))
        P.surface.blit(prof,(250,50))
        P.surface.blit(trans,(0,0))
        P.surface.blit(back,(0,0))
        a += 10
        update_screen(P)
        P.clock.tick(P.ani_spd)
    temp = P.surface.copy()
    P.surface.set_clip(Rect(0,0,800,450))
    move(P,temp,40,boy_b,-990,10,girl_b,800,-10,boy,-350,10,girl,900,-10)
    P.surface.set_clip(Rect(0,0,800,600))    
    new_txt(P)
    write(P,"Are you a boy or a girl?")
    P.surface.set_clip(Rect(0,0,800,450))
    a = -590
    b = 400
    c = 50
    d = 500
    e = 10
    end = True
    while end:
        for event in pygame.event.get(eventtype = KEYDOWN):
            if event.key == pygame.key.key_code(P.controls[2]) and e != 20:
                move(P,temp,abs(e),boy_b,a,10,girl_b,b,10,boy,c,10,girl,d,10)
                a+=10*abs(e)
                b+=10*abs(e)
                c+=10*abs(e)
                d+=10*abs(e)
                e = 20
            if event.key == pygame.key.key_code(P.controls[3]) and e != -20:
                move(P,temp,abs(e),boy_b,a,-10,girl_b,b,-10,boy,c,-10,girl,d,-10)
                a-=10*abs(e)
                b-=10*abs(e)
                c-=10*abs(e)
                d-=10*abs(e)
                e = -20
            if event.key == pygame.key.key_code(P.controls[4]) and (e == 20 or e == -20):
                temp2 = P.surface.copy()
                P.surface.set_clip(Rect(0,0,800,600))
                if a == -490:
                    new_txt(P)
                    write(P,"You're a boy, right?")
                    if choice(P,550,600):
                        P.surface.set_clip(Rect(0,0,800,450))
                        move(P,temp,39,boy_b,a,12,girl_b,b,12,boy,c,4,girl,d,12)
                        end_b = False
                        end = False
                    else:
                        P.surface.blit(temp2,(0,0))
                        new_txt(P)
                        write(P,"Are you a boy or a girl?")
                        end_b = False
                        P.surface.set_clip(Rect(0,0,800,450))
                elif a == -690:
                    new_txt(P)
                    write(P,"You're a girl, right?")
                    if choice(P,0,50):
                        P.surface.set_clip(Rect(0,0,800,450))
                        move(P,temp,40,boy_b,a,-12,girl_b,b,-12,boy,c,-12,girl,d,-3)
                        end_g = False
                        end = False
                        gen = 1
                    else:
                        P.surface.blit(temp2,(0,0))
                        new_txt(P)
                        write(P,"Are you a boy or a girl?")
                        end_g = False
                        P.surface.set_clip(Rect(0,0,800,450))
                else:
                    pass
    P.surface.set_clip(Rect(0,0,800,600))
    new_txt(P)
    write(P,"What is your name?")
    name = ""
    temp = P.surface.copy()
    a = 0
    end = True
    while end:
        for event in pygame.event.get(eventtype = KEYDOWN):
            if event.type == pygame.KEYDOWN:
                if len(name) < 10:
                    if (pygame.K_a <= event.key <= pygame.key.key_code(P.controls[4])) or (pygame.K_0 <= event.key <= pygame.K_9):
                        name += event.unicode
                    if event.key == K_SPACE:
                        name += " "
                if event.key == K_BACKSPACE:
                    name = name[:-1]
                if event.key == K_RETURN:
                    onlyspc = True
                    for let in name:
                        if let != ' ':
                            onlyspc = False
                    if onlyspc:
                        txt(P,"You can't use that name!")
                        new_txt(P)
                        write(P,"What is your name?")
                        P.surface.set_clip((0,0,800,600))
                        temp = P.surface.copy()
                    else:
                        save_w = open("save_files/S@ves.txt","r")
                        names = save_w.readlines()
                        files = []
                        for file in names:
                            files.append(file[:-1])
                        if name in files:
                            txt(P,"I'm sorry, that name is","already taken.")
                        else:
                            end = False
                        save_w.close()
        P.surface.blit(temp,(0,0))
        if len(name) == 10 or int(a/20)%2 == 1:
            txt0 = P.font.render(name,True,(0,0,0))
        else:
            txt0 = P.font.render(name+"_",True,(0,0,0))
        a += 1
        if len(name) == 10:
            P.surface.blit(ret,(270,513))
        P.surface.blit(enter,(625,500))
        P.surface.blit(txt0,(20,500))
        P.clock.tick(P.ani_spd)
        update_screen(P)
    new_w = open("save_files/"+name+".txt","w+")
    new_w.write("['"+name+"','None']\n")
    new_w.write(str(gen)+"\n")
    new_w.write("375\n")
    new_w.write("-75\n")
    new_w.write("r\n")
    new_w.write("['cruise_1','pc_am']\n")
    #update trainer
    new_w.write("[0,0,0,0,0,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0,[[-1,0,[None,None,None]],[-1,0,[None,None,None]],[-1,0,[None,None,None]],[-1,0,[None,None,None]],[-1,0,[None,None,None]],[-1,0,[None,None,None]],[-1,0,[None,None,None]],[-1,0,[None,None,None]]],0,[[0,0,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1],[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0],[0,1,0,0],[1,0,0,0],[0,0,1,0],[1,0,0,0],[0,0,0,0],[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],[0,[None,[],{}],None,None,[0,0],None,None],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],None,None,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],0]\n") #40 trainers 80 items 40 interacts
    new_w.write("[]\n")
    new_w.write("1500\n")
    new_w.write("[[],[],[],[],[]]\n")
    new_w.write("[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]\n")
    new_w.write("[00,00,00]\n")
    new_w.write("[None,None,None,None]\n")
    new_w.write("{}\n")
    new_w.close()
    save_w = open("save_files/S@ves.txt","a")
    save_w.write(name+"\n")
    save_w.close()
    read_w = open("save_files/"+name+".txt","r")
    data = read_w.readlines()
    P.save_data = save.Save(data)
    load_data(P)
    fade_out(P,P.song)

def get_rival_poke(P,pok = 0):
    num = 0
    if P.save_data.gen == 0:
        num = 1
    if P.prog[0] == 17:
        if pok == 1:
            if P.save_data.starter == 'Poliwag':
                return poke.Poke('Bounsweet',[8,num,334,"Splash",-1,"Pound",-1,"Play Nice",-1,"Razor Leaf",-1,None,None,0,"Poke Ball",0,'Leaf Guard'])
            if P.save_data.starter == 'Bounsweet':
                return poke.Poke('Fletchling',[8,num,334,"Tackle",-1,"Growl",-1,"Quick Attack",-1,None,None,None,None,0,"Poke Ball",0,'Big Pecks'])
            if P.save_data.starter == 'Fletchling':
                return poke.Poke('Poliwag',[8,num,334,"Water Sport",-1,"Bubble",-1,"Hypnosis",-1,None,None,None,None,0,"Poke Ball",0,'Water Absorb'])
            else:
                return poke.Poke('Poliwag',[8,num,334,"Water Sport",-1,"Bubble",-1,"Hypnosis",-1,None,None,None,None,0,"Poke Ball",0,'Water Absorb'])
        if pok == 0:
            if P.save_data.gen == 0:
                return poke.Poke('Skitty',[6,num,334,"Fake Out",-1,"Sing",-1,"Tail Whip",-1,"Tackle",-1,None,None,0,"Poke Ball",0,'Cute Charm'])
            else:
                return poke.Poke('Poochyena',[6,num,334,"Tackle",-1,"Howl",-1,"Sand Attack",-1,None,None,None,None,0,"Poke Ball",0,'Quick Feet'])
    if P.prog[0] == 100:
        if pok == 2:
            if P.save_data.gen == 0:
                return poke.Poke('Accelgor',[32,num,334,"Struggle Bug",-1,"Double Team",-1,"Mega Drain",-1,"Water Shruiken",-1,None,None,0,"Poke Ball",250,'Sticky Hold'])
            else:
                return poke.Poke('Escavalier',[32,num,334,"Slash",-1,"Fell Stinger",-1,"Twineedle",-1,"Quick Guard",-1,None,None,0,"Poke Ball",250,'Shell Armor'])
        if pok == 1:
            if P.save_data.starter == 'Poliwag':
                return poke.Poke('Steenee',[33,num,334,"Stomp",-1,"Teeter Dance",-1,"Magical Leaf",-1,"Rapid Spin",-1,None,None,0,"Poke Ball",350,'Leaf Guard'])
            if P.save_data.starter == 'Bounsweet':
                return poke.Poke('Fletchinder',[33,num,334,"Flame Charge",-1,"Aerial Ace",-1,"Razor Wind",-1,"Flail",-1,None,None,0,"Poke Ball",350,'Big Pecks'])
            if P.save_data.starter == 'Fletchling':
                return poke.Poke('Poliwhirl',[33,num,334,"Mud Bomb",-1,"Bubble Beam",-1,"Body Slam",-1,"Hypnosis",-1,None,None,0,"Poke Ball",350,'Water Absorb'])
            else:
                return poke.Poke('Poliwhirl',[33,num,334,"Mud Bomb",-1,"Bubble Beam",-1,"Body Slam",-1,"Hypnosis",-1,None,None,0,"Poke Ball",350,'Water Absorb'])
        if pok == 0:
            if P.save_data.gen == 0:
                return poke.Poke('Delcatty',[31,num,334,"Wake-Up Slap",-1,"Charm",-1,"Fake Out",-1,"Disarming Voice",-1,None,None,0,"Poke Ball",350,'Cute Charm'])
            else:
                return poke.Poke('Mightyena',[31,num,334,"Assurance",-1,"Swagger",-1,"Fire Fang",-1,"Scary Face",-1,None,None,0,"Poke Ball",350,'Quick Feet'])

def map_keys():
    class evt:
        def __init__(self):
            self.type = None
            self.key = 0
    events = pygame.event.get(eventtype = KEYDOWN)
    e = evt()
    l = []
    for event in events:
        l.append(event)
    if len(l) == 0:
        return [e]
    return l

def tick_buffer(P):
    if P.buffer_talk:
        P.buffer_talk -= 1
        if P.buffer_talk == 0:
            P.buffer_talk = None

def trainer_check(P,trainer,music,font = None):
    if trainer != None and trainer.in_front:
        if trainer.tid == 28:
            font = pygame.font.SysFont("courier", 70, italic = True)
        te = P.surface.copy()
        if font != None:
            P.font = font
        if trainer.tid == 16:
            first = P.party[0]
            for x in range(len(P.party)):
                if P.party[x].status == 'Faint':
                    first = P.party[x+1]
                else:
                    break
            txt(P,"Ha! With my skills, I can","predict exactly which Pokemon", "you will choose!")
            txt(P,"A measly "+first.actual_name+" will","never stand a chance against","my prized collection!")
        else:
            trainer.write()
        if font != None:
            P.font = pygame.font.SysFont("courier", 40, bold = True)
        play_music(P,"music/trainer_battle.wav",0)
        temp_habitat = P.habitat
        if trainer.tid in [0,1,8,9,10,24]:
            P.habitat = 'road'
        elif trainer.tid in [1111]:
            P.habitat = 'indoor'
        elif trainer.tid in [3,5]:
            P.habitat = 'path'
        elif trainer.tid in [22,23,33]:
            P.habitat = 'dock'
        elif trainer.tid in [32,34]:
            P.habitat = 'mount'
        elif trainer.tid in [37,38]:
            P.habitat = 'beach'
        if trainer.tid in [3,34]:
            battle(P,trainer.team,no_pc = True)
        else:
            battle(P,trainer.team)
        P.habitat = temp_habitat
        play_music(P,music)
        P.surface.blit(te,(0,0))
        fade_in(P)
        lose = True
        for x in P.party:
            if x.ch != 0:
                lose = False
        if trainer.tid == 3:
            if lose:
                t = P.surface.copy()
                txt(P,'Ha! I suppose I got a little','too excited battling with my','Pokemon again!')
                txt(P,"You may have lost, but I can","tell you've still got a lot of","growing to do!")
                txt(P,"Here, I'll heal your Pokemon","for you as an apology.")
                fade_out(P)
                P.clock.tick(1)
                P.surface.blit(t,(0,0))
                fade_in(P)
                heal_party(P)
                txt(P,"When you do get stronger, I'd","love to have another battle","with you.")
                txt(P,'Good luck out there!')
            else:
                P.prog[5][trainer.tid] = 1
                trainer.lose_write()
                txt(P,"Here, take this Eviolite. I'm","sure it will be quite useful","for your journey.")
                add_item(P,"Eviolite",1)
        elif trainer.tid == 34:
            if lose:
                t = P.surface.copy()
                txt(P,"It was a good try, but you've","still got many years until","you catch up with me!")
                txt(P,"Allow me to heal your Pokemon","for you.","")
                fade_out(P)
                P.clock.tick(1)
                P.surface.blit(t,(0,0))
                fade_in(P)
                heal_party(P)
                txt(P,"Come back once you've gotten","a little stronger, and I'll","fight you again!")
            else:
                P.prog[5][trainer.tid] = 1
                trainer.lose_write()
                txt(P,"Take this Metal Coat! When","held, it will give a small","boost to Steel-type attacks.")
                txt(P,"There are a couple species of","Pokemon that can even use it","to evolve!")
                add_item(P,"Metal Coat",1)
        else:
            P.prog[5][trainer.tid] = 1
            trainer.lose_write()
        return True
    return False

def choose_num(P,max_num,money = False,day = False) -> int:
    if max_num > 99 and money == False:
        max_num = 99
    box = load("p/choose_num_box.png")
    if money:
        max_num = int(max_num/10)
        box = load("p/1_box.png")
    num = 1
    end = True
    tim = 0
    move = 0
    move_d = 35
    back = P.surface.copy()
    # if money:
    #     pass
    # else:
    #     P.surface.set_clip((670,380,100,70))
    pygame.event.clear()
    while end:
        if money:
            P.surface.blit(box,(550,380))
        else:
            P.surface.blit(box,(670,380))
        if money == False:
            x = "x"
            if day:
                x = ""
            if num <= 9:
                txt = P.font.render(x+"0"+str(num),True,(0,0,0))
            else:
                txt = P.font.render(x+str(num),True,(0,0,0))
        else:
            txt = P.font.render("$"+str(num*10),True,(0,0,0))
        if money:
            P.surface.blit(txt,(565,395))
        elif day:
            P.surface.blit(txt,(685,395))
        else:
            P.surface.blit(txt,(685,395))
        for event in pygame.event.get(eventtype = KEYDOWN):
            if event.key == pygame.key.key_code(P.controls[5]) and tim > 10:
                P.surface.set_clip((0,0,800,600))
                P.surface.blit(back, (0, 0))
                return 0
            if event.key == pygame.key.key_code(P.controls[4]) and tim > 10:
                P.surface.set_clip((0,0,800,600))
                P.surface.blit(back, (0, 0))
                return num
        keys = pygame.key.get_pressed()
        if keys[pygame.key.key_code(P.controls[1])]and move == 0:
            if num > 1:
                num -= 1
            else:
                num = max_num
            move = int(move_d/5)
        if keys[pygame.key.key_code(P.controls[0])] and move == 0:
            if num < max_num:
                num += 1
            else:
                num = 1
            move = int(move_d/5)
        if move > 0:
            move -= 1
            if move == 0:
                if (keys[pygame.key.key_code(P.controls[0])] or keys[pygame.key.key_code(P.controls[1])]) and move_d > 15:
                    move_d -= 1
        if not (keys[pygame.key.key_code(P.controls[0])] or keys[pygame.key.key_code(P.controls[1])]):
            move_d = 35
        update_screen(P)
        P.clock.tick(P.ani_spd)
        tim += 1

def multi_choice(P,num,temp,txt1,txt2 = None,txt3 = None,txt4 = None):
    tbox = load("p/"+str(num)+"_box.png")
    P.surface.blit(tbox,(550,230))
    one = P.font.render(txt1,True,(0,0,0))
    if num > 1:
        two = P.font.render(txt2,True,(0,0,0))
    if num > 2:
        three = P.font.render(txt3,True,(0,0,0))
    if num > 3:
        four = P.font.render(txt4,True,(0,0,0))
    P.clock.tick(5)
    y_dif = 50*num
    ay = 440-y_dif
    P.surface.blit(one,(600,ay))
    if num > 1:
        P.surface.blit(two,(600,ay+50))
    if num > 2:
        P.surface.blit(three,(600,ay+100))
    if num > 3:
        P.surface.blit(four,(600,ay+150))
    temp3 = P.surface.copy()
    P.surface.blit(P.arrow,(550,ay))
    update_screen(P)
    ans = 0
    tim = 0
    end = True
    pygame.event.clear()
    while end:
        for event in pygame.event.get(eventtype = KEYDOWN):
            if event.key == pygame.key.key_code(P.controls[4]) and tim > 10:
                P.surface.set_clip(Rect(0,0,800,450))
                P.surface.blit(temp,(0,0))
                P.surface.set_clip(Rect(0,0,800,600))
                return ans
            elif event.key == pygame.key.key_code(P.controls[5]) and tim > 10:
                P.surface.set_clip(Rect(0,0,800,450))
                P.surface.blit(temp,(0,0))
                P.surface.set_clip(Rect(0,0,800,600))
                return -1
            elif event.key == pygame.key.key_code(P.controls[0]) and ans != 0:
                ans -= 1
                ay -= 50
                P.surface.blit(temp3,(0,0))
                P.surface.blit(P.arrow,(550,ay))
            elif event.key == pygame.key.key_code(P.controls[1]) and ans != num-1:
                ans += 1
                ay += 50
                P.surface.blit(temp3,(0,0))
                P.surface.blit(P.arrow,(550,ay))
        tim += 1
        P.clock.tick(P.ani_spd)
        update_screen(P)

def choice(P,ax = 550,rx = 600, pos = True, reverse = False,ymod = 0) -> bool:
    t = P.surface.copy()
    P.surface.blit(P.choicebox,(ax,330+ymod))
    yes = P.font.render("Yes",True,(0,0,0))
    no = P.font.render("No",True,(0,0,0))
    P.clock.tick(5)
    if reverse:
        P.surface.blit(yes,(rx,390+ymod))
        P.surface.blit(no,(rx,340+ymod))
    else:
        P.surface.blit(no,(rx,390+ymod))
        P.surface.blit(yes,(rx,340+ymod))
    temp3 = P.surface.copy()
    if pos == True:
        P.surface.blit(P.arrow,(ax,340+ymod))
    else:
        P.surface.blit(P.arrow,(ax,390+ymod))
    update_screen(P)
    ans = pos
    a = 0
    pygame.event.clear()
    while True:
        for event in pygame.event.get(eventtype = KEYDOWN):
            if event.key == pygame.key.key_code(P.controls[4]) and a > 15:
                P.surface.blit(t,(0,0))
                return ans
            elif event.key == pygame.key.key_code(P.controls[5]) and a > 15:
                P.surface.blit(t,(0,0))
                return False
            elif event.key == pygame.key.key_code(P.controls[0]):
                ans = True
                P.surface.blit(temp3,(0,0))
                P.surface.blit(P.arrow,(ax,340+ymod))
            elif event.key == pygame.key.key_code(P.controls[1]):
                ans = False
                P.surface.blit(temp3,(0,0))
                P.surface.blit(P.arrow,(ax,390+ymod))
        update_screen(P)
        P.clock.tick(P.ani_spd)
        a += 1

def load_data(P) -> None:
    load_trainer(P)
    P.px = P.save_data.x
    P.py = P.save_data.y
    P.x = 0
    P.y = 0
    P.xr = 0
    P.xl = 0
    P.yu = 0
    P.yd = 0
    P.npcx = 0
    P.npcy = 0
    P.nxr = 0
    P.nxl = 0
    P.nyu = 0
    P.nyd = 0
    P.party = []
    for x,y in P.save_data.party:
        P.party.append(poke.Poke(x,y))
    P.prog = P.save_data.prog
    P.loc = P.save_data.loc
    P.bag = P.save_data.bag

def new_txt(P) -> None:
    P.surface.set_clip((0,0,800,600))
    P.surface.blit(P.textbox,(0,450))

def new_battle_txt(P) -> None:
    back = load("p/battle_box.png")
    P.surface.set_clip((0,0,800,600))
    P.surface.blit(back,(0,460))
    P.surface.blit(P.battlebox,(0,460))
    
def move(P, back, num, one, one_n, o, two = None, two_n = None, tw = None, three = None, three_n = None, th = None, four = None, four_n = None, fo = None) -> None:
    x = 0    
    while x < num:
        P.surface.blit(back,(0,0))
        P.surface.blit(one,(one_n, 100))
        if two != None:
            P.surface.blit(two, (two_n, 100))
        if three != None:
            P.surface.blit(three, (three_n, 40))
        if four != None:
            P.surface.blit(four, (four_n, 20))
        update_screen(P)
        one_n+=o
        if(two!=None):
            two_n+=tw
        if(three!=None):
            three_n+=th
        if(four!=None):
            four_n+=fo
        P.clock.tick(P.ani_spd)
        x+=1

def battle_team(P, cpoke,team_type,pokee = 0):
    box = load("p/team_box_1.png")
    back = load("p/load_back.png")
    tbox = load("p/3_box.png")
    hp_b = load("p/team_hp.png")
    item_ico = pygame.transform.scale(load("p/item_icon.png"),(20,25))
    mega = pygame.transform.scale(load("p/mega_symbol.png"),(30,30))
    nurse = pygame.transform.scale(load("p/nurse_icon.png"),(30,30))
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
                box = load("p/team_box_2.png")
                if p.code[-2:] == '_S':
                    box = load("p/team_box_2_S.png")
            else:
                box = load("p/team_box_1.png")
                if p.code[-2:] == '_S':
                    box = load("p/team_box_1_S.png")
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
                status = load("p/"+p.status+"_ico.png")
                status = pygame.transform.scale(status,(50,20))
                P.surface.blit(status,(x+145,y+95))
            if p.item != None:
                P.surface.blit(item_ico,(x+70,y+70))
            pos += 1
        for event in pygame.event.get(eventtype = KEYDOWN):
            if a > 10:
                if event.key == pygame.key.key_code(P.controls[5]):
                    if P.legendary_battle and team_type != 0:
                        new_txt(P)
                        write(P,"Your escape route has been", "cut off!")
                        P.surface.set_clip((0,0,800,460))
                        cont(P)
                        a = 1
                    elif team_type == 1:
                        new_txt(P)
                        write(P,"There's no running from a", "Trainer battle!")
                        P.surface.set_clip((0,0,800,460))
                        cont(P)
                        a = 1
                    elif team_type == 2:
                        continue
                    else:
                        end = False
                elif event.key == pygame.key.key_code(P.controls[0]) and current > 1:
                    current -= 2
                elif event.key == pygame.key.key_code(P.controls[1]) and current < 4 and current+2 < len(P.party):
                    current += 2
                elif event.key == pygame.key.key_code(P.controls[3]) and current % 2 == 0 and current+1 < len(P.party):
                    current += 1
                elif event.key == pygame.key.key_code(P.controls[2]) and current % 2 != 0:
                    current -= 1                     
                elif event.key == pygame.key.key_code(P.controls[4]):
                    P.surface.set_clip(Rect(0,0,800,600))
                    new_txt(P)
                    write(P,"Do what with "+P.party[current].name+"?")
                    P.surface.blit(tbox,(550,280))
                    switch = P.font.render("Switch",True,(0,0,0))
                    summary = P.font.render("Summary",True,(0,0,0))
                    cancel = P.font.render("Cancel",True,(0,0,0))
                    P.clock.tick(5)
                    ay = 290
                    P.surface.blit(switch,(600,290))
                    P.surface.blit(summary,(600,340))
                    P.surface.blit(cancel,(600,390))
                    temp3 = P.surface.copy()
                    P.surface.blit(P.arrow,(550,ay))
                    update_screen(P)
                    ans = 0
                    tim = 0
                    end1 = True
                    while end1:
                        for event in pygame.event.get(eventtype = KEYDOWN):
                            if event.key == pygame.key.key_code(P.controls[4]) and tim > 10:
                                if ans == 0:
                                    if P.party[current].status == 'Faint':
                                        end1 = False
                                        P.surface.set_clip((0,0,800,600))
                                        new_txt(P)
                                        write(P,P.party[current].name+" has no energy left", "to battle!")
                                        cont(P)
                                        P.surface.set_clip((0,0,800,450))
                                    elif type(pokee) == poke.Poke and ((pokee.ability == 'Shadow Tag' and 'Ghost' not in cpoke.type and cpoke.ability != 'Shadow Tag') or (pokee.ability == 'Arena Trap' and cpoke.ability != 'Levitate' and cpoke.magnet_rise == 0 and 'Flying' not in cpoke.type) or (pokee.ability == 'Magnet Pull' and 'Steel' in cpoke.type) or (cpoke.trapped[1] != 0)) and 'Ghost' not in cpoke.type:
                                        txt(P,cpoke.name + " is trapped!")
                                    elif P.party[current].same(cpoke):
                                        end1 = False
                                        P.surface.set_clip((0,0,800,600))
                                        new_txt(P)
                                        write(P,cpoke.name+" is already in", "battle!")
                                        cont(P)
                                        P.surface.set_clip((0,0,800,450))
                                    else:
                                        cpoke = P.party[current]
                                        end1 = False
                                        end = False
                                if ans == 1:
                                    P.surface.set_clip(Rect(0,0,800,600))
                                    temp4 = P.surface.copy()
                                    fade_out(P)
                                    summ(P,P.party[current])
                                    P.surface.blit(temp4,(0,0))
                                    fade_in(P)
                                    P.surface.set_clip(Rect(0,0,800,450))
                                    end1 = False
                                    a = 1
                                else:
                                    end1 = False
                                    a = 1
                            elif event.key == pygame.key.key_code(P.controls[5]) and tim > 10:
                                end1 = False
                                a = 1
                            elif event.key == pygame.key.key_code(P.controls[0]) and ans != 0:
                                ans -= 1
                                ay -= 50
                                P.surface.blit(temp3,(0,0))
                                P.surface.blit(P.arrow,(550,ay))
                            elif event.key == pygame.key.key_code(P.controls[1]) and ans != 2:
                                ans += 1;
                                ay += 50
                                P.surface.blit(temp3,(0,0))
                                P.surface.blit(P.arrow,(550,ay))
                        update_screen(P)
                        P.clock.tick(P.ani_spd)
                        tim += 1
                    P.surface.set_clip(Rect(0,0,800,450))
        if a == 0:
            fade_in(P)
        if a == 2:
            P.surface.set_clip(Rect(0,0,800,600))
            new_txt(P)
            write(P,"Choose a Pokemon.")
            P.surface.set_clip(Rect(0,0,800,450))
        a += 1
        P.clock.tick(P.ani_spd)
        update_screen(P)
    P.surface.set_clip(Rect(0,0,800,600))
    fade_out(P)
    return cpoke

def txt(P,one, two = "", three = ""):
    new_txt(P)
    write(P,one,two,three)
    cont(P)

def calc_lost_money(P):
    base = 8
    if P.prog[0] >= 48:
        base = 16
    sum = 0
    for x in P.party:
        sum += x.lvl
    sum /= len(P.party)
    return int(sum*base)

def print_blackout(P):
    P.p = P.u1
    P.load_npcs()
    #rival fight
    if P.prog[0] == 17:
        P.prog[0] = 16
    #pp rocket fight
    if P.prog[0] == 33:
        P.prog[0] = 26
    #steven fight
    if P.prog[0] == 42:
        P.prog[0] = 41
    #colress fight
    if P.prog[0] == 46:
        P.prog[0] = 44
    #scarab rocket fight
    if P.prog[0] == 60:
        P.prog[0] = 54
    #thundurus
    if P.prog[0] == 75:
        P.prog[0] = 70
        P.legendary_battle = False
    #cheryl fight
    if P.prog[0] == 84:
        P.prog[0] = 82
    #route 4 rocket fight
    if P.prog[0] in [92,93]:
        P.prog[0] = 89
    #route 5 rival
    if P.prog[0] == 100:
        P.prog[0] = 99
    spd = P.txt_spd
    spd = write_h(P,spd,P.save_data.name+" scurried to a", 200,(255,255,255),2)
    spd = write_h(P,spd,"Pokemon Center, protecting the", 250,(255,255,255),2)
    spd = write_h(P,spd, "exhausted Pokemon from any", 300,(255,255,255),2)
    spd = write_h(P,spd, "further harm...", 350,(255,255,255),2)
    cont(P)
    fade_out(P)

def write(P, one: str, two: str = "", three: str = "") -> None:
    set_channel_volume(P,P.sfx_vol,2)
    pygame.mixer.Channel(2).play(P.txt_sound)
    spd = P.txt_spd
    spd = write_h(P,spd, one, 460)
    spd = write_h(P,spd, two, 500)
    spd = write_h(P,spd, three, 540)
    P.clock.tick(5)

def battle_write(P, one, two = "") -> None:
    spd = P.txt_spd*5
    spd = write_h(P,spd, one, 480)
    spd = write_h(P,spd, two, 530)
    P.surface.set_clip((0,0,800,460))

def write_h(P, spd, string, height, color = (0,0,0), spd_mult = 5) -> int:
    count = 0
    for x in string:
        for event in pygame.event.get(eventtype = KEYDOWN):
            if event.key == pygame.key.key_code(P.controls[4]):
                spd = P.txt_spd*spd_mult
        txt = P.font.render(x,True,color)
        P.surface.blit(txt,(20+count,height))
        count += 25
        P.clock.tick(spd)
        update_screen(P)
    return spd

def cont(P) -> None:
    end = True
    pygame.event.clear()
    while end:
        for event in pygame.event.get(eventtype = KEYDOWN):
            if event.key == pygame.key.key_code(P.controls[4]):
                end = False
        update_screen(P)
        P.clock.tick(P.ani_spd)

