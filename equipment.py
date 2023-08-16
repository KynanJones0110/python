import random
from items import item

#creating the array to hold item classes
inventory = [
            item("Family Artifact",3,3,"Talisman"),
            item("Family hehe",3,3,"Talisman"),
            item("Family Artifact",5,5,"Spaulders"),
            item("Dirty Cape",5,5,"Cape")
             ]
equipped = [item("Wooden Sword",0,1,"Sword"),
            item("Nothing",0,0,"Leggings"),
            item("Nothing",0,0,"Chestpiece"),
            item("Nothing",0,0,"Boots"),
            item("Nothing",0,0,"Helm"),
            item("Nothing",0,0,"Talisman"),
            item("Nothing",0,0,"Cape"),
            item("Nothing",0,0,"Shoulders")
            ]

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'  # Reset text color to default

coins = 10
# Define constants for item types
WEP_TYPES = ["Sword", "Dagger", "Axe"]
LEG_TYPES = ["Leggings", "Pants", "Greaves"]
CHEST_TYPES = ["Chestpiece", "Breastplate", "Tunic"]
FEET_TYPES = ["Boots", "Greaves", "Treads"]
TRINK_TYPES = ["Talisman", "Amulet", "Pendant","Medallion"]
CAPE_TYPES = ["Cape", "Cloak", "Drape"]
SHLDR_TYPES = ["Shoulderplates", "Pauldrons", "Spaulders", "Shoulders"]

def getCoins():
    print(YELLOW + "You have " + str(coins) + " coins" + RESET)
def viewEquipped():
    print("\n[Equipped]")
    i = 0
    temp_test = 0
    for equipped_items in equipped: # loops through items in equipped array
        i +=1
        if equipped_items.name == "Nothing":
            print("[" + str(i) + "] " + RED + equipped_items.name + RESET + " Health:" + str(equipped_items.hp) + " Damage:" + str(equipped_items.dmg) +" Type:"+str(equipped_items.type))
        else:
            print("[" + str(i) + "] " + GREEN + equipped_items.name + RESET + " Health:" + str(equipped_items.hp) + " Damage:" + str(equipped_items.dmg) +" Type:"+str(equipped_items.type))

def viewInventory():
    print("\n[Inventory]")
    i = 0    
    for inventory_item in inventory: # loops through items in inventory array
        i +=1
        print("[" + str(i) + "] " + GREEN + inventory_item.name + RESET  + " Health: " + str(inventory_item.hp) + " Damage: " + str(inventory_item.dmg) + " Type: "+str(inventory_item.type) )
    if len(inventory) != 0: # Confirm inventory isn't empty prior to asking to equip
        try:
            equipChoice = int(input("Would you like to equip any of these items? If so, enter the number prefixing the item! [Number/No]"))
            equipItem(equipChoice)
        except ValueError: # if anything but int returned
            pass  

def lootItem(): # loot random item
    rand_chance = random.randint(2,50)
    if rand_chance == 1:
        print("You looted: " + YELLOW + str(rand_chance) + " coins!" + RESET)
        coins +=rand_chance
    else:
        rand_loot = random.randint(0, (len(loot_pool) - 1))
        looted = loot_pool[rand_loot] 
        print("You looted: " + GREEN + looted.name + RESET)
        inventory.append(looted)
        
def external_lootItem(looted): # loot random item
        global coins
        inventory.append(looted)
        coins -= looted.cost
        print("You purchased " + looted.name + "!")
        getCoins()

def initEquip(): # initalizes variables for equipment on start 
    global equipped_weapon, equipped_legs, equipped_chest, equipped_boots, equipped_helm, equipped_trinket, equipped_cape, equipped_shoulders
    equipped_weapon = equipped[0]
    equipped_legs = equipped[1]
    equipped_chest = equipped[2]
    equipped_boots = equipped[3]
    equipped_helm = equipped[4]
    equipped_trinket = equipped[5]
    equipped_cape = equipped[6]
    equipped_shoulders = equipped[7]
      
def updateEquip(): # update equipment values, will handle modifiers (stats)
    global equipped_weapon, equipped_legs, equipped_chest, equipped_boots, equipped_helm, equipped_trinket, equipped_cape, equipped_shoulders
    equipped[0] = equipped_weapon
    equipped[1] = equipped_legs
    equipped[2] = equipped_chest
    equipped[3] = equipped_boots
    equipped[4] = equipped_helm
    equipped[5] = equipped_trinket
    equipped[6] = equipped_cape
    equipped[7] = equipped_shoulders 

def equipItem(id): # equipping an item, ID is passed from inventory index (-1)
    global equipped_weapon, equipped_legs, equipped_chest, equipped_boots, equipped_helm, equipped_trinket, equipped_cape, equipped_shoulders
    try: 
        toEquip = inventory[id - 1]
        if toEquip.type == "Nothing":
            skip = True
        if toEquip.type in WEP_TYPES:
            if equipped_weapon and equipped_weapon.name != "Nothing":
                print("\nYou unequipped " + GREEN + equipped_weapon.name + RESET)
                inventory.append(equipped_weapon)
                equipped_weapon = toEquip
                inventory.pop(id - 1)
            else:
                inventory.pop(id - 1)
                equipped_weapon = toEquip   
        elif toEquip.type in LEG_TYPES:
            if equipped_legs and equipped_legs.name != "Nothing":
                print("\nYou unequipped " + GREEN + equipped_legs.name + RESET)
                inventory.append(equipped_legs)
                equipped_legs = toEquip
                inventory.pop(id - 1)
            else:
                inventory.pop(id - 1) 
                equipped_legs = toEquip         
        elif toEquip.type in CHEST_TYPES:
            if equipped_chest and equipped_chest.name != "Nothing":
                print("\nYou unequipped " + GREEN + equipped_chest.name + RESET) 
                inventory.append(equipped_chest)
                equipped_chest = toEquip
                inventory.pop(id - 1)
            else:
                inventory.pop(id - 1)     
                equipped_chest = toEquip        
        elif toEquip.type in FEET_TYPES:
            if equipped_boots and equipped_boots.name != "Nothing":
                print("\nYou unequipped " + GREEN + equipped_boots.name + RESET)
                inventory.append(equipped_boots)
                equipped_boots = toEquip
                inventory.pop(id - 1)
            else:
                inventory.pop(id - 1)   
                equipped_boots = toEquip  
        elif toEquip.type == "Helm" :
            if equipped_helm and equipped_helm.name != "Nothing":
                print("\nYou unequipped " + GREEN + equipped_helm.name + RESET)
                inventory.append(equipped_helm)
                equipped_helm = toEquip
                inventory.pop(id - 1)
            else:
                inventory.pop(id - 1)  
                equipped_helm = toEquip
                                             
        elif toEquip.type in TRINK_TYPES:
            if equipped_trinket and equipped_trinket.name != "Nothing":
                print("\nYou unequipped " + GREEN + equipped_trinket.name + RESET)
                inventory.append(equipped_trinket)
                equipped_trinket = toEquip
                inventory.pop(id - 1)
            else:
                inventory.pop(id - 1) 
                equipped_trinket = toEquip
                 
        elif toEquip.type in CAPE_TYPES:
            if equipped_cape and equipped_cape.name != "Nothing":
                print("\nYou unequipped " + GREEN + equipped_cape.name + RESET)
                inventory.append(equipped_cape)
                equipped_cape = toEquip
                inventory.pop(id - 1)
            else:
                inventory.pop(id - 1)  
                equipped_cape = toEquip                                   
        elif toEquip.type in SHLDR_TYPES:
            if equipped_shoulders and equipped_shoulders.name != "Nothing":
                print("\nYou unequipped " + GREEN + equipped_shoulders.name + RESET)
                inventory.append(equipped_shoulders)
                equipped_shoulders = toEquip
                inventory.pop(id - 1)
            else:
                inventory.pop(id - 1) 
                equipped_shoulders = toEquip
                   
        print("\nYou equipped " + GREEN + toEquip.name + RESET)
        viewInventory()
    except IndexError:
        print("Item doesn't exist")
        viewInventory()
  
# Weapons
poor_wep_pool = ["Wooden Dagger", "Wooden Sword", "Rusty Axe", "Cracked-Iron Sword", "Buckled Sword"]
rare_wep_pool = ["Silver Dagger", "Iron Sword", "Obsidian Sword", "Steel Axe", "Enchanted Sword"]
# Helmets
poor_helm_pool = ["Cloth Helm", "Wooden Helm", "Leather Helm", "Tarnished Helm", "Cracked Helm"]
rare_helm_pool = ["Enchanted Helm", "Steel Helm", "Golden Helm", "Emerald Helm", "Ancient Helm"]
# Chestpieces
poor_chest_pool = ["Bronze Chestpiece", "Leather Tunic", "Tattered Tunic", "Ragged Tunic", "Frayed Chestpiece"]
rare_chest_pool = ["Platinum Chestpiece", "Mage's Tunic", "Diamond Breastplate", "Sapphire Chestpiece", "Royal Chestguard"]
# Leggings
poor_leg_pool = ["Plate Leggings", "Chainmail Leggings", "Torn Pants", "Ragged Greaves", "Threadbare Leggings"]
rare_leg_pool = ["Dragonbone Blade", "Crystal Vambraces", "Silver Legplates", "Emerald Leggings", "Ancient Legguards"]
# Trinkets
poor_trinket_pool = ["Ruby Amulet", "Sapphire Amulet", "Cracked Amulet", "Tarnished Medallion", "Chipped Medallion"]
rare_trinket_pool = ["Emerald Talisman", "Ancient Talisman", "Enchanted Talisman", "Golden Talisman", "Celestial Amulet"]
# Capes
poor_cape_pool = ["Tattered Cape", "Phoenix Feather Cloak", "Worn Cape", "Tattered Drape", "Threadbare Cape"]
rare_cape_pool = ["Silk Cape", "Woven Cloak", "Enchanted Cloak", "Jeweled Drape", "Royal Drape"]
# Shoulders
poor_shoulder_pool = ["Ragged Shoulderplates", "Tattered Pauldrons", "Threadbare Spaulders", "Worn Spaulders", "Cracked Pauldrons"]
rare_shoulder_pool = ["Enchanted Shoulderplates", "Emerald Pauldrons", "Silver Spaulders", "Golden Pauldrons", "Ancient Shoulderplates"]
# Boots
poor_boot_pool = ["Tattered Boots", "Worn Treads", "Threadbare Boots", "Ragged Treads", "Cracked Boots"]
rare_boot_pool = ["Enchanted Greaves", "Emerald Cloth Greaves", "Silver Greaves", "Golden Greaves", "Ancient War Boots"]

# Create a list to hold instances of the item class
loot_pool = []
# Loop to populate the loot pool
for item_name in poor_wep_pool + rare_wep_pool + poor_helm_pool + rare_helm_pool + poor_chest_pool + rare_chest_pool + poor_leg_pool + rare_leg_pool + poor_trinket_pool + rare_trinket_pool + poor_cape_pool + rare_cape_pool + poor_shoulder_pool + rare_shoulder_pool + poor_boot_pool + rare_boot_pool:
    item_type = item_name.split()[-1]  # Extract the last word as item type
    random_damage = random.randint(0, 4)
    random_health = random.randint(0, 4)
    loot_pool.append(item(item_name, random_damage, random_health, item_type))

initEquip()
