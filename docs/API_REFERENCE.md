 📚 Referencia de API

 Módulo `generator'

Clase `EmailGenerator`

```python
def generate(
    nombre: str,
    contexto: str,
    tono: str = "formal",
    detalles: str = ""
) -> dict

Parámetros:

nombre (str)*: Nombre del destinatario (mín. 2 caracteres)

contexto (str)*: Finalidad del correo (ej. "seguimiento de ventas")

tono (str): "formal"|"casual"|"urgente" (default: "formal")

detalles (str): Información adicional

Retorna;

{
    "asunto": str,
    "cuerpo": str,
    "timestamp": str
}

Clase OpenAIClient

def send_prompt(
    system_prompt: str,
    user_prompt: str,
    model: str = "gpt-4"
) -> str
