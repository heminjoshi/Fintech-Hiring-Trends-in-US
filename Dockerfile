FROM python:alpine3.9
COPY . /app
WORKDIR /app
RUN python -m pip install --upgrade pip setuptools
EXPOSE 5000
CMD python ./app.py