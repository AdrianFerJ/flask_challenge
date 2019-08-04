# base image
FROM python:3.7.2-alpine

# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add netcat-openbsd

# Expose port 5000 for Flask (instead of doing this in composer or config file)
EXPOSE 5000

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

# run server
# CMD python test_app.py 
CMD python app.py
# TODO : Replace above command with this. See TODO seaction in readme
# CMD ["/usr/src/app/entrypoint.sh"]
