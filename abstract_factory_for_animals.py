from abc import ABC, abstractmethod
from enum import Enum


class Species(Enum):
    Dog = 0
    Cat = 1


class Sound(Enum):
    bark = 0,
    meow = 1


class Hunt(Enum):
    SmallGame = 0,
    BigGame = 1


class AnimalBase(ABC):
    @property
    @abstractmethod
    def species(self) -> Species: ...

    @property
    def Sound(self) -> Sound: ...


class DogAnimal(AnimalBase):
    @property
    def species(self): return Species.Dog

    @property
    def Sound(self): return Sound.bark

    @property
    def Hunt(self): return Hunt.SmallGame


class CatAnimal(AnimalBase):
    @property
    def species(self): return Species.Cat

    @property
    def Sound(self): return Sound.meow


class AnimalCreatorBase(ABC):

    @abstractmethod
    def createanimal(self) -> AnimalBase: ...


class DogAnimalCreator(AnimalCreatorBase):
    def createanimal(self) -> AnimalBase:
        return DogAnimal()


class CatAnimalCreator(AnimalCreatorBase):
    def createanimal(self) -> AnimalBase:
        return CatAnimal()


class AnimalFactory:
    def __init__(self, creator: AnimalCreatorBase):
        self.creator = creator

    def createanimal(self) -> AnimalBase:
        return self.creator.createanimal()


factory = AnimalFactory(DogAnimalCreator())

i = 0

while i < 1:
    animal = factory.createanimal()
    print('Animal', i, animal.species, animal.Sound, animal.Hunt)
    i = i+1
