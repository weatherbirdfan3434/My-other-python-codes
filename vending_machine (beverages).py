money = 0.00
loop = 1

def choose_beverage():
    beverage = input("\nPlease choose the beverage you want.\n\n1 = Sprite\n2 = Coca-cola\n3 = Diet Coke\n4 = Coke Zero\n5 = Mountain Dew\n6 = Mello Yello\n7 = Sierra Mist\n8 = 7Up\n9 = Lemonade\n0 = Water\n\nAll cost $1.25.\n\n")
    if beverage == '1':
        print("\nSprite")
    elif beverage == '2':
        print("\nCoca-cola")
    elif beverage == '3':
        print("\nDiet Coke")
    elif beverage == '4':
        print("\nCoke Zero")
    elif beverage == '5':
        print("\nMountain Dew")
    elif beverage == '6':
        print("\nMello Yello")
    elif beverage == '7':
        print("\nSierra Mist")
    elif beverage == '8':
        print("\n7Up")
    elif beverage == '9':
        print("\nLemonade")
    elif beverage == '0':
        print("\nWater")

while True:
    print("Insert money.\n")
    while True:
        if loop == 1:
            coin = input("P = insert penny\nN = insert nickel\nD = insert dime\nQ = insert quarter\nH = insert half-dollar coin\nC = insert dollar coin\n1 = insert 1-dollar bill\n2 = insert 2-dollar bill\nZ = Move on to choosing beverage.\n\n")
        else:
            coin = input("\n")
        if coin == 'P':
            money = money + 0.01
        elif coin == 'N':
            money = money + 0.05
        elif coin == 'D':
            money = money + 0.10
        elif coin == 'Q':
            money = money + 0.25
        elif coin == 'H':
            money = money + 0.50
        elif coin == 'C':
            money = money + 1.00
        elif coin == '1':
            money = money + 1.00
        elif coin == '2':
            money = money + 2.00
        elif coin == 'Z':
            choose_beverage()
            break
        else:
            print("\nInvalid coin.")
        print("\n" + str(money))
        loop = loop + 1
    if money - 1.25 < 0:
        print("\nNot enough money inserted.")
    break

print("\nThank you. Your change is $" + str(money - 1.25) + ".\n")
    
