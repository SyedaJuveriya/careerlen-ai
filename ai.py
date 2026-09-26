from openai import OpenAI

import json
import os
import re

from dotenv import load_dotenv


# Load environment variables
load_dotenv()


# Get OpenRouter API key from .env
api_key = os.getenv("OPENROUTER_API_KEY")


# Create OpenRouter client
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)


def analyze_resume(resume_text, user_goal):

    prompt = f"""
You are a resume reviewer.

The candidate's goal is:
{user_goal}

Here is their resume:

{resume_text}

Analyze the resume and provide a detailed review.

Give a JSON response with these keys:

- "score": a number out of 100
- "strengths": a list of strong points
- "weaknesses": a list of gaps or issues
- "suggestions": a list of specific improvements to reach the candidate's goal

Only return valid JSON.
Do not use markdown code blocks.
Do not add any explanation before or after the JSON.
"""

    response = client.chat.completions.create(

        model="openrouter/free",

        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant "
                    "that analyzes resumes."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        max_tokens=4000,

        temperature=0.3
    )

    # Get AI response
    raw_output = response.choices[0].message.content

    # Try direct JSON parsing
    try:
        return json.loads(raw_output.strip())
    except json.JSONDecodeError:
        pass

    # Try extracting JSON from markdown code fences
    cleaned = raw_output.strip()
    if "```" in cleaned:
        parts = cleaned.split("```")
        if len(parts) >= 2:
            cleaned = parts[1]
            if cleaned.startswith("json"):
                cleaned = cleaned[4:]
            cleaned = cleaned.strip()
            try:
                return json.loads(cleaned)
            except json.JSONDecodeError:
                pass

    # Last resort: regex extract the first {...} block
    match = re.search(r'\{.*\}', raw_output, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            pass

    # Return error if JSON cannot be parsed
    return {
        "error": "Could not parse AI response",
        "raw": raw_output
    }