# Tequila_Sunset_Bot

Данный репозиторий содержит код Telegram-бота, являющегося финальным проектом в курсе [DLSchool (Часть I, Осень 2022)](https://stepik.org/course/124069/syllabus) и реализующим перенос стиля.


## Особенности бота

Бот основан на фреймворке [aiogram](https://aiogram.dev), который позволяет обеспечить асинхронность "из коробки".

Данный бот использует подход, описанный Leon A. Gatys et al. в [данной статье](https://arxiv.org/abs/1508.06576). Имплементация взята [отсюда](https://pytorch.org/tutorials/advanced/neural_style_tutorial.html). Часть кода, отвечающая за перенос, выделена в отдельный класс и немного доработана для сопряжения с ботом.


## Развертывание бота

В качестве поставщика облака был выбран [timeweb](https://timeweb.com/ru/), предоставляющий виртуальные серверы по доступной цене. Выбрана конфигурация с 2 GB RAM.

Для развертывания бота необходимо выполнить следующие шаги:

1. Скопировать файлы из репозитория на сервер (с помощью git или по ssh).

2. Открыть консоль и перейти в каталог с загруженными файлами.

3. Обновить список пакетов и установить pip3:

    > sudo apt update

    > sudo apt install python3-pip

4. Установить необходимые пакеты:

    > pip3 install -r requirements.txt

5. Ввести в консоль токен своего Telegram-бота:

    > export TG_API_TOKEN="<ваш_токен>"

6. Запустить бота:

    > nohup python -u main.py 


_Примечание: эти шаги удобно было бы вынести в отдельный файл, что я и сделал. Файл setup.sh не включен в репозиторий, чтобы не раскрывать API-токен Telegram-бота._

## Примеры работы бота

### I. Собака + абстракционизм

Контент-изображение:

![Собака](https://i.imgur.com/CGJuWec.jpg)

Стиль-изображение:

![Абстракционизм](https://i.imgur.com/7mqtAUA.jpg)

Результат переноса:

!["Aбстрактная" собака](https://i.imgur.com/8S5rorv.jpg)


### II. Кошка + кубизм

Контент-изображение:

![Кошка](https://i.imgur.com/jaE1ZZS.jpg)

Стиль-изображение:

![Кубизм](https://i.imgur.com/nxgXiql.jpg)

Результат переноса:

!["Кубическая" кошка](https://i.imgur.com/UC4uwvM.jpg)


### III. Зимородок + укиё-э 

Контент-изображение:

![Зимородок](https://i.imgur.com/KOVqPLg.jpg)

Стиль-изображение:

![Укиё-э](https://i.imgur.com/ICIGAAi.jpg)

Результат переноса:

!["Укиё-э" зимородок](https://i.imgur.com/qAQKXFC.jpg)


## Подтверждение работы

[Исходные изображения (контент)](https://drive.google.com/drive/folders/1i0auQKNb_hAwqvAiNjCikSgrxchbxPZP?usp=sharing)

[Исходные изображения (стиль)](https://drive.google.com/drive/folders/1U_dTlL4cXMyMC5Fdhyhup-th9S5z_tGz?usp=sharing)

[Скриншоты работы](https://drive.google.com/drive/folders/18Z1hHPKDpA3P1KdHej70QdzbLUtWToJo?usp=sharing)

[Видео работы (результат появляется на отметке 18:40)](https://drive.google.com/file/d/1WkcVrILeZ7V0TTR4CjOX_UH-0_mLSnGH/view?usp=sharing)


## Благодарности

Хотел бы поблагодарить коллектив Deep Learning School за данный курс, отличные лекции и интересные задания. Отдельное спасибо за то, что сделали его бесплатным.Также хотел бы выразить признательность коммьюнити данного курса, у членов которого я почерпнул немалое количество необходимой информации.


## Список использованных источников

1. [Курс Deep Learning School на Stepik](https://stepik.org/course/124069/syllabus)

2. [Телеграм-канал осеннего продвинутого потока](https://t.me/dls_fall2022_advanced)

3. [Телеграм-канал финального проекта "Telegram-боты"](https://t.me/+ge3EASnRQtUyNzAy)

4. [Статья Leon A. Gatys et al.](https://arxiv.org/abs/1508.06576)

5. [Pytorch-туториал по Neural Style Transfer](https://pytorch.org/tutorials/advanced/neural_style_tutorial.html)

6. [Официальный сайт aiogram](https://aiogram.dev)


## Примечания

1. Бот может быть выключен, чтобы не расходовать имеющиеся на счете поставщика облачных услуг средства.

2. При возникновении вопросов, пожалуйста, обратитесь к [автору](https://t.me/Papayaspark) в Telegram.

3. Название боты - отсылка к Disco Elysium, так как первоначально хотел сделать что-то связанное с этой замечательной игрой.
