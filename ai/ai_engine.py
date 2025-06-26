# ai/ai_engine.py

import openai

def setup_ai(api_key):
    # Store the API key in OpenAI's client object
    global client
    client = openai.OpenAI(api_key=api_key)

def summarize_with_ai(output_data):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Summarize and prioritize the following scan results."},
                {"role": "user", "content": output_data}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[!] AI summarization failed: {e}"
