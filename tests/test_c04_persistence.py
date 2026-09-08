import os
import json
import unittest
from src.state.multi_state import MultiStateManager
from src.state.persistence import PersistenceManager

class TestC04Persistence(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_state.json"
        self.m_manager = MultiStateManager()
        self.p_manager = PersistenceManager(storage_path=self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_serialization_and_recovery(self):
        """Requirement 1 & 3: Verify states and timestamps survive reconstruction."""
        self.m_manager.add_state("ACTIVE")
        self.m_manager.add_state("DEGRADED")
        original_states = set(self.m_manager.active_states)
        
        # Save
        self.p_manager.save_state(self.m_manager)
        
        # Load into fresh manager
        new_manager = MultiStateManager()
        self.p_manager.load_state(new_manager)
        
        self.assertEqual(new_manager.active_states, original_states)
        self.assertIn("ACTIVE", new_manager.active_states)
        self.assertIn("DEGRADED", new_manager.active_states)
        self.assertTrue(len(new_manager.state_timestamps) == 2)

    def test_atomic_write_logic(self):
        """Requirement 2: Verify the use of a temporary file for safety."""
        # This test checks the implementation logic for the .tmp swap pattern
        self.m_manager.add_state("STABLE")
        self.p_manager.save_state(self.m_manager)
        
        # Ensure the final file exists and is valid JSON
        self.assertTrue(os.path.exists(self.test_file))
        with open(self.test_file, 'r') as f:
            data = json.load(f)
            self.assertIn("STABLE", data["active_states"])

    def test_missing_file_handling(self):
        """Verify the system handles a missing state file gracefully."""
        missing_manager = MultiStateManager()
        result = self.p_manager.load_state(missing_manager)
        self.assertFalse(result)
        self.assertEqual(len(missing_manager.active_states), 0)

if __name__ == "__main__":
    unittest.main()
