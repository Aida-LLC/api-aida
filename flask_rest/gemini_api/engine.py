import textwrap
import google.generativeai as genai
from .credentials import gemini_key


class Engine:
    def __init__(self, genai=genai):
        self.genai = genai
        self.GOOGLE_API_KEY=gemini_key
        self.genai.configure(api_key=self.GOOGLE_API_KEY)
        self.model = None

    def list_models(self):
        _models = []
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                _models.append(m)
        return _models

    def load_model(self, model_name):
        self.model = genai.GenerativeModel(model_name)

    def generate_text(self, prompt):
        if self.model is None:
            raise ValueError("Model not loaded")
        return self.model.generate_content(prompt)
