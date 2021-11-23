# maps and modules assignment


# the display map
def openMap():
    with open('mymaps.txt') as file:
        contents = file.read()
    print(contents)


# the movement map
dstart = "start"
dcliffside = "there is an impassable cliff here"
dgemspot = "you found a shiny thing"
denemy = "oh no an enemy"
dsupplies = "you restock here"
dnothing = "there is nothing here"

def Bringmap():
  drubyRush = [
      [dcliffside, dstart, dgemspot, denemy, dcliffside],
      [dcliffside, denemy, denemy, dsupplies, dcliffside],
      [dcliffside, dnothing, dsupplies, denemy, dcliffside],
      [dcliffside, dnothing, dnothing, dsupplies, dcliffside],
      [dcliffside, denemy, denemy, dnothing, dcliffside],
      [dcliffside, dgemspot, denemy, dsupplies, dcliffside],
  ]
  return drubyRush

# prints the display for the map
# def printMap():
#  xp = 0
#  for i in range(6):
#    yp = 0
#    print ("----------------------------------------------------------")
#    print("|", end = " ")
#    for a in range(5):
#      print(rubyRush[xp][yp], end = " ")
#      spacePrint = len(rubyRush[xp][yp])
#      for s in range(8):
#        if spacePrint < 8:
#          print(" ", end = "")
#          spacePrint +=1
#      print("|", end = " ")
#      yp += 1
#    print(" ")
#    xp += 1
#  print("----------------------------------------------------------")

#list of the places you can
directions = ["up", "down", "left", "right", "explore"]

hold = 1

lx = 1
ly = 0

# shows the original map
# printMap()



# movment controls
def mapmenu(drubyRush):
    global ly
    global lx
    print("")
    print("where to?")
    for i in directions:
        print(i)
    print("")
    direction = input()
    # does the maths for location
    if direction.lower() == "up" and ly > 0:
        ly -= 1
        print(f"{drubyRush[ly][lx]}")
    elif direction.lower() == "down" and ly < 5:
        ly += 1
        print(f"{drubyRush[ly][lx]}")
    elif direction.lower() == "left" and lx > 0:
        lx -= 1
        print(f"{drubyRush[ly][lx]}")
    elif direction.lower() == "right" and lx < 4:
        lx += 1
        print(f"{drubyRush[ly][lx]}")
    elif direction.lower() == "explore":
        openMap()
        print(f"{drubyRush[ly][lx]}")
    else:
        print("can't do that")
