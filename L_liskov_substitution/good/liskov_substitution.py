from L_liskov_substitution.good.classes.SwimmingBird import SwimmingBird
from L_liskov_substitution.good.classes.filyingBird import FlyingBird


def make_it_move(bird):
    print(bird.move())

def good_Function_L():
    make_it_move(FlyingBird())
    make_it_move(SwimmingBird())
