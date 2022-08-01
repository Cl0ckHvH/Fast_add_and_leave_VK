<h1 align="center">НОВЫЙ БОТ ТУТ: <a href="https://github.com/Cl0ckHvH/VKB_AlwaysInConversation">КЛИК</a></h1>
<p align="center">
    <img alt="Made with Python" src="https://img.shields.io/badge/Made%20with-Python-%23FFD242?logo=python&logoColor=white"></img>
</p>

## Подготовка
1. [Получите](https://vkhost.github.io/) токен вашего аккаунта
2. Отключите двухэтапную аутентификацию, если ещё не сделали этого

## Установка
### На Heroku
Понадобится аккаунт Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Cl0ckHvH/Fast_add_and_leave_VK)

1. Нажмите на кнопку Deploy to Heroku
2. В поле token введите токен вашего аккаунта
3. В поле user_id и user_password введите ваши логин и пароль (не волнуйтесь, ваши данные не уйдут в левые руки, можно даже код посмотреть)
4. В поле ID_user_to_add, ID_your, ID_chat введите ID пользователя, которого хотите добавить, ваш ID и ID чата 
5. В меню выбора региона выберите Europe для лучшей производительности и нажмите Deploy app
6. Готово. Чтобы он стабильно работал, держите его выключенным

### Локально
1. Установите [Python](https://www.python.org/downloads/) версии не ниже 3.6 и не выше 3.8.13, если ещё не сделали этого. При установке убедитесь, что отметили галочку ![Add Python to PATH](https://user-images.githubusercontent.com/42045258/69171091-557d2780-0b0c-11ea-8adf-7f819357f041.png)
2. [Скачайте](https://github.com/Cl0ckHvH/Fast_add_and_leave_VK/archive/refs/heads/main.zip) и распакуйте в любое место
3. Откройте командную строку и введите следующую команду:
```sh
pip install -r requirements.txt --upgrade
```
4. Откройте файл `config.toml` любым текстовым редактором и настройте приложение под себя
5. Для запуска введите в командную строку `python start.py`

##

Приложение было создано с целью, чтобы быстро зайти в беседу, добавить аккаунт и выйти с беседы, чтобы не смогли кикнуть

##

### Made by Cl0ck (me)
