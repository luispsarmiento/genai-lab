import os
import sys

# Añadir src al path para poder importar server
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from server import server

# Configurar el servidor
server.settings.log_level = os.environ.get("LOG_LEVEL", "INFO")
port = int(os.environ.get("PORT", "8000"))
server.settings.port = port
server.settings.host = "0.0.0.0"

# Iniciar el servidor directamente
if __name__ == "__main__":
    # Puedes usar transport="stdio" para MCP estándar sobre stdin/stdout
    # o transport="streamable-http" para comunicación vía HTTP
    transport = os.environ.get("TRANSPORT", "streamable-http")
    server.run(transport=transport)
