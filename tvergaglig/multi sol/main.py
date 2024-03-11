from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask"

if __name__== '__main__':
    app.run(debug=True)

import arcade

# Screen title and size
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_TITLE = "Drag and Drop Cards"


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        pass

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        self.clear()

        # Draw a rectangle
        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                     200, 100, arcade.color.RED)

        # Draw text
        arcade.draw_text("Hello, Arcade!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                         arcade.color.WHITE, font_size=24, anchor_x="center")

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user presses a mouse button. """
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """
        pass


def main():
    """ Main function """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

