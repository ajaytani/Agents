import os
from dotenv import load_dotenv
from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent
from tasks.task_definitions import TaskDefinitions

def main():
    load_dotenv()
    
    # Initialize agents
    researcher = ResearchAgent()
    writer = WriterAgent()
    
    # Define a topic
    topic = "The impact of AI Agents on Software Engineering in 2026"
    
    print(f"--- Starting Research on: {topic} ---")
    research_data = researcher.run(topic)
    
    print("--- Generating Report ---")
    final_report = writer.run(research_data)
    
    with open("output_report.md", "w") as f:
        f.write(final_report)
    
    print("Done! Report saved to output_report.md")

if __name__ == "__main__":
    main()