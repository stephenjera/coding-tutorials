FROM alpine:latest

RUN apk update && apk add postgresql-client

WORKDIR /usr/src/app

COPY load_csv.sh .

RUN chmod +x load_csv.sh

CMD ["./load_csv.sh"]
