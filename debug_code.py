import openai

# Add your GPT-4 API key here
openai.api_key = "AIzaSyDWV45ORraCLR-82vvkeXpYiQX9I35pFVs"

def debug_code(code_snippet, language="cpp"):
    prompt = f"Debug the following {language} code:\n{code_snippet}\nExplain the issues and suggest fixes."
    
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=500
    )

    return response.choices[0].text.strip()
