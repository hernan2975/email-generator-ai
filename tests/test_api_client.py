import pytest
from unittest.mock import Mock

class TestOpenAIClient:
    def test_send_prompt(self, mock_api_client):
        response = mock_api_client.send_prompt(
            system_prompt="test",
            user_prompt="test"
        )
        assert response == "Mocked API response"
    
    def test_connection_error(self, mock_api_client):
        mock_api_client.send_prompt = Mock(side_effect=ConnectionError)
        with pytest.raises(ConnectionError):
            mock_api_client.send_prompt("", "")
