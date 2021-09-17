from numpy.random import choice

class Tile:

    color_reset = "\u001b[0m"
    color_base = "\u001b["

    def __init__(self, tile_info):
        self.code = tile_info[0]
        self.color = Tile.color_base + tile_info[1]
        self.animation_type = tile_info[2]
        self.animation_frame = 0
        self.sprite_sheet = tile_info[3]
        self.weight_distribution = self.treat_weight_distribution(tile_info[4].split("/"))

    def __str__(self):
        return '%s%s%s' %(self.color, self.define_sprite(self.animation_type, self.animation_frame, self.sprite_sheet), Tile.color_reset)

    def treat_weight_distribution(self, weight_data):
        weight_distribution = []
        for value in weight_data:
            weight_distribution.append(float(value))
        return weight_data


    def define_sprite(self, animation_type, animation_frame, sprite_sheet):
        if animation_type == "s":
            return sprite_sheet
        elif animation_type == "r":
            return choice(list(sprite_sheet), p=self.weight_distribution)
        elif animation_type == "a":
            frame = sprite_sheet[animation_frame]
            if self.animation_frame == len(sprite_sheet) - 1:
                self.animation_frame = 0
            else:
                self.animation_frame += 1
            return frame
