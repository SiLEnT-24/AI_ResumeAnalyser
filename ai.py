import os
import json
from openai import OpenAI


def analyze_resume(resume_text, use_goal):
    prompt = f"""

you are a senior software engineer and hiring manager

Evaluate the resume based on the user's goal

User goal: "{use_goal}"

STRICT RULES:
- Extractionly relevant skills for this goal
- Remove irrelevant tools [excel for backened, etc]
- Identify real gaps
- Generate roadmap only for missing fields
- Make output DIFFERENT based on goal

Return only JSON:
{{
    "skills":[],
    "missing_skills":[],
    "roadmap":[
        {{"step": "Step title", "resources": ["Resource 1", "Resource 2"]}}
    ],
    "interview_questions":[
        {{"question": "Question text?", "tip": "How to answer hint"}}
    ]
}}

Resume:
{resume_text}

"""

    try:
        client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )
        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            temperature=0.3,
            messages=[
                {"role": "system", "content": "You are a senior software engineer and hiring manager."},
                {"role": "user", "content": prompt}
            ]
        )

        message = response.choices[0].message
        content = getattr(message, "content", "")
        start = content.find("{")
        end = content.rfind("}") + 1
        return json.loads(content[start:end])

    except Exception as e:
        return {
            "skills": [],
            "missing_skills": [],
            "roadmap": [],
            "interview_questions": [],
            "error": str(e),
        }