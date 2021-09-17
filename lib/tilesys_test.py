from os import system
from tile import Tile
import time

#read, open and treat the map
map_file = open("./files/tilesys_test.csv", "r")
map_data = map_file.read()
map_rows = map_data.split("\n")
raw_map = []

for row in map_rows:
    split_row = row.split(",")
    raw_map.append(split_row)

#read, open the tiles
tile_file = open("./files/tiles.csv", "r")
tile_data = tile_file.read()
tile_rows = tile_data.split("\n")
tile_map = []

for row in tile_rows:
    split_row = row.split(",")
    tile_map.append(split_row)


#assemble the tile palette
tile_palette = []

for tile in tile_map:
    tile_palette.append(Tile(tile))
    print(tile[3], tile[4])

for tile in tile_palette:
    print(tile.sprite_sheet, tile.weight_distribution)
#create the map with each singular tile
tiled_map = []
for row in raw_map:
    tiled_row = []
    for item in row:
        for char in tile_palette:
            if item == char.code:
                tiled_row.append(char)
    tiled_map.append(tiled_row)

'''
#prints the map with each tic
while True:
    system("clear")
    for row in tiled_map:
        for item in row:
            print(item, end="")
        print()
    time.sleep(1)
'''