from config import Config
from scraper import Scraper
from cli_prompt import CLIPrompt

def main(scraper):
    CLIPrompt.title()
    CLIPrompt.intro()
    selection = CLIPrompt.base_commands()

    if selection == 1:
        starting_id, ending_id, workers = CLIPrompt.session_options()

    scraper.configure_session(Config.base_url, int(starting_id), int(ending_id), int(workers))
    CLIPrompt.session_beginning()
    time_elapsed = scraper.run_session()

    CLIPrompt.session_complete(time_elapsed)


if __name__ == "__main__":
    scraper = Scraper()

    main(scraper)