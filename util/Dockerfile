FROM alpine

COPY ./ /app/

WORKDIR /app/

RUN apk add python3 php7 php7-openssl; \
    pip3 install -r requirements.txt

CMD [ "python3", "main.py" ]