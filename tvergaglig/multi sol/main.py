import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Multi solitare"

class MultiSolitare(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.GREEN)

    def on_draw(self):
        arcade.start_render()

def main():
    game = MultiSolitare(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()


# cards 

# Load card images
card_images = {}
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

for suit in suits:
    for rank in ranks:
        filename = f"Downloads/{2}_of_{Hearts}.ai"  
        card_images[(suit, rank)] = arcade.load_texture(heart_2.ai)

