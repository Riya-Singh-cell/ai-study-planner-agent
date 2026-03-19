from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Initialize LLM (Groq)
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant"
)

# ---------------- STUDY PLAN ---------------- #
def generate_plan(goal: str, days: int, level: str, hours: int):
    prompt = ChatPromptTemplate.from_template(
        """
        You are an intelligent AI study planner.

        Student Details:
        - Level: {level}
        - Study hours per day: {hours}
        - Days left: {days}

        Syllabus:
        {goal}

        Instructions:
        - Beginner → start from basics, fewer topics per day
        - Intermediate → balanced theory + practice
        - Revision → fast + formulas + important questions

        - Distribute topics across days
        - Include daily tasks
        - Keep realistic schedule

        Output format:

        Day 1:
        - Topic:
        - Practice:
        - Time:

        Day 2:
        ...
        """
    )

    chain = prompt | llm
    response = chain.invoke({
        "goal": goal,
        "days": days,
        "level": level,
        "hours": hours
    })

    return response.content


# ---------------- NOTES GENERATOR ---------------- #
def generate_notes(topic: str, level: str):
    prompt = ChatPromptTemplate.from_template(
        """
        You are an expert teacher.

        Generate easy-to-understand notes for the topic: {topic}

        Student level: {level}

        Instructions:
        - Beginner → simple explanation + examples
        - Intermediate → concise + clarity
        - Revision → short notes + formulas

        Include:
        - Explanation
        - Key points
        - Important formulas
        - Example problems

        Keep it structured and clean.
        """
    )

    chain = prompt | llm
    response = chain.invoke({
        "topic": topic,
        "level": level
    })

    return response.content