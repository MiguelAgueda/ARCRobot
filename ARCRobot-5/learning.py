class Collision:
    def __init__(self, settings):
        self.stg = settings
        self.collision_count = 0
        self.no_collision_count = 0

    def collision_occurred(self):
        self.collision_count += 1
        self.no_collision_count = 0
        self.stg.safe_front_dist += 5
        print("Collision occurred!\nIncreasing safe distance to " + str(self.stg.safe_front_dist) + ".")

    def no_collision_occurred(self):
        self.no_collision_count += 1
        if self.no_collision_count % 10 == 0:
            self.stg.safe_front_dist -= 1
            print("Collision free!\nDecreasing safe distance.")
        else:
            pass
