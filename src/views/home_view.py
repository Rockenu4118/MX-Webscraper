from rich.prompt import IntPrompt

class HomeView:
    def startup(self):
        print("  __  __  __   __   __          __         _                                                       ")
        print(" |  \/  | \ \ / /   \ \        / /        | |                                                      ")
        print(" | \  / |  \ V /     \ \  /\  / /    ___  | |__    ___    ___   _ __    __ _   _ __     ___   _ __ ")
        print(" | |\/| |   > <       \ \/  \/ /    / _ \ | '_ \  / __|  / __| | '__|  / _` | | '_ \   / _ \ | '__|")
        print(" | |  | |  / . \       \  /\  /    |  __/ | |_) | \__ \ | (__  | |    | (_| | | |_) | |  __/ | |   ")
        print(" |_|  |_| /_/ \_\       \/  \/      \___| |_.__/  |___/  \___| |_|     \__,_| | .__/   \___| |_|   ")
        print("                                                                              | |                  ")
        print("                                                                              |_|                \n")
        print("Welcome to the MX Webscraper!")
        print(f"Version: 1.0")

    def display(self):
        self.startup()
        while True:
            print("Base commands:\n")
            print("[1] Begin scraping session\n")
            selection = IntPrompt.ask("Enter a numeric value")

            return selection

        
