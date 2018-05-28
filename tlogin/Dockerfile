FROM python:2.7-onbuild
MAINTAINER Rejeesh "rejeeshmangad@gmail.com"
COPY . /usr/src/app
RUN pip install -r requirements.txt
CMD ["python","-u","api.py"]