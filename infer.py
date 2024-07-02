import os
import sys
from faster_whisper import WhisperModel

if len(sys.argv) < 2:
    print("Please provide a file path that relative to /app/ as an argument.")
    print()
    print("Usage 1: python /root/infer.py <file_path>")
    print("Usage 2: python /root/infer.py <file_path> '<initial_prompt>'")
    sys.exit(1)

file = sys.argv[1]

model = WhisperModel("medium", device="cuda")

segments, info = model.transcribe(file,
                                  # language="zh",
                                  initial_prompt=sys.argv[2] if len(
                                      sys.argv) > 2 else "請以繁體中文輸出",
                                  word_timestamps=True,
                                  vad_filter=True,
                                  vad_parameters=dict(min_silence_duration_ms=500))

print("Detected language '%s' with probability %f" %
      (info.language, info.language_probability))

vtt_file = os.path.splitext(file)[0] + ".vtt"

# Open the file in write mode
with open(vtt_file, "w") as f:
    # Write the VTT header
    f.write("WEBVTT\n\n")

    # Write each segment as a VTT cue
    for segment in segments:
        print("[%.2fs -> %.2fs] %s" %
              (segment.start, segment.end, segment.text))

        start_time = segment.start
        end_time = segment.end
        text = segment.text

        # Format the start and end times in HH:MM:SS.MS format
        start_time_str = "{:02d}:{:02d}:{:06.3f}".format(
            int(start_time // 3600), int((start_time % 3600) // 60), start_time % 60)
        end_time_str = "{:02d}:{:02d}:{:06.3f}".format(
            int(end_time // 3600), int((end_time % 3600) // 60), end_time % 60)

        # Write the cue identifier, start and end times, and text
        f.write("{} --> {}\n{}\n\n".format(start_time_str, end_time_str, text))
        f.flush()

print("VTT subtitles have been saved to {}".format(vtt_file))
