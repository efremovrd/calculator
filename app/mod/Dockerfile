from python:3.9

run groupadd --gid 5006 minotauro \
    && useradd --home-dir /home/minotauro --create-home --uid 5006 \
    --gid 5006 --shell /bin/sh --skel /dev/null minotauro

run mkdir /home/minotauro/mod
copy . /home/minotauro/mod
workdir /home/minotauro/mod

user minotauro

run pip install --no-cache-dir -r requirements.txt

entrypoint ["python", "main.py"]
