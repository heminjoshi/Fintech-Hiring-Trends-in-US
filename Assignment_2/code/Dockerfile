FROM python:3.7
COPY . /code
WORKDIR /code
RUN python -m pip install --upgrade pip setuptools
RUN pip install luigi
RUN pip install pandas
RUN pip install NumPy
EXPOSE 5000
CMD ["python", "FeaturePipeline.py"]