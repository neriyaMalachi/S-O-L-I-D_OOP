from L_liskov_substitution.good.classes.bird import Bird


class SwimmingBird(Bird):
    def move(self):
        return "Swimming"