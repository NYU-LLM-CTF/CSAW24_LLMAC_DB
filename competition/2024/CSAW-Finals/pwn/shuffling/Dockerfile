FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat
RUN apt-get install -y gcc-4.9
RUN apt-get install -y binutils
RUN apt-get upgrade -y libstdc++6
RUN apt-get install -y gcc-12 g++-12
RUN useradd -ms /bin/sh ctf
WORKDIR /home/ctf

COPY ./shuffle ./
COPY ./flag.txt /

RUN chown -R ctf:ctf /home/ctf && \
     chmod 750 /home/ctf && \
     chmod 550 /home/ctf/shuffle && \
     chown ctf:ctf /flag.txt && \
     chmod 440 /flag.txt

EXPOSE 9999

USER ctf

CMD ["socat", "-T60", "TCP-LISTEN:9999,reuseaddr,fork","EXEC:/home/ctf/shuffle,pty,stderr"]
