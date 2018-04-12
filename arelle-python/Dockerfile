FROM docker.io/ubuntu:latest

RUN apt-get update
RUN apt-get -y install wget
RUN wget --directory-prefix="/tmp" http://arelle.org/wordpress/wp-content/uploads/downloads/2017/06/arelle-linux-x86_64-2017-06-01.tar.gz
RUN mkdir /opt/arelle
RUN tar xvfz /tmp/arelle-linux-x86_64-2017-06-01.tar.gz -C /opt/arelle/
RUN rm /tmp/arelle-linux-x86_64-2017-06-01.tar.gz
RUN apt-get -y install python
RUN apt-get -y install python2.7 python2.7-lxml python2.7-tk
RUN apt-get -y install python3.5 python3.5-lxml python3.5-tk
RUN apt-get -y install git-core
