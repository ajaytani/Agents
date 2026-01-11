# Copilot Instructions for AI Agent Codegen Project

## Project Overview
This is a Python-based code generation tool that uses Google's Gemini AI to automatically generate professional Python code for AI agent requirements. The core functionality is in `codegen.py`, which interfaces with the Gemini 1.5 Flash model for fast code generation.

## Key Dependencies and Setup
- **Google Generative AI**: Use `google.generativeai` (imported as `genai`) for all AI interactions
- **Environment Variables**: Load API key from `.env` file using `GEMINI_API_KEY`
- **Model**: Always use `'gemini-1.5-flash'` for optimal speed in coding tasks

## Code Generation Patterns
- **Prompt Structure**: Prefix user prompts with "Write professional Python code for the following AI agent requirement:" and append ". Only return the code block."
- **Response Processing**: Strip markdown code blocks (`\`\`\`python` and `\`\`\``) from AI responses before saving
- **Output**: Save generated code to `generated_agent.py` in the project root

## File Structure
- `codegen.py`: Main script containing the `generate_agent_logic()` function
- `generated_agent.py`: Auto-generated output file (created/overwritten on each run)
- `.env`: Contains `GEMINI_API_KEY` (not committed to version control)

## Example Usage
```python
generate_agent_logic("A Python class that uses BeautifulSoup to scrape news and summarize it.")
```
This generates a complete, runnable Python class in `generated_agent.py` that implements web scraping functionality.

## Development Workflow
- Install dependencies: `pip install google-generativeai python-dotenv`
- Set up `.env` with your Gemini API key
- Run `python codegen.py` to test the generation (uses the hardcoded example prompt)
- Modify the prompt in `generate_agent_logic()` call for custom code generation

## Integration Points
- External API: Google Gemini via `genai.generate_content()`
- No internal services or databases; standalone script
- Output integrates with standard Python execution (generated code is immediately runnable)