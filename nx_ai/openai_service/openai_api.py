from openai import OpenAI

from nx_ai.openai_service.gpt_models import GPTResponse


client = OpenAI()


def say_hello_to_gpt():
    response = client.responses.create(
        model="gpt-4o-mini",
        input="Hello, World!"
    )
    gpt_response = GPTResponse(response)
    
    return gpt_response
