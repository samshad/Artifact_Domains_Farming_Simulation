import random


def get_value(stat):
    hp = [209.13, 239.00, 268.88, 298.75]
    atk = [13.62, 15.56, 17.51, 19.45]
    def_ = [16.20, 18.52, 20.83, 23.15]
    hpp = [4.08, 4.66, 5.25, 5.83]
    atkp = [4.08, 4.66, 5.25, 5.83]
    defp = [5.10, 5.83, 6.56, 7.29]
    em = [16.32, 18.65, 20.98, 23.31]
    er = [4.53, 5.18, 5.83, 6.48]
    cr = [2.72, 3.11, 3.50, 3.89]
    cd = [5.44, 6.22, 6.99, 7.77]

    if stat == 'hp':
        return random.choices(hp, k=1)[0]
    if stat == 'atk':
        return random.choices(atk, k=1)[0]
    if stat == 'def':
        return random.choices(def_, k=1)[0]
    if stat == 'hpp':
        return random.choices(hpp, k=1)[0]
    if stat == 'atkp':
        return random.choices(atkp, k=1)[0]
    if stat == 'defp':
        return random.choices(defp, k=1)[0]
    if stat == 'em':
        return random.choices(em, k=1)[0]
    if stat == 'er':
        return random.choices(er, k=1)[0]
    if stat == 'cr':
        return random.choices(cr, k=1)[0]
    if stat == 'cd':
        return random.choices(cd, k=1)[0]
