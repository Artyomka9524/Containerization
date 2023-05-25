# Задача
Необходимо создать Dockerfile, основанный на любом образе (вы в праве выбрать самостоятельно).
В него необходимо поместить приложение, написанное на любом известном вам языке программирования (Python, Java, C, С#, C++).
При запуске контейнера должно запускаться самостоятельно написанное приложение.
# Создаем скрипт в Python
# Прописываем в Dockerfile
FROM ubuntu:latest
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install numpy pandas

# Команды в терминале
1) Перейти в папку со скриптом, выполнив команду cd <foldername>.
2) Выполнить команду:
docker build -t imagename .
3) После построения образа запускаем его командой:
docker run -v /home/ <username>/ <foldername>/:/dir imagename python3 dir<em>/</em>hw.py
