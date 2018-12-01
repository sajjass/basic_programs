# Classes and Objects
# Properties
# Behaviours
# initializers and instances
# inheritance

class super_inheritance():
    #initialize properties
    var1 = 0
    var2 = 0
    var3 = ""
    input = 2
    input_1 = 0

    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def super_method(self, input_1):
        if (input_1 > 0 and input_1 < 100):
            self.input += 100
        elif input_1 < 0:
            self.input -= 100

class tmp_inherited(super_inheritance):
    var4 = 0

    def __init__(self, var1, var2, var3):
        super(tmp_inherited, self).__init__(var1, var2, var3)
        self.var4 = 4

    def super_method(self, input_1):
        super(tmp_inherited, self).super_method(input_1)
        if input_1 == 100:
            self.input *=100


obj_super_inheritance = super_inheritance(2000, 3000.33, "sajjas")

obj_inherited = tmp_inherited(3000, 4000.44, "asha")

#print (obj_super_inheritance.var3)
#print (obj_inherited.var4)

obj_inherited.super_method(100)
print(obj_inherited.input)