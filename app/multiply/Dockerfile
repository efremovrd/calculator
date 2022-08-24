from python:3.9

run groupadd --gid 5002 minotauro \
    && useradd --home-dir /home/minotauro --create-home --uid 5002 \
    --gid 5002 --shell /bin/sh --skel /dev/null minotauro

run mkdir /home/minotauro/multiply
copy . /home/minotauro/multiply
workdir /home/minotauro/multiply

user minotauro

run pip install --no-cache-dir -r requirements.txt

entrypoint ["python", "main.py"]
