import os
from server import server

# Configurar el servidor
server.settings.log_level = os.environ.get("LOG_LEVEL", "INFO")
port = int(os.environ.get("PORT", "8000"))
server.settings.port = port
server.settings.host = "0.0.0.0"

# Iniciar el servidor directamente
if __name__ == "__main__":
    server.run(transport="streamable-http")