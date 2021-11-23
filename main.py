import playerselect
import maps

goonInventories = playerselect.bringGoons()
drubyRush = maps.Bringmap()

menuDone = 1
playerselect.selectInventory(goonInventories)
lx = 1
ly = 0

maps.openMap()
print(drubyRush[ly][lx])

while True:
  maps.mapmenu(drubyRush)

