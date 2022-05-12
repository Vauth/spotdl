FROM sandy1709/catuserbot:slim-buster

#clonning repo 
RUN git clone https://github.com/marshallcares/spotdl.git /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN python3 -m pip install --upgrade pip wheel && \
    python3 -m pip install -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
