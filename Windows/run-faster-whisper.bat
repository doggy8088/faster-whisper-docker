@echo off
setlocal enabledelayedexpansion

set "file_path=%~1"
set "file_name=%~nx1"
set "folder_path=%~dp1"

echo Debug Info:
echo file_path=%file_path%
echo file_name=%file_name%
echo folder_path=%folder_path%

cd "%folder_path%"

powershell -Command "& docker run -it --rm --gpus all -v faster-whisper-data:/root/.cache -v '%folder_path%:/app/' willh/faster-whisper '%file_name%' '�ХH�c�餤���X'"

echo ���槹���C�Ы����N�䵲��...
pause > nul