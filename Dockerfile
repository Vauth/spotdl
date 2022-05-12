FROM sandy1709/catuserbot:slim-buster

#clonning repo 
RUN git clone https://github.com/marshallcares/spotdl.git /root/userbot
#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip install -r --no-cache-dir requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
