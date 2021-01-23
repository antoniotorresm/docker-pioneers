FROM fedora:33
MAINTAINER Antonio Torres <atorresm@protonmail.com>

RUN dnf install pioneers pip -y

ADD ./create_game_file_and_start_server.py create_game_file_and_start_server.py
ADD ./requirements.txt requirements.txt
RUN chmod +x create_game_file_and_start_server.py
RUN pip3 install -r requirements.txt

EXPOSE 5556

ENV BASE_FILE=/usr/share/games/pioneers/default.game \
    TITLE="Pioneers Game" \
    RANDOM_TERRAIN=true \
    STRICT_TRADE=true \
    DOMESTIC_TRADE=true \
    NUM_PLAYERS=4 \
    SEVENS_RULE=0 \
    VICTORY_POINTS=10

CMD ./create_game_file_and_start_server.py \
    --base-file $BASE_FILE \
    --title "$TITLE" \
    --random-terrain $RANDOM_TERRAIN \
    --strict-trade $STRICT_TRADE \
    --domestic-trade $DOMESTIC_TRADE \
    --num-players $NUM_PLAYERS \
    --sevens-rule $SEVENS_RULE \
    --victory-points $VICTORY_POINTS