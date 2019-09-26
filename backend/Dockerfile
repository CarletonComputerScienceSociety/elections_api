FROM alpine

COPY ./ /app/

WORKDIR /app/

RUN apk add python3 php7 php7-openssl; \
    pip3 install -r util/requirements.txt

CMD [ "python3", "-u", "server.py" ]