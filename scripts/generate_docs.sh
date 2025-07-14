#!/bin/bash
# Genera documentación automática

echo "📝 Generando docs..."
pdoc --html src/generator -o docs/api --force

echo "📊 Estadísticas"
echo "Líneas de código: $(find src -name "*.py" | xargs wc -l | tail -1)"
