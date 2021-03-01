class ChatLogger:
    def __init__(self) -> None:
        self.chatlist = []

    def chat(self, m: str):
        self.chatlist.append(m)

    def delete(self, m):
        if m in self.chatlist:
            while m in self.chatlist:
                self.chatlist.remove(m)

    def edit(self, o: str, n: str):
        for i, m in enumerate(self.chatlist):
            if m == o:
                self.chatlist[i] = n

    def pin(self, m: str):
        counter = 0
        while m in self.chatlist:
            if m in self.chatlist:
                self.chatlist.remove(m)
                counter += 1
        for _ in range(counter):
            self.chatlist.append(m)

    def spam(self, l: list):
        self.chatlist.extend(l)

    def __repr__(self) -> str:
        nl = '\n'
        return nl.join(self.chatlist)


log = ChatLogger()

while True:
    data = input()
    if data == 'end':
        print(log)
        break
    command, *token = data.split()
    if command == 'Chat':
        log.chat(*token)
    elif command == 'Delete':
        log.delete(*token)
    elif command == 'Edit':
        log.edit(*token)
    elif command == 'Pin':
        log.pin(*token)
    elif command == 'Spam':
        log.spam(token)
