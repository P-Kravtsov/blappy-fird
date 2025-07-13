# Screen dimensions
SCREEN_WIDTH = 864
SCREEN_HEIGHT = 936

# Game variables
FPS = 60
GRAVITY = 0.75
JUMP_STRENGTH = -12
PIPE_GAP = 300
PIPE_FREQUENCY = 1500 # milliseconds

# --- Asset Paths & Configs ---
FONT_PATH = 'assets/04B_19.TTF'
HIGHSCORE_FILE = 'highscore.txt'

# A dictionary for our assets to make life easier
ASSETS = {
    'bird': [
        'assets/bird1.png',
        'assets/bird2.png',
        'assets/bird3.png'
    ],
    'sounds': {
        'jump': 'assets/wing.wav',
        'hit': 'assets/hit.wav',
        'score': 'assets/point.wav',
    }
}


