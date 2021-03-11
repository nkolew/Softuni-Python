class Ticket:
    def __init__(self, id: str) -> None:
        self.id = id
        self.prize = 'Valid'
        self.symbol = ''
        self.count = 0

    def validate(self):
        VALID_TICKET_LEN = 20
        JACKPOT_COUNT = 10
        SYMBOLS = ['@', '#', '$', '^']

        def get_count(side: str, symbol: str) -> int:
            i = 0
            count = 0
            while i < len(side):
                current = 0
                if side[i] == symbol:
                    current += 1
                    while i + 1 < len(side):
                        i += 1
                        if side[i] == symbol:
                            current += 1
                            if i == len(side)-1:
                                count = max(current, count)
                        else:
                            count = max(current, count)
                            break
                i += 1
            return count

        def check_prize():
            l = self.id[:10]
            r = self.id[10:]
            for symbol in SYMBOLS:
                if l.count(symbol) == r.count(symbol) == JACKPOT_COUNT:
                    self.prize = 'Jackpot'
                    self.symbol = symbol
                    self.count = JACKPOT_COUNT
                elif l.count(symbol) >= 6 and r.count(symbol) >= 6:
                    l_count = get_count(l, symbol)
                    r_count = get_count(r, symbol)
                    winning = min(l_count, r_count) >= 6
                    if winning:
                        self.count = min(l_count, r_count)
                        self.prize = 'Winner'
                        self.symbol = symbol

        if len(self.id) != VALID_TICKET_LEN:
            self.prize = 'Invalid'
        else:
            check_prize()

    def __repr__(self) -> str:
        self.validate()
        if self.prize != 'Valid':
            if self.prize == 'Invalid':
                return f'invalid ticket'
            elif self.prize == 'Jackpot':
                return f'ticket "{self.id}" - {self.count}{self.symbol} Jackpot!'
            elif self.prize == 'Winner':
                return f'ticket "{self.id}" - {self.count}{self.symbol}'
        return f'ticket "{self.id}" - no match'


data = input().split(', ')
for t in data:
    ticket_id = t.strip()
    print(Ticket(ticket_id))
