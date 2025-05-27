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

> ## Paso 1
>> Clona el repositorio
> `git clone https://github.com/EricEscobar527/django_rest`

> ## Paso 2
>> Nos dirigiremos a la raíz de nuestro proyecto donde se encuentra el archivo docker-compose.yml y ejecutamos el siguiente comando
> `docker-compose up --build -d`

> ## Paso 3
>> Validaremos que nuestro contenedor se haya creado de forma correcta
> Ingresando a alguna de las siguientes rutas

*   __localhost:8000__ 
*   __tu_ip:8000__ 

## Documentacion

*   __localhost:8000/api/redoc/__ 
*   __tu_ip:8000/api/redoc/__ 

# Contacto

*   __e888953@gmail.com__