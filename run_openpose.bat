@echo off
REM ===== Double-click to process one hard-coded video =====
REM Change testvideo.mp4 to whatever file lives in .\input\

docker run --rm --gpus all -it ^
  -v "%CD%\models:/opt/openpose/models" ^
  -v "%CD%\input:/opt/openpose/input" ^
  -v "%CD%\output:/opt/openpose/output" ^
  uoresearch/openpose:cuda12 ^
  /opt/openpose/build/examples/openpose/openpose.bin ^
  --model_folder /opt/openpose/models ^
  --video /opt/openpose/input/testvideo.mp4 ^
  --write_video /opt/openpose/output/out.avi ^
  --write_json  /opt/openpose/output ^
  --display 0 --face --hand

pause
