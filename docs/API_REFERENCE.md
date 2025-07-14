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
