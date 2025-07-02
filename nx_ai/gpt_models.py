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


class GPTCleanedArticle:
    def __init__(self, raw_response):
        self.raw = raw_response
        try:
            self.text = raw_response.output[1].content[0].text
        except (AttributeError, IndexError) as e:
            raise ValueError(f"Error when cleaning data from response: {e}")
        
    def __repr__(self):
        return f"<GPTResponse: {self.text[:60]}...>"

    def to_dict(self):
        return {
            "text": self.text
        }
