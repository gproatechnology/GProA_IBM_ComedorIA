# Sistema de Comedor IA - IBM

MVP de un sistema de gestión de cafetería corporativa con asistencia AI para entornos IBM.

## Arquitectura

- **Backend**: Flask con Blueprints, SQLAlchemy, PostgreSQL.
- **Frontend**: HTML5/CSS3/JS vanilla, responsivo y optimizado para kioscos.
- **Autenticación**: Role-based (admin, employee, kiosk) con Flask-Login.
- **AI**: Stub service para futuras integraciones (IBM watsonx).

## Instalación

1. Clona el repo: `git clone https://github.com/gproatechnology/GProA_IBM_ComedorIA.git`
2. Crea un entorno virtual: `python -m venv venv`
3. Activa: `source venv/bin/activate` (Linux/Mac) o `venv\Scripts\activate` (Windows)
4. Instala dependencias: `pip install -r requirements.txt`
5. Configura variables de entorno en `.env`:
   ```
   SECRET_KEY=tu_clave_secreta
   DATABASE_URL=postgresql://user:password@localhost/comedor_db
   DEBUG=True
   ```
6. Inicializa DB: `flask db init` (si usas Flask-Migrate), o ejecuta `python run.py` para crear tablas automáticamente.

## Ejecución Local

- `python run.py`
- Accede a http://localhost:5000

## Despliegue

- **Local**: Usa Flask dev server.
- **Producción**: Gunicorn + Nginx, PostgreSQL en cloud.
- **Kioscos**: Navegadores en modo fullscreen.

## Uso

- **Empleados**: Login → Dashboard → Seleccionar menú.
- **Admins**: Login → Admin panel → Gestionar menús, ver reportes.
- **Kiosk**: /kiosk → Seleccionar menú sin login.

## Extensión

- AI: Implementar en `app/services/ai_service.py` para recomendaciones.
- Más features: Agregar Blueprints nuevos siguiendo la estructura.

## Licencia

Ver LICENSE.