gifts_list = input().split()
command = input()


while command != 'No Money':

    if 'OutOfStock' in command:

        current_command, current_gift = command.split()

        if current_gift in gifts_list:

            for idx, gift in enumerate(gifts_list):

                if gift == current_gift:
                    gifts_list[idx] = 'None'

    elif 'Required' in command:

        current_command, current_gift, index = command.split()
        idx = int(index)

        if 0 <= idx < len(gifts_list):
            gifts_list[idx] = current_gift

    elif 'JustInCase' in command:

        current_command, current_gift = command.split()
        gifts_list[-1] = current_gift

    command = input()


for gift in gifts_list:

    if gift != 'None':
        print(gift, end=' ')