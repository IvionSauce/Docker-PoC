FROM alpine:3.15
RUN apk add --no-cache curl jq

WORKDIR /app
COPY mock-client.sh .
RUN chmod +x mock-client.sh

CMD ["./mock-client.sh"]
