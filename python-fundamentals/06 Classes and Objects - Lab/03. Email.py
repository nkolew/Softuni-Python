class Email:
    def __init__(self, sender, receiver, content) -> None:
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: ' \
            f'{self.content}. Sent: {self.is_sent}'


class EmailManager:
    def __init__(self) -> None:
        self.emails = []

    def add(self, email):
        self.emails.append(email)

    def send(self, idx):
        self.emails[idx].send()

    def print(self):
        for email in self.emails:
            print(email.get_info())


em = EmailManager()

while True:
    email = input()
    if email == 'Stop':
        break

    sender, receiver, content = email.split()

    em.add(
        Email(sender, receiver, content)
    )

emails_to_send = list(map(int, input().split(', ')))

for idx in emails_to_send:
    em.send(idx)

em.print()
