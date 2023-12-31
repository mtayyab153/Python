from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="API_KEY"
)



# openai.my_api_key = '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'

response = client.chat.completions.create(
model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Prompt",
        }
    ]
)

print(response)
print(response.choices[0].message["content"])