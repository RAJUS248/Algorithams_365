from agent import MotivationalAgent

class AgentWrapper:
    def __init__(self, api_key):
        self.agent = MotivationalAgent(api_key=api_key)

    def get_motivation(self, user_name, motivation_type):
        return self.agent.generate_response(user_name, motivation_type)
