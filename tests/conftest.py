import pytest
from src.generator.prompts import EmailPromptTemplate
from src.generator.api_client import OpenAIClient

@pytest.fixture
def prompt_template():
    return EmailPromptTemplate()

@pytest.fixture
def mock_api_client(monkeypatch):
    def mock_send(*args, **kwargs):
        return "Mocked API response"
    
    monkeypatch.setattr(OpenAIClient, "send_prompt", mock_send)
    return OpenAIClient(api_key="test_key")
