# base image
FROM python:3.7.2-alpine

# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add netcat-openbsd

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./project/requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY . /usr/src/app

# run server
CMD python manage.py run -h 0.0.0.0
# CMD python project/app.py 
# CMD python project/app.py run -h 127.0.0.1:5000 

# TODO : Replace above command with this. See TODO seaction in readme
# CMD ["/usr/src/app/entrypoint.sh"]
