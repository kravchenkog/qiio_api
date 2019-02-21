

FROM ubuntu:latest

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

RUN apt-get update && apt-get install -y git

WORKDIR /qiio_api

RUN git clone https://kravchenkog@bitbucket.org/kravchenkog/qiio_api.git .
RUN pip install -r requirements.txt

CMD ["pytest", ".", "--doctest-modules", "--spec", "--html=out/index.html"]
