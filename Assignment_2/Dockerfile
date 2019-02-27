FROM python:alpine3.9
COPY . /code
WORKDIR /code
RUN python -m pip install --upgrade pip setuptools
EXPOSE 5000
CMD ["python", "FeaturePipeline.py"]