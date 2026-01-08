FROM python

WORKDIR /app/

COPY * .

RUN pip install -r ./requirements.txt

CMD [ "fastapi", "run", "/app/server.py", "--port", "8080", "--proxy-headers" ]
