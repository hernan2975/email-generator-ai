# 📚 API Reference

## Clase `EmailPromptTemplate`
```python
generate(inputs: EmailPromptInputs) -> str

Parámetros:

nombre (str): Mínimo 2 caracteres.

contexto (str): Descripción del propósito del correo.

tono (str): Valores permitidos: formal, casual, urgente.

Clase OpenAIClient

send_prompt(prompt: str) -> str

Returns:

Respuesta generada por GPT-4.


#### **3. `docs/EXAMPLES.md`**  
```markdown
# 📌 Ejemplos de Uso

## Generar correo formal
```python
from src.generator import EmailGenerator

generator = EmailGenerator()
correo = generator.generate(
    nombre="Carlos",
    contexto="recordatorio de pago",
    tono="formal"
)
Usar desde CLI
python src/main.py --nombre "Ana" --contexto "agradecimiento"


#### **4. `scripts/setup_environment.sh`**  
```bash
#!/bin/bash
# Configura el entorno de desarrollo

echo "Instalando dependencias..."
pip install -e .[dev]

echo "Configurando variables de entorno..."
cp .env.template .env

echo "¡Listo! Asegúrate de añadir tu API key en .env"

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
