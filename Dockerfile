FROM python:3.8-slim
RUN apt-get update && \
    apt-get upgrade --yes
RUN useradd --create-home kate
USER kate
WORKDIR /home/kate/tic-tac-toe
ENV VIRTUALENV=/home/kate/tic-tac-toe/venv 
RUN python -m venv $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"
COPY --chown=kate constraints.txt pyproject.toml ./
RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -c constraints.txt ".[dev]"
COPY --chown=kate src/ src/
COPY --chown=kate test/ test/
RUN python -m pip install . -c constraints.txt && \
    python -m pytest test/
ENTRYPOINT ["python", "./src/tic_tac_toe/main.py"]
