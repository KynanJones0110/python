class item:
    nature = ""
    bonus_text = "None"
    bonus_dmg = 0
    cost = 0
    def __init__(self,name,hp,dmg,type):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.type = type
    def special_ability(self):
        print("Item goes brr")
