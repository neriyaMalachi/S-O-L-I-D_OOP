from L_liskov_substitution.bad.classes.Penguin import Penguin
from L_liskov_substitution.bad.classes.bird import Bird


def make_it_move(bird):
    print(bird.move())

def bad_Function_L():
    make_it_move(Bird())
    make_it_move(Penguin())  # קורס
