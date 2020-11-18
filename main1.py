class Hero:
        jumlah = 0
        
        def __init__(self, inputName, inputHealth, inputPower, inputArmor):
                self.name = inputName
                self.health = inputHealth
                self.power = inputPower
                self.armor = inputArmor
                Hero.jumlah += 1
                print("Membuat Hero dengan nama " +inputName)

       #desktruktor
        def __del__(self):
                class_name = self.__class__.__name__
                Hero.jumlah -=1
                print("Sebuah Objek ", class_name,", Yaitu ", self.name," Dihapus")
                 


hero1 = Hero("sniper",100, 10, 4)
print("jumlah Hero :",Hero.jumlah)
hero2 = Hero("mirana",100, 15, 1)
print("jumlah Hero :",Hero.jumlah)
hero3 = Hero("ucup",1000, 10, 0)
print("jumlah Hero :",Hero.jumlah)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)


del hero1
print("Jumlah Hero :", Hero.jumlah)
