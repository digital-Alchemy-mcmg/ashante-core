import time

class MultiStateManager:
    def __init__(self):
        self.active_states = set()
        self.state_timestamps = {}

    def add_state(self, state):
        if state not in self.active_states:
            self.active_states.add(state)
            self.state_timestamps[state] = time.time()
            return True
        return False

    def remove_state(self, state):
        if state in self.active_states:
            self.active_states.remove(state)
            self.state_timestamps.pop(state, None)
            return True
        return False

    def is_active(self, state):
        return state in self.active_states

    def get_elapsed_time(self, state):
        if state in self.state_timestamps:
            return time.time() - self.state_timestamps[state]
        return 0

    def can_transition_to_offline(self, threshold_seconds):
        if not self.is_active("UNAVAILABLE"):
            return False
        elapsed = self.get_elapsed_time("UNAVAILABLE")
        return elapsed >= threshold_seconds
