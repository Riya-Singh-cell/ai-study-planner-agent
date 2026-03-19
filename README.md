# 📚 AI Study Planner Agent – Intelligent Learning Assistant

AI Study Planner Agent is an **Agentic AI-powered web application** that generates personalized study schedules and dynamically adapts learning based on user level, available time, and exam deadlines. It also provides **AI-generated notes and explanations**, making it a complete smart learning assistant.

---

## 🚀 Project Objective

The goal of this project is to:

- Build an **adaptive AI system** for personalized study planning  
- Implement **agentic behavior** (plan + assist + guide)  
- Provide **level-based learning (Beginner / Intermediate / Revision)**  
- Integrate **AI-generated notes and explanations**  
- Develop an interactive and user-friendly dashboard  

---

## 🧠 AI Approach

The system leverages **Large Language Models (LLMs)** to:

- Analyze user input (syllabus, time, level)  
- Generate structured study plans  
- Adapt learning strategies based on difficulty level  
- Produce topic-wise notes and explanations  

The application behaves like an **AI study mentor** that:
- Plans  
- Guides  
- Explains  

---

## ⚙️ System Workflow

1. User inputs:
   - Syllabus/topics  
   - Days left  
   - Study hours  
   - Learning level  

2. AI generates:
   - Day-wise study plan  
   - Balanced theory + practice tasks  

3. User can:
   - Generate notes for any topic  
   - Learn concepts with examples  

---

## 📥 Input Parameters

- Study Topics / Syllabus  
- Days Remaining for Exam  
- Study Hours per Day  
- Learning Level:
  - Beginner  
  - Intermediate  
  - Revision  

---

## 📤 Output

- 📅 Personalized study schedule  
- 📚 AI-generated notes  
- 🧠 Concept explanations  
- 🎯 Structured daily tasks  

---

## 🏗️ Tech Stack

- Python  
- Streamlit (Frontend UI)  
- LangChain  
- Groq API (LLM inference)  
- python-dotenv  

---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/ai-study-planner-agent.git
cd ai-study-planner-agent

pip install -r requirements.txt
streamlit run streamlit_app.py
