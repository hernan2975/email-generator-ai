from dataclasses import dataclass
from pydantic import BaseModel, Field

class EmailPromptInputs(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    contexto: str = Field(..., max_length=100)
    tono: str = Field("formal", pattern="^(formal|casual|urgente)$")
    detalles: str = Field("", max_length=200)

@dataclass
class EmailPromptTemplate:
    def generate(self, inputs: EmailPromptInputs) -> str:
        return f"""
        Asunto: {inputs.contexto.capitalize()}
        Cuerpo:
        Estimado/a {inputs.nombre},
        {self._get_tone_phrase(inputs.tono)} {inputs.contexto}.
        {inputs.detalles if inputs.detalles else ""}
        Saludos cordiales,
        [Tu Nombre]
        """
    
    def _get_tone_phrase(self, tono: str) -> str:
        phrases = {
            "formal": "Le escribo en relación a",
            "casual": "Te contacto por",
            "urgente": "Es urgente que hablemos sobre"
        }
        return phrases.get(tono, "")
