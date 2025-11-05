from L_liskov_substitution.good.classes.bird import Bird


class FlyingBird(Bird):
    def move(self):
        return "Flying"