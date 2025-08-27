from config import llm
from prompts import SYSTEM_PROMPT

class ChatBot:
    def __init__(self):
        self.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    def chat(self, user_input: str) -> str:
        """Process user input and generate Gemini response."""
        try:
            if any(word in user_input.lower() for word in ["exit", "quit", "end", "goodbye", "terminate"]):
                return "Thank you for your time! The interview process has ended. You will be contacted later."

            self.messages.append({"role": "user", "content": user_input})
            response = llm.invoke(self.messages)

            assistant_message = response.content
            self.messages.append({"role": "assistant", "content": assistant_message})

            return assistant_message

        except Exception as e:
            return f"Error processing message: {str(e)}"
