import arcade

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Multi solitaire"

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class RegisterView(arcade.View):
    def __init__(self):
        super().__init__()
        self.username = ""
        self.password = ""
        self.current_input = "username"

    def on_show(self):
        arcade.set_background_color(arcade.color.GRAY_ASPARAGUS)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f"Username: {self.username}", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50,
                         arcade.color.BLACK, font_size=20, anchor_x="center")
        arcade.draw_text(f"Password: {'*' * len(self.password)}", SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50,
                         arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            if self.current_input == "username":
                self.current_input = "password"
            elif self.current_input == "password":
                user = User(self.username, self.password)
                game_view = MultiSolitaire(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
                self.window.show_view(game_view)
        elif symbol == arcade.key.BACKSPACE:
            if self.current_input == "username" and self.username:
                self.username = self.username[:-1]
            elif self.current_input == "password" and self.password:
                self.password = self.password[:-1]
        else:
            char = chr(symbol)
            if self.current_input == "username":
                self.username += char
            elif self.current_input == "password":
                self.password += char

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
                filename = f"cards/2_of_Diamonds.png"
                self.card_images[(suit, rank)] = arcade.load_texture(filename)

        # Initialize card position
        self.card_x = SCREEN_WIDTH // 2
        self.card_y = SCREEN_HEIGHT // 2

    def on_draw(self):
        arcade.start_render()

        # Draw the card at its current position
        suit = 'Diamonds'  # Example suit
        rank = '2'          # Example rank
        card_texture = self.card_images[(suit, rank)]
        arcade.draw_texture_rectangle(self.card_x, self.card_y, card_texture.width, card_texture.height, card_texture)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        # Update card position when mouse is dragged
        self.card_x += dx
        self.card_y += dy

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    register_view = RegisterView()
    window.show_view(register_view)
    arcade.run()

if __name__ == "__main__":
    main()
