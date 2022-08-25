from python:3.9

run groupadd --gid 5005 minotauro \
    && useradd --home-dir /home/minotauro --create-home --uid 5005 \
    --gid 5005 --shell /bin/sh --skel /dev/null minotauro

run mkdir /home/minotauro/degree
copy . /home/minotauro/degree
workdir /home/minotauro/degree

user minotauro

run pip install --no-cache-dir -r requirements.txt

entrypoint ["python", "main.py"]
