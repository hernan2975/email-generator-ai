# 📧 Email Generator AI

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Genera correos electrónicos personalizados con IA. Perfecto para equipos de ventas, soporte y más.

## ✨ Features
- ✅ Generación con GPT-4.
- ✅ Soporta múltiples tonos (formal, casual).
- ✅ Validación de inputs con Pydantic.
- ✅ Logging profesional.

## 🛠️ Instalación
```bash
git clone https://github.com/tu-usuario/email-generator-ai.git
cd email-generator-ai
pip install -e .

🚀 Uso Rápido

from src.generator import EmailGenerator

generator = EmailGenerator(api_key="tu_key")
print(generator.generate(nombre="Ana", contexto="seguimiento"))

📄 Licencia
MIT. Ver LICENSE.
