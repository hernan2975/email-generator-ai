
#!/bin/bash
# Despliegue en producción

ENV=${1:-dev}

case $ENV in
    prod)
        echo "🚀 Desplegando en producción..."
        pip install -e .[prod]
        ;;
    *)
        echo "🔧 Modo desarrollo"
        pip install -e .[dev]
        ;;
esac

echo "⚡ Ejecutando tests..."
pytest -v || {
    echo "❌ Tests fallidos";
    exit 1;
}

echo "🎉 Despliegue exitoso"
