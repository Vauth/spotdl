FROM sandy1709/catuserbot:slim-buster

#clonning repo 
RUN git clone https://github.com/marshallcares/spotdl.git /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip install https://github.com/New-dev0/Telethon/archive/Artifact.zip

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
