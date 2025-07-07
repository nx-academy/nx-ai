from openai import OpenAI


client = OpenAI()


def say_hello_to_gpt():
    response = client.responses.create(
        model="gpt-4o-mini",
        input="Hello, World!"
    )
    
    return response
