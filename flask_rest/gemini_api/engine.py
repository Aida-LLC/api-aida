import textwrap
import google.generativeai as genai
from .credentials import gemini_key


class Engine:
    """
    A class used to interact with Google's Generative AI models.

    Attributes
    ----------
        genai : module
            A reference to the google.generativeai module.
        GOOGLE_API_KEY : str
            The API key used to authenticate with Google's AI services.
        model : GenerativeModel
            The currently loaded generative model.

    Methods
    -------
        list_models():
            Returns a list of all generative models that support the 'generateContent' method.
        load_model(model_name: str):
            Loads a generative model by its name.
        generate_text(prompt: str):
            Generates text using the currently loaded model and a given prompt.
    """
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
        else:
            # try:
            response = self.model.generate_content(prompt)
            return response.text
            # except:
            #     return "Failed to generate response. Please try again."

