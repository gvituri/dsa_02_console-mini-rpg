from lib.map import Map
from lib.npc import Npc

test_map = Map("test")
test_map.print_map()
test_map.print_map("visual")
test_map.print_map("barrier")

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