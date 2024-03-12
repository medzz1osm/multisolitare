import arcade

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Multi solitaire"

class MultiSolitaire(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.GO_GREEN)

        # Load card images
        self.card_images = {}
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        for suit in suits:
            for rank in ranks:
                filename = f"cards/yuio.png"  # Corrected line
                self.card_images[('Diamonds', 'Diamonds')] = arcade.load_texture("cards/2_of_Diamonds.png")

    def on_draw(self):
        arcade.start_render()

        # Draw a card example
        suit = 'Diamonds'  # Example suit
        rank = '2'       # Example rank
        card_texture = self.card_images[('Diamonds', 'Diamonds')]
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, card_texture.width, card_texture.height, card_texture)

def main():
    game = MultiSolitaire(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()
