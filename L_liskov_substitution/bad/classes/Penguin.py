from L_liskov_substitution.bad.classes.bird import Bird


class Penguin(Bird):
    def move(self):
        print("Penguin can't fly!")  # שובר את ההיגיון