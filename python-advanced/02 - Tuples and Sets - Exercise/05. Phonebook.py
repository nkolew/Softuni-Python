from typing import Dict, List


def get_items_until_stop(stop: str) -> List[str]:
    items = []
    while True:
        item = input()
        if item == stop:
            return items
        items.append(item)


def parse_data(l: List[str]) -> Dict[str, str]:
    d = {}
    for s in l:
        k, v = s.split('-')
        d[k] = v
    return d


def search_contacts(l: List[str], d: Dict[str, str]) -> List[str]:
    return [get_contact_info(name, d) for name in l]


def get_contact_info(name: str, d: Dict[str, str]) -> str:
    if name in d:
        return f'{name} -> {d[name]}'
    return f'Contact {name} does not exist.'


def fmt_output(l: List[str]) -> str:
    nl = '\n'
    return nl.join(l)


def main() -> None:
    data = get_items_until_stop('search')
    phones = parse_data(data)
    searched_names = get_items_until_stop('stop')
    print(fmt_output(search_contacts(searched_names, phones)))


main()
