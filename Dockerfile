FROM sandy1709/catuserbot:slim-buster

#clonning repo 
RUN git clone https://github.com/marshallcares/spotdl.git /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN wget https://raw.githubusercontent.com/TgCatUB/catuserbot/master/requirements.txt && pip3 install -r --no-cache-dir requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
