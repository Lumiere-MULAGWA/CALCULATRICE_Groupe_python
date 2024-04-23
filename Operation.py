
class  Operation:
    def __init__(self):
        pass

    def click(self,num):
        print(num)
        return num
    def calcul(self,args):
        
       
        print( eval(args))

def factoriel(number):
        if number == 0:
            return 1
        else:
            return number * factoriel(number - 1)

test = Operation()
test.click(3)
test.calcul("(5+4)*2 +factoriel(5)")
