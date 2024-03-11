import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Multi solitare"

class MultiSolitare(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.GO_GREEN)

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


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(800, 600, "Display Card Example")
      

        # Load card images
        self.card_image = arcade.load_texture("2_of_Diamonds.png")

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()

        # Display the card image
        arcade.draw_texture_rectangle(400, 300, self.card_image.width, self.card_image.height, self.card_image)

def main():
    """ Main function """
    window = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()

