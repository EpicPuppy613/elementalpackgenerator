#ELEMENTAL PACK GENERATOR PROTOTYPE
print("Loading - Modules(0/4)")
import time as t
starttime = t.time()
t.sleep(0.25)
import json as j
#vars
print("Loading - Arrays(1/4)")
t.sleep(0.25)
elements = []
formulas = []
colors = {}
catagories = []
hex_list = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
print("Loading - Varaiables(2/4)")
t.sleep(0.25)
filename = None
elem1 = None
elem2 = None
elem3 = None
cat_name = None
cat_color = None
print("Loading - Data(3/4)")
t.sleep(0.25)
print("loading - Functions(4/4)")
t.sleep(0.25)
def addcat():
    cat_name = input("What do you want to name the catagory?\n>")
    while True:
        cat_color = input("What color do you want the catagory to be?\n#")
        if len(cat_color) == 6:
            good = True
            for i in cat_color:
                if any(item.lower() == i.lower() for item in hex_list):
                    continue
                else:
                    good = False
                    break
            if good == False:
                print("Oops! Not a valid hex code!")
                continue
            else:
                print("Making catagory " + cat_name + " with color #" + cat_color)
                return({"name":cat_name, "color":cat_color})
endtime = t.time()
loadtime = endtime - starttime
loadtime = round(loadtime, 3)
print("Done! Took " + str(loadtime) + "s")
while True:
    print("""[0]Add Category
[1]Add Element
[2]Add Equation
[3]Compile
[4]Export""")
    try:
        choice = int(float(input("What do you want to do?")))
    except:
        choice = -1
    if choice == 0:
        catagories.append(addcat())
        print(catagories)