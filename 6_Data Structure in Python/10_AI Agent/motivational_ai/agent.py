import openai
import os

class MotivationalAgent:
    def __init__(self, name="Motivo", api_key=None):
        self.name = name
        openai.api_key = api_key or os.getenv("OPENAI_API_KEY")

    def build_prompt(self, user_name, motivation_type):
        return f"""
You are a motivational coach named {self.name}. Your job is to inspire people based on their needs.

User name: {user_name}
Motivation type: {motivation_type}

Give a short, powerful motivational message tailored to this person.
"""

    def generate_response(self, user_name, motivation_type):
        prompt = self.build_prompt(user_name, motivation_type)
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.9
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {e}"
