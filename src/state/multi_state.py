# C03: Multi-State Manager (DRAFT - CONTAINS ERRORS)
# TODO: Fix multi-state coexistence and timing gates.
class MultiStateManager:
    def __init__(self, initial_state):
        self.current_state = initial_state

    def set_state(self, state):
        self.current_state = state

    def check_timing_gate(self, last_seen):
        pass
