from rich.prompt import IntPrompt, Confirm
from rich.progress import (
    Progress,
    BarColumn,
    MofNCompleteColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn
)

class SessionView:
    def __init__(self, session_controller):
        self.session_controller = session_controller

    def display(self):
        while True:
            self.session_configuration()
            if self.session_confirmation() == True:
                break

        self.run_session()

    def run_session(self):
        self.progress_bar = Progress(
            TextColumn("[progress.description]{task.description}"),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            BarColumn(),
            MofNCompleteColumn(),
            TimeElapsedColumn(),
            TextColumn("•"),
            TimeRemainingColumn(),
            TextColumn("•"),
            TextColumn("[progress.speed]{task.speed} iter/s"),
        )
        session_time = self.session_controller.run_session(self.progress_bar)
        print("\nSession complete.")
        print(F"Time elapsed: {session_time}")
        
    def session_configuration(self):
        starting_id = IntPrompt.ask("What player Id would you like to start with?")
        ending_id   = IntPrompt.ask("What player Id would you like to end with?")
        threads     = IntPrompt.ask("How many threads would you like to run?")

        self.session_controller.configure_session(starting_id=starting_id, ending_id=ending_id, workers=threads)
    
    def session_confirmation(self):
        confirm = Confirm.ask("Confirm session configuration and begin?")            
        return confirm
    
    

    
