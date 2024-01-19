```bash
docker run --rm --interactive --tty --workdir "/app" --volume ".:/app" --publish 5000:5000 python:3.11.2 /bin/bash
```