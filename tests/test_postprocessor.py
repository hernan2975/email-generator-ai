
from src.generator.postprocessor import EmailPostProcessor

class TestEmailPostProcessor:
    def test_extract_subject(self):
        raw_text = "Asunto: Urgente\n\nCuerpo del mensaje..."
        processor = EmailPostProcessor()
        result = processor.process(raw_text)
        assert result["asunto"] == "Urgente"
    
    def test_empty_input(self):
        with pytest.raises(ValueError):
            EmailPostProcessor().process("")
