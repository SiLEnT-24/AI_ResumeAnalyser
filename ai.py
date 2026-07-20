from openai import OpenAI
import json

client = OpenAI()

def analyze_resume(resume_text, use_goal):
    prompt = f"""

you are a senior software engineer and hiring manager

Evaluate the resume based on the user's goal

User goal:"{user_goal}"

STRICT RULES:
-Extractionly relevant skills for this goal
-Remove irrelevant tools [excel for backened, etc]
-Identify real gaps
-Generate roadmap only for missing fields
-Makes output DIFFERENT based on goal

Return only JSON:
{{
    "skills":[],
    "missing_skills":[],
    "roadmap":[],
    "interview_questions":[]
}}

Resume:
{resume_text}

"""

   try:
    response = client.chat.completions.create(
        models="gpt-4.1-mini",
        temperature=0.3,
        messages=[
            {"role":"system","content": "you're a strict hiring manager."}
            {"role":"user", "content":prompt}
        ]
    )

    content = response.choice[0]