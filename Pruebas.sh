#!/bin/bash

# ===========================================================
# SCRIPT DE PRUEBAS - SERVICIO DE HORA (SOCKETS TCP y UDP)
# ===========================================================
# Este script automatiza las pruebas para los programas Python:
# Cliente_TCP.py, Cliente_UDP.py, Servidor_TCP.py, Servidor_UDP.py
# ===========================================================

echo "=========================================="
echo "  SCRIPT DE PRUEBAS - SERVICIO DE HORA"
echo "=========================================="
echo ""

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Función para probar UDP
test_udp_python() {
    echo -e "${YELLOW}[TEST UDP PYTHON]${NC} Iniciando pruebas..."
    echo ""
    echo "Paso 1: Abre una nueva terminal y ejecuta el servidor con:"
    echo "        python3 Servidor_UDP.py"
    echo ""
    echo "Paso 2: Espera 2 segundos y presiona Enter para ejecutar el cliente"
    read -p ""
    
    echo "Ejecutando cliente UDP Python..."
    python3 Cliente_UDP.py
    echo ""
    
    echo "Para múltiples solicitudes automáticas, puedes ejecutar:"
    echo "for i in {1..5}; do python3 Cliente_UDP.py; sleep 1; done"
    echo ""
    
    echo "Para ver sockets UDP activos (en Linux):"
    echo "netstat -u | grep 12345"
    echo ""
}

# Función para probar TCP
test_tcp_python() {
    echo -e "${YELLOW}[TEST TCP PYTHON]${NC} Iniciando pruebas..."
    echo ""
    echo "Paso 1: Abre una nueva terminal y ejecuta el servidor con:"
    echo "        python3 Servidor_TCP.py"
    echo ""
    echo "Paso 2: Espera 2 segundos y presiona Enter para ejecutar el cliente"
    read -p ""
    
    echo "Ejecutando cliente TCP Python..."
    python3 Cliente_TCP.py
    echo ""
    
    echo "Para probar múltiples clientes concurrentes, abre más terminales y ejecuta:"
    echo "python3 Cliente_TCP.py"
    echo ""
    
    echo "Para ver conexiones TCP activas (en Linux):"
    echo "ss -tlnp | grep 12345"
    echo ""
}

# Función de prueba automática (requiere que los servidores estén corriendo)
test_automatico() {
    echo -e "${YELLOW}[TEST AUTOMÁTICO]${NC}"
    echo "Esta opción asume que los servidores UDP y TCP ya están ejecutándose."
    echo ""

    if netstat -tuln | grep -q ":12345"; then
        echo -e "${GREEN}✓${NC} Servidor detectado en puerto 12345"
        echo ""
        
        echo "Ejecutando 3 solicitudes UDP..."
        for i in {1..3}; do
            echo "--- Solicitud UDP $i ---"
            python3 Cliente_UDP.py 2>&1
            sleep 1
        done
        
        echo ""
        echo "Ejecutando 3 solicitudes TCP..."
        for i in {1..3}; do
            echo "--- Solicitud TCP $i ---"
            python3 Cliente_TCP.py 2>&1
            sleep 1
