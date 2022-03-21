# pull the official base image
FROM python:3.9-alpine3.13

# set work directory
WORKDIR /P13

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV IMAGE adebayo935/python-lettings:circleci

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# copy project
COPY ./P13 /P13


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
