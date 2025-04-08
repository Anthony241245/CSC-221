# Anthony Raynor
# 4/8/25
# M4Pro
# Use openai library to allow chatgpt
from openai import OpenAI

client = OpenAI(api_key="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")

response = client.responses.create(
    model="gpt-4o",
    input = "Tell me a short story about panda bears."
)

print(response.output_text)

