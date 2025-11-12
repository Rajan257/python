# from openai import OpenAI

# # client=OpenAI
# client=OpenAI(api_key="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", )

# compelition =client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system","content": "You are a vitual assistant named jarvis, skilled in explaining complex programming concepts with creative flairs."},
#         {"role": "user", "content": " what is coding."}
#     ]
# )
# print(compelition.choice[0].message)

from openai import OpenAI

client = OpenAI(api_key="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")  # Make sure the key is valid

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "What is coding?"}
    ]
)

print(completion.choices[0].message.content)
