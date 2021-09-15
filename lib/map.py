from copy import deepcopy

class Map:
    def __init__(self, name) -> None:
        self.name = name
        self.raw_map = self.read_file(self.name)
        self.border_map = self.add_map_borders(self.raw_map)
        self.visual_map = self.assemple_visual_map(self.border_map)
        self.barrier_map = self.assemple_barrier_map(self.border_map)

        self.print_test(self.raw_map)
        self.print_test(self.border_map)
        self.print_test(self.visual_map)
        self.print_test(self.barrier_map)
        
    def read_file(self, name):
        map_file = open("./lib/files/%s.csv" %(name), "r")
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
            map.append(["╳"] * len(map[0]))

        for x in range(10):
            map.insert(0, ["╳"] * len(map[0]))

        for row in map:
            for x in range(10):
                row.append("╳")
        
        for row in map:
            for x in range(10):
                row.insert(0, "╳")

        return map

    def assemple_visual_map(self, border_map):

        map = deepcopy(border_map)

        i = 0
        for row in map:
            for char in row:
                if char == "╳":
                    row[i] = " "
                i += 1
            i = 0

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

    def print_test(self, map):
        for row in map:
            for item in row:
                print(item, end = "")
            print()