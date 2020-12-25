FROM python:3
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN useradd -ms /bin/bash appuser
USER appuser
ENTRYPOINT python3 /app/subs.py
