import re
from .exceptions import FormatError

class EmailPostProcessor:
    def process(self, raw_text: str) -> dict:
        try:
            asunto = re.search(r"Asunto: (.+)", raw_text).group(1)
            cuerpo = re.split(r"Cuerpo:\n", raw_text)[1]
            return {"asunto": asunto, "cuerpo": cuerpo.strip()}
        except (AttributeError, IndexError):
            raise FormatError("Invalid email format")
