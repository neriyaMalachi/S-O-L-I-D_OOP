from D_dependency_inversion.good.classes.ConsoleLogger import ConsoleLogger
from D_dependency_inversion.good.classes.UserService import UserService


def good_Function_D():
    logger = ConsoleLogger()
    UserService(logger).add_user("Avi")
