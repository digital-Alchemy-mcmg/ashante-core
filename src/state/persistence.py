import json
import os
import time

class PersistenceManager:
    def __init__(self, storage_path="state_store.json"):
        self.storage_path = storage_path

    def save_state(self, multi_state_manager):
        """Serializes and saves the current state to disk."""
        data = {
            "active_states": list(multi_state_manager.active_states),
            "state_timestamps": multi_state_manager.state_timestamps,
            "last_saved": time.time()
        }
        
        # Atomic write via temporary file
        temp_path = f"{self.storage_path}.tmp"
        with open(temp_path, 'w') as f:
            json.dump(data, f, indent=4)
        os.replace(temp_path, self.storage_path)
        return True

    def load_state(self, multi_state_manager):
        """Loads state from disk into the manager."""
        if not os.path.exists(self.storage_path):
            return False

        try:
            with open(self.storage_path, 'r') as f:
                data = json.load(f)
                
            multi_state_manager.active_states = set(data.get("active_states", []))
            multi_state_manager.state_timestamps = data.get("state_timestamps", {})
            return True
        except (json.JSONDecodeError, IOError) as e:
            print(f"Persistence Error: Failed to load state: {e}")
            return False

# Integration Example
if __name__ == "__main__":
    from multi_state import MultiStateManager
    
    # Setup
    m_manager = MultiStateManager()
    p_manager = PersistenceManager()
    
    # Simulate state change
    m_manager.add_state("ACTIVE")
    m_manager.add_state("UNAVAILABLE")
    
    # Save
    p_manager.save_state(m_manager)
    print("State persisted to disk.")
    
    # Clear and Load
    new_manager = MultiStateManager()
    p_manager.load_state(new_manager)
    print(f"Restored States: {new_manager.active_states}")
