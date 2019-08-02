# FROM alpine:3.10
FROM mysql:8.0.17

# Install mysql client
# RUN apk add --no-cache mysql-client

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d

# ENTRYPOINT ["mysql"]