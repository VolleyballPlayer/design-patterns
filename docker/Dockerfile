FROM ubuntu:latest

RUN apt-get install -y default-jre
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-arm64

RUN apt-get install -y graphviz
ENV GRAPHVIZ_DOT=/usr/bin/dot

ENV PLANTUML_JAR=/opt/plantuml.jar
RUN apt-get -y update; \ 
    apt-get -y install curl; \
    curl -L https://sourceforge.net/projects/plantuml/files/1.2023.7/plantuml.1.2023.7.jar > ${PLANTUML_JAR}

RUN apt-get -y update; \
    apt-get -y install python3; \
    apt-get -y install python3-pip; \ 
    apt-get -y install pipx

RUN apt-get -y update; \
    apt-get -y install git; \
    git clone https://github.com/VolleyballPlayer/design-patterns.git && cd design-patterns; \
    pipx install tomlq; \
    pipx install -ve .
ENV PATH=$PATH:/root/.local/bin/

ENTRYPOINT [ "/bin/bash" ]