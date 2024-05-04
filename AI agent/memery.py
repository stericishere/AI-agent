from prompt import new_prompt
class SessionMemory:
    def __init__(self):
        self.sessions = {}

    def add_interaction(self, session_id, user_input, bot_response):
        if session_id not in self.sessions:
            self.sessions[session_id] = []
            self.sessions[session_id].append({"user": new_prompt, "bot": "sure"})
        self.sessions[session_id].append({"user": user_input, "bot": bot_response})


    def get_session_history(self, session_id):
        history = "Previous interactions:\n"
        for conversation in self.sessions.get(session_id, []):
            history += f"User: {conversation['user']}\n"
            history += f"Agent Response: {str(conversation['bot'])}\n"
        return history if history != "Previous interactions:\n" else "No history found."

    def end_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]  # Clear session data to free memory

# Example Usage
memory = SessionMemory()