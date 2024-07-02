# Faster Whisper Docker

## Just Run

```bash
docker run -it --rm --gpus all -v faster-whisper-data:/root/.cache -v "${PWD}:/app" willh/faster-whisper audio.mp3
```

```bash
docker run -it --rm --gpus all -v faster-whisper-data:/root/.cache -v "${PWD}:/app" willh/faster-whisper audio.mp3 "請以繁體中文輸出"
```

## Build

```bash
docker build -t faster-whisper -t willh/faster-whisper .
```

## Push

```bash
docker push willh/faster-whisper
```

## Run

Use PowerShell on Windows or Bash on Linux.

```powershell
docker run -it --rm --gpus all -v faster-whisper-data:/root/.cache -v "${PWD}:/app" faster-whisper <audiofile.mp3>
```

## Build and Run Locally

1. Setup Python Virtual Environment

    ```bash
    python -m venv .venv

    # Windows Batch
    .\.venv\Scripts\activate.bat

    # Windows PowerShell
    & .\.venv\Scripts\activate.ps1

    # Linux Bash
    source .venv/bin/activate
    ```

2. Install Dependencies

    ```bash
    python.exe -m pip install --upgrade pip

    pip3 install faster-whisper
    ```

3. Run

    `<Initial Prompt>` can be `請以繁體中文輸出` or `Please output in Traditional Chinese`.

    ```bash
    python3 infer.py "audio.mp3" "<Initial Prompt>"
    ```

    > There are issues: `Could not locate cudnn_ops_infer64_8.dll. Please make sure it is in your library path!` and `Could not locate cublasLt64_11.dll. Please make sure it is in your library path!`.

## Links

- [SYSTRAN/faster-whisper: Faster Whisper transcription with CTranslate2](https://github.com/SYSTRAN/faster-whisper)
- [willh/faster-whisper general | Docker Hub](https://hub.docker.com/r/willh/faster-whisper)
