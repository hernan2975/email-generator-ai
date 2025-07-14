
from dataclasses import dataclass
from pydantic import BaseModel, Field

class EmailPromptInputs(BaseModel):
    """Valida inputs del usuario con Pydantic."""
    nombre: str = Field(..., min_length=2)
    contexto: str = Field(..., max_length=100)
    tono: str = Field("formal", pattern="^(formal|casual|urgente)$")

@dataclass
class EmailPromptTemplate:
    SYSTEM_PROMPT = "Eres un asistente de redacción profesional..."
    
    def generate(self, inputs: EmailPromptInputs) -> str:
        return f"""
        Asunto: {inputs.contexto}
        Cuerpo:
        Estimado/a {inputs.nombre},
        ..."""
