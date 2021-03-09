FROM ***.dkr.ecr.ap-northeast-1.amazonaws.com/python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE 8001
CMD [ "uwsgi","--socket",":8001","--module","dw.wsgi","--py-autoreload","1","--logto", "/tmp/uwsgi.log" ] 