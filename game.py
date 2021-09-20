from os import system
import time

from lib.tile import Tile
from lib.map import Map
from lib.npc import Npc

#Loading tile information and assembling tile palette for usage in map rendering
tile_file = open("./lib/files/tiles.csv", "r")
tile_data = tile_file.read()
tile_rows = tile_data.split("\n")
tile_list = []

for row in tile_rows:
    split_row = row.split(",")
    tile_list.append(split_row)

tile_palette = []

for tile in tile_list:
    tile_palette.append(Tile(tile))

#Loading and testing map rendering and colliders
test_map = Map("test", tile_palette)

while True:
    system("clear")
    test_map.print_map("visual")
    time.sleep(1)

#TODO Make map_content.cvs to get player spawns, npc's positions, monster spawns, etc...
#read and position content on the map
#get the player view
#print the player view every 1'

'''
#load_npc's
npc_file = open("./lib/files/npc_test.csv", "r")
npc_data = npc_file.read()
npc_rows = npc_data.split("\n")
npc_raw_list = []

for row in npc_rows:
    split_row = row.split(",")
    npc_raw_list.append(split_row)

npc_list = []
for npc in npc_raw_list:
    npc_list.append(Npc(npc[0], npc[1], npc[2], npc[3]))

test_map.position_npc(npc_list)

test_map.print_map()
test_map.print_map("visual")
test_map.print_map("barrier")
'''