#!/usr/bin/env python3

# This file creates Pioneers game file
# from environment variables and starts
# a game server with these values

import click
import os


@click.command()
@click.option("--base-file", default="/usr/share/games/pioneers/default.game")
@click.option("--title", default="Pioneers Game")
@click.option("--random-terrain", type=bool)
@click.option("--strict-trade", type=bool)
@click.option("--domestic-trade", type=bool)
@click.option("--num-players", type=int)
@click.option("--sevens-rule", type=int)
@click.option("--victory-points", type=int)
@click.option("--desc", default="A Pioneers game")
@click.option("--port", default=5556)
def main(
    base_file,
    title,
    random_terrain,
    strict_trade,
    domestic_trade,
    num_players,
    sevens_rule,
    victory_points,
    desc,
    port,
):
    base_lines = open(base_file).read().split("\n")
    output_lines = []

    # Set new parameters
    for line in base_lines:
        new = ""
        if "title" in line:
            new = update_line(line, title, "title")
        elif "random-terrain" in line:
            new = update_line(line, random_terrain, "random-terrain")
        elif "strict-trade" in line:
            new = update_line(line, strict_trade, "strict-trade")
        elif "domestic-trade" in line:
            new = update_line(line, domestic_trade, "domestic-trade")
        elif "num-players" in line:
            new = update_line(line, num_players, "num-players")
        elif "sevens-rule" in line:
            new = update_line(line, sevens_rule, "sevens-rule")
        elif "victory-points" in line:
            new = update_line(line, victory_points, "victory-points")
        elif "desc" in line:
            new = update_line(line, desc, "desc")
        else:
            # keep line without modification
            new = line
        output_lines.append(new + "\n")

    # Convert output lines to file
    output_file = title.lower().replace(" ", "_") + ".game"
    f = open(output_file, "w")
    f.writelines(output_lines)
    f.close()

    # Launch server
    os.system(
        "pioneers-server-console"
        + " -p "
        + str(port)
        + " --file "
        + output_file
        + " --auto-quit --empty-timeout 3600 --debug"
    )


def update_line(original, new, param_name):
    if new is None:
        return original
    if type(new) is bool:
        if new:
            return param_name
        else:
            return "#" + param_name
    else:
        return param_name + " " + str(new)


if __name__ == "__main__":
    main()