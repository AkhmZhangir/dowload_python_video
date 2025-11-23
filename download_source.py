import yt_dlp
import os

# Открытие окна командной строки
os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана, для Windows или Unix-подобных систем

print("Введите ссылку на видео для скачивания:")

video_url = input()  # Получение URL видео

ydl_opts = {
    'format': 'bestvideo*+bestaudio/best',
    'merge_output_format': 'mp4',
    'postprocessor_args': [
        '-c:v', 'copy',       # не перекодировать видео
        '-c:a', 'aac',        # перекодировать аудио в AAC
        '-b:a', '192k'        # битрейт аудио
    ],
    'outtmpl': '%(title)s.%(ext)s'  # имя файла как название видео
}

# Скачивание видео
yt_dlp.YoutubeDL(ydl_opts).download([video_url])
