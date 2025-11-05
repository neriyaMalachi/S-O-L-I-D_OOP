
class UserService:
    def __init__(self, logger):
        self.logger = logger  # הזרקה מבחוץ

    def add_user(self, name):
        self.logger.log(f"Added {name}")
