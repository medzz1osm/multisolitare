import arcade

SCREEN_WIDTH = 1400
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
                game_view = MultiSolitaire(self.window, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
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

class MultiSolitaire(arcade.View):
    def __init__(self, window: arcade.Window, width: int, height: int, title: str):
        super().__init__(window)
        self.window = window
        self.width = width
        self.height = height
        self.title = title
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
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    register_view = RegisterView()
    window.show_view(register_view)
    arcade.run()

if __name__ == "__main__":
    main()