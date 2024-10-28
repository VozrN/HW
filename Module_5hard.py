import hashlib
import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()
        self.age = age

    def data_user(self):
        return self.nickname, self.password, self.age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def data_video(self):
        return self.title, self.duration, self.time_now, self.adult_mode


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, name, passw):
        for exm in self.users:
            passw_hash = hashlib.sha256(passw.encode()).hexdigest()
            if exm.data_user()[0] == name and exm.data_user()[1] == passw_hash:
                self.current_user = exm.data_user()[0]
        print(self.current_user)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for new_video in args:
            flag = 0
            for old_video in self.videos:
                if old_video.data_video()[0] == new_video.data_video()[0]:
                    flag = 1
                    break
            if flag == 0:
                self.videos.append(new_video)

    def get_videos(self, search_word):
        search_videos = []
        for old_video in self.videos:
            if old_video.data_video()[0].lower().find(search_word.lower()) != -1:
                search_videos.append(old_video.data_video()[0])
        return search_videos

    def watch_video(self, film_title):
        for i in self.videos:
            if film_title == i.data_video()[0]:
                if self.current_user != None:
                    for user_name in self.users:
                        if self.current_user == user_name.data_user()[0]:
                            user_age = user_name.data_user()[2]
                    if user_age >= 18:
                        for timing in range(i.data_video()[2], i.data_video()[1]):
                            time.sleep(1)
                            print(timing + 1, end=' ')
                        i.time_now = 0
                        print('Конец видео')
                    else:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    print('Войдите в аккаунт, чтобы смотреть видео')

    def register(self, name, passw, age):
        for exm in self.users:
            # print('проверка по ',exm.data_user())
            if exm.data_user()[0] == name:
                print(f'Пользователь {name} уже существует')
                return
        self.users.append(User(name, passw, age))
        self.current_user = self.users[-1].data_user()[0]


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
