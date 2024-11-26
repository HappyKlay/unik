from abc import ABC, abstractmethod

# Реалізація для відтворення контенту
class MediaImplementor(ABC):
    @abstractmethod
    def play(self, file_name: str):
        pass
# Аудіо реалізація
class AudioPlayer(MediaImplementor):
    def play(self, file_name: str):
        print(f"Playing audio file: {file_name}")

# Відео реалізація
class VideoPlayer(MediaImplementor):
    def play(self, file_name: str):
        print(f"Playing video file: {file_name}")
# Абстракція, яка використовує реалізацію
class MediaPlayer(ABC):
    def __init__(self, implementor: MediaImplementor):
        self._implementor = implementor

    @abstractmethod
    def play_media(self, file_name: str):
        pass
# Клас для роботи з аудіо
class AudioMediaPlayer(MediaPlayer):
    def play_media(self, file_name: str):
        print("Audio player:")
        self._implementor.play(file_name)

# Клас для роботи з відео
class VideoMediaPlayer(MediaPlayer):
    def play_media(self, file_name: str):
        print("Video player:")
        self._implementor.play(file_name)
# Створення об'єкта для відтворення аудіо
audio_player = AudioMediaPlayer(AudioPlayer())
audio_player.play_media("song.mp3")  # Виведе: Audio player: Playing audio file: song.mp3

# Створення об'єкта для відтворення відео
video_player = VideoMediaPlayer(VideoPlayer())
video_player.play_media("movie.mp4")  # Виведе: Video player: Playing video file: movie.mp4
