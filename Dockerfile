# FROM balenalib/asus-tinker-board-alpine-python:3.9.5-build as build
# WORKDIR /
# ENV CFLAGS="${CFLAGS} -fcommon -Wno-deprecated-declarations"
#     # -fcommon: https://www.raspberrypi.org/forums/viewtopic.php?t=244375
# RUN install_packages python3-dev \
#     && pip3 install hg-git \
#     && hg clone http://hg.code.sf.net/p/raspberry-gpio-python/code ./RPi.GPIO \
#     && cd ./RPi.GPIO \
#     && python3 setup.py build
# CMD [ "python3" ]

FROM balenalib/asus-tinker-board-alpine-python:3.10-edge-run-20211014 as dev
LABEL version="1.0.0-dev"
WORKDIR /app
ADD . /app
# RUN install_packages libgpiod py3-libgpiod \
RUN pip3 install --upgrade setuptools pip \
    && pip3 install -r requirements.dev.txt \
    && pip3 cache purge \
    && chmod +x app.py
CMD [ "python3" ]

# FROM balenalib/asus-tinker-board-alpine-python:3.9-run-20210705
# LABEL version="1.0.0"
# LABEL maintainer="15333619+hsghost@users.noreply.github.com"
# WORKDIR /app
# ADD . /app
# COPY --from=build /RPi.GPIO ./RPi.GPIO
# RUN pip3 install --upgrade setuptools pip \
#     && pip3 install -r requirements.txt \
    # && cd ./RPi.GPIO && python3 ./setup.py install \
    # && cd .. && rm -rf ./RPi.GPIO \
#     && pip3 cache purge \
#     && rm /app/requirements*.txt
# CMD [ "python3", "./app.py" ]
