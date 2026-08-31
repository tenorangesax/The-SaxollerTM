import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.scanners.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB
from kmk.keys import KC

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

PINS = [board.D1, board.D2, board.D3, board.D4]
keyboard.matrix = KeysScanner(pins=PINS, value_when_pressed=False)


encoder = EncoderHandler()
keyboard.modules.append(encoder)
encoder.pins = ((board.D5, board.D6),)


rgb = RGB(
    pixel_pin=board.D7,  
    num_pixels=4,        
    val_limit=64,       
    order="GRB",
    mode=RGB.RGB_MODE_STATIC   
)
keyboard.extensions.append(rgb)



layer0_color = [0xFFFF00] * 4  

layer1_color = [0xFF8000] * 4  

layer2_color = [0x0000FF] * 4  


rgb.layers = [layer0_color, layer1_color, layer2_color]

rgb.effect = RGB.RGB_EFFECT_BREATH
rgb.effect_speed = 8  
rgb.effect_brightness = 64  


keyboard.keymap = [

    [
        KC.LGUI(KC.C),
        KC.LGUI(KC.V),
        KC.LGUI(KC.TAB),
        KC.LGUI(KC.W),
    ],

    [KC.NO, KC.NO, KC.NO, KC.NO],

    [KC.LEFT, KC.DOWN, KC.UP, KC.RIGHT],
]


encoder.map = [

    (KC.VOLD, KC.VOLU, KC.TO(1)),

    (KC.TO(0), KC.TO(2), KC.TO(0)),

    (KC.VOLD, KC.VOLU, KC.TO(0)),
]

if __name__ == '__main__':
    keyboard.go()
