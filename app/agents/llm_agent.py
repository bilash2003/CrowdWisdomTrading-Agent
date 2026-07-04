from app.services.openrouter_service import OpenRouterService


class LLMAgent:

    def __init__(self):
        self.llm = OpenRouterService()

    def ask(self, question: str):

        return self.llm.ask(question)