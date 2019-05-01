FROM alpine

RUN apk update

#create user 'enduser' to run the system
RUN adduser -Ds /bin/sh enduser

#install python3
RUN apk add python3

COPY smart_rockets.py /home/enduser/smart_rockets.py

USER enduser
WORKDIR /home/enduser/

ENTRYPOINT [ "python3", "smart_rockets.py" ]
