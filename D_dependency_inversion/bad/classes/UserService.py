from D_dependency_inversion.bad.classes.FileLogger import FileLogger


class UserService:
    def __init__(self):
        self.logger = FileLogger()  # תלות ישירה

    def add_user(self, name):
        self.logger.log(f"Added {name}")
