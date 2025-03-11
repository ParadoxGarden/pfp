FROM python

WORKDIR /app/

COPY * .

#RUN chmod 0744 ./upload.sh


RUN pip install -r ./requirements.txt


CMD [ "fastapi", "run", "/app/server.py", "--port", "8080", "--proxy-headers" ]
