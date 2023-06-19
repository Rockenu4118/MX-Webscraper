from views.home_view import HomeView
from views.session_view import SessionView
from controllers.session_controller import SessionController

def main():
    # Initialize views
    # TODO: home_controller = HomeController()
    session_controller = SessionController()
    
    # Initialize controllers
    home_view = HomeView()
    session_view = SessionView(session_controller)
    
    # Display home view and recieve menu selection
    selection = home_view.display()

    if selection == 1:
        session_view.display()
        


if __name__ == "__main__":
    main()

