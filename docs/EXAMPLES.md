# 🚀 Ejemplos Prácticos

## Ejemplo 1: Correo Formal
```python
from src.generator import EmailGenerator

gen = EmailGenerator()
response = gen.generate(
    nombre="Laura Méndez",
    contexto="confirmación de reunión",
    detalles="El jueves 25/04 a las 15:00"
)

-Ejemplo 2:

from src.generator import OpenAIClient

client = OpenAIClient(api_key="tu_key")
response = client.send_prompt(
    system_prompt="Eres un asistente financiero...",
    user_prompt="Genera un email sobre..."
)

Ejemplo CLI

python src/main.py \
    --nombre "Carlos Ruiz" \
    --contexto "recordatorio de pago" \
    --tono "urgente"
