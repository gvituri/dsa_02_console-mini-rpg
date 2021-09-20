from .event import subscribe_to

class Test:

    def __init__(self):
        self.name = "This is a test"
        self.setup_timer_event_handlers()

    def print_proof_of_notification(self):
        print(self.name)

    def setup_timer_event_handlers(self):
        subscribe_to("tic", self.print_proof_of_notification)
