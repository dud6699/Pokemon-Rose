import save
import ast
import os
import poke
import items
import poke_func
import pygame
import random
from pygame.locals import*

#eturn 0 = player, 1 = enemy

class Move:
    def __init__(self,name):
        self.name = name
        file = open("moves/"+name+".txt","r")
        data = file.readlines()
        self.type = data[0][:-1]
        self.ori_type= self.type
        self.cat = data[1][:-1]
        self.pow = data[2][:-1]
        self.acc = data[3][:-1]
        self.eff = ast.literal_eval(data[4])
        self.tar = data[5][:-1]
        self.pp = int(data[6][:-1])
        self.desc = ast.literal_eval(data[7])
        if len(self.desc) != 0 and len(self.desc[0]) > 20:
            self.desc = poke_func.split_text(self.desc[0],20,6)
        self.priority = int(data[8])
        self.sec = data[9]
        self.boost = 1

    def cast(self,P,pokes,pokee,mvnum,eturn = 1) -> None:
        if pokes.exit:
            if eturn == 1:
                if not poke_func.last_poke(P.opponent):
                    return [3,False,0,[],0,0]
                else:
                    pokes.exit = False
            else:
                if not poke_func.last_poke(P.party):
                    return [3,False,0,[],0,0]
                else:
                    pokes.exit = False
        pokes.can_sucker = False
        if pokee.status == 'Faint':
            opp_dead = True
            for x in P.opponent:
                if type(x) != str and x.status != 'Faint':
                    opp_dead = False
            if opp_dead:
                return [3,False,0,[],0,0]
        if pokes.get_ability() == 'Meditate' and pokes.ch == pokes.hp:
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P,pokes.get_name() + " is", "meditating!")
            P.clock.tick(P.bat_spd)
            return [3,False,0,[],0,0]
        if pokes.get_ability() == 'Aerialate' and self.type == 'Normal':
            self.type = 'Flying'
            self.boost *= 1.2
        if pokes.get_ability() == 'Pixilate' and self.type == 'Normal':
            self.type = 'Fairy'
            self.boost *= 1.2
        if pokes.get_ability() == 'Refrigerate' and self.type == 'Normal':
            self.type = 'Ice'
            self.boost *= 1.2
        if P.ion_deluge and self.type == 'Normal':
            self.type  = 'Electric'
            self.boost *= 1.2
        if pokes.get_ability() == 'Normalize':
            self.type = 'Normal'
            self.boost *= 1.2
        pp_amount = 1
        if pokee.get_ability() == 'Pressure':
            pp_amount = 2
        if mvnum == 0:
            pokes.p1 = max(0,pokes.p1-pp_amount)
            if pokes.last_resort[0] == 0 and self.name !='Last Resort':
                pokes.last_resort[0] = 1
        elif mvnum == 1:
            pokes.p2 = max(0,pokes.p2-pp_amount)
            if pokes.last_resort[1] == 0 and self.name !='Last Resort':
                pokes.last_resort[1] = 1
        elif mvnum == 2:
            pokes.p3 = max(0,pokes.p3-pp_amount)
            if pokes.last_resort[2] == 0 and self.name !='Last Resort':
                pokes.last_resort[2] = 1
        elif mvnum == 3:
            pokes.p4 = max(0,pokes.p4-pp_amount)
            if pokes.last_resort[3] == 0 and self.name !='Last Resort':
                pokes.last_resort[3] = 1
        move = 0
        if pokes.inf and random.random() <= 0.5:
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P,pokes.get_name() + " is","immobilized by love!")
            P.clock.tick(P.bat_spd)
            move = 1
            poke_func.cancelled(pokes)
        if pokes.status == 'Par':
            if random.random() <= 0.25:
                poke_func.new_battle_txt(P)
                poke_func.battle_write(P,pokes.get_name() + " is","paralyzed! It can't move!")
                P.clock.tick(P.bat_spd)
                pokes.bide = [0,0]
                move = 1
                poke_func.cancelled(pokes)
        elif pokes.status == 'Frz':
            if random.random() <= 0.2:
                pokes.status = None
                poke_func.new_battle_txt(P)
                poke_func.battle_write(P,pokes.get_name() + " thawed", "out!")
                P.clock.tick(P.bat_spd)
            else:
                poke_func.new_battle_txt(P)
                poke_func.battle_write(P,pokes.get_name() + " is frozen", "solid!")
                P.clock.tick(P.bat_spd)
                pokes.bide = [0,0]
                move = 1
        elif pokes.status == 'Slp':
            if pokes.slptim == 0:
                pokes.status = None
                poke_func.new_battle_txt(P)
                poke_func.battle_write(P,pokes.get_name() + " woke up!")
                P.clock.tick(P.bat_spd)
            else:
                pokes.slptim -= 1
                poke_func.new_battle_txt(P)
                poke_func.battle_write(P,pokes.get_name() + " is fast", "asleep!")
                P.clock.tick(P.bat_spd)
                pokes.bide = [0,0]
                if self.name != 'Snore':
                    move = 1
        if pokes.flinch == True:
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P,pokes.get_name() + " flinched!")
            if pokes.get_ability() == 'Steadfast':
                if pokes.spdm < 6:
                    pokes.spdm += 1
                    poke_func.show_ability(P,'Steadfast',abs(1-eturn))
            P.clock.tick(P.bat_spd)
            pokes.bide = [0,0]
            move = 1
        if pokes.cfs > 0 and move == 0:
            pokes.cfs -= 1
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P,pokes.get_name() + " is", "confused!")
            P.clock.tick(P.bat_spd)
            if pokes.cfs == 0:
                poke_func.new_battle_txt(P)
                poke_func.battle_write(P,pokes.get_name() + " snapped", "out of confusion!")
                P.clock.tick(P.bat_spd)
            elif random.random() <= 0.33:
                poke_func.new_battle_txt(P)
                poke_func.battle_write(P,pokes.get_name() + " hurt", "itself in it's confusion!")
                P.clock.tick(P.bat_spd)
                pokes.bide = [0,0]
                eff = self.hurt_cfs(P,pokes,pokee)
                return eff
        if self.priority > 0 and pokee.get_ability() == 'Queenly Majesty':
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P,pokes.get_name() + " cannot", "use " + self.name + '!')
            P.clock.tick(P.bat_spd)
            move = 1
        if move == 0:
            if self.sec == '3' and pokes.charge == None and not (P.battle_weather != None and P.battle_weather[0] == 'Sunny' and self.name in ['Solar Beam','Solar Blade']):
                pokes.charge = self.name
                poke_func.new_battle_txt(P)
                if self.name == 'Razor Wind':
                    poke_func.battle_write(P,f'{pokes.get_name()} whipped up','a whirlwind!')
                elif self.name == 'Solar Blade' or self.name == 'Solar Beam':
                    poke_func.battle_write(P,f'{pokes.get_name()} took in','sunlight!')
                elif self.name == 'Sky Attack':
                    poke_func.battle_write(P,f'{pokes.get_name()} became','cloaked in a harsh light!')
                elif self.name == 'Skull Bash':
                    poke_func.battle_write(P,f'{pokes.get_name()} tucked in', 'its head!')
                    P.clock.tick(P.bat_spd)
                    self = Move("Withdraw")
                    eff = self.use(P,pokes,pokee,eturn)
                    return eff
                else:
                    poke_func.battle_write(P,"I'm missing a description!")
                P.clock.tick(P.bat_spd)
            elif self.name == 'Bide':
                if pokee.status == 'Faint':
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P, "But there was no target...")
                    P.clock.tick(P.bat_spd)
                elif pokes.bide[0] == 0:
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,pokes.get_name() + " used", self.name + "!")
                    P.clock.tick(P.bat_spd)
                    pokes.bide[0] += 1
                elif pokes.bide[0] == 1:
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,pokes.get_name() + " is storing", "energy!")
                    P.clock.tick(P.bat_spd)
                    pokes.bide[0] += 1
                elif pokes.bide[0] == 2:
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,pokes.get_name() + " unleashed", "energy!")
                    P.clock.tick(P.bat_spd)
                    if pokes.bide[1] == 0:
                        print_fail(P)
                    elif 'Ghost' in pokee.type and pokee.idf == False:
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,f'It doesn\'t affect',pokee.get_name(True) +'!')
                        P.clock.tick(P.bat_spd)
                    elif pokee.protect:
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,pokee.get_name() + " is", "protecting itself!")
                        P.clock.tick(P.bat_spd)
                    else:
                        eff = self.use_bide(P,pokes,pokee,eturn)
                    pokes.bide = [0,0]
            else:
                if self.name == 'Focus Punch' and pokes.damage_taken != 0:
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,pokes.get_name() + " lost its", "focus and couldn't move!")
                    P.clock.tick(P.bat_spd)
                else:
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,pokes.get_name() + " used", self.name + "!")
                    P.clock.tick(P.bat_spd)
                if self.name == 'Nature Power':
                    change = 'Tri Attack'
                    if poke_func.in_terrain(P,'Electric'):
                        change = 'Thunderbolt'
                    elif poke_func.in_terrain(P,'Misty'):
                        change = 'Moonblast'
                    elif P.habitat == 'cave':
                        change = 'Power Gem'
                    elif P.habitat in ['beach','path','mount']:
                        change = 'Earth Power'
                    elif P.habitat in ['grass','forest','mount_grass']:
                        change = 'Energy Ball'
                    self = Move(change)
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,"Nature Power turned into",self.name+"!")
                    P.clock.tick(P.bat_spd)
                if self.name == 'Metronome':
                    move_list = []
                    for file in os.listdir("moves"):
                        if file.endswith(".txt") and file.startswith("OUTLINE") == False and file.startswith("Metronome") == False:
                            move_list.append(file[:-4])
                    new_move = move_list[random.randint(0,len(move_list))]
                    self = Move(new_move)
                    P.metronome = new_move
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,pokes.get_name() + " used", self.name + "!")
                    P.clock.tick(P.bat_spd)
                if self.name == 'Chip Away':
                    teva = pokee.evam
                    pokee.evam = 0
                if pokee.item == 'Lax Incense':
                    self.acc = float(self.acc) - 0.1
                    if self.acc < 0:
                        self.acc = 0
                if pokee.idf == True and pokee.evam <= 0:
                    acc = float(self.acc)*self.acc_mod(pokes.accm)
                elif pokes.get_ability() == 'Keen Eye' and pokee.evam <= 0:
                    acc = float(self.acc)*self.acc_mod(pokes.accm)
                else:
                    acc = float(self.acc)*self.acc_mod(pokes.accm)*self.acc_mod(pokee.evam)
                if self.name == 'Chip Away':
                    pokee.evam = teva
                if self.name in ['Protect','Spiky Shield','Baneful Bunker','Endure','Detect']:
                    acc = float(0.3**pokes.procount)
                    pokes.procount += 1
                else:
                    pokes.procount = 0
                if self.sec == '4':
                    acc = (pokes.lvl-pokee.lvl+30)/100
                if self.name in ['Heavy Slam','Stomp','Steamroller','Body Slam','Glacial Press'] and pokee.minimize:
                    acc = 100
                if pokes.get_ability() == 'Compound Eyes':
                    acc *= 1.3
                if pokee.get_ability() == 'Tangled Feet' and pokee.cfs > 0:
                    acc *= 0.5
                if pokes.get_ability() == 'Hustle' and self.cat == '0':
                    acc *= 0.8
                if P.battle_weather != None and P.battle_weather[0] == 'Hail' and pokee.ability == 'Snow Cloak':
                    acc *= 0.8
                #weather
                if P.battle_weather != None and P.battle_weather[0] == 'Rain':
                    if self.name == 'Thunder' or self.name == 'Hurricane':
                        acc = 100
                if P.battle_weather != None and P.battle_weather[0] == 'Sunny':
                    if self.name == 'Thunder' or self.name == 'Hurricane':
                        acc = 0.5
                if P.battle_weather != None and P.battle_weather[0] == 'Hail' and self.name == 'Blizzard':
                    acc = 100
                pokestar_acc = 1
                if P.pokestar_battle != 0 and pokes.player:
                    pokestar_acc = 1+(P.pokestar_skills[1]/250)
                random_variable = 0
                if self.cat == '2':
                    for e in self.eff:
                        if ('BPs' in self.eff[e] or 'Frz' in self.eff[e] or 'Brn' in self.eff[e] or 'Psn' in self.eff[e] or 'Slp' in self.eff[e] or 'Par' in self.eff[e]) and pokee.status != None:
                            print_fail(P)
                            random_variable = 1
                        elif (('BPs' in self.eff[e] or 'Psn' in self.eff[e]) and not pokee.can_status(P,'Psn')) or ('Frz' in self.eff[e] and not pokee.can_status(P,'Frz')) or ('Brn' in self.eff[e] and not pokee.can_status(P,'Brn')) or ('Par' in self.eff[e] and not pokee.can_status(P,'Par')) or ('Slp' in self.eff[e] and not pokee.can_status(P,'Slp')):
                            poke_func.new_battle_txt(P)
                            if ('Slp' in self.eff[e] and poke_func.in_terrain(P,'Electric',pokee)):
                                poke_func.battle_write(P,pokee.get_name() + " can't fall","asleep!")
                                P.clock.tick(P.bat_spd)
                            elif poke_func.in_terrain(P,'Misty',pokee):
                                poke_func.battle_write(P,pokee.get_name() + " surrounds","itself with a protective mist!")
                                P.clock.tick(P.bat_spd)
                            else:
                                poke_func.battle_write(P,f'It doesn\'t affect',pokee.get_name(True) +'!')
                                if ('BPs' in self.eff[e] or 'Psn' in self.eff[e]) and pokee.get_ability() == 'Immunity':
                                    poke_func.show_ability(P,'Immunity',eturn)
                                elif ('Slp' in self.eff[e]) and pokee.get_ability() == 'Insomnia':
                                    poke_func.show_ability(P,'Insomnia',eturn)
                                else:
                                    P.clock.tick(P.bat_spd)
                            random_variable = 2
                if pokee.status == 'Faint' and not (self.cat == '2' and self.tar == '0'):
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P, "But there was no target...")
                    P.clock.tick(P.bat_spd)
                elif random_variable != 0:
                    pass
                elif self.name == 'Captivate' and (pokes.gen == pokee.gen or pokee.get_ability() == 'Oblivious' or pokes.gen == 2 or pokee.gen == 2):
                    poke_func.new_battle_txt(P)
                    if pokee.get_ability() == 'Oblivious':
                        poke_func.battle_write(P,f'It doesn\'t affect',pokee.get_name(True) +'!')
                        poke_func.show_ability(P,'Oblivious',eturn)
                    else:
                        poke_func.battle_write(P,"But it failed!")
                    P.clock.tick(P.bat_spd)
                elif pokee.get_ability() == 'Dodge' and self.cat != '2':
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,pokee.get_name() + " nimbly","dodged your attack!")
                    P.clock.tick(P.bat_spd)
                elif pokee.get_ability() == 'Ranged' and self.is_contact():
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,pokee.get_name() + " is out of","range!")
                    P.clock.tick(P.bat_spd)
                elif pokee.get_ability() == 'Endless Hunger' and self.cat == '1' and random.random() < 0.33:
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,pokee.get_name() + " swallowed","the attack!")
                    poke_func.show_ability(P,'Endless Hunger',eturn)
                    P.clock.tick(P.bat_spd)
                elif self.name == 'Future Sight':
                    if eturn == 0 and P.future_sight[0] > 0:
                        print_fail(P)
                    elif eturn == 1  and P.future_sight[1] > 0:
                        print_fail(P)
                    elif random.random() <= acc*pokestar_acc or pokes.get_ability() == 'No Guard' or pokee.get_ability() == 'No Guard':
                        if P.pokestar_battle != 0 and acc < 1:
                            P.pokestar_gain(P,1,(1-acc)*20)
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,pokes.get_name() + " foresaw an","attack!")
                        P.clock.tick(P.bat_spd)
                        P.future_sight[eturn] = 3
                    else:
                        print_fail(P)
                elif self.name == 'Spikes' and ((eturn == 1 and P.self_traps[0] == 3) or (eturn == 0 and P.enemy_traps[0] == 3)):
                    print_fail(P)
                elif self.name == 'Toxic Spikes' and ((eturn == 1 and P.self_traps[1] == 2) or (eturn == 0 and P.enemy_traps[1] == 2)):
                    print_fail(P)
                elif self.name == 'Stealth Rock' and ((eturn == 1 and P.self_traps[2] == 1) or (eturn == 0 and P.enemy_traps[2] == 1)):
                    print_fail(P)
                elif self.name == 'Sticky Web' and ((eturn == 1 and P.self_traps[3] == 1) or (eturn == 0 and P.enemy_traps[3] == 1)):
                    print_fail(P)
                elif self.name == 'Last Resort' and sum(pokes.last_resort) < pokes.known_moves()-1:
                    print_fail(P)
                elif self.name == 'Snore' and pokes.status != 'Slp':
                    print_fail(P)
                elif (self.name == 'Metal Burst' and pokes.damage_taken == 0) or (self.name == 'Counter' and (pokes.type_hit != '0' or pokes.damage_taken == 0)) or (self.name == 'Mirror Coat' and (pokes.type_hit != '1' or pokes.damage_taken == 0)):
                    print_fail(P)
                elif (self.name == 'Sucker Punch' and pokee.can_sucker == False):
                    print_fail(P)
                elif self.name == 'Rain Dance' and P.battle_weather != None and P.battle_weather[0] in ['Rain','Windy']:
                    if P.battle_weather[0] == 'Windy':
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,"The mysterious strong winds", "blow on regardless!")
                        P.clock.tick(P.bat_spd)
                    else:
                        print_fail(P)
                elif self.name == 'Sunny Day' and P.battle_weather != None and P.battle_weather[0] in ['Sunny','Windy']:
                    if P.battle_weather[0] == 'Windy':
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,"The mysterious strong winds", "blow on regardless!")
                        P.clock.tick(P.bat_spd)
                    else:
                        print_fail(P)
                elif self.name == 'Hail' and P.battle_weather != None and P.battle_weather[0] in ['Hail','Windy']:
                    if P.battle_weather[0] == 'Windy':
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,"The mysterious strong winds", "blow on regardless!")
                        P.clock.tick(P.bat_spd)
                    else:
                        print_fail(P)
                elif self.name == 'Tailwind' and ((eturn == 1 and P.enemy_buffs[0] > 0) or (eturn == 0 and P.player_buffs[0] > 0)):
                    print_fail(P)
                elif self.name == 'Light Screen' and ((eturn == 1 and P.enemy_buffs[1] > 0) or (eturn == 0 and P.player_buffs[1] > 0)):
                    print_fail(P)
                elif self.name == 'Reflect' and ((eturn == 1 and P.enemy_buffs[2] > 0) or (eturn == 0 and P.player_buffs[2] > 0)):
                    print_fail(P)
                elif self.name == 'Electric Terrain' and poke_func.in_terrain(P,"Electric"):
                    print_fail(P)
                elif self.name == 'Misty Terrain' and poke_func.in_terrain(P,"Misty"):
                    print_fail(P)
                elif self.name == 'Magnet Rise' and pokes.magnet_rise > 0:
                    print_fail(P)
                elif self.name == 'Stockpile' and pokes.stockpile[0] == 3:
                    print_fail(P)
                elif self.name == 'Focus Punch' and pokes.damage_taken != 0:
                    pass
                elif self.name in ['Spit Up','Swallow'] and pokes.stockpile[0] == 0:
                    print_fail(P)
                elif self.name == 'Rest' and (pokes.get_ability() == 'Insomnia' or pokes.ch == pokes.hp or poke_func.in_terrain(P,'Electric',pokes) or poke_func.in_terrain(P,'Misty',pokes)):
                    print_fail(P)
                elif self.name in ['Swallow','Recover','Roost','Synthesis','Soft-Boiled','Rejuvenate','Heal Pulse','Moonlight'] and pokes.ch == pokes.hp:
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,pokes.get_name()+"'s HP is","full!")
                    P.clock.tick(P.bat_spd)
                elif self.name in ['Dream Eater','Nightmare'] and pokee.status != 'Slp':
                    print_fail(P)
                elif self.name == 'Nightmare' and pokee.nightmare:
                    print_fail(P)
                elif self.name == 'Curse' and 'Ghost' in pokes.type and pokee.curse:
                    print_fail(P)
                elif self.name == 'Belly Drum' and (pokes.ch/pokes.hp <= 0.5 or pokes.akm == 6):
                    print_fail(P)
                elif self.name == 'Taunt' and pokee.taunt > 0:
                    print_fail(P)
                elif self.name == 'Teleport' and (P.legendary_battle or len(P.opponent) > 1 or ((pokee.get_ability() == 'Shadow Tag' and pokes.get_ability() != 'Shadow Tag' and 'Ghost' not in pokes.type) or (pokee.get_ability() == 'Arena Trap' and pokes.get_ability() != 'Levitate' and pokes.magnet_rise == 0 and 'Flying' not in pokes.type) or (pokee.get_ability() == 'Magnet Pull' and 'Steel' in pokes.type) or (pokes.trapped[1] != 0)) and (pokes.get_ability() != 'Run Away' or 'Ghost' in pokes.type)):
                    print_fail(P)
                elif self.name in ['Roar','Whirlwind'] and (type(P.opponent[0]) != str and pokes.player):
                    print_fail(P)
                elif self.cat == '2' and pokes.taunt > 0:
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,pokes.get_name() + " can't use",self.name+" due to taunt!")
                    pokes.taunt -= 1
                    P.clock.tick(P.bat_spd)
                elif self.name in ['Fake Out','First Impression'] and pokes.turn_count > 0:
                    print_fail(P)
                elif (self.name == 'Self-Destruct' or self.name == 'Explosion') and (pokes.get_ability() == 'Damp' or pokee.get_ability() == 'Damp'):
                    print_fail(P)
                    if pokes.get_ability() == 'Damp':
                        poke_func.show_ability(P,'Damp',1)
                    else:
                        poke_func.show_ability(P,'Damp',0)
                elif self.name == 'Endeavor' and pokes.ch >= pokee.ch:
                    print_fail(P)
                elif self.name == 'Yawn' and (pokee.status != None or pokee.yawn != 0 or poke_func.in_terrain(P,'Electric',pokee)):
                    print_fail(P)
                elif self.name == 'Taunt' and pokee.taunt != 0:
                    print_fail(P)
                elif self.name == 'Taunt' and pokee.get_ability() == 'Oblivious':
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,f'It doesn\'t affect',pokee.get_name(True) +'!')
                    poke_func.show_ability(P,'Oblivious',eturn)
                elif self.name == 'Attract' and (pokee.inf == True or pokes.gen == pokee.gen or pokes.gen == 2 or pokee.gen == 2):
                    print_fail(P)
                elif self.name == 'Leech Seed' and (pokee.leech == True or 'Grass' in pokee.type):
                    print_fail(P)
                elif self.name == 'Gastro Acid' and (pokee.gastro or pokee.ability in ['Meditate','Stun','Dodge','Ranged','Puppet','Multitype','Stance Change','Schooling','Comatose','Shields Down','Disguise','RKS System','Battle Bond','Power Construct']):
                    print_fail(P)
                elif self.name == 'Simple Beam' and (pokee.ability in ['Meditate','Stun','Dodge','Ranged','Puppet','Simple','Truant','Multitype','Stance Change','Schooling','Comatose','Shields Down','Disguise','RKS System','Battle Bond','Power Construct']):
                    print_fail(P)
                elif self.name == 'Worry Seed' and (pokee.ability in ['Meditate','Stun','Dodge','Ranged','Puppet','Insomnia','Truant','Multitype','Stance Change','Schooling','Comatose','Shields Down','Disguise','RKS System','Battle Bond','Power Construct']):
                    print_fail(P)
                elif self.name == 'Entrainment' and (pokee.ability == pokes.ability or pokee.ability in ['Meditate','Stun','Dodge','Ranged','Puppet','Truant','Multitype','Stance Change','Schooling','Comatose','Shields Down','Disguise','RKS System','Battle Bond'] or pokes.ability in ['Trace','Forecast','Flower Gift','Zen Mode','Illusion','Imposter','Power of Alchemy','Receiver','Disguise','Power Construct','Neutralizing Gas']):
                    print_fail(P)
                elif self.name == 'Role Play' and (pokee.ability == pokes.ability or pokee.ability in ['Meditate','Stun','Dodge','Ranged','Puppet','Trace','Wonder Guard','Forecast','Flower Gift','Multitype','Illusion','Zen Mode','Imposter','Stance Change','Power of Alchemy','Receiver','Schooling','Comatose','Shields Down','Power Construct','Disguise','RKS System','Battle Bond'] or pokes.ability in ['Multitype','Stance Change','Schooling','Zen Mode','Comatose','Shields Down','RKS System','Power Construct','Disguise','Battle Bond']):
                    print_fail(P)
                elif self.name == 'Skill Swap' and (pokee.ability in ['Meditate','Stun','Dodge','Ranged','Puppet','Wonder Guard','Multitype','Illusion','Stance Change','Schooling','Comatose','Shields Down','Disguise','RKS System','Battle Bond','Power Construct','Neutralizing Gas'] or pokes.ability in ['Meditate','Stun','Dodge','Ranged','Puppet','Wonder Guard','Multitype','Illusion','Stance Change','Schooling','Comatose','Shields Down','Disguise','RKS System','Battle Bond','Power Construct','Neutralizing Gas']):
                    print_fail(P)
                elif (pokee.status != 'Psn' or pokee.status != 'BPs') and self.name == 'Venom Drench':
                    print_fail(P)
                #special status moves
                elif (self.name == 'Poison Powder' or self.name == 'Stun Spore' or self.name == 'Sleep Powder' or self.name == 'Spore' or self.name == 'Powder' or self.name == 'Cotton Spore' or self.name == 'Magic Powder') and 'Grass' in pokee.type:
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,f'It doesn\'t affect',pokee.get_name(True) +'!')
                    P.clock.tick(P.bat_spd)
                elif random.random() <= acc*pokestar_acc or pokes.get_ability() == 'No Guard' or pokee.get_ability() == 'No Guard':
                    if P.pokestar_battle != 0 and acc < 1:
                        poke_func.pokestar_gain(P,1,(1-acc)*20)
                    fail = False
                    if self.name in ['Protect','Spiky Shield','Detect','Baneful Bunker']:
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,pokes.get_name() + " protected","itself!")
                        P.clock.tick(P.bat_spd)
                        if self.name == 'Protect' or self.name == 'Detect':
                            pokes.protect = True
                        elif self.name == 'Spiky Shield':
                            pokes.spikyshield[0] = True
                        elif self.name == 'Baneful Bunker':
                            pokes.spikyshield[1] = True
                    if self.name == 'Endure':
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,pokes.get_name() + " braced","itself!")
                        P.clock.tick(P.bat_spd)
                        pokes.endure = True
                    if self.name == 'Punishment':
                        sc = 60
                        if pokee.akm > 0:
                            sc += 20*pokee.akm
                        if pokee.sakm > 0:
                            sc += 20*pokee.sakm
                        if pokee.dfm > 0:
                            sc += 20*pokee.dfm
                        if pokee.sdfm > 0:
                            sc += 20*pokee.sdfm
                        if pokee.spdm > 0:
                            sc += 20*pokee.spdm
                        if pokee.critm > 0:
                            sc += 20*pokee.critm
                        if pokee.accm > 0:
                            sc += 20*pokee.accm
                        if pokee.evam > 0:
                            sc += 20*pokee.evam
                        self.pow = sc
                    if self.name == 'Water Spout':
                        self.pow = int(max(1,150*pokes.ch/pokes.hp))
                    if self.name == 'Wring Out':
                        self.pow = int(120*(pokee.ch/pokee.hp))
                    if self.name in ['Heavy Slam','Glacial Press']:
                        if pokee.weight/pokes.weight > 0.5:
                            self.pow = 40
                        elif pokee.weight/pokes.weight > 0.33:
                            self.pow = 60
                        elif pokee.weight/pokes.weight > 0.25:
                            self.pow = 80
                        elif pokee.weight/pokes.weight > 0.2:
                            self.pow = 100
                        else:
                            self.pow = 120
                    if self.name == 'Spit Up':
                        self.pow = 100*pokes.stockpile[0]
                    if self.name in ['Low Kick','Grass Knot']:
                        if pokee.weight < 10:
                            self.pow = 20
                        elif pokee.weight < 25:
                            self.pow = 40
                        elif pokee.weight < 50:
                            self.pow = 60
                        elif pokee.weight < 100:
                            self.pow = 80
                        elif pokee.weight < 200:
                            self.pow = 100
                        else:
                            self.pow = 120
                    if self.name == 'Electro Ball':
                        if pokee.get_spd(P) >= pokes.get_spd(P):
                            self.pow = 40
                        elif pokee.get_spd(P)/pokes.get_spd(P) >= 0.5:
                            self.pow = 60
                        elif pokee.get_spd(P)/pokes.get_spd(P) >= 0.33:
                            self.pow = 80
                        elif pokee.get_spd(P)/pokes.get_spd(P) >= 0.25:
                            self.pow = 120
                        else:
                            self.pow = 150
                    if self.name == 'Power Trip':
                        if pokes.akm > 0:
                            self.pow += 20*pokes.akm
                        if pokes.sakm > 0:
                            self.pow += 20*pokes.sakm
                        if pokes.dfm > 0:
                            self.pow += 20*pokes.dfm
                        if pokes.sdfm > 0:
                            self.pow += 20*pokes.sdfm
                        if pokes.spdm > 0:
                            self.pow += 20*pokes.spdm
                        if pokes.accm > 0:
                            self.pow += 20*pokes.accm
                        if pokes.evam > 0:
                            self.pow += 20*pokes.evam
                    if self.name == 'Gyro Ball':
                        self.pow = int(min(150,(25*pokee.get_spd(P)/pokes.get_spd(P))+1))
                        if self.pow == 0:
                            self.pow = 1
                    if self.name == 'Echoed Voice':
                        self.pow = int(self.pow)+P.echoed[0]
                        P.echoed[1] = 2
                        if P.echoed[0] <= 160:
                            P.echoed[0] += 40
                    if self.name == 'Return':
                        self.pow = int(pokes.friend/4)
                    if self.name == 'Frustration':
                        self.pow = int((400 - pokes.friend)/3)
                    if self.name == 'Reversal':
                        perc = pokes.ch/pokes.hp
                        if perc >= .6875:
                            self.pow = 20
                        elif perc >= .3542:
                            self.pow = 40
                        elif perc >= .2083:
                            self.pow = 80
                        elif perc >= .1042:
                            self.pow = 100
                        elif perc >= .0417:
                            self.pow = 150
                        else:
                            self.pow = 200
                    if self.name == 'Flail':
                        pc = float(pokes.ch/pokes.hp)
                        if pc >= 0.6875:
                            self.pow = 20
                        elif pc >= .3542:
                            self.pow = 40
                        elif pc >= .2083:
                            self.pow = 80
                        elif pc >= .1042:
                            self.pow = 100
                        elif pc >= .0417:
                            self.pow = 150
                        else:
                            self.pow = 200
                    if self.name == 'Magnitude':
                        r = random.random()
                        if r <= 0.05:
                            self.pow = 10
                            num = 4
                        elif r <= 0.15:
                            self.pow = 30
                            num = 5
                        elif r <= 0.35:
                            self.pow = 50
                            num = 6
                        elif r <= 0.65:
                            self.pow = 70
                            num = 7
                        elif r <= 0.85:
                            self.pow = 90
                            num = 8
                        elif r <= 0.95:
                            self.pow = 110
                            num = 9
                        else:
                            self.pow = 150
                            num = 10
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,"Magnitude "+str(num)+"!")
                        P.clock.tick(P.bat_spd)
                    if self.name == 'Aromatherapy' or self.name == 'Heal Bell':
                        fail = True
                        if eturn == 0:
                            for pk in P.party:
                                if pk.status != None and pk.status != 'Faint':
                                    fail = False
                        else:
                            if pokes.status != None:
                                fail = False
                    if self.cat != '2' and (self.pow == '---' or self.pow == '???'):
                        #self.name == 'Super Fang' or self.name == 'Night Shade' or self.sec == '4' or self.name == 'Endeavor' or self.name == 'Seismic Toss':
                        self.pow = 0
                    if self.cat == '2' and ((pokee.status != None and self.tar == '1') or (pokes.status != None and self.tar == '0')):
                        for x,y in self.eff.items():
                            if x == 1 and (y == ['Brn'] or y == ['Par'] or y == ['Slp'] or y == ['Frz'] or y == ['Psn'] or y == ['Bps']):
                                fail = True
                    if self.name == 'Synchronoise':
                        fail = True
                        for typ in pokes.type:
                            if typ != None and typ in pokee.type:
                                fail = False
                    if pokee.protect and self.tar == '1':
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,pokee.get_name() + " is", "protecting itself!")
                        P.clock.tick(P.bat_spd)
                        if pokes.cont_move[0] != None and pokes.cont_move[0] != "Uproar":
                            pokes.cont_move = [None,0]
                    elif (self.name == 'Teeter Dance' or self.name == 'Confuse Ray' or self.name == 'Supersonic' or self.name == 'Sweet Kiss') and pokee.cfs > 0:
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,pokee.get_name() + " is already","confused!")
                        P.clock.tick(P.bat_spd)
                    elif (pokee.spikyshield[0] or pokee.spikyshield[1]) and self.tar == '1':
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,pokee.get_name() + " is", "protecting itself!")
                        P.clock.tick(P.bat_spd)
                        if pokes.cont_move[0] != None and pokes.cont_move[0] != "Uproar":
                            pokes.cont_move = [None,0]
                        mes = []
                        if self.is_contact():
                            if pokee.spikyshield[0]:
                                rec = int(pokes.hp/8)
                                if pokes.ch - rec < 0:
                                    rec = pokes.ch
                                mes.append([6,rec,pokes.get_name()])
                            elif pokee.spikyshield[1] and pokes.can_status(P,'Psn'):
                                pokes.status = 'Psn'
                                #mes.append([7,rec,pokes.get_name()]):
                        return [3,False,0,mes,0,0]
                    elif fail:
                        print_fail(P)
                    else:
                        eff = self.use(P,pokes,pokee,eturn)
                        return eff
                else:
                    poke_func.new_battle_txt(P)
                    if self.name in ['Protect','Spiky Shield','Endure','Detect','Baneful Bunker']:
                        poke_func.battle_write(P,'But it failed!')
                    else:
                        poke_func.cancelled(pokes)
                        poke_func.battle_write(P,pokes.get_name() + "'s attack", "missed!")
                    pokes.procount = 0
                    P.clock.tick(P.bat_spd)
                    if self.name in ['High Jump Kick','Jump Kick']:
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,f'{pokes.get_name()} kept going', 'and crashed!')
                        P.clock.tick(P.bat_spd)
                        if pokes.ch > int(pokes.hp/2):
                            pokes.take_damage(P,int(pokes.hp/2))
            if self.name in ['Explosion','Self-Destruct']:
                pokes.explode = True
                return [3,False,pokes.ch,[],0,0]
        return [3,False,0,[],0,0]

    def use(self,P,pokes,pokee,eturn,blit_p = None, blit_e = None) -> list:
        if blit_p == None:
            blit_p = pokes
        if blit_e == None:
            blit_e = pokee
        if pokes.child_hit:
            poke_func.show_ability(P, 'Parental Bond', abs(eturn-1))
        if self.name == 'Ion Deluge':
            P.ion_deluge = True
        pok = [pokes,pokee]
        if self.tar == '1':
            targ = 1
        else:
            targ = 0
        message = []
        if pokee.get_ability() == 'Magic Bounce' and targ == 1 and self.cat == '2':
            targ = 0
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P,pokee.get_name() +" bounced","the "+self.name+" back!")
            poke_func.show_ability(P,'Magic Bounce',eturn)
        elif pokee.magic_coat and targ == 1 and self.cat == '2':
            targ = 0
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P,self.name +" was bounced","back by Magic Coat!")
            P.clock.tick(P.bat_spd)
        if targ == 1:
            mod = self.effective(P,pok[targ],pokes,eturn)
            if self.name == 'Flying Press':
                flying_move = Move('Wing Attack')
                mod *= flying_move.effective(P,pok[targ],pokes,eturn)
        else:
            mod = 1
        eff = 3
        if targ == 1:
            pokee.type_hit = self.cat
            if mod == 0:
                if self.cat != '2':
                    eff = 0
                    if not ((self.type == 'Water' and pok[targ].get_ability() == 'Water Absorb') or (self.type == 'Electric' and pok[targ].get_ability() == 'Volt Absorb')):
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,"It doesn't affect ", pok[targ].get_name(True) + '!')
                        P.clock.tick(P.bat_spd)
                        if pok[targ].get_ability() == 'Soundproof' and self.in_soundproof():
                            poke_func.show_ability(P,'Soundproof',eturn)
                else:
                    mod = 1
            elif mod < 1:
                eff = 1
            elif mod > 1:
                eff = 2
            else:
                eff = 3
        if eff != 0:
            if P.gem_active or (pokes.item != None and items.Item(pokes.item).type[0] == 'Gem' and self.type == items.Item(pokes.item).mod() and self.pow != '---' and self.pow != '???' and int(self.pow) > 0):
                self.pow = int(self.pow) * 1.5
                if P.gem_active == False:
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,"The "+items.Item(pokes.item).name +" strengthened",self.name+"'s power!")
                    P.clock.tick(P.bat_spd)
                    pokes.item = None
                    P.gem_active = True
            if P.ani_on:
                self.animate(P,blit_p,blit_e,eturn)
        else:
            if pokes.cont_move[0] != None and pokes.cont_move[0] != "Uproar":
                pokes.cont_move = [None,0]
        if self.name == 'Beat Up':
            if pokes.beat_up == []:
                self.pow = (pokes.orig_stats[1]*5)+5
            else:
                self.pow = pokes.beat_up[0]+5
        if self.pow != '---' and self.pow != '???':
            power = int(self.pow)
            power *= self.boost
        else:
            power = 0
        if self.name == 'Fury Cutter':
            for x in range(pokes.fury_count):
                power *= 2
        if self.name == 'Hex' and pok[targ].status != None:
            power *= 2
        if self.name == 'Brine' and pok[targ].ch/pok[targ].hp < 0.5:
            power *= 2
        if self.name in ['Revenge','Avalanche'] and pokes.damage_taken > 0:
            power *= 2
        if self.type == 'Electric' and pokes.chrg == 2:
            power *= 2
        if self.type == 'Facade' and pokes.status != None:
            power *= 2
        if self.name == 'Wake-Up Slap' and pok[targ].status == 'Slp':
            power *= 2
            pok[targ].slptim = 0
        if pokes.child_hit:
            power *= 0.25
        #weather
        if P.battle_weather != None and P.battle_weather[0] == 'Rain' and self.cat != '2':
            if self.type == 'Water':
                power *= 1.5
            if self.type == 'Fire':
                power *= 0.5
            if self.name == 'Solar Blade' or self.name == 'Solar Beam':
                power *= 0.5
        if P.battle_weather != None and P.battle_weather[0] == 'Hail' and self.name in ['Solar Beam','Solar Blade']:
            power *= 0.5
        if P.battle_weather != None and P.battle_weather[0] == 'Sunny' and self.cat != '2':
            if self.type == 'Fire':
                power *= 1.5
            if self.type == 'Water':
                power *= 0.5
        if P.battle_weather != None and P.battle_weather[0] != 'Windy' and self.name == 'Weather Ball':
            power *= 2
            if P.battle_weather[0] == 'Rain':
                self.type = 'Water'
            elif P.battle_weather[0] == 'Hail':
                self.type = 'Ice'
            elif P.battle_weather[0] == 'Sunny':
                self.type = 'Fire'
            else:
                self.type = 'Rock'
        #terrain
        if poke_func.in_terrain(P,'Electric',pokes) and self.type == 'Electric' and self.cat != '2':
            power *= 1.5
        sheer = False
        if self.cat != '2' and self.eff != [] and pokes.get_ability() == 'Sheer Force':
            sheer = True
            for x in self.eff:
                if x < 0 and (('AD' in self.eff[x]) or ('DD' in self.eff[x]) or ('SDD' in self.eff[x]) or ('SAD' in self.eff[x]) or ('SD' in self.eff[x]) or ('AcD' in self.eff[x]) or ('EvD' in self.eff[x])):
                    sheer = False
        if sheer:
            power *= 1.3
        if self.name == 'Acrobatics' and pokes.item == None:
            power *= 2
        if self.name == 'Defense Curl':
            pokes.dc = True
        if (self.name == 'Bug Bite' or self.name == 'Pluck') and pok[targ].get_ability() != 'Sticky Hold':
            pok[targ].bugbite = True
        if self.name == 'Magnet Rise':
            pokes.magnet_rise = 5
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, pokes.get_name() + " levitated", "with electromagnetism!")
            P.clock.tick(P.bat_spd)
        if self.name == 'Uproar' and pokes.cont_move == [None,0]:
            pokes.cont_move = ['Uproar',3]
            message.append([7,pokes.get_name()+" caused an","uproar!"])
        if self.sec == '6':
            if pokes.cont_move == [None,0]:
                pokes.cont_move = [self.name,random.randint(2,3)]
            elif pokes.cont_move[1] == 1:
                if pokes.cfs == 0:
                    if poke_func.in_terrain(P,'Misty',pokes):
                        message.append([7,pokes.get_name()+" surrounds","itself with a protective mist!"])
                    if pokes.get_ability() == 'Own Tempo':
                        message.append([2,[pokes.get_name()+" can't be","confused!"],'Own Tempo',eturn])
                    else:
                        pokes.cfs = random.randint(2,5)
        if self.name == 'Fury Cutter':
            if pokes.fury_count < 2:
                pokes.fury_count += 1
        else:
            pokes.fury_count = 0
        if self.name == 'Magic Coat':
            pokes.magic_coat = True
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, pokes.get_name() + " shrouded", "itself with Magic Coat!")
            P.clock.tick(P.bat_spd)
        if self.name == 'Nightmare':
            pok[targ].nightmare = True
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, pok[targ].get_name() + " began", "having a nightmare!")
            P.clock.tick(P.bat_spd)
        if self.name == 'Curse' and 'Ghost' in pokes.type:
            pokee.curse = True
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, pokes.get_name() + " cut its HP", "to curse "+pokee.get_name(True)+"!")
            P.clock.tick(P.bat_spd)
        if self.name == 'Toxic Spikes':
            poke_func.new_battle_txt(P)
            if eturn == targ and P.self_traps[1] < 2:
                poke_func.battle_write(P,"Poison spikes were scattered", "all around your team!")
                P.self_traps[1] += 1
            elif P.enemy_traps[1] < 2:
                poke_func.battle_write(P,"Poison spikes were scattered", "all around the opposing team!")
                P.enemy_traps[1] += 1
            else:
                print_fail(P)
            P.clock.tick(P.bat_spd)
        if self.name == 'Spikes':
            poke_func.new_battle_txt(P)
            if eturn == targ and P.self_traps[0] < 3:
                poke_func.battle_write(P,"Spikes were scattered all", "around your team!")
                P.self_traps[0] += 1
            elif P.enemy_traps[0] < 3:
                poke_func.battle_write(P,"Spikes were scattered all", "around the opposing team!")
                P.enemy_traps[0] += 1
            else:
                print_fail(P)
            P.clock.tick(P.bat_spd)
        if self.name == 'Stealth Rock':
            poke_func.new_battle_txt(P)
            if eturn == targ and P.self_traps[2] == 0:
                poke_func.battle_write(P,"Pointed stones float in the", "air around your team!")
                P.self_traps[2] += 1
            elif P.enemy_traps[2] == 0:
                poke_func.battle_write(P,"Pointed stones float in the", "air around the opposing team!")
                P.enemy_traps[2] += 1
            else:
                print_fail(P)
            P.clock.tick(P.bat_spd)
        if self.name == 'Sticky Web':
            poke_func.new_battle_txt(P)
            if eturn == targ and P.self_traps[3] == 0:
                poke_func.battle_write(P,"A sticky web has been laid out", "around your team!")
                P.self_traps[3] += 1
            elif P.enemy_traps[3] == 0:
                poke_func.battle_write(P,"A sticky web has been laid out", "around the opposing team!")
                P.enemy_traps[3] += 1
            else:
                print_fail(P)
            P.clock.tick(P.bat_spd)
        if self.name == 'Stockpile':
            pokes.stockpile[0] += 1
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, pokes.get_name(), "stockpiled "+str(pokes.stockpile[0])+"!")
            P.clock.tick(P.bat_spd)
        if self.name == 'Taunt':
            pok[targ].taunt = 4
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, pok[targ].get_name() + " fell for", "the taunt!")
            P.clock.tick(P.bat_spd)
        if self.name == 'Electric Terrain':
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, "An electric current ran across", "the battlefield!")
            P.clock.tick(P.bat_spd)
            P.battle_terrain = ['Electric',6,poke_func.load("p/terrain/Electric_Terrain.png")]
        if self.name == 'Misty Terrain':
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, "Mist swirled around the battlefield!")
            P.clock.tick(P.bat_spd)
            P.battle_terrain = ['Misty',6,poke_func.load("p/terrain/Misty_Terrain.png")]
        if self.name == 'Gastro Acid':
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, pok[targ].get_name() + "'s ability", "was suppressed!")
            P.clock.tick(P.bat_spd)
            pokee.set_ability("")
        if self.name == 'Simple Beam':
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, pokee.get_name() + " acquired", "Simple!")
            P.clock.tick(P.bat_spd)
            pokee.set_ability("Simple")
            poke_func.show_ability(P, "Simple", eturn)
        if self.name == 'Worry Seed':
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, pokee.get_name() + " acquired", "Insomnia!")
            P.clock.tick(P.bat_spd)
            pokee.set_ability("Insomnia")
            poke_func.show_ability(P, "Insomnia", eturn)
            if pokee.status == 'Slp':
                pokee.status = None
                poke_func.new_battle_txt(P)
                poke_func.battle_write(P,pokee.get_name() + " woke up!")
                P.clock.tick(P.bat_spd)
        if self.name == 'Entrainment':
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, pokee.get_name() + " acquired", pokes.ability+"!")
            P.clock.tick(P.bat_spd)
            pokee.set_ability(pokes.ability)
            poke_func.show_ability(P, pokes.ability, eturn)
            poke_func.start_abilities(P,pokee,pokes,eturn,False)
        if self.name == 'Role Play':
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, pokes.get_name() + " acquired", pokee.ability+"!")
            P.clock.tick(P.bat_spd)
            pokes.set_ability(pokee.ability)
            poke_func.show_ability(P, pokee.ability, abs(eturn-1))
            poke_func.start_abilities(P,pokes,pokee, abs(eturn-1),False)
        if self.name == 'Skill Swap':
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, pokes.get_name() + " swapped", "abilities with its target!")
            P.clock.tick(P.bat_spd)
            temp_ability = pokee.ability
            pokee.set_ability(pokes.ability)
            pokes.set_ability(temp_ability)
            poke_func.show_ability(P, pokee.ability, eturn)
            poke_func.show_ability(P, pokes.ability, abs(eturn-1))
            poke_func.start_abilities(P,pokee,pokes, eturn,False)
            poke_func.start_abilities(P,pokes,pokee, abs(eturn-1),False)
        if self.name == 'Tailwind':
            poke_func.new_battle_txt(P)
            if eturn == 1:
                poke_func.battle_write(P, "The tailwind blew from behind", "the opposing team!")
                P.enemy_buffs[0] = 4
            else:
                poke_func.battle_write(P, "The tailwind blew from behind", "your team!")
                P.player_buffs[0] = 4
            P.clock.tick(P.bat_spd)
        if self.name == 'Light Screen':
            poke_func.new_battle_txt(P)
            if eturn == 1:
                poke_func.battle_write(P, "Light Screen raised the other", "team's Special Defense!")
                P.enemy_buffs[1] = 5
            else:
                poke_func.battle_write(P, "Light Screen raised your", "team's Special Defense!")
                P.player_buffs[1] = 5
            P.clock.tick(P.bat_spd)
        if self.name == 'Brick Break':
            if eturn == 0 and (P.enemy_buffs[1] > 0 or P.enemy_buffs[2] > 0):
                poke_func.new_battle_txt(P)
                poke_func.battle_write(P,"It shattered the barrier!")
                P.clock.tick(P.bat_spd)
                P.enemy_buffs[1] = 0
                P.enemy_buffs[2] = 0
            elif eturn == 1 and (P.player_buffs[1] > 0 or P.player_buffs[2] > 0):
                poke_func.new_battle_txt(P)
                poke_func.battle_write(P,"It shattered the barrier!")
                P.clock.tick(P.bat_spd)
                P.player_buffs[1] = 0
                P.player_buffs[2] = 0
        if self.name == 'Reflect':
            poke_func.new_battle_txt(P)
            if eturn == 1:
                poke_func.battle_write(P, "Reflect raised the opposing", "team's Defense!")
                P.enemy_buffs[2] = 5
            else:
                poke_func.battle_write(P, "Reflect raised your team's", "Defense!")
                P.player_buffs[2] = 5
            P.clock.tick(P.bat_spd)
        if self.name == 'Rain Dance':
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, "It started to rain!")
            rain_temp = P.surface.copy()
            rain_val = 0
            if P.ani_on:
                for r in range(60):
                    P.surface.blit(rain_temp,(0,0))
                    poke_func.blit_rain(P,rain_val)
                    poke_func.update_screen(P)
                    P.clock.tick(P.ani_spd)
                    rain_val += 1
                    if rain_val == 40:
                        rain_val = -20
            else:
                P.clock.tick(P.bat_spd)
            if pokes.item == 'Damp Rock':
                P.battle_weather = ['Rain',9]
            else:
                P.battle_weather = ['Rain',6]
        if self.name == 'Hail':
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, "It started to hail!")
            hail_temp = P.surface.copy()
            hail_val = 0
            if P.ani_on:
                for r in range(60):
                    P.surface.blit(hail_temp,(0,0))
                    poke_func.blit_hail(P,hail_val)
                    poke_func.update_screen(P)
                    P.clock.tick(P.ani_spd)
                    hail_val += 1
                    if hail_val == 40:
                        hail_val = -20
            else:
                P.clock.tick(P.bat_spd)
            if pokes.item == 'Icy Rock':
                P.battle_weather = ['Hail',9]
            else:
                P.battle_weather = ['Hail',6]
        if self.name == 'Sunny Day':
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P, "The sunlight turned harsh!")
            sun_temp = P.surface.copy()
            sun_val = 0
            if P.ani_on:
                for r in range(60):
                    P.surface.blit(sun_temp,(0,0))
                    poke_func.blit_sun(P,sun_val)
                    poke_func.update_screen(P)
                    P.clock.tick(P.ani_spd)
                    sun_val += 1
            else:
                P.clock.tick(P.bat_spd)
            if pokes.item == 'Heat Rock':
                P.battle_weather = ['Sunny',9]
            else:
                P.battle_weather = ['Sunny',6]
        if self.name == 'Autotomize':
            pokes.weight -= 100
            if pokes.weight <= 0.1:
                pokes.weight = 0.1
        if self.name == 'Minimize':
            pokes.minimize = True
        crit = False
        critm = pokes.critm
        if (self.sec == '1' or self.name == 'Razor Wind' or self.name == 'Sky Attack') and critm < 4:
            critm += 1
        if pokes.item == 'Razor Claw':
            critm += 1
        if (pokes.get_ability() == 'Super Luck'):
            critm += 1
        if eff != 0 and (((self.name in ['Storm Throw','Frost Breath'] or (pokes.get_ability() == 'Merciless' and pok[targ].status in ['Psn','BPs'])) and pok[targ].get_ability() != 'Shell Armor' and pok[targ].get_ability() != 'Battle Armor') or (self.cat != '2' and random.random() <= self.crit_mod(critm) and self.name != 'Psywave' and pok[targ].get_ability() != 'Shell Armor' and self.name != 'Night Shade' and self.name != 'Super Fang' and self.name != 'Final Gambit' and self.name != 'Seismic Toss' and self.sec != '4')):
            crit = True
        if self.cat == '0':
            akm = poke_func.pokestar_mod(P,pokes.player,pokes.akm,modifier(pokes.akm))
            dfm = poke_func.pokestar_mod(P,pokee.player,pokee.dfm,modifier(pokee.dfm))
            if self.name == 'Chip Away':
                dfm = 1
            if self.name == 'Rollout':
                for x in range(pokes.rollcount):
                    power *= 2
                pokes.rollcount += 1
                if pokes.dc == True:
                    power *= 2
                if pokes.rollcount == 5:
                    pokes.rollcount = 0
            elif self.name == 'Ice Ball':
                if pokes.rollcount == 0:
                    pokes.rollcount = 6
                else:
                    for x in range(pokes.rollcount-5):
                        power *= 2
                    pokes.rollcount += 1
                if pokes.dc == True:
                    power *= 2
                if pokes.rollcount == 10:
                    pokes.rollcount = 0
            elif pokes.pursuit:
                power *= 2
            if crit == True:
                if akm < 1:
                    akm = 1
                if dfm > 1:
                    dfm = 1
            ak = pokes.ak
            if pokes.get_ability() == 'Guts' and pokes.status != None:
                ak *= 1.5
            if self.name == 'Foul Play':
                ak = pok[targ].ak
                if pok[targ].get_ability() == 'Guts' and pok[targ].status != None:
                    ak *= 1.5
            if pokes.get_ability() == 'Technician' and power <= 60:
                power *= 1.5
            if pokes.item in ['Splash Plate','Icicle Plate','Stone Plate','Hard Stone','Never-Melt Ice','Metal Coat','Miracle Seed','Mystic Water','Rose Incense','Odd Incense','Rock Incense','Sea Incense','Smoke Incense'] and self.type == items.Item(pokes.item).mod():
                power *= 1.2
            if pokes.get_ability() == 'Iron Fist' and self.name in ['Bullet Punch','Comet Punch','Dizzy Punch','Drain Punch','Dynamic Punch','Fire Punch','Focus Punch','Hammer Arm','Ice Hammer','Ice Punch','Mach Punch','Mega Punch','Meteor Mash','Plasma Fists','Power-Up Punch','Shadow Punch','Sky Uppercut','Thunder Punch']:
                power *= 1.2
            if pokes.get_ability() == 'Reckless' and self.name in ['Brave Bird','Double-Edge','Flare Blitz','Head Charge','Head Smash','High Jump Kick','Jump Kick','Light of Ruin','Submission','Take Down','Volt Tackle','Wood Hammer','Wild Charge']:
                power *= 1.2
            if pokee.get_ability() == 'Thick Fat' and (self.type == 'Fire' or self.type == 'Ice'):
                poke_func.new_battle_txt(P)
                poke_func.battle_write(P,pok[targ].get_name() + " is", "protected by it's Thick Fat!")
                poke_func.show_ability(P, 'Thick Fat', eturn)
                ak *= 0.5
            if pokes.get_ability() == 'Swarm' and (pokes.ch/pokes.hp) < 0.33 and self.type == 'Bug':
                ak *= 1.5
            if pokes.get_ability() == 'Blaze' and (pokes.ch/pokes.hp) < 0.33 and self.type == 'Fire':
                ak *= 1.5
            if pokes.get_ability() == 'Torrent' and (pokes.ch/pokes.hp) < 0.33 and self.type == 'Water':
                ak *= 1.5
            if pokes.get_ability() == 'Overgrow' and (pokes.ch/pokes.hp) < 0.33 and self.type == 'Grass':
                ak *= 1.5
            if pokes.ff == 1 and self.type == 'Fire':
                ak *= 1.5
            pdf = pokee.get_df()
            damage = (((2*pokes.lvl/5)*power*(ak*akm)/(pdf*dfm)/50)+2)
        elif self.cat == '1':
            sakm = poke_func.pokestar_mod(P,pokes.player,pokes.sakm,modifier(pokes.sakm))
            sdfm = poke_func.pokestar_mod(P,pokee.player,pokee.sdfm,modifier(pokee.sdfm))
            if crit == True:
                if sakm < 1:
                    sakm = 1
                if sdfm > 1:
                    sdfm = 1
            if self.name == 'Venoshock' and (pok[targ].status == 'Psn' or pok[targ].status == 'BPs'):
                power *= 2
            sak = pokes.sak
            if pokes.get_ability() == 'Technician' and power <= 60:
                power *= 1.5
            if pokee.get_ability() == 'Thick Fat' and (self.type == 'Fire' or self.type == 'Ice'):
                poke_func.new_battle_txt(P)
                poke_func.battle_write(P,pok[targ].get_name() + " is", "protected by it's Thick Fat!")
                poke_func.show_ability(P, 'Thick Fat', eturn)
                sak *= 0.5
            if (pokes.get_ability() == 'Plus' or pokes.get_ability() == 'Minus') and (pokee.get_ability() == 'Plus' or pokee.get_ability() == 'Minus'):
                sak *= 1.5
            if pokes.get_ability() == 'Swarm' and (pokes.ch/pokes.hp) < 0.33 and self.type == 'Bug':
                sak *= 1.5
            if pokes.get_ability() == 'Blaze' and (pokes.ch/pokes.hp) < 0.33 and self.type == 'Fire':
                sak *= 1.5
            if pokes.get_ability() == 'Torrent' and (pokes.ch/pokes.hp) < 0.33 and self.type == 'Water':
                sak *= 1.5
            if pokes.get_ability() == 'Overgrow' and (pokes.ch/pokes.hp) < 0.33 and self.type == 'Grass':
                sak *= 1.5
            if pokes.ff == 1 and self.type == 'Fire':
                sak *= 1.5
            psdf = pokee.sdf
            if pokee.item == 'Eviolite' and pokee.evo != [] and pokee.evo[0] != 'Mega':
                psdf *= 1.5
            if self.name == 'Psyshock':
                psdf = pokee.get_df()
            damage = (((2*pokes.lvl/5)*power*(sak*sakm)/(psdf*sdfm)/50)+2)
            if self.name == 'Psyshock':
                damage = (((2*pokes.lvl/5)*power*(sak*sakm)/(psdf*poke_func.pokestar_mod(P,pokee.player,pokee.dfm,modifier(pokee.dfm)))/50)+2)
        else:
            damage = 0
        if self.is_contact() and pokee.get_ability() == 'Static':
            if random.random() <= 0.3 and pokes.can_status(P,'Par'):
                if pokes.status == None:
                    message.append([1,'Static',eturn,pokes,'Par','Paralyzed!'])
        if self.is_contact() and pokee.get_ability() == 'Flame Body':
            if random.random() <= 0.3 and pokes.can_status(P,'Brn'):
                if pokes.status == None:
                    message.append([1,'Flame Body',eturn,pokes,'Brn','Burned!'])
        if self.is_contact() and pokee.get_ability() == 'Poison Point':
            if random.random() <= 0.3 and pokes.can_status(P,'Psn'):
                message.append([1,'Poison Point',eturn,pokes,'Psn','Poisoned!'])
        if self.is_contact() and pokee.get_ability() == 'Effect Spore':
            r = random.random()
            if r <= 0.1 and pokes.can_status(P,'Psn'):
                message.append([1,'Effect Spore',eturn,pokes,'Psn','Poisoned!'])
            elif r > 0.1 and r <= 0.2 and pokes.can_status(P,'Slp'):
                if pokes.status == None:
                    message.append([1,'Effect Spore',eturn,pokes,'Slp','Asleep!'])
            elif r > 0.2 and r <= 0.3 and pokes.can_status(P,'Par'):
                if pokes.status == None:
                    message.append([1,'Effect Spore',eturn,pokes,'Par','Paralyzed!'])
        if pok[targ].get_ability() == 'Motor Drive' and self.type == 'Electric' and targ == 1:
            if pok[targ].spdm < 6:
                pok[targ].spdm += 1
            elif [3, pok[targ].get_name(), 'speed'] not in message:
                message.append([3, pok[targ].get_name(), 'speed'])
        if pok[targ].get_ability() == 'Storm Drain' and self.type == 'Water' and targ == 1:
            if pok[targ].sakm < 6:
                pok[targ].sakm += 1
            elif [3, pok[targ].get_name(), 'special attack'] not in message:
                message.append([3, pok[targ].get_name(), 'special attack'])
        if pok[targ].get_ability() == 'Lightning Rod' and self.type == 'Electric' and targ == 1:
            if pok[targ].sakm < 6:
                pok[targ].sakm += 1
            elif [3, pok[targ].get_name(), 'special attack'] not in message:
                message.append([3, pok[targ].get_name(), 'special attack'])
        orig_stats = pok[targ].copy()
        if pokee.get_ability() == 'Weak Armor' and self.cat == '0':
            if pok[targ].dfm > -6:
                pok[targ].dfm -= 1
            elif [4,pok[targ].get_name(),'defense'] not in message and pok[targ].dfm == orig_stats.dfm:
                message.append([4,pok[targ].get_name(),'defense'])
            if pok[targ].spdm < 6:
                pok[targ].spdm += 1
            elif [3,pok[targ].get_name(),'speed'] not in message and pok[targ].spdm == orig_stats.spdm:
                message.append([3,pok[targ].get_name(),'speed'])
            if pok[targ].spdm < 6:
                pok[targ].spdm += 1
            elif [3,pok[targ].get_name(),'speed'] not in message and pok[targ].spdm == orig_stats.spdm:
                message.append([3,pok[targ].get_name(),'speed'])
            message.append([2, ["",""], 'Weak Armor',eturn])
        # targ_temp = targ
        # orig_stats_temp = orig_stats
        if self.name == 'Acupressure':
            stat_list = []
            if pokes.akm < 6:
                stat_list.append('AU')
            if pokes.sakm < 6:
                stat_list.append('SAU')
            if pokes.dfm < 6:
                stat_list.append('DU')
            if pokes.sdfm < 6:
                stat_list.append('SDU')
            if pokes.accm < 6:
                stat_list.append('AcU')
            if pokes.spdm < 6:
                stat_list.append('SU')
            if pokes.evam > -6:
                stat_list.append('EvU')
            r = random.randint(0,len(stat_list)-1)
            self.eff = {1:[stat_list[r],stat_list[r]]}
        if self.name in ['Spit Up','Swallow']:
            stat_list = []
            for x in range(pokes.stockpile[1]):
                stat_list.append('DD')
            for x in range(pokes.stockpile[2]):
                stat_list.append('SDD')
            if self.name == 'Spit Up':
                pokes.stockpile = [0,0,0]
                self.eff = {-1:stat_list}
            else:
                self.eff = {1:stat_list}
        if self.name == 'Secret Power':
            effect = 'Par'
            if poke_func.in_terrain(P,'Psychic'):
                effect = 'SD'
            elif poke_func.in_terrain(P,'Misty'):
                effect = 'SAD'
            elif P.habitat == 'cave':
                effect = 'Fln'
            elif P.habitat in ['beach','path','mount']:
                effect = 'AcD'
            elif P.habitat in ['grass','mount_grass','forest']:
                effect = 'Slp'
            self.eff = {0.3:effect}
        if self.eff != {} and mod != 0 and not sheer:
            if P.battle_weather != None and P.battle_weather[0] == 'Sunny' and self.name == 'Growth':
                self.eff = {1:['AU','AU','SAU','SAU']}
            for x in self.eff:
                if x < 0:
                    targ_temp = abs(targ-1)
                    x_mod = x*-1
                    orig_stats_temp = pok[targ_temp].copy()
                else:
                    targ_temp = targ
                    orig_stats_temp = orig_stats
                    x_mod = x
                if pokes.get_ability() == 'Serene Grace':
                    x_mod *= 2
                if random.random()<x_mod and (self.cat == '2' or pokee.get_ability() != 'Shield Dust' or x < 0):
                    for y in self.eff[x]:
                        if y == 'Fln':
                            if pok[targ_temp].get_ability() == 'Inner Focus':
                                if x == 1:
                                    message.append([2,[pok[targ_temp].get_name()+" won't","flinch with its Inner Focus!"],'Inner Focus',eturn])
                            else:
                                pok[targ_temp].flinch = True
                        elif y in ['Brn','Frz','Psn','BPs','Par','Slp'] and pok[targ_temp].can_status(P,y,self.cat):
                            if pok[targ_temp].status == None:
                                if y == 'Slp' and poke_func.in_terrain(P,'Electric',pok[targ_temp]):
                                    message.append([7,pok[targ_temp].get_name()+" can't fall","asleep!"])
                                elif poke_func.in_terrain(P,'Misty',pok[targ_temp]):
                                    message.append([7,pok[targ_temp].get_name()+" surrounds","itself with a protective mist!"])
                                elif y in ['Psn','BPs'] and pok[targ_temp].get_ability() == 'Immunity':
                                    message.append([2,["It doesn't affect ", pok[targ_temp].get_name(True) + '!'],'Immunity',eturn])
                                elif y == 'Par' and pok[targ_temp].get_ability() == 'Limber':
                                    message.append([2,[pok[targ_temp].get_name()+" can't be", "Paralyzed!"],'Limber',eturn])
                                elif y == 'Slp' and pok[targ_temp].get_ability() == 'Insomnia':
                                    message.append([2,["It doesn't affect ", pok[targ_temp].get_name(True) + '!'],'Insomnia',eturn])
                                else:
                                    pok[targ_temp].status = y
                                    if y == 'Slp':
                                        pok[targ_temp].slptim = random.randint(1,4)
                                        if pok[targ_temp].get_ability() == 'Early Bird':
                                            pok[targ_temp].slptim = int(pok[targ_temp].slptim/2)
                        elif y == 'AD':
                            if pok[targ_temp].akm > -6:
                                if pok[targ_temp].get_ability() == 'Hyper Cutter' and x > 0:
                                    if x == 1:
                                        message.append([2,[pok[targ_temp].get_name()+"'s attack","can't be lowered!"],'Hyper Cutter',eturn])
                                elif pok[targ_temp].get_ability() == 'Clear Body' and x > 0:
                                    if x == 1:
                                        message.append([2,[pok[targ_temp].get_name()+"'s attack","can't be lowered!"],'Clear Body',eturn])
                                else:
                                    pok[targ_temp].akm -= 1
                            elif [4,pok[targ_temp].get_name(),'attack'] not in message and pok[targ_temp].akm == orig_stats_temp.akm:
                                message.append([4,pok[targ_temp].get_name(),'attack'])
                        elif y == 'SAD':
                            if pok[targ_temp].sakm > -6:
                                if pok[targ_temp].get_ability() == 'Clear Body' and x > 0:
                                    if x == 1:
                                        message.append([2,[pok[targ_temp].get_name()+"'s special","attack can't be lowered!"],'Clear Body',eturn])
                                else:
                                    pok[targ_temp].sakm -= 1
                            elif [4,pok[targ_temp].get_name(),'special attack'] not in message and pok[targ_temp].sakm == orig_stats_temp.sakm:
                                message.append([4,pok[targ_temp].get_name(),'special attack'])
                        elif y == 'DD':
                            if pok[targ_temp].dfm > -6:
                                if pok[targ_temp].get_ability() == 'Big Pecks' and x > 0:
                                    if x == 1:
                                        message.append([2,[pok[targ_temp].get_name()+"'s defense","can't be lowered!"],'Big Pecks',eturn])
                                elif pok[targ_temp].get_ability() == 'Clear Body' and x > 0:
                                    if x == 1:
                                        message.append([2,[pok[targ_temp].get_name()+"'s defense","can't be lowered!"],'Clear Body',eturn])
                                else:
                                    pok[targ_temp].dfm -= 1
                            elif [4,pok[targ_temp].get_name(),'defense'] not in message and pok[targ_temp].dfm == orig_stats_temp.dfm:
                                message.append([4,pok[targ_temp].get_name(),'defense'])
                        elif y == 'SDD':
                            if pok[targ_temp].sdfm > -6:
                                if pok[targ_temp].get_ability() == 'Clear Body' and x > 0:
                                    if x == 1:
                                        message.append([2,[pok[targ_temp].get_name()+"'s special","defense can't be lowered!"],'Clear Body',eturn])
                                else:
                                    pok[targ_temp].sdfm -= 1
                            elif [4,pok[targ_temp].get_name(),'special defense'] not in message and pok[targ_temp].sdfm == orig_stats_temp.sdfm:
                                message.append([4,pok[targ_temp].get_name(),'special defense'])
                        elif y == 'SD':
                            if pok[targ_temp].spdm > -6:
                                if pok[targ_temp].get_ability() == 'Clear Body' and x > 0:
                                    if x == 1:
                                        message.append([2,[pok[targ_temp].get_name()+"'s speed","can't be lowered!"],'Clear Body',eturn])
                                else:
                                    pok[targ_temp].spdm -= 1
                            elif [4,pok[targ_temp].get_name(),'speed'] not in message  and pok[targ_temp].spdm == orig_stats_temp.spdm:
                                message.append([4,pok[targ_temp].get_name(),'speed'])
                        elif y == 'AcD':
                            if pok[targ_temp].accm > -6:
                                if pok[targ_temp].get_ability() == 'Keen Eye' and x > 0:
                                    if x == 1:
                                        message.append([2,[pok[targ_temp].get_name()+"'s accuracy","can't be lowered!"],'Keen Eye',eturn])
                                elif pok[targ_temp].get_ability() == 'Clear Body' and x > 0:
                                    if x == 1:
                                        message.append([2,[pok[targ_temp].get_name()+"'s accuracy","can't be lowered!"],'Clear Body',eturn])
                                else:
                                    pok[targ_temp].accm -= 1
                            elif [4,pok[targ_temp].get_name(),'accuracy'] not in message:
                                message.append([4,pok[targ_temp].get_name(),'accuracy']) and pok[targ_temp].accm == orig_stats_temp.accm
                        elif y == 'EvD':
                            if pok[targ_temp].evam < 6:
                                if pok[targ_temp].get_ability() == 'Clear Body' and x > 0:
                                    if x == 1:
                                        message.append([2,[pok[targ_temp].get_name()+"'s evasion","can't be lowered!"],'Clear Body',eturn])
                                else:
                                    pok[targ_temp].evam += 1
                            elif [3,pok[targ_temp].get_name(),'evasion'] not in message and pok[targ_temp].evam == orig_stats_temp.evam:
                                message.append([4,pok[targ_temp].get_name(),'evasion'])
                        elif y == 'AU':
                            if pok[targ_temp].akm < 6:
                                pok[targ_temp].akm += 1
                            elif [3,pok[targ_temp].get_name(),'attack'] not in message and pok[targ_temp].akm == orig_stats_temp.akm:
                                message.append([3,pok[targ_temp].get_name(),'attack'])
                        elif y == 'SAU':
                            if pok[targ_temp].sakm < 6:
                                pok[targ_temp].sakm += 1
                            elif [4,pok[targ_temp].get_name(),'special attack'] not in message and pok[targ_temp].sakm == orig_stats_temp.sakm:
                                message.append([3,pok[targ_temp].get_name(),'special attack'])
                        elif y == 'DU':
                            if pok[targ_temp].dfm < 6:
                                pok[targ_temp].dfm += 1
                                if self.name == 'Stockpile':
                                    pokes.stockpile[1] += 1
                            elif [3,pok[targ_temp].get_name(),'defense'] not in message and pok[targ_temp].dfm == orig_stats_temp.dfm:
                                message.append([3,pok[targ_temp].get_name(),'defense'])
                        elif y == 'SDU':
                            if pok[targ_temp].sdfm < 6:
                                pok[targ_temp].sdfm += 1
                                if self.name == 'Stockpile':
                                    pokes.stockpile[2] += 1
                            elif [3,pok[targ_temp].get_name(),'special defense'] not in message and pok[targ_temp].sdfm == orig_stats_temp.sdfm:
                                message.append([3,pok[targ_temp].get_name(),'special defense'])
                        elif y == 'SU':
                            if pok[targ_temp].spdm < 6:
                                pok[targ_temp].spdm += 1
                            elif [3,pok[targ_temp].get_name(),'speed'] not in message and pok[targ_temp].spdm == orig_stats_temp.spdm:
                                message.append([3,pok[targ_temp].get_name(),'speed'])
                        elif y == 'AcU':
                            if pok[targ_temp].accm < 6:
                                pok[targ_temp].accm += 1
                            elif [3,pok[targ_temp].get_name(),'accuracy'] not in message and pok[targ_temp].accm == orig_stats_temp.accm:
                                message.append([3,pok[targ_temp].get_name(),'accuracy'])
                        elif y == 'EvU':
                            if pok[targ_temp].evam > -6:
                                pok[targ_temp].evam -= 1
                            elif [4,pok[targ_temp].get_name(),'evasion'] not in message and pok[targ_temp].evam == orig_stats_temp.evam:
                                message.append([3,pok[targ_temp].get_name(),'evasion'])
                        elif y == 'CU':
                            if pok[targ_temp].critm < 4:
                                pok[targ_temp].critm += 1
                            elif [3,pok[targ_temp].get_name(),'crit rate'] not in message and pok[targ_temp].critm == orig_stats_temp.critm:
                                message.append([3,pok[targ_temp].get_name(),'crit rate'])
                        elif y == 'Idf':
                            if pok[targ_temp].idf == False:
                                pok[targ_temp].idf = True
                            else:
                                poke_func.new_battle_txt(P)
                                poke_func.battle_write(P,"But it failed!")
                                P.clock.tick(P.bat_spd)
                        elif y == 'Inf':
                            if pok[targ_temp].inf == False:
                                pok[targ_temp].inf = True
                        elif y == 'Seed':
                            if pok[targ_temp].leech == False:
                                pok[targ_temp].leech = True
                        elif y == 'Cfs':
                            if pok[targ_temp].cfs == 0:
                                if poke_func.in_terrain(P,'Misty',pok[targ_temp]):
                                    if self.cat == '2':
                                        message.append([7,pok[targ_temp].get_name()+" surrounds","itself with a protective mist!"])
                                elif pok[targ_temp].get_ability() == 'Own Tempo':
                                    if self.cat == '2':
                                        message.append([2,[pok[targ_temp].get_name()+" can't be","confused!"],'Own Tempo',eturn])
                                else:
                                    pok[targ_temp].cfs = random.randint(2,5)
                        elif y == 'Bnd':
                            if pok[targ_temp].trapped[1] == 0:
                                pok[targ_temp].trapped = [self.name,random.randint(4,5)]
                                if self.name == 'Wrap':
                                    message.append([7,pok[targ_temp].get_name()+" was","wrapped!"])
                                elif self.name == 'Bind':
                                    message.append([7,pok[targ_temp].get_name()+" was","squeezed!"])
                                elif self.name == 'Infestation':
                                    message.append([7,pok[targ_temp].get_name()+" has been","afflicted with an infestation!"])
                                elif self.name == 'Clamp':
                                    message.append([7,pokes.get_name()+" clamped",pok[targ_temp].get_name(True)+"!"])
                                elif self.name == 'Sand Tomb':
                                    message.append([7,pok[targ_temp].get_name()+" became","trapped by Sand Tomb!"])
                                else:
                                    message.append([7,pok[targ_temp].get_name()+" became","trapped in the vortex!"])
            if P.pokestar_battle != 0 and pokes.player:
                if pok[targ_temp].player:
                    inc_stats = max(pok[targ_temp].critm-orig_stats_temp.critm,0) + max(pok[targ_temp].evam-orig_stats_temp.evam,0) + max(pok[targ_temp].accm-orig_stats_temp.accm,0) + max(pok[targ_temp].spdm-orig_stats_temp.spdm,0) + max(pok[targ_temp].sdfm-orig_stats_temp.sdfm,0) + max(pok[targ_temp].dfm-orig_stats_temp.dfm,0) + max(pok[targ_temp].sakm-orig_stats_temp.sakm,0) + max(pok[targ_temp].akm-orig_stats_temp.akm,0)
                else:
                    inc_stats = max(orig_stats_temp.critm-pok[targ_temp].critm,0) + max(orig_stats_temp.evam-pok[targ_temp].evam,0) + max(orig_stats_temp.accm-pok[targ_temp].accm,0) + max(orig_stats_temp.spdm-pok[targ_temp].spdm,0) + max(orig_stats_temp.sdfm-pok[targ_temp].sdfm,0) + max(orig_stats_temp.dfm-pok[targ_temp].dfm,0) + max(orig_stats_temp.sakm-pok[targ_temp].sakm,0) + max(orig_stats_temp.akm-pok[targ_temp].akm,0)
                poke_func.pokestar_gain(P,2,inc_stats*1.5)
        if pokes.get_ability() == 'Stun':
            if pok[targ].get_ability() == 'Inner Focus':
                if x == 1:
                    message.append([2,[pok[targ_temp].get_name()+" won't","flinch with its Inner Focus!"],'Inner Focus',eturn])
            else:
                pok[targ].flinch = True
        if self.name in ['Dragon Tail','Roar','Whirlwind','Circle Throw'] and ((eturn == 1 and not poke_func.last_poke(P.party)) or (eturn == 0 and not poke_func.last_poke(P.opponent))):
            pok[targ].exit = True
            pok[targ].drag = True
        if self.name in ['Dragon Tail','Circle Throw'] and type(P.opponent[0]) != str and P.legendary_battle == False and P.tourney_battle == False and P.pokestar_battle == 0 and pokes.player:
            P.end_battle = pok[targ]
            pok[targ].drag = True
        if self.name == 'Rest':
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P,pokes.get_name()+' slept and', 'became healthy!')
            P.clock.tick(P.bat_spd)
            pokes.status = 'Slp'
            pokes.slptim = 2
            if pokes.get_ability() == 'Early Bird':
                pokes.slptim = 1
        if self.name == 'Haze':
            poke_func.battle_txt(P,'All stat changes were eliminated!')
            pokes.akm,pokes.sakm,pokes.dfm,pokes.sdfm,pokes.spdm,pokes.accm,pokes.evam,pokes.critm = 0,0,0,0,0,0,0,0
            pokee.akm,pokee.sakm,pokee.dfm,pokee.sdfm,pokee.spdm,pokee.accm,pokee.evam,pokee.critm = 0,0,0,0,0,0,0,0
            P.haze_active = 2
        if self.name == 'Psych Up':
            poke_func.battle_txt(P,pokes.get_name() + " copied "+pokee.get_name(True)+"'s stat changes!")
            pokes.akm,pokes.sakm,pokes.dfm,pokes.sdfm,pokes.spdm,pokes.accm,pokes.evam,pokes.critm = pokee.akm,pokee.sakm,pokee.dfm,pokee.sdfm,pokee.spdm,pokee.accm,pokee.evam,pokee.critm
            P.haze_active = 2
        if self.name == 'Teleport':
            P.end_battle = pokes
        if self.name == 'Charge':
            pok[targ].chrg = 1
        if self.name == 'Focus Energy' and [3,pok[targ].get_name(),'crit rate'] not in message:
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P,f'{pok[targ].get_name()}\'s getting', 'pumped!')
            P.clock.tick(P.bat_spd)
        if self.sec == '3':
            pokes.charge = None
        if self.sec == '5':
            pokes.charge = 'Splash'
        if self.name == 'Aromatherapy' or self.name == 'Heal Bell':
            if eturn == 0:
                for pk in P.party:
                    if pk.status != None and pk.status != 'Faint':
                        pk.status = None
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,f'{pk.get_name()} was', 'cured!')
                        P.clock.tick(P.bat_spd)
            else:
                if pokes.status != None:
                    pokes.status = None
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,f'{pokes.get_name()} was', 'cured!')
                    P.clock.tick(P.bat_spd)
        #end
        if pok[0].status == 'Brn' and self.cat == '0' and pokes.get_ability() != 'Guts':
            damage = damage/2
        damage *= mod
        if self.type in pok[0].type:
            if pok[0].get_ability() == 'Adaptability':
                damage *= 2
            else:
                damage *= 1.5
        if crit == True:
            damage *= 1.5
            if pokes.get_ability() == 'Sniper':
                damage *= 1.5
        if pok[targ].minimize and self.name in ['Heavy Slam','Steamroller','Stomp','Body Slam','Glacial Press']:
            damage *= 2
        if self.name == 'Assurance' and pok[targ].damage_taken > 0:
            damage *= 2
        if self.type == 'Water' and pokes.get_ability() == 'Water Bubble':
            damage *= 2
        if self.type == 'Steel' and pokes.get_ability() == 'Steelworker':
            damage *= 1.5
        if pokee.get_ability() == 'Water Bubble' and self.type == 'Fire':
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P,pok[targ].get_name() + " is", "protected by it's Bubble!")
            poke_func.show_ability(P, 'Water Bubble', eturn)
            damage *= 0.5
        if poke_func.in_terrain(P,'Misty',pokee) and self.type == 'Dragon':
            damage *= 0.5
        if eff == 2 and pok[targ].get_ability() in ['Filter','Rock Solid']:
            damage *= .75
        if pokes.get_ability() == 'Rivalry' and pok[targ] == pokee:
            if pokes.gen == pokee.gen:
                damage *= 1.25
            elif pokes.gen != 2 and pokee.gen != 2:
                damage *= .75
        if self.type == 'Fairy' and P.loc in ['silfide_gymb','silfide_gym3'] and P.prog[22][2] == 0:
            poke_func.battle_txt(P,pokes.get_name() + "'s attack","was boosted by the orb!")
            damage *= 1.3
        if pokes.get_ability() == 'Tough Claws' and self.is_contact():
            damage *= 1.3
        if pokes.get_ability() == 'Mega Launcher' and self.name in ['Dark Pulse','Water Pulse','Aura Sphere','Dragon Pulse']:
            damage *= 1.5
        #fixed damage attacks
        if (pokee.get_ability() == 'Puppet' or self.sec == '4') and damage > 0:
            damage = pokee.ch
            eff = 3
            if pok[targ].endure == False:
                message.append([7,'It\'s a one-hit KO!'])
        if self.name == 'Psywave' and damage > 0:
            damage = int(pokes.lvl*(random.randint(0,100)+50)/100)
            eff = 3
        if self.name in ['Counter','Mirror Coat']:
            damage = int(2*(pokes.damage_taken))
            eff = 3
        if self.name == 'Metal Burst':
            damage = int(1.5*(pokes.damage_taken))
            eff = 3
        if self.name == 'Final Gambit' and damage > 0:
            damage = pokes.ch
            eff = 3
        if self.name in ['Night Shade','Seismic Toss'] and damage > 0:
            damage = pokes.lvl
            eff = 3
        if self.name == 'Sonic Boom' and damage > 0:
            damage = 20
            eff = 3
        if self.name == 'Dragon Rage' and damage > 0:
            damage = 40
            eff = 3
        if self.name == 'Endeavor' and damage > 0:
            damage = pokee.ch-pokes.ch
            eff = 3
        if self.name == 'Super Fang' and damage > 0:
            damage = (pokee.ch/2)
            if damage < 1:
                damage = 1
            eff = 3
        if self.name == 'Pain Split':
            pokes.ch = int((pokee.ch+pokes.ch)/2)
            pokee.ch = int((pokee.ch+pokes.ch)/2)
            if pokes.ch > pokes.hp:
                pokes.ch = pokes.hp
            if pokee.ch > pokee.hp:
                pokee.ch = pokee.hp
        if self.name == 'Power Split':
            aktot = int((pokes.ak + pokee.ak) / 2)
            saktot = int((pokes.sak + pokee.sak) / 2)
            pokes.stat_swap = [None,aktot > pokes.ak,saktot > pokes.sak,None,None,None]
            pokee.stat_swap = [None,aktot > pokee.ak,saktot > pokee.sak,None,None,None]
            pokes.ak = aktot
            pokes.sak = saktot
            pokee.ak = aktot
            pokee.sak = saktot
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P,pokes.get_name() + " shared its", "power with the target!")
            P.clock.tick(P.bat_spd)
        if self.name == 'Guard Split':
            dftot = int((pokes.df + pokee.df) / 2)
            sdftot = int((pokes.sdf + pokee.sdf) / 2)
            pokes.stat_swap = [None,None,None,dftot > pokes.df,sdftot > pokes.sdf,None]
            pokee.stat_swap = [None,None,None,dftot > pokee.df,sdftot > pokee.sdf,None]
            pokes.df = dftot
            pokes.sdf = sdftot
            pokee.df = dftot
            pokee.sdf = sdftot
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P,pokes.get_name() + " shared its", "guard with the target!")
            P.clock.tick(P.bat_spd)
        if self.name == 'Yawn':
            pok[targ].yawn = 1
            poke_func.new_battle_txt(P)
            poke_func.battle_write(P,pok[targ].get_name() + " grew", "drowsy!")
            P.clock.tick(P.bat_spd)
        if self.name == 'Roost':
            pok[targ].ch += int(pok[targ].hp/2)
            if pok[targ].ch > pok[targ].hp:
                pok[targ].ch = pok[targ].hp
            if pokes.type[1] == None and pokes.type[0] == 'Flying':
                pokes.type[0] = 'Normal'
                pokes.roost = 1
            elif pokes.type[0] != None and pokes.type[1] == 'Flying':
                pokes.type[1] = None
                pokes.roost = 2
            elif pokes.type[1] != None and pokes.type[0] == 'Flying':
                pokes.type[0] = None
                pokes.roost = 1
        if ((self.type == 'Electric' and pok[targ].get_ability() == 'Volt Absorb') or (self.type == 'Water' and pok[targ].get_ability() == 'Water Absorb')) and targ == 1:
            damage = -(pok[targ].hp/4)
        if pok[targ].ch == pok[targ].hp and pok[targ].get_ability() == 'Sturdy' and damage > pok[targ].ch:
            damage = pok[targ].ch - 1
            message.append([2,[pok[targ].get_name()+" endured", "the hit!"],'Sturdy',eturn])
        if self.name == 'False Swipe' and pok[targ].ch-damage < 1 and damage > 0:
            damage = pok[targ].ch-1
        if pok[targ].ch-damage < 1 and pok[targ].endure and damage > 0:
            message.append([7,pok[targ].get_name()+' endured','the hit!'])
            damage = pok[targ].ch-1
        if self.name == 'Rest':
            damage = -(pokes.hp-pokes.ch)
            pokes.rest = True
        if self.name == 'Swallow':
            if pokes.stockpile[0] == 1:
                mod = .25
            elif pokes.stockpile[0] == 2:
                mod = 0.5
            else:
                mod = 1
            damage = -(pokes.hp*mod)
            pokes.stockpile = [0,0,0]
        if self.name in ['Recover','Soft-Boiled','Heal Pulse','Slack Off']:
            if pokes.ability == 'Mega Launcher' and self.name == 'Heal Pulse':
                damage = -(pokes.hp/1.3)
            else:
                damage = -(pokes.hp/2)
        if self.name == 'Rejuvenate':
            damage = -(pokes.hp-pokes.ch)
        if self.name == 'Synthesis':
            mod = 2
            if P.battle_weather != None:
                if P.battle_weather[0] == 'Sunny':
                    mod = 1.5
                elif P.battle_weather[0] != 'Windy':
                    mod = 4
            damage = -(pokes.hp/mod)
        if self.name == 'Moonlight':
            mod = 2
            if P.battle_weather != None:
                if P.battle_weather[0] == 'Sunny':
                    mod = 1.5
                elif P.battle_weather[0] != 'Windy':
                    mod = 4
            if (poke_func.get_time() > 19 or poke_func.get_time() < 6):
                mod /= 2
            damage = -(pokes.hp/mod)
        if self.name == 'Morning Sun':
            mod = 2
            if P.battle_weather != None:
                if P.battle_weather[0] == 'Sunny':
                    mod = 1.5
                elif P.battle_weather[0] != 'Windy':
                    mod = 4
            if (poke_func.get_time() > 19 or poke_func.get_time() < 6):
                mod /= 2
            damage = -(pokes.hp/mod)
        if self.name == 'Belly Drum':
            damage = pokes.hp/2
            pokes.bellydrum = True
            pokes.akm = 6
            message.append([7,pok[targ].get_name()+' cut its','HP and maximized its attack!'])
        if self.name == 'Curse' and 'Ghost' in pokes.type:
            damage = pokes.hp/2
            pokes.bellydrum = True
        print('power'+str(damage))
        #take damage
        # if damage < 1 and damage > 0:
        #     damage = 1
        # if pok[targ].ch-int(damage) < 0:
        #     damage = pok[targ].ch
        if self.cat != '2' and (self.type == 'Fire' or self.name in ['Scald','Steam Eruption']) and pok[targ].status == 'Frz':
            pok[targ].status = None
            message.append([7,pok[targ].get_name() + " thawed", "out!"])
        if damage < 0:
            if P.tourney_battle or pokes.legendary:
                pok[targ].ch -= int(damage/4)
            elif P.pokestar_battle != 0:
                pok[targ].ch -= int(damage/2)
            else:
                pok[targ].ch -= int(damage)
            if pok[targ].ch > pok[targ].hp:
                pok[targ].ch = pok[targ].hp
        elif self.name != 'Psywave' and self.name != 'Night Shade' and self.name != 'Super Fang' and self.name != 'Final Gambit' and self.name != 'Seismic Toss':
            if not pok[targ].player and ((P.enemy_buffs[1] > 0 and self.cat == '1') or (P.enemy_buffs[2] > 0 and self.cat == '0')):
                damage /= 2
            elif pok[targ].player and ((P.player_buffs[1] > 0 and self.cat == '1') or (P.player_buffs[2] > 0 and self.cat == '0')):
                damage /= 2
            pok[targ].take_damage(P,damage)
        else:
            pok[targ].take_damage(P,damage)
        if pokee.get_ability() == 'Cute Charm' and pok[targ].ch != 0 and self.is_contact() and random.random() < 0.3 and pokee.gen != pokes.gen and pokes.get_ability() != 'Oblivious' and pokes.gen != 2 and pokee.gen != 2 and pokes.inf == False:
            message.append([8,pokes,eturn])
        if pok[targ].ch == 0:
            if self.name == 'Fell Stinger':
                for x in range(3):
                    if pokes.akm < 6:
                        pokes.akm += 1
                    elif [3,pokes.get_name(),'attack'] not in message:
                        message.append([3,pokes.get_name(),'attack'])
            if pokes.get_ability() == 'Moxie':
                if pokes.akm < 6:
                    message.append([9, pokes, abs(eturn - 1)])
                elif [3,pokes.get_name(),'attack'] not in message:
                    message.append([3,pokes.get_name(),'attack'])
        if pok[targ].bide[0] == 1 or pok[targ].bide[0] == 2:
            pok[targ].bide[1] += damage
        if self.name == 'Struggle':
            recoil = int(pok[0].hp/4)
        elif self.name in ['Head Smash'] and pokes.get_ability() != 'Rock Head':
            recoil = int(pokee.damage_taken/2)
            if recoil == 0:
                recoil = 1
        elif self.name in ['Wood Hammer','Double-Edge','Volt Tackle','Brave Bird','Flare Blitz'] and pokes.get_ability() != 'Rock Head':
            recoil = int(pokee.damage_taken/3)
            if recoil == 0:
                recoil = 1
        elif self.name in ['Wild Charge','Submission','Take Down'] and pokes.get_ability() != 'Rock Head':
            recoil = int(pokee.damage_taken/4)
            if recoil == 0:
                recoil = 1
        elif (self.name == 'Final Gambit' and damage > 0) or (self.name in ['Explosion','Self-Destruct']):
            recoil = int(pokes.hp)
            pokes.explode = True
        else:
            recoil = 0
        if self.name == 'Strength Sap':
            ss_mod = modifier(pokee.akm)
            ss_heal = int(pokee.ak*ss_mod)
            if ss_heal > pokes.hp-pokes.ch:
                ss_heal = pokes.hp-pokes.ch
            message.append([10,pokes,ss_heal])
        if self.name in ['Horn Leech','Absorb','Dream Eater','Leech Life','Mega Drain','Giga Drain','Drain Punch','Parabolic Charge']:
            drain = pokee.damage_taken/2
        elif self.name == 'Draining Kiss':
            drain = pokee.damage_taken*0.75
        else:
            drain = 0
        if pokes.item == 'Shell Bell':
            drain += pokee.damage_taken/8
        if drain > 0 and drain < 1:
            drain = 1
        if drain != 0:
            drain = int(drain)
        if pokes.ch + drain > pokes.hp:
            drain = int(pokes.hp-pokes.ch)
        if self.is_contact() and (pokee.get_ability() == 'Rough Skin' or pokee.get_ability() == 'Iron Barbs'):
            roughskin = int(pokes.hp/8)
            if pokes.ch - roughskin < 0:
                roughskin = pokes.ch
            numr = 0
            if pokee.get_ability() == 'Iron Barbs':
                numr = 1
            message.append([5,roughskin,pokes.get_name(),numr])
        if pokes.ch - recoil < 0:
            recoil = pokes.ch
        ran = random.random()
        repeat = 0
        if self.name == 'Twineedle' or self.name == 'Double Kick' or self.name == 'Double Hit' or self.name == 'Dual Chop' or self.name == 'Gear Grind' or self.name == 'Bonemerang':
            repeat = 1
        if self.name == 'Beat Up':
            first_time = False
            if pokes.beat_up == []:
                first_time = True
            if pokes.player:
                party = P.party
            else:
                party = P.opponent
            count = 0
            for p in party:
                if type(p) != str and not p.equals(pokes) and p.status == None:
                    if first_time:
                        pokes.beat_up.append(p.orig_stats[1]*5)
                    count += 1
            repeat = count
            if not first_time:
                del pokes.beat_up[0]
        if self.sec == '2':
            if pokes.get_ability() == 'Skill Link':
                repeat = 4
            elif ran <= .33:
                repeat = 1
            elif ran <= .66:
                repeat = 2
            elif ran <= .83:
                repeat = 3
            else:
                repeat = 4
        if repeat == 0 and pokes.get_ability() == 'Parental Bond' and self.cat != '2':
            repeat = 1
            pokes.child_hit = True
        return [eff,crit,recoil,message,repeat,drain]

    def animate(self,P,pokes,pokee,eturn):
        if eturn == 1:
            temp = pokes.copy()
            pokes = pokee.copy()
            pokee = temp.copy()
        if P.habitat != None:
            day_night = ""
            if P.habitat in ['grass','forest','dock','road','path','beach','mount_grass','mount','snow','snow_grass']:
                if ((poke_func.get_time() > 19 or poke_func.get_time() < 6) or P.lighting == 'Night') and P.lighting != 'Day':
                    day_night = '_night'
                else:
                    day_night = '_day'
            if P.fishing and P.loc in ['echo_cave','forbidden_8']:
                back = poke_func.load("p/terrain/"+P.habitat+day_night+"_fishing.png")
            else:
                back = poke_func.load("p/terrain/"+P.habitat+day_night+".png")
            plate = poke_func.load("p/terrain/enemy_"+P.habitat+day_night+".png")
            plats = poke_func.load("p/terrain/self_"+P.habitat+day_night+".png")
        else:
            back = poke_func.load("p/terrain/indoor.png")
            plate = poke_func.load("p/terrain/enemy_indoor.png")
            plats = poke_func.load("p/terrain/self_indoor.png")
        mega = pygame.transform.scale(poke_func.load("p/mega_symbol.png"),(30,30))
        nurse = pygame.transform.scale(poke_func.load("p/nurse_icon.png"),(30,30))
        infoboxs = pygame.image.load("p/battle_info_boxs.png")
        if pokes.code[-2:] == '_S':
            infoboxs = pygame.image.load("p/battle_info_boxs_S.png")
        infoboxe = pygame.image.load("p/battle_info_boxe.png")
        if pokee.code[-2:] == '_S':
            infoboxe = pygame.image.load("p/battle_info_boxe_S.png")
        hpbar = pygame.image.load("p/team_hp.png")
        boy = pygame.image.load("p/ui/boy_ico.png")
        girl = pygame.image.load("p/ui/girl_ico.png")
        expbar = pygame.image.load("p/summ_exp.png")
        pokesname = P.font_s.render(pokes.name,True,(255,255,255))
        sname_size = P.font_s.size(pokes.name)[0]
        pokeename = P.font_s.render(pokee.name,True,(255,255,255))
        ename_size = P.font_s.size(pokee.name)[0]
        pokeslvl = P.font_s.render("Lv."+str(pokes.lvl),True,(255,255,255))
        pokeelvl = P.font_s.render("Lv."+str(pokee.lvl),True,(255,255,255))
        pokemone = pygame.transform.scale(pygame.image.load("p/poke/"+pokee.code+"_bf.png"),(290,290))
        pokemons = pygame.transform.scale(pygame.image.load("p/poke/"+pokes.code+"_bb.png"),(410,410))
        end = True
        a = 0
        pokeex = 0
        pokeey = 0
        pokesx = 0
        pokesy = 0
        while end:
            xmod = 0

            #back start
            P.surface.blit(back,(0,0))
            P.surface.blit(plate,(400,200))
            P.surface.blit(plats,(0,360))
            if P.battle_terrain != None and P.battle_terrain[1] != 6:
                P.surface.blit(P.battle_terrain[2],(0,0))
            #back end
            P.surface.blit(pokemone,(455+pokeex,-35+pokeey-abs(P.poke_m[0])))
            #first box start
            P.surface.blit(infoboxe,(0,100))
            if pokee.gen == 0:
                P.surface.blit(boy,(5,110))
            elif pokee.gen == 1:
                P.surface.blit(girl,(5,110))
            P.surface.blit(pokeename,(50,115))
            if pokee.code[:5] == 'Mega_':
                P.surface.blit(mega,(55+ename_size,117))
                xmod += 30
            if pokee.code_nos() in P.save_data.pokedex and P.save_data.pokedex[pokee.code_nos()][0] == 1:
                P.surface.blit(P.caught_icon,(-340+P.infoepos+ename_size+xmod,120))
                if pokee.code[:5] == 'Mega_':
                    xmod -= 30
            if pokee.status != None:
                if pokee.name in P.save_data.pokedex and P.save_data.pokedex[pokee.name][0] == 1:
                    xmod += 40
                sta = pygame.image.load("p/ui/"+pokee.status+"_ico.png")
                sta = pygame.transform.scale(sta,(50,20))
                P.surface.blit(sta,(60+ename_size+xmod,122))
            if P.pokestar_battle == 0:
                P.surface.blit(pokeelvl,(10,155))
            if pokee.ch/pokee.hp >= 0.5:
                P.surface.fill((0,255,0), Rect(164,165,int(200*(pokee.ch/pokee.hp)),10))
            elif pokee.ch/pokee.hp >= 0.25:
                P.surface.fill((255,255,0), Rect(164,165,int(200*(pokee.ch/pokee.hp)),10))
            else:
                P.surface.fill((255,50,0), Rect(164,165,int(200*(pokee.ch/pokee.hp)),10))
            P.surface.blit(hpbar,(120,160))
            #first box end
            P.surface.blit(pokemons,(-5+pokesx,75+pokesy-abs(P.poke_m[1])))
            #second box start
            P.surface.blit(infoboxs,(400,300))
            if pokes.gen == 0:
                P.surface.blit(boy,(455,310))
            elif pokes.gen == 1:
                P.surface.blit(girl,(455,310))
            P.surface.blit(pokesname,(500,315))
            xmod = 0
            if pokes.code[:5] == 'Mega_':
                P.surface.blit(mega,(505+sname_size,317))
                xmod += 30
            if pokes.nurse != 0:
                P.surface.blit(nurse,(505+sname_size,317))
                xmod += 30
            if pokes.status != None:
                sta = pygame.image.load("p/ui/"+pokes.status+"_ico.png")
                sta = pygame.transform.scale(sta,(50,20))
                szn = P.font_s.size(pokes.name)
                P.surface.blit(sta,(510+szn[0]+xmod,322))
            if P.pokestar_battle == 0:
                P.surface.blit(pokeslvl,(430,380))
                P.surface.fill((255,255,255),Rect(450,425,350,10))
                if pokes.lvl != 100:
                    P.surface.fill((0,0,255), Rect(474,425,int(320*(pokes.exp/pokes.get_exp())),10))
                else:
                    P.surface.fill((0,0,255), Rect(474,425,320,10))
                P.surface.blit(expbar,(420,420))
            hps = P.font_s.render(str(pokes.ch) + "/" + str(pokes.hp),True,(255,255,255))
            hpsze = P.font_s.size(str(pokes.ch) + "/" + str(pokes.hp))
            P.surface.blit(hps,(720-hpsze[0],380))
            if pokes.ch/pokes.hp >= 0.5:
                P.surface.fill((0,255,0), Rect(584,365,int(200*(pokes.ch/pokes.hp)),10))
            elif pokes.ch/pokes.hp >= 0.25:
                P.surface.fill((255,255,0), Rect(584,365,int(200*(pokes.ch/pokes.hp)),10))
            else:
                P.surface.fill((255,50,0), Rect(584,365,int(200*(pokes.ch/pokes.hp)),10))
            P.surface.blit(hpbar,(540,360))
            #second bar end
            if a < 5 and self.cat == '0':
                if eturn == 0:
                    pokesx += 5
                    pokesy -= 5
                else:
                    pokeex -= 5
                    pokeey += 5
            elif a < 10 and self.cat == '0':
                if eturn == 0:
                    pokesx -= 5
                    pokesy += 5
                else:
                    pokeex += 5
                    pokeey -= 5
            if a == 10 and self.cat == '0':
                end = False
            if self.cat == '1':
                end = False
            if self.cat == '2':
                end = False
            a += 1
            poke_func.update_screen(P)
            P.clock.tick(P.ani_spd)

    def use_bide(self,P,pokes,pokee,eturn) -> list:
        if P.ani_on:
            self.animate(P,pokes,pokee,eturn)
        damage = pokes.bide[1]
        pokee.take_damage(P,2*damage)
        # pokee.ch -= 2*int(damage)
        # if pokee.ch < 0:
        #     pokee.ch = 0
        return [3,False,0,[],0,0]

    def hurt_cfs(self,P,pokes,pokee) -> list:
        poke_func.cancelled(pokes)
        akm = poke_func.pokestar_mod(P,pokes.player,pokes.akm,modifier(pokes.akm))
        dfm = poke_func.pokestar_mod(P,pokes.player,pokes.dfm,modifier(pokes.dfm))
        ak = pokes.ak
        if pokes.get_ability() == 'Guts' and pokes.status != None:
            ak *= 1.5
        damage = int((((2*pokes.lvl/5)*40*(ak*akm)/(pokes.get_df()*dfm)/50)+2))
        if (P.tourney_battle or pokes.legendary) and pokes.bellydrum == False and pokes.explode == False:
            damage /= 4
        elif P.pokestar_battle != 0 and pokes.bellydrum == False and pokes.explode == False:
            damage /= 2
        if damage > 0 and damage < 1:
            damage = 1
        if damage > pokes.ch:
            damage = pokes.ch
        pokes.ch -= int(damage)
        return [3,False,0,[],0,0]

    def acc_mod(self,stage) -> float:
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

    def crit_mod(self,stage) -> float:
        if stage == 0:
            return 0.042
        elif stage == 1:
            return .125
        elif stage == 2:
            return 0.5
        return 1

    def effective(self, P, poke, user, eturn) -> float:
        eff = 1.0
        if self.type == 'Normal':
            if 'Ghost' in poke.type and poke.idf == False and self.name != 'Struggle' and user.get_ability() != 'Scrappy':
                eff *= 0
            if 'Steel' in poke.type:
                eff *= 0.5
            if 'Rock' in poke.type:
                eff *= 0.5
        elif self.type == 'Fighting':
            if 'Ghost' in poke.type and user.get_ability() != 'Scrappy':
                eff *= 0
            if 'Steel' in poke.type:
                eff *= 2
            if 'Rock' in poke.type:
                eff *= 2
            if 'Normal' in poke.type:
                eff *= 2
            if 'Ice' in poke.type:
                eff *= 2
            if 'Dark' in poke.type:
                eff *= 2
            if 'Bug' in poke.type:
                eff *= 0.5
            if 'Fairy' in poke.type:
                eff *= 0.5
            if 'Flying' in poke.type:
                eff *= 0.5
            if 'Poison' in poke.type:
                eff *= 0.5
            if 'Psychic' in poke.type:
                eff *= 0.5
        elif self.type == 'Flying':
            if 'Bug' in poke.type:
                eff *= 2
            if 'Fighting' in poke.type:
                eff *= 2
            if 'Grass' in poke.type:
                eff *= 2
            if 'Electric' in poke.type:
                eff *= 0.5
            if 'Rock' in poke.type:
                eff *= 0.5
            if 'Steel' in poke.type:
                eff *= 0.5
        elif self.type == 'Poison':
            if 'Steel' in poke.type:
                eff *= 0
            if 'Fairy' in poke.type:
                if P.loc in ['silfide_gymb','silfide_gym4'] and P.prog[22][3] == 0 and 'Steel' not in poke.type:
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,"The power of the orb weakened the attack!")
                    P.clock.tick(P.bat_spd)
                else:
                    eff *= 2
            if 'Grass' in poke.type:
                eff *= 2
            if 'Poison' in poke.type:
                eff *= 0.5
            if 'Ground' in poke.type:
                eff *= 0.5
            if 'Rock' in poke.type:
                eff *= 0.5
            if 'Ghost' in poke.type:
                eff *= 0.5
        elif self.type == 'Ground':
            if 'Flying' in poke.type or poke.get_ability() == 'Levitate' or poke.magnet_rise > 0:
                if poke.get_ability() == 'Levitate':
                    poke_func.show_ability(P, 'Levitate', eturn)
                eff *= 0
            if 'Electric' in poke.type:
                eff *= 2
            if 'Fire' in poke.type:
                eff *= 2
            if 'Poison' in poke.type:
                eff *= 2
            if 'Rock' in poke.type:
                eff *= 2
            if 'Steel' in poke.type:
                eff *= 2
            if 'Bug' in poke.type:
                eff *= 0.5
            if 'Grass' in poke.type:
                eff *= 0.5
        elif self.type == 'Rock':
            if 'Bug' in poke.type:
                eff *= 2
            if 'Fire' in poke.type:
                eff *= 2
            if 'Flying' in poke.type:
                if P.battle_weather != None and P.battle_weather[0] == 'Windy':
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,"The mysterious strong winds", "weakened the attack!")
                    P.clock.tick(P.bat_spd)
                else:
                    eff *= 2
            if 'Ice' in poke.type:
                eff *= 2
            if 'Fighting' in poke.type:
                eff *= 0.5
            if 'Ground' in poke.type:
                eff *= 0.5
            if 'Steel' in poke.type:
                eff *= 0.5
        elif self.type == 'Bug':
            if 'Dark' in poke.type:
                eff *= 2
            if 'Grass' in poke.type:
                eff *= 2
            if 'Psychic' in poke.type:
                eff *= 2
            if 'Fairy' in poke.type:
                eff *= 0.5
            if 'Fighting' in poke.type:
                eff *= 0.5
            if 'Fire' in poke.type:
                eff *= 0.5
            if 'Flying' in poke.type:
                eff *= 0.5
            if 'Ghost' in poke.type:
                eff *= 0.5
            if 'Poison' in poke.type:
                eff *= 0.5
            if 'Steel' in poke.type:
                eff *= 0.5
        elif self.type == 'Ghost':
            if 'Normal' in poke.type:
                eff *= 0
            if 'Ghost' in poke.type:
                eff *= 2
            if 'Psychic' in poke.type:
                eff *= 2
            if 'Dark' in poke.type:
                eff *= 0.5
        elif self.type == 'Steel':
            if 'Fairy' in poke.type:
                if P.loc in ['silfide_gymb','silfide_gym4'] and P.prog[22][3] == 0:
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,"The power of the orb weakened the attack!")
                    P.clock.tick(P.bat_spd)
                else:
                    eff *= 2
            if 'Ice' in poke.type:
                eff *= 2
            if 'Rock' in poke.type:
                eff *= 2
            if 'Electric' in poke.type:
                eff *= 0.5
            if 'Fire' in poke.type:
                eff *= 0.5
            if 'Steel' in poke.type:
                eff *= 0.5
            if 'Water' in poke.type:
                eff *= 0.5
        elif self.type == 'Fire':
            if 'Bug' in poke.type:
                eff *= 2
            if 'Grass' in poke.type:
                eff *= 2
            if 'Ice' in poke.type:
                eff *= 2
            if 'Steel' in poke.type:
                eff *= 2
            if 'Dragon' in poke.type:
                eff *= 0.5
            if 'Fire' in poke.type:
                if poke.get_ability() == 'Flash Fire':
                    eff *= 0
                    if poke.ff == 0:
                        poke.ff = 1
                        poke_func.new_battle_txt(P)
                        poke_func.battle_write(P,poke.get_name()+"'s fire","attacks got boosted!")
                        poke_func.show_ability(P,'Flash Fire',eturn)
                else:
                    eff *= 0.5
            if 'Rock' in poke.type:
                eff *= 0.5
            if 'Water' in poke.type:
                eff *= 0.5
        elif self.type == 'Water':
            if poke.get_ability() == 'Storm Drain' or poke.get_ability() == 'Water Absorb':
                if poke.get_ability() == 'Water Absorb':
                    poke_func.new_battle_txt(P)
                    if poke.ch < poke.hp:
                        poke_func.battle_write(P,poke.get_name()+" had its","HP restored!")
                    else:
                        poke_func.battle_write(P,poke.get_name()+" was","unaffected!")
                    poke_func.show_ability(P,'Water Absorb',eturn)
                elif poke.get_ability() == 'Storm Drain':
                    poke_func.show_ability(P, 'Storm Drain', eturn)
                eff *= 0
            if 'Fire' in poke.type:
                eff *= 2
            if 'Ground' in poke.type:
                eff *= 2
            if 'Rock' in poke.type:
                eff *= 2
            if 'Dragon' in poke.type:
                eff *= 0.5
            if 'Grass' in poke.type:
                eff *= 0.5
            if 'Water' in poke.type:
                eff *= 0.5
        elif self.type == 'Grass':
            if 'Ground' in poke.type:
                eff *= 2
            if 'Rock' in poke.type:
                eff *= 2
            if 'Water' in poke.type:
                eff *= 2
            if 'Bug' in poke.type:
                eff *= 0.5
            if 'Dragon' in poke.type:
                eff *= 0.5
            if 'Fire' in poke.type:
                eff *= 0.5
            if 'Flying' in poke.type:
                eff *= 0.5
            if 'Grass' in poke.type:
                eff *= 0.5
            if 'Poison' in poke.type:
                eff *= 0.5
            if 'Steel' in poke.type:
                eff *= 0.5
        elif self.type == 'Electric':
            if 'Ground' in poke.type or poke.get_ability() == 'Motor Drive' or poke.get_ability() == 'Lightning Rod' or poke.get_ability() == 'Volt Absorb':
                if poke.get_ability() == 'Volt Absorb':
                    poke_func.new_battle_txt(P)
                    if poke.ch < poke.hp:
                        poke_func.battle_write(P,poke.get_name()+" had its","HP restored!")
                    else:
                        poke_func.battle_write(P,poke.get_name()+" was","unaffected!")
                    poke_func.show_ability(P,'Volt Absorb',eturn)
                elif poke.get_ability() == 'Motor Drive':
                    poke_func.show_ability(P,'Motor Drive',eturn)
                elif poke.get_ability() == 'Lightning Rod':
                    poke_func.show_ability(P, 'Lightning Rod', eturn)
                eff *= 0
            if 'Flying' in poke.type:
                if P.battle_weather != None and P.battle_weather[0] == 'Windy' and 'Ground' not in poke.type:
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,"The mysterious strong winds", "weakened the attack!")
                    P.clock.tick(P.bat_spd)
                else:
                    eff *= 2
            if 'Water' in poke.type:
                eff *= 2
            if 'Dragon' in poke.type:
                eff *= 0.5
            if 'Electric' in poke.type:
                eff *= 0.5
            if 'Grass' in poke.type:
                eff *= 0.5
        elif self.type == 'Psychic':
            if 'Dark' in poke.type:
                eff *= 0
            if 'Fighting' in poke.type:
                eff *= 2
            if 'Poison' in poke.type:
                eff *= 2
            if 'Psychic' in poke.type:
                eff *= 0.5
            if 'Steel' in poke.type:
                eff *= 0.5
        elif self.type == 'Ice':
            if 'Dragon' in poke.type:
                eff *= 2
            if 'Flying' in poke.type:
                if P.battle_weather != None and P.battle_weather[0] == 'Windy':
                    poke_func.new_battle_txt(P)
                    poke_func.battle_write(P,"The mysterious strong winds", "weakened the attack!")
                    P.clock.tick(P.bat_spd)
                else:
                    eff *= 2
            if 'Grass' in poke.type:
                eff *= 2
            if 'Ground' in poke.type:
                eff *= 2
            if 'Ice' in poke.type:
                eff *= 0.5
            if 'Water' in poke.type:
                if self.name == 'Freeze-Dry':
                    eff *= 2
                else:
                    eff *= 0.5
            if 'Fire' in poke.type:
                eff *= 0.5
            if 'Steel' in poke.type:
                eff *= 0.5
        elif self.type == 'Dragon':
            if 'Fairy' in poke.type:
                eff *= 0
            if 'Dragon' in poke.type:
                eff *= 2
            if 'Steel' in poke.type:
                eff *= 0.5
        elif self.type == 'Dark':
            if 'Ghost' in poke.type:
                eff *= 2
            if 'Psychic' in poke.type:
                eff *= 2
            if 'Dark' in poke.type:
                eff *= 0.5
            if 'Fairy' in poke.type:
                eff *= 0.5
            if 'Fighting' in poke.type:
                eff *= 0.5
        elif self.type == 'Fairy':
            if 'Dark' in poke.type:
                eff *= 2
            if 'Dragon' in poke.type:
                eff *= 2
            if 'Fighting' in poke.type:
                eff *= 2
            if 'Fire' in poke.type:
                eff *= 0.5
            if 'Poison' in poke.type:
                eff *= 0.5
            if 'Steel' in poke.type:
                eff *= 0.5
        if poke.get_ability() == 'Soundproof' and self.in_soundproof():
            eff = 0
        if P.tourney_battle or P.pokestar_battle != 0:
            if eff == 0.25:
                eff = 0.5
            elif eff == 0.5:
                eff = 0.75
            elif eff == 2:
                eff = 1.5
            elif eff == 4:
                eff = 2
        return eff

    def eff_no_print(self,P,poke,caster = None) -> float:
        eff = 1.0
        cability = ""
        if caster != None:
            cability = caster.get_ability()
            if cability == 'Pixilate' and self.type == 'Normal':
                self.type = 'Fairy'
                eff *= 1.2
            if cability == 'Normalize':
                self.type = 'Normal'
                eff *= 1.2
            if cability == 'Refrigerate' and self.type == 'Ice':
                self.type = 'Fairy'
                eff *= 1.2
            if cability == 'Aerialate' and self.type == 'Normal':
                self.type = 'Flying'
                eff *= 1.2
        if self.type == 'Normal':
            if 'Ghost' in poke.type and poke.idf == False and self.name != 'Struggle' and cability != 'Scrappy':
                eff *= 0
            if 'Steel' in poke.type:
                eff *= 0.5
            if 'Rock' in poke.type:
                eff *= 0.5
        elif self.type == 'Fighting':
            if 'Ghost' in poke.type and cability != 'Scrappy':
                eff *= 0
            if 'Steel' in poke.type:
                eff *= 2
            if 'Rock' in poke.type:
                eff *= 2
            if 'Normal' in poke.type:
                eff *= 2
            if 'Ice' in poke.type:
                eff *= 2
            if 'Dark' in poke.type:
                eff *= 2
            if 'Bug' in poke.type:
                eff *= 0.5
            if 'Fairy' in poke.type:
                eff *= 0.5
            if 'Flying' in poke.type:
                eff *= 0.5
            if 'Poison' in poke.type:
                eff *= 0.5
            if 'Psychic' in poke.type:
                eff *= 0.5
        elif self.type == 'Flying':
            if 'Bug' in poke.type:
                eff *= 2
            if 'Fighting' in poke.type:
                eff *= 2
            if 'Grass' in poke.type:
                eff *= 2
            if 'Electric' in poke.type:
                eff *= 0.5
            if 'Rock' in poke.type:
                eff *= 0.5
            if 'Steel' in poke.type:
                eff *= 0.5
        elif self.type == 'Poison':
            if 'Steel' in poke.type:
                eff *= 0
            if 'Fairy' in poke.type and not (P.loc in ['silfide_gymb','silfide_gym4'] and P.prog[22][3] == 0):
                eff *= 2
            if 'Grass' in poke.type:
                eff *= 2
            if 'Poison' in poke.type:
                eff *= 0.5
            if 'Ground' in poke.type:
                eff *= 0.5
            if 'Rock' in poke.type:
                eff *= 0.5
            if 'Ghost' in poke.type:
                eff *= 0.5
        elif self.type == 'Ground':
            if 'Flying' in poke.type or poke.get_ability() == 'Levitate' or poke.magnet_rise > 0:
                eff *= 0
            if 'Electric' in poke.type:
                eff *= 2
            if 'Fire' in poke.type:
                eff *= 2
            if 'Poison' in poke.type:
                eff *= 2
            if 'Rock' in poke.type:
                eff *= 2
            if 'Steel' in poke.type:
                eff *= 2
            if 'Bug' in poke.type:
                eff *= 0.5
            if 'Grass' in poke.type:
                eff *= 0.5
        elif self.type == 'Rock':
            if 'Bug' in poke.type:
                eff *= 2
            if 'Fire' in poke.type:
                eff *= 2
            if 'Flying' in poke.type and not (P.battle_weather != None and P.battle_weather[0] == 'Windy'):
                eff *= 2
            if 'Ice' in poke.type:
                eff *= 2
            if 'Fighting' in poke.type:
                eff *= 0.5
            if 'Ground' in poke.type:
                eff *= 0.5
            if 'Steel' in poke.type:
                eff *= 0.5
        elif self.type == 'Bug':
            if 'Dark' in poke.type:
                eff *= 2
            if 'Grass' in poke.type:
                eff *= 2
            if 'Psychic' in poke.type:
                eff *= 2
            if 'Fairy' in poke.type:
                eff *= 0.5
            if 'Fighting' in poke.type:
                eff *= 0.5
            if 'Fire' in poke.type:
                eff *= 0.5
            if 'Flying' in poke.type:
                eff *= 0.5
            if 'Ghost' in poke.type:
                eff *= 0.5
            if 'Poison' in poke.type:
                eff *= 0.5
            if 'Steel' in poke.type:
                eff *= 0.5
        elif self.type == 'Ghost':
            if 'Normal' in poke.type:
                eff *= 0
            if 'Ghost' in poke.type:
                eff *= 2
            if 'Psychic' in poke.type:
                eff *= 2
            if 'Dark' in poke.type:
                eff *= 0.5
        elif self.type == 'Steel':
            if 'Fairy' in poke.type and not (P.loc in ['silfide_gymb','silfide_gym4'] and P.prog[22][3] == 0):
                eff *= 2
            if 'Ice' in poke.type:
                eff *= 2
            if 'Rock' in poke.type:
                eff *= 2
            if 'Electric' in poke.type:
                eff *= 0.5
            if 'Fire' in poke.type:
                eff *= 0.5
            if 'Steel' in poke.type:
                eff *= 0.5
            if 'Water' in poke.type:
                eff *= 0.5
        elif self.type == 'Fire':
            if 'Bug' in poke.type:
                eff *= 2
            if 'Grass' in poke.type:
                eff *= 2
            if 'Ice' in poke.type:
                eff *= 2
            if 'Steel' in poke.type:
                eff *= 2
            if 'Dragon' in poke.type:
                eff *= 0.5
            if 'Fire' in poke.type:
                if poke.get_ability() == 'Flash Fire':
                    eff *= 0
                else:
                    eff *= 0.5
            if 'Rock' in poke.type:
                eff *= 0.5
            if 'Water' in poke.type:
                eff *= 0.5
        elif self.type == 'Water':
            if poke.get_ability() == 'Storm Drain' or poke.get_ability() == 'Water Absorb':
                eff *= 0
            if 'Fire' in poke.type:
                eff *= 2
            if 'Ground' in poke.type:
                eff *= 2
            if 'Rock' in poke.type:
                eff *= 2
            if 'Dragon' in poke.type:
                eff *= 0.5
            if 'Grass' in poke.type:
                eff *= 0.5
            if 'Water' in poke.type:
                eff *= 0.5
        elif self.type == 'Grass':
            if 'Ground' in poke.type:
                eff *= 2
            if 'Rock' in poke.type:
                eff *= 2
            if 'Water' in poke.type:
                eff *= 2
            if 'Bug' in poke.type:
                eff *= 0.5
            if 'Dragon' in poke.type:
                eff *= 0.5
            if 'Fire' in poke.type:
                eff *= 0.5
            if 'Flying' in poke.type:
                eff *= 0.5
            if 'Grass' in poke.type:
                eff *= 0.5
            if 'Poison' in poke.type:
                eff *= 0.5
            if 'Steel' in poke.type:
                eff *= 0.5
        elif self.type == 'Electric':
            if 'Ground' in poke.type or poke.get_ability() == 'Motor Drive' or poke.get_ability() == 'Lightning Rod' or poke.get_ability() == 'Volt Absorb':
                eff *= 0
            if 'Flying' in poke.type and not (P.battle_weather != None and P.battle_weather[0] == 'Windy'):
                eff *= 2
            if 'Water' in poke.type:
                eff *= 2
            if 'Dragon' in poke.type:
                eff *= 0.5
            if 'Electric' in poke.type:
                eff *= 0.5
            if 'Grass' in poke.type:
                eff *= 0.5
        elif self.type == 'Psychic':
            if 'Dark' in poke.type:
                eff *= 0
            if 'Fighting' in poke.type:
                eff *= 2
            if 'Poison' in poke.type:
                eff *= 2
            if 'Psychic' in poke.type:
                eff *= 0.5
            if 'Steel' in poke.type:
                eff *= 0.5
        elif self.type == 'Ice':
            if 'Dragon' in poke.type:
                eff *= 2
            if 'Flying' in poke.type and not (P.battle_weather != None and P.battle_weather[0] == 'Windy'):
                eff *= 2
            if 'Grass' in poke.type:
                eff *= 2
            if 'Ground' in poke.type:
                eff *= 2
            if 'Ice' in poke.type:
                eff *= 0.5
            if 'Water' in poke.type:
                if self.name == 'Freeze-Dry':
                    eff *= 2
                else:
                    eff *= 0.5
            if 'Fire' in poke.type:
                eff *= 0.5
            if 'Steel' in poke.type:
                eff *= 0.5
        elif self.type == 'Dragon':
            if 'Fairy' in poke.type:
                eff *= 0
            if 'Dragon' in poke.type:
                eff *= 2
            if 'Steel' in poke.type:
                eff *= 0.5
        elif self.type == 'Dark':
            if 'Ghost' in poke.type:
                eff *= 2
            if 'Psychic' in poke.type:
                eff *= 2
            if 'Dark' in poke.type:
                eff *= 0.5
            if 'Fairy' in poke.type:
                eff *= 0.5
            if 'Fighting' in poke.type:
                eff *= 0.5
        elif self.type == 'Fairy':
            if 'Dark' in poke.type:
                eff *= 2
            if 'Dragon' in poke.type:
                eff *= 2
            if 'Fighting' in poke.type:
                eff *= 2
            if 'Fire' in poke.type:
                eff *= 0.5
            if 'Poison' in poke.type:
                eff *= 0.5
            if 'Steel' in poke.type:
                eff *= 0.5
        if poke.get_ability() == 'Soundproof' and self.in_soundproof():
            eff = 0
        if caster != None and self.type in caster.type:
            if cability == 'Adaptability':
                eff *= 2
            else:
                eff *= 1.5
        if P.tourney_battle or P.pokestar_battle != 0:
            if eff == 0.25:
                eff = 0.5
            elif eff == 0.5:
                eff = 0.75
            elif eff == 2:
                eff = 1.5
            elif eff == 4:
                eff = 2
        return eff

    def is_contact(self):
        if self.cat == '0':
            if self.name not in ['Attack Order','Barrage','Beak Blast','Beat Up','Bone Club','Bone Rush','Bonemerang','Bulldoze','Bullet Seed','Diamond Storm','Earthquake','Egg Bomb','Explosion','Feint','Fissure','Fling','Freeze Shock','Fusion Bolt','Gunk Shot','Ice Shard','Icicle Crash','Icicle Spear',"Land's Wrath",'Leafage','Magnet Bomb','Magnitude','Metal Burst','Natural Gift','Pay Day','Petal Blizzard','Pin Missile','Poison Sting','Precipice Blades','Present','Psycho Cut','Razor Leaf','Rock Blast','Rock Slide','Rock Throw','Rock Tomb','Rock Wrecker','Sacred Fire','Sand Tomb','Secret Power','Seed Bomb','Self-Destruct','Shadow Bone','Sky Attack','Smack Down','Spike Cannon','Spirit Shackle','Stone Edge','Thousand Arrows','Thousand Waves','Twineedle']:
                return True
            return False
        if self.cat == '1':
            if self.name not in ['Infestation','Draining Kiss','Grass Knot','Wring Out','Trump Card','Petal Dance']:
                return False
            return True
        return False

    def in_soundproof(self):
        return self.name in ['Boomburst','Bug Buzz','Chatter','Clanging Scales','Confide','Disarming Voice','Echoed Voice','Grass Whistle','Growl','Hyper Voice','Metal Sound','Noble Roar','Parting Shot','Relic Song','Roar','Round','Screech','Sing','Snarl','Snore','Sparkling Aria','Supersonic','Uproar']




def print_fail(P):
    poke_func.new_battle_txt(P)
    poke_func.battle_write(P, "But it failed!")
    P.clock.tick(P.bat_spd)

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


