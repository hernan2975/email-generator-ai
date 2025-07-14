from src.generator import EmailGenerator

class TestEmailGenerationFlow:
    def test_full_flow(self, mock_api_client):
        generator = EmailGenerator(api_client=mock_api_client)
        result = generator.generate(
            nombre="Laura",
            contexto="confirmación",
            tono="formal"
        )
        assert isinstance(result, dict)
        assert "asunto" in result
        assert "cuerpo" in result
