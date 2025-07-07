from openai import OpenAI

from nx_ai.openai_service.gpt_models import GPTResponse, FakeResponse


client = OpenAI()


def say_hello_to_gpt(simulate):
    if simulate:
        mock_text = "Hello, simulated World"
        mock_response = GPTResponse(FakeResponse(mock_text))
        
        return mock_response
    
    response = client.responses.create(
        model="gpt-4o-mini",
        input="Hello, World!"
    )
    gpt_response = GPTResponse(response)
    
    return gpt_response
