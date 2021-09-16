class Tile:

    color_reset = "\u001b[0m"
    color_base = "\u001b["

    def __init__(self, tile_info):
        self.code = tile_info[0]
        self.name = tile_info[1]
        self.color = Tile.color_base + tile_info[2]
        self.anim_type = tile_info[3]
        self.character = tile_info[4]

    def __str__(self):
        return '%s%s%s' %(self.color, self.character, Tile.color_reset)