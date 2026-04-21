# API Inventario TI

API REST desarrollada con Flask para gestionar dispositivos de TI.

## Endpoints

- GET /devices → Obtener todos los dispositivos
- GET /devices/{id} → Obtener un dispositivo
- POST /devices → Crear dispositivo
- PUT /devices/{id} → Actualizar dispositivo
- DELETE /devices/{id} → Eliminar dispositivo

## Ejemplo JSON

{
  "nombre": "Laptop Dell",
  "tipo": "Laptop",
  "estado": "Disponible",
  "area": "Sistemas"
}

## Cómo ejecutar

pip install -r requirements.txt  
python app.py

## Tecnologías

- Python
- Flask
- Flask-CORS