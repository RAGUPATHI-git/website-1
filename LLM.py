from huggingface_hub import InferenceClient



def llm(prompt : str):
    file = open('../PROJECT-1/Files/llm.txt', "w+")

    client = InferenceClient(
    "mistralai/Mistral-Nemo-Instruct-2407",
    token="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",
)

    for message in client.chat_completion(
        messages=[{"role": "user", "content": f"write the story about {prompt}"}],
        max_tokens=500,
        stream=True,
    ):
        file.write(message.choices[0].delta.content)
    file.close()
      





