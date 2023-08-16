from items import item
from equipment import external_lootItem,coins
import random
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'  # Reset text color to default
    
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

#creating the array to hold item classes
inventory = []
item_pool = [] # helps with getting pool for a random selection each visit
# Loop to populate the loot pool
for item_name in  rare_wep_pool + rare_helm_pool + rare_chest_pool + rare_leg_pool + rare_trinket_pool + rare_cape_pool + rare_shoulder_pool + rare_boot_pool:
    item_type = item_name.split()[-1]  # Extract the last word as item type
    random_damage = random.randint(4, 12)
    random_health = random.randint(4, 12)
    item_pool.append(item(item_name, random_damage, random_health, item_type))

def generateShop():

    for i in range (1,10+1):
        random_item = random.randint(0,len(item_pool) - 1)
        inventory.append(item_pool[random_item])
         
def openShop():
    print("\n[Mackle's Tackle]")
    i = 0    
    for inventory_item in inventory: # loops through items in inventory array
        i +=1
        random_cost = random.randint(1,10)
        inventory_item.cost = random_cost
        print("[" + str(i) + "] " + GREEN + inventory_item.name + RESET  + " Health: " + str(inventory_item.hp) + " Damage: " + str(inventory_item.dmg) + " Type: "+str(inventory_item.type) + " Cost :" + str(inventory_item.cost) + " coins" )
    if len(inventory) != 0: # Confirm inventory isn't empty prior to asking to equip
        try:
            purchaseChoice = int(input("Would you like to purchase any of these? If so, enter the number prefixing the item! [Number/No]"))
            purchaseItem(purchaseChoice)
        except ValueError: # if anything but int returned
            pass  

def purchaseItem(id):
    global coins
    
    targetItem = inventory[id-1]
    print(coins)
    if coins < targetItem.cost:
        print("You can't afford that! You need " + str(targetItem.cost - coins) + " more coin(s).")
    else:
        external_lootItem(targetItem)
        inventory.pop(id-1)
    openShop() 
generateShop()
