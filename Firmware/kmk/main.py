"""Pulsar."""
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, \
    OledReactionType
from kmk.extensions.neopixel import NeoPixel
from kmk.modules.macros import Press, Release, Tap, Macros


keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)


neopixel_ext = NeoPixel(
    pin=board.GP3,  # Update with your data pin
    num_pixels=2,    # Number of SK6812MINI LEDs
    brightness=0.2
)
keyboard.extensions.append(neopixel_ext)


ROW_PINS = [board.D4, board.D7, board.D11]
COL_PINS = [board.D10, board.D9, board.D8]
keyboard.matrix = MatrixScanner(
    row_pins=ROW_PINS,
    col_pins=COL_PINS,
    diode_orientation=MatrixScanner.DIODE_COL2ROW,
)

# keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
macros.macros = {
    0: [Tap(KC.H), Tap(KC.E), Tap(KC.L), Tap(KC.L), Tap(KC.O), Tap(KC.SPC),
        Tap(KC.W), Tap(KC.O), Tap(KC.R), Tap(KC.L), Tap(KC.D), Tap(KC.DOT)],
    1: [Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)],
}

keyboard.keymap = [
    [
        KC.A, KC.DELETE, KC.Macro(0), KC.Macro(1),
        KC.B, KC.C, KC.D, KC.MUTE, # last one is encoder
    ]
]

encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = ((board.GP1, board.GP2),)

encoder_handler.map = [
    (KC.VOLD, KC.VOLU),  # (CCW, CW), press handled in matrix
]


oled_ext = Oled(
    width=128,
    height=32,
    to_display=OledDisplayMode.LAYER,
    reaction=OledReactionType.KEYPRESS
)
keyboard.extensions.append(oled_ext)


# Start kmk!
if __name__ == '__main__':
    keyboard.go()
