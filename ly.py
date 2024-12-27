import re
from pydub import AudioSegment

def extract_timestamps_from_lrc(lrc_file):
    timestamps = []
    with open(lrc_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            match = re.match(r'\[(\d{2}):(\d{2}\.\d{2})\]', line)
            if match:
                minutes = int(match.group(1))
                seconds = float(match.group(2))
                timestamp = minutes * 60 + seconds
                timestamps.append(timestamp)
    return timestamps

def split_audio(audio_file, timestamps):
    audio = AudioSegment.from_file(audio_file)

    timestamps = [ts * 1000 for ts in timestamps]

    segments = []
    start_time = 0
    for time_point in timestamps:
        segment = audio[start_time:time_point]
        segments.append(segment)
        start_time = time_point

    segments.append(audio[start_time:])

    # 导出每
    for i, segment in enumerate(segments):
        segment.export(f"anno/output_{i+1}.mp3", format="mp3")


lrc_file = "あれくん; 『ユイカ』 - あのね。.lrc"  # LRC文件路径
audio_file = "anone -3db_vocals_anon1.0_12key_sovits_rmvpe.wav"  # 音频文件路径

timestamps = extract_timestamps_from_lrc(lrc_file)
split_audio(audio_file, timestamps)
