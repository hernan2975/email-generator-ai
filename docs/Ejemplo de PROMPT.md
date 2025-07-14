# Ejemplo de prompt estructurado (en español)
PROMPT_TEMPLATE = """
Eres un asistente de redacción de correos profesionales. Genera un correo electrónico en español basado en los siguientes datos:
- Destinatario: {nombre}
- Contexto: {contexto}
- Tono: {tono} (formal/casual/urgente)
- Detalles adicionales: {detalles}

Ejemplo de salida (tono formal):
---
Asunto: Recordatorio: Reunión de seguimiento  
Cuerpo:  
Estimado/a {nombre},  

Le escribo para recordarle nuestra reunión programada el [fecha] a las [hora]. Será una oportunidad para revisar [detalles].  

Quedo atento/a a su confirmación.  

Saludos cordiales,  
[Tu nombre]  
---

Genera un correo similar adaptado a los datos proporcionados.  
"""
