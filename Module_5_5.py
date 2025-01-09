import hashlib
import time


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hash_password(password)
        self.age = age
        # print(f'User: {nickname}  password: {password}  age: {age}')

    def hash_password(self, password):
        return hashlib.sha224(password.encode()).hexdigest()

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __str__(self):
        return f'{self.nickname}'


class Video:

    def __init__(self, title, duration, time_now, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title.lower() == other.title.lower()

    def __str__(self):
        return f"Video(title='{self.title}', duration={self.duration}, adult_mode={self.adult_mode})"

class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = hashlib.sha224(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Пользователь {nickname} вошёл в систему.")
                return True
        print("Ошибка входа: неверный логин или пароль.")
        return False

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user in self.users:
            print(f"Пользователь {nickname} уже существует.")
        else:
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add_video(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_video(self, get_title):
        get_movi = get_title.lower()
        return [video.title for video in self.videos if get_movi in video.title.lower()]

    def watch_video(self, title):
        if self.current_user not in self.users:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for time_in_sec in range(video.time_now, video.duration):
                    print(time_in_sec, end=' ')
                    time.sleep(1)
                print("Конец видео")
                video.time_now = 0
                return


Urban_Tu = UrTube()
video1 = Video('Лучший язык программирования 2024 года', 100, 0)
video2 = Video('Для чего девушкам парень программист?', 10, 0, adult_mode=True)

Urban_Tu.add_video(video2, video1)

print(Urban_Tu.get_video('лучший'))
print(Urban_Tu.get_video('ПРОГ'))

Urban_Tu.register('vasya_pupkin', 'fixpass', 13)
Urban_Tu.watch_video('Для чего девушкам парень программист?')

Urban_Tu.register('urban_pythonist', 'DfgKL456NBVn%I', 25)
Urban_Tu.watch_video('Для чего девушкам парень программист?')

Urban_Tu.register('vasya_pupkin', 'fixpass', 55)
print(Urban_Tu.current_user)

Urban_Tu.watch_video('язык программирования 2024 года!')