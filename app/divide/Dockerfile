from python:3.9

run groupadd --gid 5004 minotauro \
    && useradd --home-dir /home/minotauro --create-home --uid 5004 \
    --gid 5004 --shell /bin/sh --skel /dev/null minotauro

run mkdir /home/minotauro/divide
copy . /home/minotauro/divide
workdir /home/minotauro/divide

user minotauro

run pip install --no-cache-dir -r requirements.txt

entrypoint ["python", "main.py"]
