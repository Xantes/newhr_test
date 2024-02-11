# Тестовое задание для newhr.

## 1. Запрос к postgresql
> Даны две таблицы в Postgresql, таблица статей и таблица комментариев к этим статьям. Необходимо написать запрос, который выведет все статьи без комментариев (у которых нет комментариев)

С использование left join:
```plpgsql
select a.id, a.title
from article a
left join comment c 
on a.id = c.article_id
where c.article_id is null;
```

С использование подзапроса:
```plpgsql
select a.id, a.title
from article a
where not exists (
    select c.article_id
    from comment c
    where c.article_id = a.id
)
```
С использование подзапроса:
```plpgsql
select a.id, a.title
from article a
where a.id not in (
    select distinct c.article_id
    from comment c
)
```

## 2. Скрипт на bash/lua/python
> Написать скрипт на Bash или Lua*/Python. Который должен распознать внешний IP адрес, далее необходимо получить информацию о регионе данного IP.

Пример кода в 1/app.py

## 3. Замена chmod
> На сервере с linux случайно удалили права на исполнение у программы - chmod. Как вернуть данной программе, права на исполнение? Перечислить несколько вариантов.

1. Используя acl можно установить право на выполнение программы для пользователя/группы
2. Выполнить из загрузчика /lib/ld-linux.so /bin/chmod +x /bin/chmod


## 4. Пропавший маршрут
>  Произошел сбой, на узле сети пропал интернет. Узел получает настройки через DHCP (он же роутер 192.168.33.1). Отключение интерфейса не помогает. Как починить доступ в Интернет (не прибегая к перезагрузке)?

Можно использовать ip route add default via 192.168.33.1, но сначала нужно присвоить интерфейсу enp6s0 статический адрес ip address add 192.168.33.78/255.255.255.0 dev enp6s0 

## 5. Voip в моих руках
> У тебя есть на руках Voip-шлюз, одного из клиентов. Шлюз рабочий, нельзя сбрасывать настройки. У тебя есть логин и пароль от шлюза. НО в сетевых интерфейсах прописан статический IP адрес внутренней сети клиента (клиент его не знает). Как определить IP адрес?

1. Можно подключить напрямую к сетевому интерфейсу, запустить wireshark/tcpdump и проанализировать присылаемые пакеты. В arp или иных запросах можно будет получить адрес отправителя
2. Зайти веб-интерфейс/консоль шлюза и используя консольные команды, попытаться получить информацию об интерфейсе

## 6. Парсим в bash
>Есть файл с некоторым данными, в формате:

>9000000000,1
>9000000001,3
>9000000000,5
>9000000000,2
>9000000000,3
>9650000000,1

>Как посчитать кол-во уникальных значений по 1 столбику, используя инструменты bash?

Скрипт можно посмотреть в 2\parser.sh <файл с некоторыми данными>

## 7. Строки в числа
> Есть скрипт который сравнивает 2 числа и результатом его работы является вывод, какое число больше (или равны). Но скрипт работает не корректно, найти ошибку.

1. Можно заменить [[]] на (()), для того, чтобы сравнение происходило в контексте чисел. В таком случае операции сравнения должны выглядеть как if (( a > b ))
2. Можно использовать оператоы -gt или -lt вместо > и <. В таком случае операции сравнения должны выглядеть как if [[ $a -gt $b ]]

## 8. Что у нас в top
> На одном из хостов (вирт. машина на KVM), обнаружена аномальная нагрузка. Мы использовали команду top. Какую проблему мы здесь наблюдаем?

Высокие показатель steal time - виртуальная машина недополучает ресурсы процессора от хоста

## 9. Мнимое свободное место
> На одном из хостов возникла проблема с созданием файла, при попытки создать файл мы получаем ошибку. Но при проверки свободного места, мы видим следующую картину (картинка). Почему не создается файл?

Можно посмотреть с помощью df -ih количество свободных inodes на диске. Скорее всего проблема в их недостаточном количестве

## 10. Что с моим докерфайлом, чувак?
> Есть Dockerfile. Какие ошибки, на ваш взгляд, допущены?

1. From ubuntu:latest
    - Желательно использовать конкретную версию образа на основании которого будет стартовать контейнер
    - По возможности стараться использовать облегченные версии образова
    - Возможно, стоит использовать специализированный образ. Например, python или nginx
2. Add ./code /opt/coolproject/code и workdir /opt/coolproject
    - Возможно, стоит поменять директивы местами и тогда директива add сократится до copy . . , а entrypoint станет сильно короче.
3. Все директивы RUN желательно объединить в одну. Также, желательно исключить из RUN установку уже существующих пакетов. В целом, можно воспользоваться multistage сборкой
4. Желательно заменить CMD на Entrypoint ["bash", "start.sh"]

## 11. По хребтине от сисадмина
> Вы находитесь в одноранговой сети (один L2 домен), вам необходимо получить трафик соседнего компьютера. Вы знаете его IP адрес, как с помощью вашего компьютера это сделать (доступа к коммутатору нет, только ваш компьютер)?

Можно используя протокол ARP узнать MAC-адрес соседнего компьютера. После этого подменить MAC собственной сетевой карты

## 12. Detroit: becoming human как пошлое предсказание будущего
1. Контейнеры + менеджеры конфигурации + iaas. Теперь приложение и инфраструктуру для него можно развернуть за относильно короткое время. 
2. Микросервисная архитектура. Теперь можно спокойно обновлять и дорабатывать части приложения. Разработка стала гораздо гибче
3. Redis и git. С однной стороны очень быстрая база данных, с другой стороны очень удобный инструмент для работы в команде и версионирования
