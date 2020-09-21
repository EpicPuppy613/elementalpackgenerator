#ELEMENTAL PACK GENERATOR PROTOTYPE
print("Loading - Modules(0/4)")
import time as t
starttime = t.time()
t.sleep(0.25)
import json as j
import os as o
#vars
print("Loading - Arrays(1/4)")
t.sleep(0.25)
elements = []
formulas = []
colors = {}
categories = []
hex_list = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
alphanum = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
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
    cat_name = input("What do you want to name the category?\n>")
    while True:
        cat_color = input("What color do you want the category to be?\n#")
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
def addelem():
    if len(categories) == 0:
        print("Oops! You don't have any categories made yet! You should do that first.")
        raise(Exception("No Categories"))
    else:
        while True:
            x = 0
            for i in categories:
                print("["+str(x)+"]"+i["name"])
                x += 1
            while True:
                try:
                    elem_cat = int(float(input("What Category do you want your element to be?")))
                    break
                except:
                    print("Oops! Not a valid number!")
            if elem_cat >= len(categories):
                print("Oops! Not a valid category!")
                continue
            else:
                break
        elem_name = input("What do you want to name your element?")
        print("Added Element: "+elem_name+" in category: "+categories[elem_cat]["name"])
        return({"name": elem_name, "category": categories[elem_cat]["name"]})
def export():
    while True:
        pack_folder = input("What do you want to name the folder that the pack is stored in? (Can only contain alpha-numeric characters)")
        good = True
        for i in pack_folder:
            if any(item.lower() == i.lower() for item in alphanum):
                continue
            else:
                good = False
                break
        if good == False:
            print("Oops! Not a valid folder name!")
            continue
        else:
            pack_name = input("What do you want to name your pack?")
            pack_desc = input("What do you want the description of your pack to be?")
            pack_author = input("What is the name of the author that made the pack?")
            print("Exporting - Creating Folder (0/4)")
            try:
                o.mkdir("C:\Elemental Pack Generator")
            except:
                print("", end="")
            try:
                o.mkdir("C:\Elemental Pack Generator\\"+pack_folder)
            except:
                print("", end="")
            t.sleep(0.1)
            print("Exporting - Exporting Pack Info (1/4)")
            pack = open("C:\Elemental Pack Generator\\"+pack_folder+"\pack.json", "w")
            pack.write('{'+'"name": "' + pack_name + '",'+'"description": "' + pack_desc + '",'+'"author": "' + pack_author + '"'+'}')
            pack.close()
            print("Exporting - Exporting Categories (2/4)")
            if len(categories) != 0:
                pack = open("C:\Elemental Pack Generator\\"+pack_folder+"\categories.json", "w")
                pack.write(j.dumps(categories))
                pack.close()
                t.sleep(0.1)
            print("Exporting - Exporting Elements (3/4)")
            if len(elements) != 0:
                pack = open("C:\Elemental Pack Generator\\"+pack_folder+"\elems.json", "w")
                pack.write(j.dumps(elements))
                pack.close()
                t.sleep(0.1)
            print("Exporting - Exporting Formulas (4/4)")
            if len(formulas) != 0:
                pack = open("C:\Elemental Pack Generator\\"+pack_folder+"\\formulas.json", "w")
                pack.write(j.dumps(formulas))
                pack.close()
                t.sleep(0.1)
            print("Done! Exported under C:\Elemental Pack Generator\[Your Pack Name]")
            break
def addform():
    inputs = []
    if len(elements) == 0:
        print("Oops! You don't have any elements made yet! You should do that first.")
        raise(Exception("No Elements"))
    while True:
        try:
            input_count = int(float(input("How many inputs do you want?(2-4)")))
        except:
            print("Oops! Not a valid number!")
            continue
        if input_count > 1 and input_count < 5:
            break
        else:
            print("Oops! Not a valid amount!")
    for i in range(0, input_count):
        y = 0
        for x in elements:
            print("["+str(y)+"]"+x["name"])
            y += 1
        while True:
            try:
                input_choice = int(float(input("What element do you want to add to the formula?")))
            except:
                print("Oops! Not a valid number!")
                continue
            if input_choice >= 0 and input_choice < len(elements):
                inputs.append(elements[input_choice]["name"])
                break
    y = 0
    for x in elements:
        print("["+str(y)+"]"+x["name"])
        y += 1
    while True:
        try:
            output_choice = int(float(input("What element do you want as a output?")))
        except:
            print("Oops! Not a valid number!")
            continue
        if output_choice >= 0 and output_choice < len(elements):
            output = elements[output_choice]["name"]
            break
    print("Creating formula with inputs: "+str(inputs)+" and output: "+output)
    return({"inputs": inputs, "output": output})
endtime = t.time()
loadtime = endtime - starttime
loadtime = round(loadtime, 3)
print("Done! Took " + str(loadtime) + "s")
while True:
    print("""[0]Add Category
[1]Add Element
[2]Add Formula
[3]Export""")
    try:
        choice = int(float(input("What do you want to do?")))
    except:
        choice = -1
    if choice == 0:
        categories.append(addcat())
        print(categories)
    elif choice == 1:
        try:
            elements.append(addelem())
        except Exception:
            print("Please use '0' to create a category.")
        print(elements)
    elif choice == 2:
        try:
            formulas.append(addform())
        except Exception:
            print("Please use '1' to create a element.")
        print(formulas)
    elif choice == 3:
        export()
        break