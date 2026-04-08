from zai import ZaiClient
from Back_end.config import ZAI_API_KEY

client = ZaiClient(api_key=ZAI_API_KEY)

response = client.chat.completions.create(
    model="glm-4.6",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one short sentence."
        }
    ],
    max_tokens=50,
    temperature=0.7,
)

print(response.choices[0].message.content)
