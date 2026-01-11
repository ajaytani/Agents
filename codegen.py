import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load the API key from your .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the model (Gemini 1.5 Flash is fastest for coding)
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_agent_logic(prompt):
    full_prompt = f"Write professional Python code for the following AI agent requirement: {prompt}. Only return the code block."
    
    response = model.generate_content(full_prompt)
    
    # Save the generated code to a new file
    with open("generated_agent.py", "w") as f:
        f.write(response.text.replace("```python", "").replace("```", ""))
    
    print("Code successfully generated in generated_agent.py")

# Test it
generate_agent_logic("A Python class that uses BeautifulSoup to scrape news and summarize it.")