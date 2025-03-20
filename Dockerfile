FROM ubuntu:latest

ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-arm64
ENV GRAPHVIZ_DOT=/usr/bin/dot
ENV PLANTUML_JAR=/opt/plantuml.jar

RUN apt-get -y update; \
    apt-get install -y default-jre; \
    apt-get install -y graphviz; \
    apt-get -y install curl; \
    curl -L https://sourceforge.net/projects/plantuml/files/1.2023.7/plantuml.1.2023.7.jar > ${PLANTUML_JAR}; \
    apt-get -y install python3; \
    apt-get -y install python3-pip; \
    apt-get -y install pipx; \
    apt-get -y install git; \
    git clone https://github.com/VolleyballPlayer/design-patterns.git && cd design-patterns; \
    python3 -m venv .venv && chmod +x .venv/bin/activate && . .venv/bin/activate && pip install -e .[dev,docs,test]; \
    . ./docs/source/call_sphinx_apidoc.sh; \
    cd docs; sphinx-build -b html -E source html; \
    run-creational-pattern factory-method; \
    run-creational-pattern builder; \
    run-creational-pattern abstract-factory; \
    run-creational-pattern prototype; \
    run-creational-pattern singleton; \
    run-structural-pattern adapter; \
    run-structural-pattern facade; \
    run-structural-pattern bridge; \
    run-structural-pattern composite; \
    run-structural-pattern flyweight; \
    run-structural-pattern decorator; \
    run-structural-pattern proxy; \
    run-behavioral-pattern strategy; \
    run-behavioral-pattern observer; \
    run-behavioral-pattern command; \
    run-behavioral-pattern mediator; \
    run-behavioral-pattern template-method; \
    run-behavioral-pattern iterator; \
    run-behavioral-pattern chain-of-responsibility; \
    run-behavioral-pattern visitor; \
    run-behavioral-pattern state

ENTRYPOINT [ "/bin/bash" ]
