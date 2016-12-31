from PIL import Image
import itertools

START_UP = (7,84,19,255)
START_LEFT = (139,57,137,255)
TURN_RIGHT = (182,149,72,255)
TURN_LEFT = (123,131,154,255)
STOP = (51,69,169,255)
WHITE = (255,255,255,255)

def get_next_pixel(current_px, direction):
    if direction == 'UP':
        return (current_px[0], current_px[1] - 1)
    elif direction == 'LEFT':
        return (current_px[0] - 1, current_px[1])
    elif direction == 'DOWN':
        return (current_px[0], current_px[1] + 1)
    elif direction == 'RIGHT':
        return (current_px[0] + 1, current_px[1])

def turn(current_direction, to_clockwise):
    directions = ['UP', 'LEFT', 'DOWN', 'RIGHT']
    step = -1 if to_clockwise else 1
    return directions[(directions.index(current_direction) + step) % 4]

img = Image.open('3663c24c-c5db-11e6-8be5-e358d0e0215a.png')
pixels = img.load()
pixels_to_draw = []

for px in itertools.product(range(img.size[0]), range(img.size[1])):   

    current_color = pixels[px]

    if current_color == START_UP or current_color == START_LEFT:

        pixels_to_draw.append(px)
        current_direction = 'UP' if current_color == START_UP else 'LEFT'
        next_px = get_next_pixel(px, current_direction)

        while True:
            pixels_to_draw.append(next_px)
            current_color = pixels[next_px]
            if current_color == STOP:
                break
            if current_color == TURN_RIGHT or current_color == TURN_LEFT:
                current_direction = turn(current_direction, (current_color == TURN_RIGHT))
            next_px = get_next_pixel(next_px, current_direction)

for px in pixels_to_draw:
    pixels[px] = WHITE

img.show()
