import os
import google.generativeai as genai

class WriterAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def run(self, research_material):
        prompt = f"""
        You are a Tech Journalist. Using the research below, write a professional 
        Markdown blog post with a Title, Introduction, Key Points, and Conclusion.
        
        Research: {research_material}
        """
        return self.model.generate_content(prompt).text