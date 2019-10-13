import random
class Warrior:
    health=0
    attack_power=0
    name=""
    n=0
    def __init__(self,name):
        self.name=name
        self.health=random.randint(100,150)
        self.attack_power=random.randint(20,30)
    def show_health(self):
        return self.health
    def show_attack_power(self):
        if self.n==2:
            p = random.random()
            if p < 0.2:
                new_power = 2 * self.attack_power
                return new_power
            else:
                return self.attack_power
        else:
            return self.attack_power

    def DamageReceived(self,hit):
        self.health=self.health-hit
        if self.health<0:
            print(self.name, " получил ", hit, " урона и погиб.")
        else:
            print(self.name, " получил ", hit, " урона.", "Осталось ", self.health, " здоровья")

class WarriorWithShield(Warrior):
    n=1
    защита=random.randint(5,10)
    def DamageReceived(self,hit):
        Warrior.DamageReceived(self,hit-self.защита)

class WarriorExpert(Warrior):
    n=2




#1 задание
print("Сила атаки воинов")
warrior1=Warrior("Воин1")
warrior2=WarriorWithShield("Воин2")
warrior3=WarriorExpert("Воин3")
print(warrior1.show_attack_power())
print(warrior2.show_attack_power())
print(warrior3.show_attack_power())


#2 задание
print("Бой между двумя воинами")
def battle_w1(w1,w2):
    r=2
    while w1.show_health()>=0 and w2.show_health()>=0:
        if r==2:
            w2.DamageReceived(w1.show_attack_power())
            r=1
        elif r==1:
            w1.DamageReceived(w2.show_attack_power())
            r=2
    if w1.show_health()<=0:
        print("Победил", w2.name)
    else:
        print("Победил", w1.name)

one1=Warrior("первый")
two1=WarriorWithShield("второй")
battle_w1(one1,two1)
one2=Warrior("первый")
tree2=WarriorExpert("третий")
battle_w1(one2,tree2)
two3=WarriorWithShield("второй")
tree3=WarriorExpert("третий")
battle_w1(two3,tree3)

#3 задание
print("Бой между двумя армиями")
army1=[Warrior('Воин' + str(i + 1) + ' из армии 1') for i in range(4)] + [WarriorWithShield('Воин со щитом' + str(i + 1) + ' из армии 1') for i in range(4)] + [WarriorExpert('Воин эксперт' + str(i + 1) + ' из армии 1') for i in range(2)]
army2=[Warrior('Воин' + str(i + 1) + ' из армии 2') for i in range(4)] + [WarriorWithShield('Воин со щитом' + str(i + 1) + ' из армии 2') for i in range(4)] + [WarriorExpert('Воин эксперт' + str(i + 1) + ' из армии 2') for i in range(2)]
def battle_w2(w1,w2):
    r=2
    while w1.show_health()>=0 and w2.show_health()>=0:
        if r==2:
            w2.DamageReceived(w1.show_attack_power())
            r=1
        elif r==1:
            w1.DamageReceived(w2.show_attack_power())
            r=2
while len(army1)>0 and len(army2)>0:
    rand1=random.randint(0,len(army1)-1)
    rand2=random.randint(0,len(army2)-1)
    battle_w2(army1[rand1], army2[rand2])
    if army1[rand1].show_health()<0:
        army1.pop(rand1)
    else:
        army2.pop(rand2)
if len(army1)==0:
    print("Победила армия 2")
else:
    print("Победила армия 1")

