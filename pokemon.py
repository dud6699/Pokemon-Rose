import sys
import poke
import pygame
import npc
import random
import save
import os
import ast
import poke_func
import map_func
import threading
import items
from pygame.locals import *

class Pokemon:
    def __init__(self):
        pygame.display.set_mode((800,600))
        #self.poke_tester()
        self.running = True
        self.state = 1
        #1
        f = open("save_files/Sett!ngs.txt","r")
        data = f.readlines()
        self.txt_spd = ast.literal_eval(data[0][:-1])
        self.ani_on = ast.literal_eval(data[1][:-1])
        self.walk_spd = ast.literal_eval(data[2][:-1])
        self.graphic = ast.literal_eval(data[3][:-1])
        self.lighting = data[4][:-1]
        self.vol = ast.literal_eval(data[5][:-1])
        self.sfx_vol = ast.literal_eval(data[6][:-1])
        self.controls = ast.literal_eval(data[7][:-1])
        self.load_images()
        self.song = "music/title.wav"
        self.ocean = -10
        self.clock = pygame.time.Clock()
        self.font_l = pygame.font.SysFont("courier", 50, bold = True)
        self.font = pygame.font.SysFont("courier", 40, bold = True)
        self.font_s = pygame.font.SysFont("courier", 30, bold = True)
        self.font_vs = pygame.font.SysFont("courier", 20, bold = True)
        self.leveled_up = []
        self.ani_spd = 60
        #60
        self.bat_spd = 1.25
        #1.5
        self.moving = False
        self.ledge = 0
        self.foam = 0
        self.echoed = [0,0]
        self.buffer_talk = None
        self.new_location = True
        self.loc_in_txt = None
        self.loc_txt = None
        self.ion_deluge = False
        self.grass_prob = 0.01
        self.gem_active = False
        self.use_key_item = None
        self.register_click = 0
        self.move_out_dir = None
        self.turncount = 0
        self.double_money = False
        self.haze_active = 0
        self.loc = ""
        self.habitat = None
        self.legendary_battle = False
        self.tourney_battle = False
        self.prog = [0]
        self.metronome = None
        self.txt_sound = pygame.mixer.Sound('music/sfx/text_sfx.wav')

    def poke_tester(self):
        no_shiny = []
        shiny = []
        problem = []
        for file in os.listdir("poke"):
            if file.endswith(".txt") and file.startswith("OUTLINE") == False:
                try:
                    bf = pygame.image.load("p/poke/"+file[:-4]+"_S_bf.png")
                    problem.append(file[:-4])
                    bfw = pygame.image.load("p/poke/" + file[:-4] + "_S_bfw.png")
                    bb = pygame.image.load("p/poke/" + file[:-4] + "_S_bb.png")
                    bbw = pygame.image.load("p/poke/" + file[:-4] + "_S_bbw.png")
                    ico = pygame.image.load("p/poke/" + file[:-4] + "_S_ico.png")
                    full = pygame.image.load("p/poke/" + file[:-4] + "_S_full.png")
                    shiny.append(file[:-4])
                except:
                    no_shiny.append(file[:-4])
        for x in shiny:
            problem.remove(x)
        print(shiny)
        print(problem)
        print(no_shiny)

    def switch_locations(self):
        while self.running:
            if self.state == 1:
                poke_func.title_screen(self)
                self.state = 2
            if self.state == 2:
                save_r = open("save_files/S@ves.txt","r")
                save_files = save_r.readlines()
                save_r.close()
                self.state = 3
                if save_files == []:
                    poke_func.new_save(self)
                else:
                    poke_func.load_save(save_files, self)
                if self.state == 3:
                    self.load_npcs()
            if self.state == 3:
                self.xl = 0
                self.xr = 0
                self.yu = 0
                self.yd = 0
                self.x = 0
                self.y = 0
                poke_func.update_locs(self)
                if self.loc == "route_1":
                    map_func.route_1(self)
                elif self.loc == 'beedrill':
                    map_func.bee_zone(self)
                elif self.loc == "route_2":
                    map_func.route_2(self)
                elif self.loc == "echo_cave":
                    map_func.echo_cave(self)
                elif self.loc == "vigore":
                    map_func.vigore_dam(self)
                elif self.loc == "cruise_1":
                    map_func.cruise_1(self)
                elif self.loc == "cruise_2":
                    map_func.cruise_2(self)
                elif self.loc == "dock_1":
                    map_func.dock_1(self)
                elif self.loc == "am_square":
                    map_func.am_square(self)
                elif self.loc == "square_1":
                    map_func.square_1(self)
                elif self.loc == "north_am":
                    map_func.north_am(self)
                elif self.loc == "egida":
                    map_func.egida(self)
                elif self.loc == "egida_under":
                    map_func.egida_under(self)
                elif self.loc == 'egida_mine':
                    map_func.egida_mine(self)
                elif self.loc == 'egida_lab':
                    map_func.egida_lab(self)
                elif self.loc == "egi_gym":
                    map_func.egida_gym_main(self)
                elif self.loc == "egi_gym_l":
                    map_func.egida_gym_l(self)
                elif self.loc == "egi_gym_r":
                    map_func.egida_gym_r(self)
                elif self.loc == "egi_gym_b":
                    map_func.egida_gym_b(self)
                elif self.loc == "power_plant_1":
                    map_func.power_plant_1(self)
                elif self.loc == "power_plant_b":
                    map_func.power_plant_b(self)
                elif self.loc == "power_plant_2":
                    map_func.power_plant_2(self)
                elif self.loc == 'route_3':
                    map_func.route_3(self)
                elif self.loc == 'scarab_l':
                    map_func.scarab_l(self)
                elif self.loc == 'scarab_r':
                    map_func.scarab_r(self)
                elif self.loc == 'fiore':
                    map_func.fiore(self)
                elif self.loc == 'fiore_garden':
                    map_func.fiore_garden(self)
                elif self.loc == 'pianura':
                    map_func.pianura(self)
                elif self.loc == 'pianura_nursery':
                    map_func.pianura_nursery(self)
                elif self.loc == 'pianura_bakery':
                    map_func.pianura_bakery(self)
                elif self.loc == 'mirror_cave':
                    map_func.mirror_cave(self)
                elif self.loc == 'pia_gym':
                    map_func.pia_gym_main(self)
                elif self.loc == 'pia_gymb':
                    map_func.pia_gymb(self)
                elif self.loc == 'route_4':
                    map_func.route_4(self)
                elif self.loc == 'isola':
                    map_func.isola(self)
                elif self.loc == 'route_5':
                    map_func.route_5(self)
                elif self.loc == 'verde':
                    map_func.verde(self)
                elif self.loc[:3] == "pc_":
                    self.save_data.pc = self.loc
                    map_func.poke_center(self,self.loc[3:])
                elif self.loc[:7] == "house_1":
                    map_func.house_1(self,int(self.loc[8:]))
                elif self.loc[:8] == "house_21":
                    map_func.house_2_1(self,int(self.loc[9:]))
                elif self.loc[:8] == "house_22":
                    map_func.house_2_2(self,int(self.loc[9:]))
                elif self.loc[:7] == "house_3":
                    map_func.house_3(self,int(self.loc[8:]))
                elif self.loc[:7] == "pia_gym":
                    map_func.pia_gym(self,int(self.loc[8:]))
            poke_func.update_screen(self)
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def run(self) -> None:
        pygame.display.set_caption("Pokemon Rose")
        pygame.display.set_mode((800,600))
        #self.surface = pygame.Surface((800,600))
        #self.screen = pygame.display.get_surface()
        self.surface = pygame.display.get_surface()
        t1 = threading.Thread(target = self.close_window)
        #t2 = threading.Thread(target = self.close_window)
        t1.start()
        #t2.start()
        self.switch_locations()
        t1.join()
        #t2.join()
        #self.switch_locations()

    def close_window(self):
        end = True
        while end:
            if self.running == False:
                end = False
            # if pygame.event.peek(eventtype = pygame.QUIT,pump = True):
            #     self.running = False
            for event in pygame.event.get(eventtype = pygame.QUIT):
                self.running = False
            self.clock.tick(self.ani_spd)

    def load_npcs(self):
        #npcs:
        #trainers
        if self.prog[5][0] == 0:
            self.r1_timmy = npc.NPC(self,'Youngster','Timmy',[1200,-450],[['d',100]],["Stop right there!","","","You're gonna have to get past","me if you wanna mess around in", "my field!"],["Ack! Not again...","",""],True,[0,200,0,0],[poke.Poke('Bellsprout',[7,random.randint(0,1),334,"Growth",1,"Vine Whip",0,None,None,None,None,None,None,0,"Poke Ball",0,"Chlorophyll"])],0,loc = "route_1")
        else:
            self.r1_timmy = npc.NPC(self,'Youngster','Timmy',[1200,-450],[['d',100]],["Just you wait!","I'm gonna get you back for","beating me!"],loc = "route_1")
        if self.prog[5][1] == 0:
            self.r1_amy = npc.NPC(self,'Lass','Amy',[1600,-850],[['d',100],['r',100]],["Hey wanna see what I learned","today?",""],["Oh, I guess it wasn't very","useful.",""],True,[0,250,0,300],[poke.Poke('Oddish',[5,random.randint(0,1),334,"Absorb",-1,"Growth",-1,"Sweet Scent",-1,None,None,None,None,0,"Poke Ball"]),poke.Poke('Skitty',[6,random.randint(0,1),334,"Fake Out",-1,"Tackle",-1,"Tail Whip",-1,"Growl",-1,None,None,0,"Poke Ball",0,"Cute Charm"])],1,loc = "route_1")
        else:
            self.r1_amy = npc.NPC(self,'Lass','Amy',[1600,-850],[['d',100]],["My teacher could learn a thing ","or two from you.",""],loc = "route_1")
        if self.prog[5][2] == 0:
            self.r1_robb = npc.NPC(self,'Bug Catcher','Robb',[1500,-1200],[['d',60],['r',80],['l',90],['u',40]],["You there!","Check out this cool Pokemon I","just found!"],["Your Pokemon are pretty cool","too I guess...",""],True,[50,200,100,200],[poke.Poke('Weedle',[5,random.randint(0,1),334,"String Shot",-1,"Poison Sting",-1,None,None,None,None,None,None,0,"Poke Ball"]),poke.Poke('Caterpie',[5,random.randint(0,1),334,"Tackle",-1,"String Shot",-1,None,None,None,None,None,None,0,"Poke Ball"]),poke.Poke('Scyther',[6,random.randint(0,1),334,"Quick Attack",-1,"Leer",-1,"Focus Energy",-1,"Vacuum Wave",-1,None,None,0,"Poke Ball",0,"Swarm"])],2,loc = "route_1")
        else:
            self.r1_robb = npc.NPC(self,'Bug Catcher','Robb',[1500,-1200],[['u',100]],["I bet there's an even cooler","Pokemon hiding in this grass!",""],loc = "route_1")
        if self.prog[5][3] == 0:
            self.r1_noland = npc.NPC(self,'Gentleman','Noland',[2850,-500],[['r',100]],["It's not often I see a new","adventurer around here.","","Perhaps you would be willing", "to entertain this old man with","a battle?"],["Hmmph!","That certainly brought back","old memories!","It's been ages since I got","this heated over a Pokemon","battle!","Who knows, maybe you have what", "it takes to beat the champion!","Ha!"],True,[50,150,50,200],[poke.Poke('Nidorino',[16,0,334,"Focus Energy",-1,"Leer",-1,"Double Kick",-1,"Poison Sting",-1,'Eviolite',None,0,"Luxury Ball",400,"Rivalry"]),poke.Poke('Nidorina',[16,1,334,"Growl",-1,"Scratch",-1,"Poison Sting",-1,"Double Kick",-1,'Eviolite',None,0,"Luxury Ball",400,"Rivalry"])],3,loc = "route_1")
        else:
            self.r1_noland = npc.NPC(self,'Gentleman','Noland',[1500,-550],[['l',100]],["I still remember when this was","a statue of Cynthia back when","she oversaw the city.","I heard you can still find","that statue standing in the", "Alto Mare gym."],loc = "route_1")
        if self.prog[5][4] == 0:
            self.r2_ayla = npc.NPC(self,'Battle Girl','Ayla',[950,-1100],[['d',40],['r',20],['l',20],['md',20],['u',40],['r',20],['l',20],['mu',20]],["Hey you look pretty strong!","Beating you will be part of my","training!"],["Ha ha! Just kidding!","You're way too strong...",""],True,[100,100,50,100],[poke.Poke('Machop',[9,random.randint(0,1),334,"Low Kick",-1,"Leer",-1,"Focus Energy",-1,"Karate Chop",-1,None,None,0,"Poke Ball",0,"Guts"]),poke.Poke('Timburr',[9,random.randint(0,1),334,"Pound",-1,"Leer",-1,"Bide",-1,"Focus Energy",-1,None,None,0,"Poke Ball",0,"Sheer Force"])],4,loc = "route_2")
        else:
            self.r2_ayla = npc.NPC(self,'Battle Girl','Ayla',[950,-1100],[['d',40],['r',20],['l',20],['md',20],['u',40],['r',20],['l',20],['mu',20]],["I'm gonna beat the next","trainer I see as part of my","training!","Not you of course!","",""],loc = "route_2")
        if self.prog[5][5] == 0:
            self.r2_robby = npc.NPC(self,'Hiker','Robby',[800,-1450],[['mr',140],['ml',140]],["The road ahead is pretty", "dangerous.", "","You're gonna have to beat me", "in a battle if you wanna", "survive in there!"],["Ha! You're a lot stronger than","you look! I don't know what I","was so worried about."],True,[0,0,150,150],[poke.Poke('Spearow',[7,random.randint(0,1),334,"Peck",-1,"Growl",-1,"Leer",-1,None,None,None,None,0,"Poke Ball",0,"Keen Eye"]),poke.Poke('Aron',[8,random.randint(0,1),334,"Harden",-1,"Mud-Slap",-1,"Headbutt",-1,"Tackle",-1,None,None,0,"Poke Ball",0,"Sturdy"]),poke.Poke('Trapinch',[10,random.randint(0,1),334,"Mud-Slap",-1,"Bite",-1,"Bulldoze",-1,"Bide",-1,None,None,0,"Premier Ball",0,"Arena Trap"])],5,loc = "route_2")
        else:
            self.r2_robby = npc.NPC(self,'Hiker','Robby',[800,-1450],[['mr',140],['ml',140]],["Heh.", "I've never actually gone into", "the caves.","I'm too scared of the creepy","sounds you hear just standing", "at the entrance..."],loc = "route_2")
        if self.prog[5][6] == 0:
            self.echo_carlos = npc.NPC(self,'Preschoolerb','Carlos',[550,-600],[['mr',60],['md',40],['ml',60],['mu',40]],["E C H O O O O O ! ! ! ! ! !","",""],["Ehehe...","That was pretty cool though","wasn't it?"],True,[100,100,100,100],[poke.Poke('Whismur',[8,random.randint(0,1),334,"Echoed Voice",-1,None,None,None,None,None,None,None,None,0,"Poke Ball",0,"Soundproof"]),poke.Poke('Whismur',[9,random.randint(0,1),334,"Echoed Voice",-1,None,None,None,None,None,None,None,None,0,"Poke Ball",0,"Soundproof"]),poke.Poke('Whismur',[10,random.randint(0,1),334,"Echoed Voice",-1,None,None,None,None,None,None,None,None,0,"Poke Ball",0,"Soundproof"])],6,spd = 1,loc = "echo_cave")
        else:
            self.echo_carlos = npc.NPC(self,'Preschoolerb','Carlos',[550,-600],[['mr',60],['md',40],['ml',60],['mu',40]],["This place is awesome!!!","I can yell as much as I want","and Mom won't get mad at me!"],spd = 1,loc = "echo_cave")
        if self.prog[5][7] == 0:
            self.echo_vivi = npc.NPC(self,'Ace Trainerf','Vivian',[1300,-1700],[['d',100]],["Ha! What a shame!","Climbing all the way up here","just to get crushed by me!"],["Yikes!","Maybe I spoke a little too", "soon..."],True,[0,150,0,0],[poke.Poke('Nidoran_F',[10,random.randint(0,1),334,"Growl",-1,"Scratch",-1,"Tail Whip",-1,"Double Kick",-1,None,None,0,"Ultra Ball",0,"Rivalry"]),poke.Poke('Noibat',[10,random.randint(0,1),334,"Screech",-1,"Supersonic",-1,"Absorb",-1,"Tackle",-1,None,None,0,"Ultra Ball",0,"Infiltrator"]),poke.Poke('Roggenrola',[10,random.randint(0,1),334,"Tackle",-1,"Sand Attack",-1,"Harden",-1,"Headbutt",-1,None,None,0,"Ultra Ball",0,"Sturdy"]),poke.Poke('Butterfree',[11,random.randint(0,1),334,"Gust",-1,"Confusion",-1,"String Shot",-1,"Tackle",-1,None,None,0,"Ultra Ball",0,"Compound Eyes"])],7,loc = "echo_cave")
        else:
            self.echo_vivi = npc.NPC(self,'Ace Trainerf','Vivian',[1300,-1700],[['d',100]],["Huh, looks like I was the one","who got crushed...",""],loc = "echo_cave")
        if self.prog[5][8] == 0:
            self.vigore_troy = npc.NPC(self,'Triathelete','Troy',[1800,-1300],[['md',20],['mr',250],['mu',20],['ml',250]],["*Huff* *puff*","I can't...last...much...","longer..."],["*Huff* *puff*","I think...this is...the end...","for me..."],True,[100,100,100,100],[poke.Poke('Joltik',[12,random.randint(0,1),334,"Fury Cutter",-1,"Absorb",-1,"Thunder Wave",-1,"Screech",-1,None,None,0,"Poke Ball",0,"Compound Eyes"]),poke.Poke('Electrike',[12,random.randint(0,1),334,"Tackle",-1,"Howl",-1,"Thunder Wave",-1,"Quick Attack",-1,None,None,0,"Poke Ball",0,"Static"]),poke.Poke('Elekid',[12,random.randint(0,1),334,"Quick Attack",-1,"Thunder Shock",-1,"Low Kick",-1,"Swift",-1,None,None,0,"Poke Ball",0,"Static"])],8,spd = 1,loc = "vigore")
        else:
            self.vigore_troy = npc.NPC(self,'Triathelete','Troy',[1800,-1300],[['md',20],['mr',250],['mu',20],['ml',250]],["*Huff* *puff*","I can't...feel...my legs...","anymore..."],spd = 1,loc = "echo_cave")
        if self.prog[5][9] == 0:
            self.vigore_genos = npc.NPC(self,'Expertm','Chuck',[1800,-1200],[['mr',250],['mu',20],['ml',250],['md',20]],["Allow me to give you a taste","of the wonders of running!",""],["Hmph! If I were younger, I","would've run circles around","you!"],True,[100,100,100,100],[poke.Poke('Pidgey',[12,random.randint(0,1),334,"Tackle",-1,"Sand Attack",-1,"Gust",-1,None,None,None,None,0,"Poke Ball",0,"Keen Eye"]),poke.Poke('Spearow',[12,random.randint(0,1),334,"Peck",-1,"Leer",-1,"Pursuit",-1,"Fury Attack",-1,None,None,0,"Poke Ball",0,"Keen Eye"]),poke.Poke('Scyther',[12,random.randint(0,1),334,"Vacuum Wave",-1,"Quick Attack",-1,"Pursuit",-1,"Focus Energy",-1,None,None,0,"Poke Ball",0,"Technician"])],9,spd = 1,loc = "echo_cave")
        else:
            self.vigore_genos = npc.NPC(self,'Expertm','Chuck',[1800,-1200],[['mr',250],['mu',20],['ml',250],['md',20]],["No breaks allowed!","Stopping to rest is admitting","defeat!"],spd = 1,loc = "echo_cave")
        if self.prog[5][10] == 0:
            self.vigore_victor = npc.NPC(self,'Ace Trainerm','Victor',[3600,-1000],[['l',20]],["Hey! You look like a suitable","trainer to test my Pokemon","against."],["Well, my dad always said that","losing is just another step in","getting stronger."],True,[0,0,100,0],[poke.Poke('Nidoran_M',[12,random.randint(0,1),334,"Leer",-1,"Peck",-1,"Focus Energy",-1,"Double Kick",-1,None,None,0,"Ultra Ball",0,"Rivalry"]),poke.Poke('Togedemaru',[12,random.randint(0,1),334,"Tackle",-1,"Thunder Shock",-1,"Defense Curl",-1,"Rollout",-1,None,None,0,"Ultra Ball",0,"Iron Barbs"]),poke.Poke('Sandile',[13,random.randint(0,1),334,"Bite",-1,"Sand Attack",-1,"Torment",-1,"Sand Tomb",-1,None,None,0,"Ultra Ball",0,"Moxie"]),poke.Poke('Beedrill',[13,random.randint(0,1),334,"Twineedle",-1,"Fury Attack",-1,"Harden",-1,"Poison Sting",-1,None,None,0,"Ultra Ball",0,"Swarm"])],10,loc = "echo_cave")
        else:
            self.vigore_victor = npc.NPC(self,'Ace Trainerm','Victor',[3600,-1000],[['l',20]],["There's an Electrike down that","trail that keeps snarling when","you approach him."],loc = "echo_cave")
        if self.prog[5][11] == 0:
            self.egi_gyml_sci = npc.NPC(self,'Scientistf','Sandy',[50,350],[['u',20]],["Sorry I didn't see you enter.","Perhaps there's something you","need assistance with?","Well, you're not getting","anything out of me unless you","beat me in a battle!"],["The main gate?","Yeah I've got the controller","for it right here!","...","...","...","Well, that's awkward. It looks","like I accidentally dropped","the controller somewhere."],True,[0,0,0,0],[poke.Poke('Klink',[14,2,334,"Vice Grip",-1,"Charge",-1,"Thunder Shock",-1,None,None,None,None,0,"Poke Ball",0,"Minus"]),poke.Poke('Togedemaru',[15,random.randint(0,1),334,"Defense Curl",-1,"Rollout",-1,"Charge",-1,"Thunder Shock",-1,None,None,0,"Poke Ball",0,"Iron Barbs"])],11,loc = "egi_gym_l")
        else:
            self.egi_gyml_sci = npc.NPC(self,'Scientistf','Sandy',[50,350],[['u',20]],["Very sorry about that. I'm","usually not so clumsy.",""],loc = "egi_gym_l")
        if self.prog[5][12] == 0:
            self.egi_gymr_sci = npc.NPC(self,'Scientistm','George',[150,300],[['d',20]],["Our research has almost hit","the stage where we can revive","Pokemon fossils!", "Imagine all those extinct","Pokemon walking the streets", "again!"],["I apologize if I scared you.","Sometimes I can't help but", "express my love for research.","*BEEP*","That should take care of the","gate outside."],True,[0,0,0,0],[poke.Poke('Klink',[13,2,334,"Vice Grip",-1,"Charge",-1,"Thunder Shock",-1,None,None,None,None,0,"Poke Ball",0,"Plus"]),poke.Poke('Aron',[14,random.randint(0,1),334,"Mud-Slap",-1,"Headbutt",-1,"Metal Claw",-1,"Rock Tomb",-1,None,None,0,"Poke Ball",0,"Sturdy"]),poke.Poke('Magnemite',[14,2,334,"Supersonic",-1,"Thunder Shock",-1,"Thunder Wave",-1,"Magnet Bomb",-1,None,None,0,"Poke Ball",0,"Magnet Pull"])],12,loc = "egi_gym_r")
        else:
            self.egi_gymr_sci = npc.NPC(self,'Scientistm','George',[150,300],[['d',20]],["Let me know if you ever want","to dabble in research. I would", "love to give you some tips."],loc = "egi_gym_r")
        if self.prog[5][13] == 0:
            self.r3_bug = npc.NPC(self,'Bug Catcher','Charlie',[2100,100],[['md',60],['d',20],['mr',40],['r',80],['mu',60],['u',60],['ml',40],['l',20]],["Are you here to find new bugs","with me? If not, you'd better","buzz off!"],["Hmph! Fine, you can play here","too. Just don't forget that I", "was here first!"],True,[100,100,100,100],[poke.Poke('Joltik',[14,random.randint(0,1),334,"Thunder Wave",-1,"Screech",-1,"Fury Cutter",-1,"Spider Web",-1,None,None,0,"Poke Ball",100,"Compound Eyes"]),poke.Poke('Venipede',[14,random.randint(0,1),334,"Defense Curl",-1,"Rollout",-1,"Screech",-1,"Pursuit",-1,None,None,0,"Poke Ball",100,"Poison Point"]),poke.Poke('Beedrill',[14,random.randint(0,1),334,"Twineedle",-1,"Fury Attack",-1,"Poison Sting",-1,"Rage",-1,None,None,0,"Poke Ball",50,"Swarm"]),poke.Poke('Butterfree',[14,random.randint(0,1),334,"Gust",-1,"Confusion",-1,"Sleep Powder",-1,"Stun Spore",-1,None,None,0,"Poke Ball",50,"Compound Eyes"])],13,loc = "route_3")
        else:
            self.r3_bug = npc.NPC(self,'Bug Catcher','Charlie',[2100,100],[['md',60],['d',20],['mr',40],['r',80],['mu',60],['u',60],['ml',40],['l',20]],["Hurry up and leave already!","I only said you could stay for", "a little while!","I can't have you finding all","the Pokemon here before I get","the chance to!"],loc = "route_3")
        if self.prog[5][14] == 0:
            self.r3_hika = npc.NPC(self,'Hiker','Bryson',[1500,200],[['u',20]],["Hey! These crystals are mine!","No one's getting their hands","on them, not even you!"],["Oh, you're not here to mine","them? Well I just wanted to", "look at them anyways..."],True,[50,0,0,0],[poke.Poke('Roggenrola',[16,random.randint(0,1),334,"Headbutt",-1,"Harden",-1,"Sand Attack",-1,"Rock Blast",-1,None,None,0,"Poke Ball",50,"Weak Armor"]),poke.Poke('Dwebble',[17,random.randint(0,1),334,"Fury Cutter",-1,"Smack Down",-1,"Rock Blast",-1,"Feint Attack",-1,None,None,0,"Poke Ball",50,"Shell Armor"])],14,loc = "route_3")
        else:
            self.r3_hika = npc.NPC(self,'Hiker','Bryson',[1500,200],[['u',20]],["Despite all the expeditions","I've been on, I've never seen", "crystals like these.","The way they're glowing...It's","almost as if they're alive!",""],loc = "route_3")
        if self.prog[5][15] == 0:
            self.r3_sci = npc.NPC(self,'Scientistf','Rosa',[1650,100],[['l',100],['mu',40],['ml',60],['d',140],['mr',60],['md',40]],["I've been analyzing this rock","for so long, I'm starting to","feel really sleepy!", "I think it's about time I had","a break from this crystal!", ""],["Woo! That was refreshing!","Now I can get right back to my", "research!"],True,[100,100,100,100],[poke.Poke('Voltorb',[15,random.randint(0,1),334,"Sonic Boom",-1,"Eerie Impulse",-1,"Screech",-1,"Rollout",-1,'Poke Ball',None,50,"Poke Ball",0,"Soundproof"]),poke.Poke('Aron',[15,random.randint(0,1),334,"Mud-Slap",-1,"Headbutt",-1,"Metal Claw",-1,"Harden",-1,None,None,0,"Poke Ball",50,"Sturdy"]),poke.Poke('Carbink',[16,2,334,"Sharpen",-1,"Tackle",-1,"Smack Down",-1,"Harden",-1,None,None,0,"Poke Ball",0,"Clear Body"])],15,loc = "route_3")
        else:
            self.r3_sci = npc.NPC(self,'Scientistf','Rosa',[1650,100],[['l',100],['mu',40],['ml',60],['d',140],['mr',60],['md',40]],["Ugh! I'm already tired again!","How important could a little", "pink crystal possibly be?"],loc = "route_3")
        if self.prog[5][16] == 0:
            self.sl_psy = npc.NPC(self,'Psychic','Hugo',[2250,-550],[['mr',60],['r',200],['md',60],['d',140],['ml',60],['l',260],['mu',60],['u',160]],["","",""],["That's not possible! I had the","power of knowledge! You never", "should have stood a chance!"],True,[100,200,100,200],[poke.Poke('Drowzee',[18,random.randint(0,1),334,"Poison Gas",-1,"Headbutt",-1,"Confusion",-1,"Disable",-1,None,None,0,"Poke Ball",100,"Insomnia"]),poke.Poke('Chimecho',[19,random.randint(0,1),334,"Astonish",-1,"Yawn",-1,"Psywave",-1,"Take Down",-1,None,None,0,"Poke Ball",150,"Levitate"])],16,loc = "scarab_l")
        else:
            self.sl_psy = npc.NPC(self,'Psychic','Hugo',[2250,-550],[['mr',60],['r',200],['md',60],['d',140],['ml',60],['l',260],['mu',60],['u',160]],["I haven't given up! Soon I'll","be able to predict everything", "a trainer could possibly do!","Then I'll be able to take on","anyone that strolls through","here!"],loc = "scarab_l")
        if self.prog[5][17] == 0:
            self.sl_rich = npc.NPC(self,'Rich Boy','Leonard',[1300,400],[['l',60],['u',40],['d',100],['r',60]],["There is so much filth and","muck everwhere! I don't even","know where I am anymore!"],["Ugh, and on top of everything,","I can't even win a battle", "against some random trainer!","This has got to be the worst","day of my life!",""],True,[100,100,100,100],[poke.Poke('Electrike',[17,random.randint(0,1),334,"Leer",-1,"Thunder Wave",-1,"Quick Attack",-1,"Spark",-1,None,None,0,"Poke Ball",100,"Static"]),poke.Poke('Nidorino',[17,0,334,"Poison Sting",-1,"Double Kick",-1,"Peck",-1,"Focus Energy",-1,None,None,0,"Poke Ball",50,"Rivalry"]),poke.Poke('Luxio',[18,random.randint(0,1),334,"Leer",-1,"Spark",-1,"Charge",-1,"Bite",-1,None,None,0,"Poke Ball",50,"Intimidate"])],17,loc = "scarab_l")
        else:
            self.sl_rich = npc.NPC(self,'Rich Boy','Leonard',[1300,400],[['d',60]],["Why did I even bother stepping","inside here? It's just been ","disasters one after another!","I followed the directions that","stupid girl gave me, and just", "look at the result!"],loc = "scarab_l")
        if self.prog[5][18] == 0:
            self.sl_ace = npc.NPC(self,'Ace Trainerf','Jesse',[3300,350],[['l',100]],["I've been training for days in","these woods. Get ready to see","the fruits of my labor!"],["No way! I lost even after all","that training? Maybe I'm not", "cut out for this..."],True,[0,0,150,0],[poke.Poke('Skitty',[17,random.randint(0,1),334,"Attract",-1,"Fake Out",-1,"Disarming Voice",-1,"Double Slap",-1,None,None,0,"Ultra Ball",150,"Normalize"]),poke.Poke('Dunsparce',[18,random.randint(0,1),334,"Screech",-1,"Mud-Slap",-1,"Yawn",-1,"Rollout",-1,None,None,0,"Ultra Ball",50,"Serene Grace"]),poke.Poke('Zubat',[17,random.randint(0,1),334,"Supersonic",-1,"Bite",-1,"Wing Attack",-1,"Confuse Ray",-1,None,None,0,"Ultra Ball",100,"Inner Focus"]),poke.Poke('Nuzleaf',[18,random.randint(0,1),334,"Razor Leaf",-1,"Fake Out",-1,"Nature Power",-1,"Growth",-1,None,None,0,"Ultra Ball",100,"Early Bird"]),poke.Poke('Heracross',[18,random.randint(0,1),334,"Endure",-1,"Aerial Ace",-1,"Chip Away",-1,"Feint",-1,None,None,0,"Ultra Ball",50,"Guts"])],18,loc = "scarab_l")
        else:
            self.sl_ace = npc.NPC(self,'Ace Trainerf','Jesse',[3300,350],[['l',100]],["I won't give up! I'll just","keep training until I can beat","even you in a battle!"],loc = "scarab_l")
        if self.prog[5][19] == 0:
            self.sr_beauty = npc.NPC(self,'Beauty','Lucille',[1100,600],[['l',60],['u',100],['r',60],['u',60]],["Hee hee! He'll never be able","to find me hiding all the way","out here!"],["Hee hee! Well that was pretty","fun, wasn't it?", ""],True,[100,100,100,100],[poke.Poke('Psyduck',[19,random.randint(0,1),334,"Confusion",-1,"Fury Swipes",-1,"Water Pulse",-1,"Disable",-1,None,None,0,"Poke Ball",100,"Damp"]),poke.Poke('Nidorina',[19,1,334,"Poison Sting",-1,"Scratch",-1,"Double Kick",-1,"Growl",-1,None,None,0,"Poke Ball",100,"Rivalry"]),poke.Poke('Maractus',[19,random.randint(0,1),334,"Cotton Spore",-1,"Mega Drain",-1,"Pin Missile",-1,"Synthesis",-1,None,None,0,"Poke Ball",150,"Water Absorb"])],19,loc = "scarab_r")
        else:
            self.sr_beauty = npc.NPC(self,'Beauty','Lucille',[1100,600],[['u',60]],["Do you think he's okay?","He hasn't texted me anything","for a while...","I mean, what's the worst that","could happen?",""],loc = "scarab_r")
        if self.prog[5][20] == 0:
            self.sr_ace = npc.NPC(self,'Ace Trainerm','James',[3000,50],[['d',100]],["You're not gonna get past me","like all those other bastards","did!"],["I don't think I can do this","any longer...", ""],True,[0,50,0,0],[poke.Poke('Mightyena',[19,random.randint(0,1),334,"Tackle",-1,"Sand Attack",-1,"Bite",-1,"Swagger",-1,None,None,0,"Ultra Ball",100,"Intimidate"]),poke.Poke('Furret',[19,random.randint(0,1),334,"Focus Energy",-1,"Fury Swipes",-1,"Quick Attack",-1,"Agility",-1,None,None,0,"Ultra Ball",100,"Keen Eye"]),poke.Poke('Murkrow',[19,random.randint(0,1),334,"Wing Attack",-1,"Haze",-1,"Pursuit",-1,"Astonish",-1,None,None,0,"Ultra Ball",100,"Super Luck"]),poke.Poke('Lombre',[20,random.randint(0,1),334,"Mega Drain",-1,"Mist",-1,"Bubble",-1,"Natural Gift",-1,None,None,0,"Ultra Ball",150,"Rain Dish"]),poke.Poke('Pinsir',[20,random.randint(0,1),334,"Vital Throw",-1,"Revenge",-1,"Seismic Toss",-1,"Bind",-1,None,None,0,"Ultra Ball",100,"Hyper Cutter"])],20,loc = "scarab_r")
        else:
            self.sr_ace = npc.NPC(self,'Ace Trainerm','James',[3000,50],[['d',100]],["That green haired guy was so","cool though! I mean he beat me","pretty badly, but still!","I want to be just like that","when I grow up! Super strong","and in charge of people!"],loc = "scarab_r")
        if self.prog[5][21] == 0:
            self.r3_battle = npc.NPC(self,'Battle Girl','Harper',[5900,200],[['mr',80],['r',100],['ml',80],['l',60]],["I've been training here all", "day! I'm so warmed up, you'll","never stand a chance!"],["*Huff* *Puff*","Maybe I'm a little too", "exhausted for this..."],True,[0,0,200,100],[poke.Poke('Machop',[21,random.randint(0,1),334,"Low Sweep",-1,"Seismic Toss",-1,"Revenge",-1,"Knock Off",-1,None,None,0,"Poke Ball",150,"Guts"]),poke.Poke('Nuzleaf',[21,random.randint(0,1),334,"Torment",-1,"Razor Leaf",-1,"Fake Out",-1,"Razor Wind",-1,None,None,0,"Poke Ball",200,"Early Bird"]),poke.Poke('Zangoose',[21,random.randint(0,1),334,"Hone Claws",-1,"Quick Attack",-1,"Pursuit",-1,"Slash",-1,None,None,0,"Poke Ball",120,"Immunity"])],21,loc = "route_3")
        else:
            self.r3_battle = npc.NPC(self,'Battle Girl','Harper',[5900,200],[['mr',80],['r',100],['ml',80],['l',60]],["I can't remember if I turned","off the oven before I left...",""],loc = "route_3")
        #just pokemon
        self.r3_fishteam = [poke.Poke('Magikarp',[19,random.randint(0,1),334,"Splash",-1,"Tackle",-1,None,None,None,None,None,None,0,"Poke Ball",50,"Swift Swim"]),poke.Poke('Magikarp',[20,random.randint(0,1),334,"Splash",-1,"Tackle",-1,None,None,None,None,None,None,0,"Poke Ball",50,"Swift Swim"]),poke.Poke('Magikarp',[21,random.randint(0,1),334,"Splash",-1,"Tackle",-1,None,None,None,None,None,None,0,"Poke Ball",50,"Swift Swim"]),poke.Poke('Magikarp',[22,random.randint(0,1),334,"Splash",-1,"Tackle",-1,None,None,None,None,None,None,0,"Poke Ball",50,"Swift Swim"]),poke.Poke('Magikarp',[23,random.randint(0,1),334,"Splash",-1,"Tackle",-1,None,None,None,None,None,None,0,"Poke Ball",400,"Swift Swim"]),poke.Poke('Gyarados',[24,random.randint(0,1),334,"Bite",-1,"Leer",-1,"Twister",-1,"Taunt",-1,None,None,0,"Net Ball",100,"Intimidate"])]
        self.r3_fishteam2 = [poke.Poke('Shellder',[22,random.randint(0,1),334,"Icicle Spear",-1,"Withdraw",-1,"Protect",-1,"Water Gun",-1,None,None,0,"Poke Ball",100,"Skill Link"]),poke.Poke('Krabby',[23,random.randint(0,1),334,"Metal Claw",-1,"Mud Shot",-1,"Bubble Beam",-1,"Vice Grip",-1,None,None,0,"Poke Ball",150,"Hyper Cutter"]),poke.Poke('Psyduck',[24,random.randint(0,1),334,"Screech",-1,"Confusion",-1,"Water Pulse",-1,"Disable",-1,None,None,0,"Poke Ball",150,"Cloud Nine"])]
        self.r3_triteam = [poke.Poke('Ponyta',[23,random.randint(0,1),334,"Flame Charge",-1,"Stomp",-1,"Flame Wheel",-1,"Tail Whip",-1,None,None,0,"Poke Ball",150,"Flash Fire"]),poke.Poke('Pidgeotto',[23,random.randint(0,1),334,"Twister",-1,"Quick Attack",-1,"Gust",-1,"Whirlwind",-1,None,None,0,"Poke Ball",250,"Tangled Feet"]),poke.Poke('Seviper',[23,random.randint(0,1),334,"Poison Fang",-1,"Glare",-1,"Screech",-1,"Wrap",-1,None,None,0,"Poke Ball",150,"Shed Skin"])]
        self.piag_team1 = [poke.Poke('Jigglypuff',[25,random.randint(0,1),334,"Disarming Voice",-1,"Stockpile",-1,"Swallow",-1,"Spit Up",-1,None,None,0,"Poke Ball",350,"Cute Charm"]),poke.Poke('Lopunny',[25,random.randint(0,1),334,"Jump Kick",-1,"Quick Attack",-1,"Baby-Doll Eyes",-1,"Foresight",-1,None,None,0,"Poke Ball",250,"Cute Charm"])]
        self.piag_team2 = [poke.Poke('Loudred',[25,random.randint(0,1),334,"Screech",-1,"Stomp",-1,"Bite",-1,"Echoed Voice",-1,None,None,0,"Poke Ball",200,"Soundproof"]),poke.Poke('Zangoose',[25,random.randint(0,1),334,"Revenge",-1,"Slash",-1,"Hone Claws",-1,"Quick Attack",-1,None,None,0,"Poke Ball",150,"Immunity"])]
        self.piag_team3 = [poke.Poke('Dunsparce',[24,random.randint(0,1),334,"Drill Run",-1,"Ancient Power",-1,"Yawn",-1,"Mud-Slap",-1,None,None,0,"Poke Ball",100,"Serene Grace"]),poke.Poke('Pidgeotto',[24,random.randint(0,1),334,"Twister",-1,"Quick Attack",-1,"Gust",-1,"Whirlwind",-1,None,None,0,"Poke Ball",300,"Keen Eye"]),poke.Poke('Noctowl',[25,random.randint(0,1),334,"Extrasensory",-1,"Psycho Shift",-1,"Echoed Voice",-1,"Hypnosis",-1,None,None,0,"Poke Ball",150,"Insomnia"])]
        self.piag_team4 = [poke.Poke('Happiny',[25,random.randint(0,1),334,"Pound",-1,"Charm",-1,"Sweet Kiss",-1,"Refresh",-1,None,None,0,"Poke Ball",400,"Natural Cure"]),poke.Poke('Azurill',[25,random.randint(0,1),334,"Bounce",-1,"Slam",-1,"Bubble Beam",-1,"Charm",-1,None,None,0,"Poke Ball",400,"Huge Power"]),poke.Poke('Igglybuff',[25,random.randint(0,1),334,"Sing",-1,"Charm",-1,"Pound",-1,"Sweet Kiss",-1,None,None,0,"Poke Ball",400,"Cute Charm"]),poke.Poke('Munchlax',[25,random.randint(0,1),334,"Screech",-1,"Body Slam",-1,"Amnesia",-1,"Lick",-1,None,None,0,"Poke Ball",400,"Thick Fat"])]
        if self.prog[5][29] == 0:
            self.mc_hex = npc.NPC(self,'Hex Maniac','Scarlett',[2250,250],[['md',80],['d',100],['mr',80],['r',60],['ml',80],['l',60],['mu',80],['u',60]],["It's cold. It's dark. You see", "creepy reflections of yourself","everywhere!","I love this place!","",""],["Spooking trainers that walk in","here is pretty fun too!", ""],True,[150,150,150,150],[poke.Poke('Misdreavus',[26,random.randint(0,1),334,"Hex",-1,"Confuse Ray",-1,"Toxic",-1,"Mean Look",-1,None,None,300,"Poke Ball",120,"Levitate"]),poke.Poke('Mightyena',[27,random.randint(0,1),334,"Swagger",-1,"Snarl",-1,"Fire Fang",-1,"Thunder Fang",-1,None,None,0,"Poke Ball",200,"Intimidate"]),poke.Poke('Hypno',[28,random.randint(0,1),334,"Psybeam",-1,"Poison Gas",-1,"Hypnosis",-1,"Nightmare",-1,None,None,0,"Poke Ball",200,"Insomnia"])],29,loc = "mirror_cave")
        else:
            self.mc_hex = npc.NPC(self,'Hex Maniac','Harper',[2250,250],[['md',80],['d',100],['mr',80],['r',60],['ml',80],['l',60],['mu',80],['u',60]],["Sometimes I like to think that","there's a Pokemon hiding","inside these mirrors!"],loc = "mirror_cave")
        if self.prog[5][30] == 0:
            self.mc_hiker = npc.NPC(self,'Hiker','Ben',[2600,-600],[['mr',120],['r',100],['ml',120],['l',80]],["I only took a quick peek in", "here, and now I've lost the","entrance!","I need something to help me","deal with this stress!",""],["Well that wasn't very stress","relieving...",""],True,[0,0,150,150],[poke.Poke('Geodude',[28,random.randint(0,1),334,"Self-Destruct",-1,"Magnitude",-1,"Smack Down",-1,"Stealth Rock",-1,None,None,0,"Poke Ball",200,"Sturdy"]),poke.Poke('Onix',[28,random.randint(0,1),334,"Slam",-1,"Smack Down",-1,"Gyro Ball",-1,"Curse",-1,None,None,200,"Poke Ball",120,"Sturdy"]),poke.Poke('Sudowoodo',[28,random.randint(0,1),334,"Rock Tomb",-1,"Low Kick",-1,"Slam",-1,"Flail",-1,None,None,0,"Poke Ball",300,"Sturdy"])],30,loc = "mirror_cave")
        else:
            self.mc_hiker = npc.NPC(self,'Hiker','Harper',[2600,-600],[['mr',120],['r',100],['ml',120],['l',80]],["Now that I think about it,","maybe it's not all that bad in","here...","Now I don't have to deal with","the stress of life!",""],loc = "mirror_cave")
        if self.prog[5][31] == 0:
            self.r4_expert = npc.NPC(self,'Expertm','Owen',[700,350],[['mr',100],['r',120],['ml',100],['l',100]],["If you've come all the way out", "here, you must be a developing","trainer!","Allow me to help you refine","your Pokemon!",""],["Hmm...perhaps you're the one","refining my Pokemon...",""],True,[0,0,150,150],[poke.Poke('Machoke',[31,random.randint(0,1),334,"Wake-Up Slap",-1,"Knock Off",-1,"Seismic Toss",-1,"Focus Energy",-1,None,None,0,"Poke Ball",300,"Guts"]),poke.Poke('Hitmonlee',[31,random.randint(0,1),334,"High Jump Kick",-1,"Focus Energy",-1,"Rolling Kick",-1,"Mega Kick",-1,None,None,0,"Poke Ball",300,"Reckless"])],31,loc = "route_4")
        else:
            self.r4_expert = npc.NPC(self,'Expertm','Harper',[700,350],[['mr',100],['r',120],['ml',100],['l',100]],["If you're looking for a place","to rest, keep heading east to","reach Isola Town!"],loc = "route_4")
        if self.prog[5][32] == 0:
            self.r4_battle = npc.NPC(self,'Battle Girl','Lily',[2150,100],[['l',80]],["I'm going to demolish this", "rock right after I've finished","demolishing you!"],["How am I supposed to crack","open this rock if I can't even","beat you?"],True,[0,0,0,0],[poke.Poke('Gurdurr',[32,random.randint(0,1),334,"Rock Throw",-1,"Chip Away",-1,"Wake-Up Slap",-1,"Bulk Up",-1,None,None,0,"Poke Ball",300,"Guts"]),poke.Poke('Hitmonchan',[32,random.randint(0,1),334,"Vacuum Wave",-1,"Bullet Punch",-1,"Mach Punch",-1,"Revenge",-1,None,None,0,"Poke Ball",400,"Iron Fist"])],32,loc = "route_4")
        else:
            self.r4_battle = npc.NPC(self,'Battle Girl','Harper',[2150,100],[['l',80]],["Considering how long I've been","swinging at this rock, I'm","sure I'll break it someday."],loc = "route_4")
        if self.prog[5][33] == 0:
            self.r4_fish = npc.NPC(self,'Fisherman','Richard',[2600,700],[['r',80]],["You know what shellfish are", "great for?","","Beating down all the trainers","passing by!",""],["Huh, I guess you proved me","wrong today!",""],True,[0,0,0,0],[poke.Poke('Kingler',[30,random.randint(0,1),334,"Stomp",-1,"Metal Claw",-1,"Mud Shot",-1,"Bubble Beam",-1,None,None,0,"Poke Ball",300,"Shell Armor"]),poke.Poke('Crawdaunt',[30,random.randint(0,1),334,"Night Slash",-1,"Bubble Beam",-1,"Protect",-1,"Double Hit",-1,None,None,0,"Poke Ball",300,"Shell Armor"]),poke.Poke('Cloyster',[32,random.randint(0,1),334,"Shell Smash",-1,"Ice Shard",-1,"Clamp",-1,"Razor Shell",-1,None,None,0,"Poke Ball",300,"Shell Armor"])],33,loc = "route_4")
        else:
            self.r4_fish = npc.NPC(self,'Fisherman','Harper',[2600,700],[['r',80]],["Well shellfish are great for","lots of other things!","","Like eating and stuff, you","know?",""],loc = "route_4")
        self.r4_team1 = [poke.Poke('Ferrothorn',[40,random.randint(0,1),334,"Pin Missile",-1,"Iron Defense",-1,"Gyro Ball",-1,"Curse",-1,'Metal Coat',None,0,"Luxury Ball",400,"Iron Barbs"]),poke.Poke('Scizor',[40,random.randint(0,1),334,"Quick Attack",-1,"Iron Defense",-1,"Bullet Punch",-1,"Pursuit",-1,'Metal Coat',None,0,"Luxury Ball",400,"Technician"]),poke.Poke('Steelix',[40,random.randint(0,1),334,"Thunder Fang",-1,"Rock Slide",-1,"Crunch",-1,"Iron Tail",-1,'Metal Coat',None,0,"Luxury Ball",400,"Sturdy"])]
        if self.prog[5][35] == 0:
            self.r5_psy = npc.NPC(self,'Psychic','Lucas',[600,-300],[['mr',40],['r',60],['md',40],['d',80],['ml',40],['l',100],['mu',40],['u',60]],["You better watch out or you'll", "end up hitting yourself!",""],["Hmm, looks like I should have","been watching out myself!",""],True,[150,150,150,150],[poke.Poke('Mismagius',[34,random.randint(0,1),334,"Confuse Ray",-1,"Pain Split",-1,"Mystical Fire",-1,"Shadow Ball",-1,None,None,0,"Poke Ball",350,"Levitate"]),poke.Poke('Wobbuffet',[35,random.randint(0,1),334,"Counter",-1,"Mirror Coat",-1,None,None,None,None,None,None,0,"Poke Ball",400,"Shadow Tag"])],35,loc = "route_5")
        else:
            self.r5_psy = npc.NPC(self,'Psychic','Harper',[600,-300],[['mr',40],['r',60],['md',40],['d',80],['ml',40],['l',100],['mu',40],['u',60]],["I'm just keeping you on your","toes! You never know what can", "happen in a Pokemon battle!"],loc = "route_5")
        if self.prog[5][36] == 0:
            self.r5_bug = npc.NPC(self,'Bug Catcher','Ethan',[1800,-450],[['mr',80],['r',120],['ml',80],['l',80]],["Woah!!!", "This one's gigantic!!!",""],["Wait, you're not a Pokemon...","",""],True,[0,0,150,150],[poke.Poke('Joltik',[32,random.randint(0,1),334,"Spider Web",-1,"Thunder Wave",-1,"Screech",-1,"Electroweb",-1,None,None,0,"Poke Ball",400,"Unnerve"]),poke.Poke('Joltik',[32,random.randint(0,1),334,"Agility",-1,"Slash",-1,"Electro Ball",-1,"Bug Bite",-1,None,None,0,"Poke Ball",400,"Compound Eyes"]),poke.Poke('Spinarak',[32,random.randint(0,1),334,"Infestation",-1,"Night Shade",-1,"Shadow Sneak",-1,"Sucker Punch",-1,None,None,0,"Poke Ball",400,"Swarm"]),poke.Poke('Ariados',[34,random.randint(0,1),334,"Fell Stinger",-1,"Swords Dance",-1,"Shadow Sneak",-1,"Sucker Punch",-1,None,None,0,"Poke Ball",300,"Swarm"])],36,loc = "route_5")
        else:
            self.r5_bug = npc.NPC(self,'Bug Catcher','Ethan',[1800,-450],[['mr',80],['r',120],['ml',80],['l',80]],["Sorry about that! You're just","kinda funny looking, so I", "mistook you for a Pokemon!"],loc = "route_5")
        if self.prog[5][37] == 0:
            self.r5_lass = npc.NPC(self,'Lass','Emma',[1900,400],[['mr',80],['r',40],['ml',80],['l',60],['md',40],['d',120],['mu',40],['u',40]],["Hey! Come here and play with", "my Pokemon!",""],["Hehe, that was pretty fun","wasn't it?",""],True,[100,100,100,100],[poke.Poke('Vulpix',[32,random.randint(0,1),334,"Hex",-1,"Will-O-Wisp",-1,"Flame Burst",-1,"Extrasensory",-1,None,None,0,"Poke Ball",400,"Flash Fire"]),poke.Poke('Furret',[33,random.randint(0,1),334,"Quick Attack",-1,"Coil",-1,"Slam",-1,"Rest",-1,None,None,0,"Poke Ball",300,"Keen Eye"]),poke.Poke('Floatzel',[34,random.randint(0,1),334,"Aqua Jet",-1,"Ice Fang",-1,"Double Hit",-1,"Quick Attack",-1,None,None,0,"Poke Ball",300,"Swift Swim"])],37,loc = "route_5")
        else:
            self.r5_lass = npc.NPC(self,'Lass','Emma',[1900,400],[['mr',80],['r',40],['ml',80],['l',60],['md',40],['d',120],['mu',40],['u',40]],["We should play again sometime!","It's boring running around all","by myself!"],loc = "route_5")
        if self.prog[5][38] == 0:
            self.r5_beauty = npc.NPC(self,'Beauty','Aria',[1000,500],[['d',80]],["I'm dying to go for a swim!", "You should come join us!",""],["Actually I take that back.","You take things waaay too","seriously!"],True,[0,50,0,0],[poke.Poke('Bellossom',[34,random.randint(0,1),334,"Sunny Day",-1,"Stun Spore",-1,"Magical Leaf",-1,"Moonlight",-1,None,None,0,"Poke Ball",300,"Chlorophyll"]),poke.Poke('Roserade',[34,random.randint(0,1),334,"Venom Drench",-1,"Giga Drain",-1,"Magical Leaf",-1,"Grass Whistle",-1,None,None,0,"Poke Ball",300,"Poison Point"])],38,loc = "route_5")
        else:
            self.r5_beauty = npc.NPC(self,'Beauty','Aria',[1000,500],[['d',80]],["You could have held back","just a little, you know?", ""],loc = "route_5")



    def load_images(self,graphics_change = False) -> None:
        if self.graphic == 1:
            self.r_flair = poke_func.load("p/red_flair.png")
            self.g_flair = poke_func.load("p/green_flair.png")
            self.wave = poke_func.load("p/waves.png")
        else:
            self.r_flair = poke_func.load("p/transparent.png")
            self.g_flair = poke_func.load("p/green_flair_low.png")
            self.wave = poke_func.load("p/waves_low.png")
        if graphics_change == False:
            self.rain_img = poke_func.load("p/terrain/rain.png")
            self.char_shad = poke_func.load("p/char_shadow.png")
            self.ss_d2 = poke_func.load("p/stair_shadow_d2.png")
            self.ss_d1 = poke_func.load("p/stair_shadow_d1.png")
            self.ss_u1 = poke_func.load("p/stair_shadow_u1.png")
            self.ss_u2 = poke_func.load("p/stair_shadow_u2.png")
            self.shadow_u = poke_func.load("p/shadow_u.png")
            self.shadow_d = poke_func.load("p/shadow_d.png")
            self.shadow_l = poke_func.load("p/shadow_l.png")
            self.shadow_r = poke_func.load("p/shadow_r.png")
            self.textbox = poke_func.load("p/textbox.png")
            self.exclaim = poke_func.load("p/exclaim.png")
            self.battlebox = poke_func.load("p/battle_txtbox.png")
            self.choicebox = poke_func.load("p/2_box.png")
            self.arrow = poke_func.load("p/arrow.png")
            self.pokeball = poke_func.load("p/Poke Ball.png")
            self.item_cave = poke_func.load("p/item_cave.png")
            self.item_out = poke_func.load("p/item.png")
            self.dwebble_rock = poke_func.load("p/dwebble.png")
            self.lamp = poke_func.load("p/am/street_lamp.png")
            self.light = poke_func.load("p/am/lamp_light.png")
            self.grass = poke_func.load("p/am/grass_bot.png")
            self.dark_grass = poke_func.load("p/am/dark_grass_bot.png")
            self.small_door = poke_func.load("p/am/house_1_door.png")
            self.traffic_cone = poke_func.load("p/egida/traffic_cone.png")
            self.black_back = poke_func.load("p/black_back.png")
            self.pc_black = poke_func.load("p/am/pc_black.png")
            self.gondolier = pygame.transform.scale(poke_func.load("p/spr/gondolier_d.png"),(45,54))
            self.gondola_1 = poke_func.load("p/am/gondola_1.png")
            self.gondola_2 = poke_func.load("p/am/gondola_2.png")
            self.gondola = self.gondola_1
            self.pcdr = poke_func.load("p/am/pc_door_r.png")
            self.pcdl = poke_func.load("p/am/pc_door_l.png")
            self.pc_light = poke_func.load("p/am/poke_center_light.png")
            self.falls = poke_func.load("p/waterfall.png")
            self.cave_out_u = poke_func.load("p/cave_out_u.png")
            self.cave_in_d = poke_func.load("p/cave_in_d.png")
            self.cave_in_r = poke_func.load("p/cave_in_r.png")
            self.cave_out_r = poke_func.load("p/cave_out_r.png")
            self.caught_icon = pygame.transform.scale(poke_func.load("p/Poke Ball.png"),(25,25))
            #route 1
            self.route_1 = poke_func.load("p/am/Route_1.png")
            self.r1_trees = poke_func.load("p/am/route_1_trees.png")
            self.r1_foam = poke_func.load("p/am/route_1_foam.png")
            self.r1_statue = poke_func.load("p/am/route_1_statue.png")
            self.r1_bridge_l = poke_func.load("p/am/bridge_r.png")
            self.r1_grass = poke_func.load("p/am/route_1_grass.png")
            self.r1_path = poke_func.load("p/am/route_1_path.png")
            self.r1_fence = poke_func.load("p/am/route_1_fence.png")
            #Egida
            self.egida = poke_func.load("p/egida/Egida_City.png")
            self.egi_f = poke_func.load("p/egida/egida_front.png")
            self.egi_gen = poke_func.load("p/egida/generators.png")
            self.egi_lift = poke_func.load("p/egida/lift.png")
            self.egi_back = poke_func.load("p/egida/Egida_Alt.png")
            self.egi_clip = poke_func.load("p/egida/Egida_clip.png")
            #route 2
            self.route_2 = poke_func.load("p/egida/Route_2.png")
            self.r2_f = poke_func.load("p/egida/Route_2_f.png")
            #route 3
            self.r3_back = poke_func.load("p/egida/Route_3.png")
            self.r3_foam = poke_func.load("p/egida/route_3_foam.png")
            self.r3_grass = poke_func.load("p/am/route_1_grass.png")
            self.r3_grass2 = poke_func.load("p/egida/route_3_grass.png")
            self.r3_grass3 = poke_func.load("p/egida/route_3_grass_bot.png")
            self.r3_beach = poke_func.load("p/pianura/route_3_beach.png")
            self.r3_f = poke_func.load("p/egida/route_3_f.png")
            self.r3_fence = poke_func.load("p/egida/route_3_fence2.png")
            self.r3_cloud = poke_func.load("p/pianura/thundurus_cloud.png")
            self.r3_shad = pygame.transform.scale(poke_func.load("p/pianura/Thundurus_shadow.png"),(150,150))
            self.r3_thun = pygame.transform.scale(poke_func.load("p/pianura/Thundurus.png"),(150,150))
            self.r3_lights = poke_func.load("p/egida/shrine_lights.png")
            self.r3_poke_shad = poke_func.load("p/egida/poke_shadow.png")
            self.r3_slow1 = pygame.transform.scale(poke_func.load("p/spr/Slowpoke_sleep1.png"),(80,50))
            self.r3_slow2 = pygame.transform.scale(poke_func.load("p/spr/Slowpoke_sleep2.png"),(80,50))
            self.r3_slow = self.r3_slow1
            #pianura
            self.pia_back = poke_func.load("p/pianura/Pianura_City.png")
            self.pia_f = poke_func.load("p/pianura/pianura_f.png")
            self.pia_foam = poke_func.load("p/pianura/pianura_foam.png")
            self.pia_light = poke_func.load("p/pianura/Lighthouse_light.png")
            self.d1_door = poke_func.load("p/am/house_2_door.png")
            self.pia_gymdoor = poke_func.load("p/pianura/gym_door.png")
            #sableye
            self.sableye_u1 = pygame.transform.scale(poke_func.load("p/spr/Sableye_u1.png"),(50,60))
            self.sableye_u2 = pygame.transform.scale(poke_func.load("p/spr/Sableye_u2.png"),(50,60))
            self.sableye_u3 = pygame.transform.scale(poke_func.load("p/spr/Sableye_u3.png"),(50,60))
            self.sableye_d1 = pygame.transform.scale(poke_func.load("p/spr/Sableye_d1.png"),(50,60))
            self.sableye_d2 = pygame.transform.scale(poke_func.load("p/spr/Sableye_d2.png"),(50,60))
            self.sableye_d3 = pygame.transform.scale(poke_func.load("p/spr/Sableye_d3.png"),(50,60))
            self.sableye_l1 = pygame.transform.scale(poke_func.load("p/spr/Sableye_l1.png"),(50,60))
            self.sableye_l2 = pygame.transform.scale(poke_func.load("p/spr/Sableye_l2.png"),(50,60))
            self.sableye_l3 = pygame.transform.scale(poke_func.load("p/spr/Sableye_l3.png"),(50,60))
            self.sableye_r1 = pygame.transform.scale(poke_func.load("p/spr/Sableye_r1.png"),(50,60))
            self.sableye_r2 = pygame.transform.scale(poke_func.load("p/spr/Sableye_r2.png"),(50,60))
            self.sableye_r3 = pygame.transform.scale(poke_func.load("p/spr/Sableye_r3.png"),(50,60))
            #route 4
            self.r4_back = poke_func.load("p/isola/route_4.png")
            self.r4_foam = poke_func.load("p/isola/route_4_foam.png")
            self.r4_f = poke_func.load("p/isola/route_4_f.png")
            self.r4_kang = pygame.transform.scale(poke_func.load("p/spr/Kangaskhan_r1.png"),(75,90))
            self.r4_cave = poke_func.load("p/isola/cave_out_r.png")
            #isola
            self.isola_back = poke_func.load("p/isola/Isola_Town.png")
            self.isola_f = poke_func.load("p/isola/Isola_f.png")
            self.isola_foam = poke_func.load("p/isola/Isola_foam.png")
            #route 5
            self.r5_back = poke_func.load("p/isola/route_5.png")
            self.r5_beach = poke_func.load("p/isola/route_5_beach.png")
            self.r5_f = poke_func.load("p/isola/route_5_f.png")
            self.r5_foam = poke_func.load("p/isola/route_5_foam.png")
            #verde
            self.verde_back = poke_func.load("p/verde/Verde_City.png")
            self.verde_foam = poke_func.load("p/verde/verde_foam.png")


if __name__ == '__main__':
    pygame.init()
    Pokemon().run()
