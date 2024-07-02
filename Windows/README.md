# 擴充 Windows 檔案總管

1. 先將 `run-faster-whisper.bat` 複製到 `C:\Windows` 目錄下。

2. 套用 `run-faster-whisper (註冊檔案總管).reg` 機碼。

    或可直接**以系統管理員身分**執行以下指令：

    ```bat
    reg add "HKEY_CLASSES_ROOT\*\shell\RunFasterWhisper" /ve /d "使用 Faster Whisper 產生字幕" /f
    reg add "HKEY_CLASSES_ROOT\*\shell\RunFasterWhisper\command" /ve /d "\"C:\Windows\run-faster-whisper.bat\" \"%1\"" /f
    ```

## 注意事項

- 無論是 `run-faster-whisper.bat` 或 `run-faster-whisper (註冊檔案總管).reg` 檔案，都必須以 `Big5` 編碼儲存，否則會有亂碼出現。
