# C05 SPECIFICATION: API GATEWAY (REST INTERFACE)

Objective: Expose the state-synchronization engine via a RESTful API to allow remote monitoring and control.

Requirements:
- Endpoint: GET /status
  Returns the current active_states and their elapsed times in JSON format.
- Endpoint: POST /state/add
  Body: {"state": "STRING"}
  Action: Adds the state to the MultiStateManager and triggers a PersistenceManager.save_state().
- Endpoint: POST /state/remove
  Body: {"state": "STRING"}
  Action: Removes the state and triggers a save.
- Endpoint: GET /health
  Returns {"status": "OK"} if the engine is initialized and persistence is writable.

Framework: Use Flask or FastAPI (FastAPI preferred for auto-documentation).
