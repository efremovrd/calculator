from python:3.9

run groupadd --gid 5000 minotauro \
    && useradd --home-dir /home/minotauro --create-home --uid 5000 \
    --gid 5000 --shell /bin/sh --skel /dev/null minotauro

run mkdir /home/minotauro/calculator
copy . /home/minotauro/calculator
workdir /home/minotauro/calculator

user minotauro

run pip install --no-cache-dir -r requirements.txt

entrypoint ["python", "main.py"]
