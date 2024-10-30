FROM python:latest

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir git+https://github.com/VolleyballPlayer/design-patterns.git

CMD ["echo", "Starting design-pattern container"]