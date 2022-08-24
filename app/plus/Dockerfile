from python:3.9

run groupadd --gid 5001 minotauro \
    && useradd --home-dir /home/minotauro --create-home --uid 5001 \
    --gid 5001 --shell /bin/sh --skel /dev/null minotauro

run mkdir /home/minotauro/plus
copy . /home/minotauro/plus
workdir /home/minotauro/plus

user minotauro

run pip install --no-cache-dir -r requirements.txt

entrypoint ["python", "main.py"]
