#!/bin/bash
# Configuración inicial del proyecto

echo "🐍 Instalando dependencias Python..."
pip install -e .[dev] || {
    echo "❌ Error al instalar dependencias";
    exit 1;
}

echo "🔐 Configurando entorno..."
if [ ! -f ".env" ]; then
    cp .env.template .env
    echo "⚠️ Edita el archivo .env con tus credenciales"
else
    echo ".env ya existe, omitiendo..."
fi

echo "✅ Setup completado"
