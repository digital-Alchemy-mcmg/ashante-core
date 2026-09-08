# C01: Core State Machine
class StateMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.transitions = {}

    def add_transition(self, from_state, to_state, validator=None):
        if from_state not in self.transitions:
            self.transitions[from_state] = {}
        self.transitions[from_state][to_state] = validator

    def transition(self, to_state, context=None):
        if to_state in self.transitions.get(self.current_state, {}):
            validator = self.transitions[self.current_state][to_state]
            if validator is None or validator(context):
                self.current_state = to_state
                return True
        return False
