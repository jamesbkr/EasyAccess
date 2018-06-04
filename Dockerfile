FROM centos:latest

MAINTAINER JamesBecker
RUN yum update -y
RUN yum install -y  epel-release
RUN yum install -y python-pip python-dev build-essemtial
RUN yum install -y unzip

COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt



COPY . /app
RUN unzip terraform_0.11.7_linux_amd64.zip
RUN mv terraform /usr/bin/
RUN terraform init -input=false terraform1/
ENTRYPOINT ["python"]
CMD ["app.py"]
