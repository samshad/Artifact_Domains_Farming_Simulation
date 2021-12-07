import random
import src.substat_values as sv
import src.attr as name_map


def get_mainstat():
    stats = ["hpp", "atkp", "defp", "cr", "cd", "healing", "em"]
    w = [22.0, 22.0, 22.0, 10.0, 10.0, 10.0, 4.0]
    return random.choices(stats, weights=w, k=1)[0]


def get_substat(mainstat):
    if mainstat == "hpp":
        substats = ["hp", "atk", "def", "atkp", "defp", "er", "em", "cr", "cd"]
        w = [15.0, 15.0, 10.0, 10.0, 10.0, 10.0, 10.0, 7.5, 7.5]
        return random.choices(substats, weights=w, k=1)[0]
    if mainstat == "atkp":
        substats = ["hp", "atk", "def", "hpp", "defp", "er", "em", "cr", "cd"]
        w = [15.0, 15.0, 10.0, 10.0, 10.0, 10.0, 10.0, 7.5, 7.5]
        return random.choices(substats, weights=w, k=1)[0]
    if mainstat == "defp":
        substats = ["hp", "atk", "def", "hpp", "atkp", "er", "em", "cr", "cd"]
        w = [15.0, 15.0, 10.0, 10.0, 10.0, 10.0, 10.0, 7.5, 7.5]
        return random.choices(substats, weights=w, k=1)[0]
    if mainstat == "cr":
        substats = ["hp", "atk", "def", "hpp", "atkp", "defp", "er", "em", "cd"]
        w = [14.63, 14.63, 14.63, 9.76, 9.76, 9.76, 9.76, 9.76, 7.32]
        return random.choices(substats, weights=w, k=1)[0]
    if mainstat == "cd":
        substats = ["hp", "atk", "def", "hpp", "atkp", "defp", "er", "em", "cr"]
        w = [14.63, 14.63, 14.63, 9.76, 9.76, 9.76, 9.76, 9.76, 7.32]
        return random.choices(substats, weights=w, k=1)[0]
    if mainstat == "healing":
        substats = ["hp", "atk", "def", "hpp", "atkp", "defp", "er", "em", "cr", "cd"]
        w = [13.64, 13.64, 13.64, 9.09, 9.09, 9.09, 9.09, 9.09, 6.82, 6.82]
        return random.choices(substats, weights=w, k=1)[0]
    if mainstat == "em":
        substats = ["hp", "atk", "def", "hpp", "atkp", "defp", "er", "cr", "cd"]
        w = [15.0, 15.0, 10.0, 10.0, 10.0, 10.0, 10.0, 7.5, 7.5]
        return random.choices(substats, weights=w, k=1)[0]


def get_circlet():
    mainstat = get_mainstat()
    mainstat_value = 0
    if mainstat == "hpp":
        mainstat_value = 7.0
    elif mainstat == "atkp":
        mainstat_value = 7.0
    elif mainstat == "defp":
        mainstat_value = 8.7
    elif mainstat == "em":
        mainstat_value = 28
    elif mainstat == "cr":
        mainstat_value = 4.7
    elif mainstat == "cd":
        mainstat_value = 9.3
    elif mainstat == "healing":
        mainstat_value = 5.4

    substats_count = random.choices([3, 4], [0.8, 0.2], k=1)[0]

    substats = []
    cnt = 0
    already_got = []
    while cnt < substats_count:
        curr_substat = get_substat(mainstat)
        if curr_substat not in already_got:
            val = sv.get_value(curr_substat)
            substats.append((name_map.abbr[curr_substat], val))
            already_got.append(curr_substat)
            cnt += 1
    return {
        "type": name_map.abbr["circlet"],
        "mainstat": name_map.abbr[mainstat],
        "mainstat_value": mainstat_value,
        "substats": substats,
        "substats_count": substats_count,
        "level": 0
    }
