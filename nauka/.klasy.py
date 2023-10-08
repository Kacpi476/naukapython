class Player:
    def __init__(self, id, hp, dmg):
        self.id = id
        self.hp = hp
        self.dmg = dmg

    def PlayerInfo(self):
        print("Twoje ID to: ", self.id)
        print("Twoje HP to: ", self.hp)
        print("Twoje obrażenia to: ", self.dmg)

p1 = Player(1, 100, 25)
p2= Player(2, 75, 30)

p1.PlayerInfo()
p2.PlayerInfo()