class Settings:
    """Settings for bob bot."""
    def __init__(self):
        # Distances before redirecting.
        self.safe_front_dist = 45
        # Trig pin
        self.trig = 27
        # Echo pin
        self.echo = 22
        # H-Bridge
        self.in1 = 2
        self.in2 = 3
        self.in3 = 4
        self.in4 = 17
        self.all_h_bridge_pins = [self.in1, self.in2, self.in3, self.in4]
