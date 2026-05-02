FROM python:3.12-slim

WORKDIR /app

COPY app.py .

RUN useradd -r -s /bin/false appuser

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8080

HEALTHCHECK --interval=15s --timeout=5s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/')" || exit 1

CMD ["python", "app.py"]
