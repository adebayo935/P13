# pull the official base image
FROM python:3.9-alpine3.13

# set work directory
WORKDIR /P13

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 9000

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# copy project
COPY . /P13


EXPOSE 9000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
