import re


demons = [i.strip() for i in input().split(',')]
pattern = r'(?P<h_chars>[^0-9\+\-\*\./]+)?(?P<d_chars>[+-]?\d+(\.[\d]+)*)?(?P<m_chars>[\*/]*)?'
demons_stats = {}
for demon in demons:
    demons_stats[demon] = {}
    demon_health = 0
    demon_damage = 0
    mods = ''
    for m in re.finditer(pattern, demon):
        h_chars = m.group('h_chars')
        d_chars = m.group('d_chars')
        m_chars = m.group('m_chars')
        if h_chars:
            for char in h_chars:
                demon_health += ord(char)
        if d_chars:
            demon_damage += float(d_chars)
        if m_chars:
            mods += m_chars
    demons_stats[demon] = {'health': demon_health,
                           'damage': demon_damage, 'mods': mods}

for demon, stats in sorted(demons_stats.items()):
    if 'mods' in stats:
        for char in stats['mods']:
            if char == '*':
                stats['damage'] *= 2
            elif char == '/':
                stats['damage'] /= 2
    print(f'{demon} - {stats["health"]} health, {stats["damage"]:.2f} damage')
