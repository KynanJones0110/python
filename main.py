import random
import time
from equipment import lootItem, initEquip, equipItem, viewInventory, viewEquipped,inventory,equipped,updateEquip,loot_pool,GREEN,YELLOW,RED,RESET,coins,getCoins
from items import item
from merchant import openShop



    
    
class entity():
    exp_to_ding = 150
    inventory= []
    def __init__(self,name,hp,dmg,level):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.level = level
        self.alive = True
        self.maxhp = hp
        self.exp = 0
 
#Derived Class      
class Interactable(entity):
    def __init__self(self,name,hp,dmg,level):
        super().__init__self(name,hp,dmg,level)
    def attack(self,target):
        target.hp -= self.dmg
        print(self.name + " hits " + target.name + " for " + RED + str(self.dmg) + RESET + " HP!")
        if target.hp <= 0:
            target.death(target)
        else:
             print(target.name + " now has " + RED + str(target.hp) + RESET + " HP left!")
    #Death Func       
    def death(self,target):
        print("\n" + RED + target.name + " is dead!" + RESET)
        self.alive = False
# Drink Pot
def drinkPotion(source):
    if source.hp == source.maxhp:
        print("You're already at full health!")
    else:
        source.hp += 5
        print(GREEN + source.name + " drinks a potion! They now have "+str(source.hp)+"hp" + RESET)
#Run
def flee(player):
    print("You attempt to flee!")
    pass
# EXPERIENCE GAIN AND LEVEL
def gainExp(player,xp):
    player.exp = player.exp + xp
    if player.exp >= player.exp_to_ding:
        player.level += 1
        player.exp = player.exp - player.exp_to_ding
        player.exp_to_ding *=2
        
        print("\n" + YELLOW + "[*] Ding! You've reached Level " + str(player.level) + " [*]\n" + RESET)
        
        print("Current Experience: " + str(player.exp) + "/" + str(player.exp_to_ding)+"\n")
    else:
        print("Current Experience: (" + str(player.exp) + "/" + str(player.exp_to_ding) +")\n")
    lootItem()    

#spawn random goblin
def genL1():
    level = random.randint(player.level,player.level + 5)
    hp = level * 10
    dmg = level + 5
    name_id = random.randint(1,len(goblin_name_pool)-1)
    temp_enemy = Interactable(goblin_name_pool[name_id],hp,dmg,level)
    temp_enemy.exp = level + dmg + hp + 100
    return temp_enemy

def gen_boss():
    level = player.level + 5
    hp = level * 20
    dmg = level + 10
    temp_enemy = Interactable("Glizzy Gobbler",hp,dmg,level)
    temp_enemy.exp = level + dmg + hp + 1000
    return temp_enemy

#combat state
def combat(player,target):
    
    print(RED + target.name + " appears and prepares to attack!" + RESET)
    # Enemy Stats:Level6 HP:60 DMG:11Total Exp Worth:77
    print("Enemy Stats: " + "Level " + str(target.level) + " HP:" + str(target.hp) + " DMG:"+ str(target.dmg) + " XP Worth:"+str(target.exp))
    print("\n")
    while player.alive and target.alive:
        try:
            action = int(input("Select an action [1] Attack [2] Drink Potion [3] Flee\n> "))
            if action == 1:
                player.attack(target)
            elif action == 2:
                drinkPotion(player)
            elif action == 3:
                flee(player)
            if target.alive == False: # only need to break here as player death will kill the loop before it can iterate back
                gainExp(player,target.exp)
                break
            random_act = random.randint(1,6)
            if random_act != 5:
                target.attack(player)
            else:
                drinkPotion(target)
            print("\n")
        except ValueError:
            print("Unknown option")
            continue
    print("\nBattle Over!\n") 
            

#prints player stats
def checkStats():
    print("\nCurrent Stats: " + "Level " + str(player.level) + " HP:" + str(player.hp) + " DMG:"+ str(player.dmg) + " XP:"+str(player.exp)+"/"+str(player.exp_to_ding)+"\n")
#updates stat modifiers via gear
def updateStats():
        # First, subtract the previously added modifiers
    player.dmg -= sum(item.dmg for item in equipped)
    player.hp -= sum(item.hp for item in equipped)
    updateEquip()
    # Then calculate and add the new modifiers
    dmg_mod = sum(item.dmg for item in equipped)
    hp_mod = sum(item.hp for item in equipped)

    player.dmg += dmg_mod
    player.hp += hp_mod
 # out of combat game loop
def adventure():
    boss_step=0
    show_action = True
    temp_blank = "hi"
    for char in temp_blank:#story_intro:
        print(char, end='',flush=True)
        time.sleep(0.02)
    print("\n")   
        
    while player.alive:
        try:
            updateStats()
            if show_action:
                time.sleep(1.0)
                action = int(input("What action would you like to take next?\n\n[1.Walk Forwards] [2.Turn Right] [3.Turn Left]\n[4.Drink Potion] [5.Check Inventory] [6.Check Stats]\n[7.Quit Game] [8.Hide/Show Full Action Options]\n> "))
            else:
                action = int(input("> "))
            plot_fluff = random.randint(1,4)
            if action == 4:
                boss_step += 1
                drinkPotion(player)
                continue 
            if action == 69:
                player.hp = 1000
                print("HP cheat activated")
                continue
            if action == 420:
                player.dmg = 1000
                print("DMG cheat activated")
                continue
            if action == 5:
                viewInventory()
            if action == 6:
                checkStats()
                viewEquipped()
                continue
            if action == 7:
                return 1
            if action == 8:
                if show_action == False:
                    print("Showing All Actions")
                    show_action = True
                else:    
                    show_action = False
                    print("Hiding All Actions")
                continue
            
            if plot_fluff == 1 or boss_step in KEY_STEPS: # nothing but keep actions for more expansive 
                boss_step += 1
                if action == 1:
                    environment_rig(boss_step)
                elif action == 2:
                    environment_rig(boss_step)
                elif action == 3:
                    environment_rig(boss_step)
                else:
                    print("Unknown option")
            if plot_fluff == 2: # loot
                if action == 1:
                    print("You stumble apon a chest and open it!")
                    lootItem()          
                elif action == 2:
                    print("You stumble apon a chest and open it!")
                    lootItem()   
                elif action == 3:
                    print("You stumble apon a chest and open it!")
                    lootItem() 
                else:
                    print("Unknown option") 
            if plot_fluff == 3:
                if action == 1:
                    combat(player,genL1())
                    pass
                elif action == 2:
                    combat(player,genL1())
                elif action == 3:
                    combat(player,genL1())
            if plot_fluff == 4:
                goShop = int(input("You see a merchant! Do you want to visit the shop? [1] for yes atm"))
                if goShop == 1:
                    getCoins()
                    openShop()
        except ValueError:
            print("Unknown action")
            continue      
              
story_intro = "In a realm enshrouded by ancient myths and impending darkness, a valiant hero emerges as the last hope against an encroaching terror. A malevolent Demon Lord, born from the depths of obscurity, casts its ominous shadow over distant lands. With courage ablaze, the hero embarks on a quest, gathering companions and defying destiny, as they march toward an epic confrontation destined to shape the fate of their world."

def environment_rig(step):
    print(step)
    if step < 3:
        print("Nothing here but in the distance, the castle appears to be getting closer.")
    if step == 3:
        print("You enter a forest filled with massive trees!")
    if step >= 4 and step < 7:
        print("Nothing here but, but within the Forest the castle can barely be seen amongst the ancient trees.")
    elif step == 7:
        print("You step onto the bridge leading to the castle.")
    elif step > 7 and step < 10:
        print("You continue to walk across the bridge")
    elif step == 10:
        print("The doors slam open and you get pulled into the castle! The doors slam shut behind you.")
    elif step > 10 and step < 13:
        print("You walk through the Castle Halls, hearing ominous breathing pulsating around the space")
    elif step == 13:
        print("Glizzy Gobbler: \"Another meal coming straight to me, excellent.\"")
        combat(player,gen_boss())
        
KEY_STEPS = [5,10,15,18,20]  
#player creation and general structure variables 
player = Interactable("Gary",1000,1001,1)  
plot = ["Castle","Mountain","Large Creature"]
plot_level = 0
environment = ""

# pool of names for goblin classes  
goblin_name_pool = ["Gnarltooth", "Snaggletoes", "Mudgrub", "Zigzag", "Squibbles",
    "Gobblefist", "Ratbag", "Stinkfoot", "Bristleback", "Snotnose",
    "Fangface", "Wartwart", "Greasefingers", "Muckmuzzle", "Grumblebelly",
    "Scuttlebutt", "Grubgrinder", "Gloomgut", "Scrapskull", "Moldysnout"]

def main():    
    adventure()
    
if __name__ == '__main__':
    main()


