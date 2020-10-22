FROM ubuntu:18.04

COPY setup-env.sh /tmp/setup-env.sh
RUN bash /tmp/setup-env.sh
RUN rm -f /tmp/setup-env.sh
