# Делаем образ на основе официального образа ubuntu с python 3.8
FROM python:3.8
# Отключаем буферизацию кода
ENV PYTHONUNBUFFERED=1
# отключаем запись байт-кода в pyc файлы
ENV PYTHONDONTWRITEBYTECODE=1
# Устанавливаем в контейнере рабочую директорию
WORKDIR /usr/src/app
# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанаваливаем необходимые для работы компоненты и зависимости
RUN apt update \
    && apt install --no-install-recommends --no-install-suggests -y python3-dev \
    && python -m pip install --upgrade pip \
    && pip3 install -r requirements.txt

# После успешной установки зависимсотей копируем исходный код проекта в контейнер
COPY . .

