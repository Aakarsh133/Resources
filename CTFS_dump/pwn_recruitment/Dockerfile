FROM ubuntu:24.04

RUN apt-get update && \
    apt-get install -y socat dash && \
    rm -rf /var/lib/apt/lists/* && \
    ln -sf /bin/dash /bin/sh

EXPOSE 1337

RUN groupadd -r ctf && useradd -r -g ctf ctf

COPY challenge/ /home/ctf/

WORKDIR /home/ctf

RUN chown -R ctf:ctf /home/ctf && chmod +x /home/ctf/recruitment

USER ctf

CMD ["socat", "tcp-l:1337,reuseaddr,fork", "EXEC:./recruitment"]
