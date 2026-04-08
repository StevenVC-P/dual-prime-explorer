FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH=/app/src \
    PORT=8000

WORKDIR /app

COPY src ./src

EXPOSE 8000

CMD python -m dual_prime_explorer --serve --host 0.0.0.0 --port ${PORT:-8000}
