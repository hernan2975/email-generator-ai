
from src.generator.prompts import EmailPromptInputs, EmailPromptTemplate

class TestEmailPromptInputs:
    def test_valid_input(self):
        inputs = EmailPromptInputs(
            nombre="Ana",
            contexto="seguimiento",
            tono="formal"
        )
        assert inputs.nombre == "Ana"
    
    def test_invalid_tone(self):
        with pytest.raises(ValueError):
            EmailPromptInputs(
                nombre="Ana",
                contexto="test",
                tono="invalid"  # Tono no permitido
            )

class TestEmailPromptTemplate:
    def test_generate_prompt(self, prompt_template):
        prompt = prompt_template.generate(
            nombre="Carlos",
            contexto="recordatorio",
            tono="urgente"
        )
        assert "Carlos" in prompt
        assert "urgente" in prompt.lower()
