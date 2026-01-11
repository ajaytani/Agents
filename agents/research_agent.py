import os
import google.generativeai as genai
from tools.search_tool import SearchTool

class ResearchAgent:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def run(self, topic):
        # Step 1: Brainstorm search queries
        plan_prompt = f"Provide 3 search queries to find the latest info on {topic}."
        queries = self.model.generate_content(plan_prompt).text.split('\n')
        
        # Step 2: Use Tool
        all_research = ""
        for q in queries:
            if q.strip():
                all_research += SearchTool.search(q)
        
        # Step 3: Summarize
        summary_prompt = f"Summarize this research for a technical writer:\n{all_research}"
        return self.model.generate_content(summary_prompt).text