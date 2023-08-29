# Utiliza la imagen base de Python
FROM python:3.10.1

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . /app

# Instala las dependencias necesarias
RUN pip install -U pip
RUN pip install rasa==3.6.6

# Expone el puerto en el que Rasa estará escuchando
EXPOSE 5005

# Comando para ejecutar Rasa
CMD ["rasa", "run", "-m", "models", "--enable-api", "--cors", "*", "--debug"]
