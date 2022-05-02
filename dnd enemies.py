

"""
DND Enemies

Class
Race
Weapons -> {Damage, Reach, Type}
Stats -> {Str, Dex, Con, Int, Wis, Cha}
Speed

"""
from abc import ABC, abstractmethod
from enum import Enum

class Class(Enum):
    Wizard = 0,
    Fighter = 1,
    Cleric = 2

class Race(Enum):
    Humans = 0,
    Elf = 1,
    Orc = 2

class WeaponType(Enum):
    Piercing = 0,
    Slashing = 1,
    Bludgeoning = 2

class Stats:
    def __init__(self, Str, Dex, Wis, Int, Con, Cha):
        self.Str = Str
        self.Dex = Dex
        self.Wis = Wis
        self.Int = Int
        self.Con = Con
        self.Cha = Cha

class Weapon:
    def __init__(self, Damage, Reach, Type):
        self.Damage: int = Damage
        self.Reach: int = Reach
        self.Type: WeaponType = Type

class EnemyBase(ABC):
    @property
    @abstractmethod
    def Race(self) -> Race: ...


    # def __init__(self, Class, Weapon, Stats, Speed):
    #     self.Class: Class = Class
    #     self.Weapon: Weapon = Weapon
    #     self.Stats: Stats = Stats
    #     self.Speed: int = Speed

class HumanEnemy(EnemyBase):
    @property
    def Race(self): return Race.Humans


    @property
    def Weapon(self): return Weapon.__init__(self, 10, 10, "salshing")

class ElfEnemy(EnemyBase):
    @property
    def Race(self): return Race.Elf

class OrcEnemy(EnemyBase):
    @property
    def Race(self): return Race.Orc

class EnemyCreatorBase(ABC):

    @abstractmethod
    def createEnemy(self) -> EnemyBase: ...

class HumanEnemyCreator(EnemyCreatorBase):
    def createEnemy(self) -> EnemyBase:
        return HumanEnemy()

class ElfEnemyCreator(EnemyCreatorBase):
    def createEnemy(self):
        return ElfEnemy()

class OrcEnemyCreator(EnemyCreatorBase):
    def createEnemy(self):
        return OrcEnemy()

class EnemyFactory():
    def __init__(self, creator: EnemyCreatorBase):
        self.creator = creator

    def createEnemy(self) -> EnemyBase:
        return self.creator.createEnemy()


factory = EnemyFactory(HumanEnemyCreator())

i = 0
while i < 10:
    enemy = factory.createEnemy()
    print('Enemy', i, enemy.Race, HumanEnemy.Weapon)
    i = i+1
