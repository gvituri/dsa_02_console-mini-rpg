from copy import deepcopy

class Map:
    def __init__(self, name, tile_palette) -> None:
        self.name = name
        self.tile_palette = tile_palette
        self.raw_map = self.read_file(self.name)
        self.border_map = self.add_map_borders(self.raw_map)
        self.visual_map = self.assemple_visual_map(self.border_map)
        self.barrier_map = self.assemple_barrier_map(self.border_map)
        
    def read_file(self, name):
        map_file = open("./lib/files/map_%s.csv" %(name), "r")
        map_data = map_file.read()
        map_rows = map_data.split("\n")
        raw_map = []

        for row in map_rows:
            split_row = row.split(",")
            raw_map.append(split_row)

        return raw_map

    def add_map_borders(self, raw_map):

        map = deepcopy(raw_map)

        for x in range(10):
            map.append(["x"] * len(map[0]))

        for x in range(10):
            map.insert(0, ["x"] * len(map[0]))

        for row in map:
            for x in range(10):
                row.append("x")
        
        for row in map:
            for x in range(10):
                row.insert(0, "x")

        return map

    def assemple_visual_map(self, border_map):
        #TODO here, get tile_palette and apply on the border_map.

        map = []

        for row in border_map:
            tiled_row = []
            for item in row:
                for char in self.tile_palette:
                    if item == char.code:
                        tiled_row.append(char)
            map.append(tiled_row)

        return map

    def assemple_barrier_map(self, border_map):

        map = deepcopy(border_map)

        barrier_chars = self.get_boundaries_characters()

        i = 0
        for row in map:
            for char in row:
                for b_char in barrier_chars:
                    if char == b_char:
                        row[i] = "▉"
                        break
                    row[i] = " "
                i += 1
            i = 0

        return map

    def get_boundaries_characters(self):

        char_file = open("./lib/files/barrier_chars.txt", "r")
        char_data = char_file.read()
        barrier_chars = char_data.split(",")

        return barrier_chars

    def position_npc(self, npc_list):
        for npc in npc_list:
            self.visual_map[npc.coordinate[1]+9][npc.coordinate[0]+9] = npc.symbol

    def print_map(self, type = "raw"):
        if type == "visual":
            for row in self.visual_map:
                for item in row:
                    print(item, end = "")
                print()
        elif type == "barrier":
            for row in self.barrier_map:
                for item in row:
                    print(item, end = "")
                print()
        else:
            for row in self.raw_map:
                for item in row:
                    print(item, end = "")
                print()            