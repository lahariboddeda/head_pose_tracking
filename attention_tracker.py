
class AttentionTracker:

    def __init__(self):

        # Left/right threshold
        self.yaw_threshold = 20

        # Up/down thresholds
        self.look_up_threshold = 110
        self.look_down_threshold = 170

    def check_attention(self, yaw, pitch):

        looking_away = False

        # LEFT / RIGHT
        if abs(yaw) > self.yaw_threshold:
            looking_away = True

        # LOOK UP
        elif pitch < self.look_up_threshold:
            looking_away = True

        # LOOK DOWN
        elif pitch > self.look_down_threshold:
            looking_away = True

        return {
            "looking_away": looking_away,
            "yaw": yaw,
            "pitch": pitch
        }

