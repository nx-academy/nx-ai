import json


# Mock class for testing / simulation purposes
class FakeResponse:
    def __init__(self, text: str):
        self.output = [FakeOutput(text)]
    
class FakeOutput:
    def __init__(self, text: str):
        self.content = [FakeText(text)]
    
class FakeText:
    def __init__(self, text: str):
        self.text = text


# Real classes use for data modeling
class GPTResponse:
    def __init__(self, raw_response):
        self.raw = raw_response
        try:
            self.text = raw_response.output[0].content[0].text
        except (AttributeError, IndexError) as e:
            raise ValueError(f"Error when extracting data from response: {e}")

    def __repr__(self):
        return f"<GPTResponse: {self.text[:60]}...>"

    def to_dict(self):
        return {
            "text": self.text
        }


class GPTSummarizedArticle:
    def __init__(self, raw_response):
        self.raw = raw_response
        try:
            self.text = raw_response.output[0].content[0].text
            self.data = self._parse_json(self.text)
        except (AttributeError, IndexError) as e:
            raise ValueError(f"Error when modeling data from gpt reponse: {e}")
    
    def __repr__(self):
        return f"<GPTSummarizedArticle: {self.text[:60]}...>"
    
    def _parse_json(self, text):
        try:
            parsed = json.loads(text)
            return parsed.get("data")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error when decoding GPT Response as JSON: {e}")
    
    def to_dict(self):
        return {
            "text": self.text,
            "data": self.data
        }
