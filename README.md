# Custom AI Agent Framework
A modular multi-agent system built with **Python**, **Gemini 1.5**, and **Continue**.

## Setup
1. Install dependencies: `pip install google-generativeai python-dotenv duckduckgo-search`
2. Add your `GEMINI_API_KEY` to a `.env` file.
3. Run `python main.py`.

## Architecture
- **ResearchAgent**: Uses DuckDuckGo to gather real-time data.
- **WriterAgent**: Synthesizes data into high-quality Markdown reports.