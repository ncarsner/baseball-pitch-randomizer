import random

grips = [
    '4-seam',
    '2-seam',
    'cutter',
    # 'sinker',
    # 'splitter',

    'curveball',
    # 'power curve',
    # 'knuckle curve',
    # 'spike curve',

    'slider',
    # 'power slider',
    # 'backup slider',
    # 'backfoot slider',

    'changeup',
]

quality = [
    'heart',
    'shadow',
    'chase',
    'waste',
]

vertical = [
    'up',
    'letters', 'belt', 'thigh', 'knee',
    'down',
]

horizontal = [
    'in', 'middle', 'away',
]

g = []
q = []
v = []
h = []

pitches = 10

for _ in range(pitches):
    random.shuffle(grips)
    random.shuffle(quality)
    random.shuffle(vertical)
    random.shuffle(horizontal)

    g.append(grips[0])
    q.append(quality[0])
    v.append(vertical[0])
    h.append(horizontal[0])

for x in range(pitches):
    print(
        g[x],
        q[x].upper(),
        v[x],
        h[x],
        sep = ', '
    )