'''flavors = ["vamilla", "chocolate", "blueberry", "mango", "salted caramel"]
toppings = ["sprinkles", "chocolate syrup", "whipped cream", "cherry"]'''

'''for flavor in flavors:
    for topping in toppings:
        print("Lets try some " + flavor + " with a scoop of " + topping + " on top!")'''

'''for i in range(3):
    print("Trying out flavor "+ str(i+1) + ":" + flavors[i])'''
    
ice_cream_flavors = ["chocolate", "vanilla", "strawberry", "mint chocolate chip", "pistachio"]
    
'''for flavor in ice_cream_flavors:
    if flavor == "mint chocolate chip":
        print("My favorite! No need to taste further.")
        break
    print("Trying " + flavor + " flavor.")'''
    
'''for flavor in ice_cream_flavors:
    if flavor == "pistachio":
         continue
    print("Enjoying a scoop of " + flavor + ".")'''
    
for flavor in ice_cream_flavors:
    if flavor == "mint chocolate chip":
        pass
    print("Sampling " + flavor + " now.")
    