class Animal(object):
    def __init__(self,type): self.type=type
    def noise(self): 
        if self.type=="Dog":
            return "Bark"
        elif self.type=="Cat":
            return "Miaow"
        elif self.type=="Cow":
            return "Moo"
        elif self.type=="Pig":
            return "Oink"

animals=[Animal("Dog"), Animal("Dog"), Animal("Cat"), Animal("Pig"), Animal("Cow"), Animal("Cat")]
for animal in animals:
    print animal.noise()

