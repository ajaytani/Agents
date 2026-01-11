class TaskDefinitions:
    @staticmethod
    def get_research_prompt(topic):
        return f"Research the following topic deeply: {topic}. Focus on 2026 trends."

    @staticmethod
    def get_writing_prompt(data):
        return f"Transform this data into a professional report: {data}"