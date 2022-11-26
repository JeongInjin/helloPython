# 상속
from turtle import speed


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("지상 유닛 이동")
        print("{0}: {1} 방향으로 이동.[속도 {2}]".format(self.name, location, self.speed))


class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0}: {1} 방향으로 공격 합니다.[공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0}, {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0}: 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))


print("---")
firebat1 = AttackUnit("파이어뱃", 50, 16, 0)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)

print("----------------")


# 다중 상속
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0}: {1} 방향으로 날아갑니다.[속도{2}]".format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("공중 유닛 이동")
        self.fly(self.name, location)


valkyrie = AttackUnit("발키리", 200, 6, 5)
valkyrie.move("3시")

valture = AttackUnit("벌쳐", 80, 10, 20)
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

valture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")

print("----------------")
# Pass
class BuildingUnitPass(Unit):
    def __int__(self, name, hp, location):
        pass


sypply_depot = BuildingUnitPass("서플라이 디폿", 500, "7시")


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    pass


game_start()
game_over()
print("----------------")
# Super
class BuildingUnit(Unit):
    def __int__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location















