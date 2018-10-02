class Settings:
    """Settings for bob bot."""
    def __init__(self):
        # Distances before redirecting.
        self.safe_front_dist = 45
        self.safe_diagonal_dist = 20
        self.safe_side_dist = 15
        # Count turns made to avoid entrapment.
        self.turn_count = 0
        self.collision_count = 0
