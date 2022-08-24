from python:3.9

run groupadd --gid 5003 minotauro \
    && useradd --home-dir /home/minotauro --create-home --uid 5003 \
    --gid 5003 --shell /bin/sh --skel /dev/null minotauro

run mkdir /home/minotauro/minus
copy . /home/minotauro/minus
workdir /home/minotauro/minus

user minotauro

run pip install --no-cache-dir -r requirements.txt

entrypoint ["python", "main.py"]
