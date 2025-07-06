import json


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
            self.data = self._parse_json(self.text)
            self.author = self.data["author"]
            self.title_fr = self.data["title_fr"]
            self.published_date = self.data["published_date"]
            self.content = self.data["article_content"]
        except (AttributeError, IndexError) as e:
            raise ValueError(f"Error when cleaning data from response: {e}")
        
    def __repr__(self):
        return f"<GPTCleanedArticle: {self.text[:60]}...>"
    
    def _parse_json(self, text):
        try:
            parsed = json.loads(text)
            return parsed.get("data")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error when decoding response as JSON: {e}")

    def to_dict(self):
        return {
            "text": self.text,
            "data": self.data,
            "author": self.author,
            "title_fr": self.title_fr,
            "published_date": self.published_date,
            "content": self.content
        }


class GPTSummarizedArticle:
    def __init__(self, raw_response):
        self.raw = raw_response
        try:
            self.text = raw_response.output[1].content[0].text
        except (AttributeError, IndexError) as e:
            raise ValueError(f"Error when parsing the summarized article: {e}")
        
    
    def __repr__(self):
        return f"<GPTSummarizedArticle: {self.text[:60]}...>"
    
    def to_dict(self):
        return {
            "text": self.text
        }


class GPTGeneratedQuiz:
    def __init__(self, raw_response):
        self.raw = raw_response
        try:
            self.text = raw_response.output[1].content[0].text
            self.data = self._parse_json(self.text)
        except (AttributeError, IndexError) as e:
            raise ValueError(f"Error when parsing the generated quiz: {e}")
    
    def __repr__(self):
        return f"<GPTGeneratedQuiz: {self.text[:60]}...>"
    
    def _parse_json(self, text):
        try:
            parsed = json.loads(text)
            return parsed.get("data", [])
        except json.JSONDecodeError as e:
            raise ValueError(f"Error when decoding response as JSON: {e}")
    
    def get_questions(self):
        return [q["question"] for q in self.data]
    
    def to_dict(self):
        return {
            "text": self.text,
            "data": self.data
        }
