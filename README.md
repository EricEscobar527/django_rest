# Prueba Técnica - Desarrollo Django REST

Prueba para Wolf Sellers

## OBJETIVO

- Desarrollar un microservicio en Django REST Framework que permita la gestión de productos
mediante una API RESTful. El sistema debe exponer endpoints para crear, leer, actualizar y
eliminar productos, y debe funcionar en un entorno Docker.

## ENDPOINTS ESPERADOS

- Utilizar Django 4.2+ y Django REST Framework.
- Exponer una API para el modelo `Producto` con los siguientes campos:
• id (auto generado)
• nombre (char, requerido)
• descripcion (texto, opcional)
• precio (decimal, requerido)
• disponible (booleano, default=True)
- Base de datos: SQLite
- Estructura del proyecto debe funcionar con Docker y docker-compose
- Incluir pruebas básicas (unitarias o de endpoints)
- Documentación en Swagger o README con instrucciones de uso

## Requisitos

- GET /api/productos/ → Listar productos
- POST /api/productos/ → Crear producto
- GET /api/productos/{id}/ → Obtener producto
- PUT /api/productos/{id}/ → Actualizar producto
- DELETE /api/productos/{id}/ → Eliminar producto

## Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

1. **Clona el repositorio o colocate en la raiz de la carpeta descargada**:
   ```bash
   git clone https://github.com/EricEscobar527/crud_reina.git
   ```

2. **Colocate en la raiz del proyecto para crear y ejecutar las migraciones**:
    ```bash 
     python manage.py migrate         
    ```

2. **Ejecuta el proyecto en tu local**:
    ```bash
     python manage.py runserver       
    ```