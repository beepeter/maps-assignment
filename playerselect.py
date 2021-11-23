# inventories for an rpg

# charachter inventories


user = "T"
def bringGoons():
  goonInventories = {
        "Big Gun": {
            "boot": {
                "description": "well fit to hold feet and tools",
                "armour": 1.5,
                "damage": 1,
                "quantity": 2
            },
            "Gun": {
                "description": "a solid item for shooting someone, with bullets",
                "armour": 0,
                "damage": 5,
                "quantity": 1
            },
            "really cool hat": {
                "description": "it looks rather dapper",
                "armour": 4,
                "damage": 1,
                "quantity": 1
            }
        },
        "Salman": {
            "bottle": {
                "description": "for holding liquids or seeing things far away",
                "armour": -1,
                "damage": 4,
                "quantity": 5
            },
            "belt buckle": {
                "description": "people really want to break it",
                "armour": 5,
                "damage": 0,
                "quantity": 1
            },
            "stepeng stool": {
                "description": "meant for steppin', used for hittin'",
                "armour": 2,
                "damage": 3,
                "quantity": 1
            }
        }
    }
  return goonInventories



goonList = {
    "BIG GUN": {
        """the Biggest Gun of the Trudyhomes inc. realestate agency Big Gun is
known for not selling houses because he is Big Gun not Resident Residence"""
    },
    "Salman": {
        """An odd person who has a pension for
fights with a peculiar lack of pistols"""
    }
}


# thing for showing all parts of a list
def showInventory(goon):
    print
    for i in (goon):
        print(f"{i}")
        for d in (goon)[i]:
            print(f"{d} - {(goon)[i][d]}")
      

def saveGoon(user, goonInventories):
    if user.title() in goonInventories:
        with open("hero.txt", "w") as f:
            f.write(f"{user.title()}\n")
        for item in goonInventories[user.title()]:
          description = goonInventories[user.title()][item]["description"]
          armour = goonInventories[user.title()][item]["armour"]
          damage = goonInventories[user.title()][item]["damage"]
          quantity = goonInventories[user.title()][item]["quantity"]
          with open ("hero.txt", "a") as f:
               f.write(f"{item}\n")
               f.write(f"{description}\n")
               f.write(f"armour: {armour}\n")
               f.write(f"damage: {damage}\n")
               f.write(f"quantity: {quantity}\n")
               f.write("\n")


# slecting your charachter

def selectInventory(goonInventories):
  global user
  while user.title() not in goonInventories:
    bringGoons()
    print
    for i in goonList:
      print(f"{i}")
      for e in goonList[i]:
          print(f"{e}")
          print(" ")
    user = input("""which guy?
""")
    print(user.title())
    if user.title() in goonInventories:
      for item in goonInventories[user.title()]:
        description = goonInventories[user.title()][item]["description"]
        armour = goonInventories[user.title()][item]["armour"]
        damage = goonInventories[user.title()][item]["damage"]
        quantity = goonInventories[user.title()][item]["quantity"]
        print(item)
        print(f"description: {description}")
        print(f"armour: {armour}")
        print(f"damage: {damage}")
        print(f"quantity: {quantity}")
      saveGoon(user, goonInventories)
    else:
      print("not a goon")
