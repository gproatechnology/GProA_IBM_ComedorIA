# app/main.py
# Punto de entrada principal para la aplicación Flask

from app import create_app

# Crear la instancia de la aplicación Flask
app = create_app()

# Ejecutar la aplicación en modo debug si se ejecuta directamente
if __name__ == '__main__':
    app.run(debug=True)