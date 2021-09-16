from tile import Tile

map_file = open("./files/tilesys_test.csv", "r")
map_data = map_file.read()
map_rows = map_data.split("\n")
raw_map = []

for row in map_rows:
    split_row = row.split(",")
    raw_map.append(split_row)

tile_file = open("./files/tiles.csv", "r")
tile_data = tile_file.read()
tile_rows = tile_data.split("\n")
tile_map = []

for row in tile_rows:
    split_row = row.split(",")
    tile_map.append(split_row)

tile_palette = []

for tile in tile_map:
    tile_palette.append(Tile(tile))

for tile in tile_palette:
    print(tile)