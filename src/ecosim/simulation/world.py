class World:

    def __init__(self):
        self.organisms = []
        self.food = []
        self.time = 0

    def update(self, dt):
        self.time += dt

        self.update_organisms(dt)
        self.handle_food()
        self.handle_reproductions()
        self.remove_dead()

    def update_organisms(self, dt):
        pass

    def handle_food(self):
        pass

    def handle_reproductions(self):
        pass

    def remove_dead(self):
        pass
