# Python oficial (leve)
FROM python:3.13-slim

# Evita buffering no log
ENV PYTHONUNBUFFERED=1

# Criar diretório do app
WORKDIR /app

# Instalar dependências do sistema (compiladores + libs)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements primeiro para cache eficiente
COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copiar todo o projeto
COPY . /app/

# Expor a porta
EXPOSE 8000

# Rodar com Gunicorn
CMD ["gunicorn", "stockpile_django.wsgi:application", "--bind", "0.0.0.0:8000"]
