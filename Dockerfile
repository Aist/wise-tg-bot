FROM python:3.9.9-slim-buster
WORKDIR /code
RUN apt-get update && apt-get install -y \
    python3 \
    tzdata

ENV TZ="Europe/Moscow"

RUN ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/timezone && \
    ln -sf /usr/share/zoneinfo/Europe/Moscow /etc/localtime

COPY . .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot.py"]%