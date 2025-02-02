import openai

openai.api_key = "your-api-key-here"

def review_code(code):
    prompt = f"Перевір код Python та дай коментарі:
{code}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    return response["choices"][0]["text"].strip()

code_snippet = "def add(a, b): return a+b"
print(review_code(code_snippet))
