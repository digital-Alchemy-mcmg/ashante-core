# C02: Event Bus
import json

class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, callback):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    def publish(self, event_type, data):
        message = json.dumps({'type': event_type, 'data': data})
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                callback(message)
