#obtener imagen base
FROM --platform=linux/amd64 python:3.10.4-slim-bullseye

#establecer variables de entorno
ENV PYTHON_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#directorio de trabajo
WORKDIR /code

#instalar dependencias
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#copiar proyecto
COPY . .