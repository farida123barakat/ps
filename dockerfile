FROM  python:3.14.2
WORKDIR /docker
COPY . .
CMD ["python", "sp.py"]