from config import Config

class CLIPrompt:

    @staticmethod
    def title():
        print("  __  __  __   __   __          __         _                                                       ")
        print(" |  \/  | \ \ / /   \ \        / /        | |                                                      ")
        print(" | \  / |  \ V /     \ \  /\  / /    ___  | |__    ___    ___   _ __    __ _   _ __     ___   _ __ ")
        print(" | |\/| |   > <       \ \/  \/ /    / _ \ | '_ \  / __|  / __| | '__|  / _` | | '_ \   / _ \ | '__|")
        print(" | |  | |  / . \       \  /\  /    |  __/ | |_) | \__ \ | (__  | |    | (_| | | |_) | |  __/ | |   ")
        print(" |_|  |_| /_/ \_\       \/  \/      \___| |_.__/  |___/  \___| |_|     \__,_| | .__/   \___| |_|   ")
        print("                                                                              | |                  ")
        print("                                                                              |_|                  ")

    @staticmethod
    def intro():
        print("Welcome to the MX Webscraper!")
        print(f"Version: {Config.version}")

    @staticmethod  
    def base_commands():
        while True:
            print("Base commands:\n")
            print("[1] Begin scraping session\n")
            selection = int(input("Enter a numeric value: "))

            if selection == 1:
                return selection
            print(f"Invalid selection: {selection}\n")
        
    @staticmethod
    def session_options():
        starting_id = input(f"What Id would you like to start with? ")
        ending_id = input(f"What Id would you like to end with? ")
        workers = input(f"How many workers would you like to run? ")
        return starting_id, ending_id, workers
    
    @staticmethod
    def session_beginning():
        print("Scraping session now in progress.\n")
    
    @staticmethod
    def session_complete(time_elapsed):
        print("\nScraping session complete.")
        print(f"Elapsed time: {time_elapsed}")