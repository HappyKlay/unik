from abc import ABC, abstractmethod

class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audio_type: str, file_name: str):
        pass
class AudioPlayer:
    def play_audio(self, file_name: str):
        print(f"Playing audio: {file_name}")
class MediaAdapter(MediaPlayer):
    def __init__(self, audio_player: AudioPlayer):
        self.audio_player = audio_player

    def play(self, audio_type: str, file_name: str):
        if audio_type.lower() == "mp3":
            self.audio_player.play_audio(file_name)
        else:
            print(f"Cannot play {audio_type} file")
class AudioPlayerAdapter(MediaPlayer):
    def __init__(self):
        self.audio_player = AudioPlayer()

    def play(self, audio_type: str, file_name: str):
        # Якщо це mp3, використовуємо MediaAdapter
        adapter = MediaAdapter(self.audio_player)
        adapter.play(audio_type, file_name)
# Створюємо клієнта
player = AudioPlayerAdapter()

# Відтворюємо mp3 файл
player.play("mp3", "song.mp3")  # Виведе: Playing audio: song.mp3

# Спроба відтворити файл іншого формату
player.play("mp4", "video.mp4")  # Виведе: Cannot play mp4 file
