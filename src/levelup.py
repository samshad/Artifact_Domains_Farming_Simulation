import random
import src.substat_values as sv
import src.attr as name_map
import src.flower as flower
import src.plume as plume
import src.sands as sands
import src.goblet as goblet
import src.circlet as circlet


def get_mainstat_increment(mainstat, lvl):
    hp = [717, 920, 1123, 1326, 1530, 1733, 1936, 2139, 2342, 2545, 2749, 2952, 3155, 3358, 3561, 3764,
          3967, 4171, 4374, 4577, 4780]
    atk = [47, 60, 73, 86, 100, 113, 126, 139, 152, 166, 179, 192, 205, 219, 232, 245, 258, 272, 285, 298, 311]
    hpp = [7.0, 9.0, 11.0, 12.9, 14.9, 16.9, 18.9, 20.9, 22.8, 24.8, 26.8, 28.8, 30.8, 32.8, 34.7, 36.7, 38.7, 40.7,
           42.7, 44.6, 46.6]
    atkp = [7.0, 9.0, 11.0, 12.9, 14.9, 16.9, 18.9, 20.9, 22.8, 24.8, 26.8, 28.8, 30.8, 32.8, 34.7, 36.7, 38.7, 40.7,
            42.7, 44.6, 46.6]
    defp = [8.7, 11.2, 13.7, 16.2, 18.6, 21.1, 23.6, 26.1, 28.6, 31, 33.5, 36, 38.5, 40.9, 43.4, 45.9, 48.4, 50.8,
            53.3, 55.8, 58.3]
    physical = [8.7, 11.2, 13.7, 16.2, 16.2, 21.1, 23.6, 26.1, 28.6, 31, 33.5, 36, 38.5, 40.9, 43.4, 45.9,
                48.4, 50.8, 53.3, 55.8, 58.3]
    elemental = [7.0, 9.0, 11.0, 12.9, 14.9, 16.9, 18.9, 20.9, 22.8, 24.8, 26.8, 28.8, 30.8, 32.8, 34.7,
                 36.7, 38.7, 40.7, 42.7, 44.6, 46.6]
    em = [28, 36, 44, 52, 60, 68, 76, 84, 91, 99, 107, 115, 123, 131, 139, 147, 155, 163, 171, 179, 187]
    er = [7.8, 10.0, 12.2, 14.4, 16.6, 18.8, 21.0, 23.2, 25.4, 27.6, 29.8, 32.0, 34.2, 36.4, 38.6, 40.8, 43.0, 45.2,
          47.4, 49.6, 51.8]
    cr = [4.7, 6.0, 7.4, 8.7, 10.0, 11.4, 12.7, 14.0, 15.4, 16.7, 18.0, 19.3, 20.7, 22.0, 23.3, 24.7, 26.0,
          27.3, 28.7, 30.0, 31.1]
    cd = [9.3, 11.9, 14.6, 17.2, 19.9, 22.5, 25.2, 27.8, 30.5, 33.1, 35.8, 38.4, 41.1, 43.7, 46.3, 49.0,
          51.6, 54.3, 56.9, 59.6, 62.2]
    healing = [5.4, 6.9, 8.4, 10.0, 11.5, 13.0, 14.5, 16.1, 17.6, 19.1, 20.6, 22.2, 23.7, 25.2, 26.7, 28.3,
               29.8, 31.3, 32.8, 34.4, 35.9]

    if mainstat == "hp":
        return hp[lvl]
    if mainstat == "atk":
        return atk[lvl]
    if mainstat == "hpp":
        return hpp[lvl]
    if mainstat == "atkp":
        return atkp[lvl]
    if mainstat == "defp":
        return defp[lvl]
    if mainstat == "physical":
        return physical[lvl]
    if mainstat == "em":
        return em[lvl]
    if mainstat == "er":
        return er[lvl]
    if mainstat == "cr":
        return cr[lvl]
    if mainstat == "cd":
        return cd[lvl]
    if mainstat == "healing":
        return healing[lvl]
    return elemental[lvl]


def Levelup_onetime(artifact):
    indexes = [0, 1, 2, 3]
    index = random.choices(indexes, k=1)[0]

    v = sv.get_value(name_map.abbr_rev[artifact['substats'][index][0]])
    artifact['substats'][index][1] += v

    artifact['level'] += 4
    artifact['mainstat_value'] = get_mainstat_increment(
        name_map.abbr_rev[artifact['mainstat']], artifact['level'])

    if artifact['level'] == 20:
        artifact['canlevelup'] = False

    return artifact


def Levelup(artifact):
    if not artifact['canlevelup']:
        return artifact

    if artifact['substats_count'] == 3:
        if name_map.abbr_rev[artifact['type']] == "flower":
            cur_substats = []
            for stat in artifact['substats']:
                cur_substats.append(name_map.abbr_rev[stat[0]])

            new_substat = ''
            while True:
                new_substat = flower.get_substat()
                if new_substat not in cur_substats:
                    break

            new_substat_v = sv.get_value(new_substat)
            artifact['substats'].append([name_map.abbr[new_substat], new_substat_v])
            artifact['substats_count'] = 4

            artifact['level'] += 4
            artifact['mainstat_value'] = get_mainstat_increment(
                name_map.abbr_rev[artifact['mainstat']], artifact['level'])

        elif name_map.abbr_rev[artifact['type']] == "plume":
            cur_substats = []
            for stat in artifact['substats']:
                cur_substats.append(name_map.abbr_rev[stat[0]])

            new_substat = ''
            while True:
                new_substat = plume.get_substat()
                if new_substat not in cur_substats:
                    break

            new_substat_v = sv.get_value(new_substat)
            artifact['substats'].append([name_map.abbr[new_substat], new_substat_v])
            artifact['substats_count'] = 4

            artifact['level'] += 4
            artifact['mainstat_value'] = get_mainstat_increment(
                name_map.abbr_rev[artifact['mainstat']], artifact['level'])

        elif name_map.abbr_rev[artifact['type']] == "sands":
            cur_substats = []
            for stat in artifact['substats']:
                cur_substats.append(name_map.abbr_rev[stat[0]])

            new_substat = ''
            while True:
                new_substat = sands.get_substat(name_map.abbr_rev[artifact['mainstat']])
                if new_substat not in cur_substats:
                    break

            new_substat_v = sv.get_value(new_substat)
            artifact['substats'].append([name_map.abbr[new_substat], new_substat_v])
            artifact['substats_count'] = 4

            artifact['level'] += 4
            artifact['mainstat_value'] = get_mainstat_increment(
                name_map.abbr_rev[artifact['mainstat']], artifact['level'])

        elif name_map.abbr_rev[artifact['type']] == "goblet":
            cur_substats = []
            for stat in artifact['substats']:
                cur_substats.append(name_map.abbr_rev[stat[0]])

            new_substat = ''
            while True:
                new_substat = goblet.get_substat(name_map.abbr_rev[artifact['mainstat']])
                if new_substat not in cur_substats:
                    break

            new_substat_v = sv.get_value(new_substat)
            artifact['substats'].append([name_map.abbr[new_substat], new_substat_v])
            artifact['substats_count'] = 4

            artifact['level'] += 4
            artifact['mainstat_value'] = get_mainstat_increment(
                name_map.abbr_rev[artifact['mainstat']], artifact['level'])

        else:
            cur_substats = []
            for stat in artifact['substats']:
                cur_substats.append(name_map.abbr_rev[stat[0]])

            new_substat = ''
            while True:
                new_substat = circlet.get_substat(name_map.abbr_rev[artifact['mainstat']])
                if new_substat not in cur_substats:
                    break

            new_substat_v = sv.get_value(new_substat)
            artifact['substats'].append([name_map.abbr[new_substat], new_substat_v])
            artifact['substats_count'] = 4

            artifact['level'] += 4
            artifact['mainstat_value'] = get_mainstat_increment(
                name_map.abbr_rev[artifact['mainstat']], artifact['level'])

        if artifact['levelup'] == 0:
            return artifact

        else:
            while artifact['level'] < 20:
                artifact = Levelup_onetime(artifact)
            return artifact

    if artifact['levelup'] == 0:
        artifact = Levelup_onetime(artifact)

    else:
        while artifact['level'] < 20:
            artifact = Levelup_onetime(artifact)

    return artifact

