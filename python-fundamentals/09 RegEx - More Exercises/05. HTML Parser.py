import re


data = input()
head_text = ''
body_text = ''

head_pattern = r'(?<=\<title\>)(?P<title>[A-Za-z ]+)(?=\</title\>)'
body_pattern = r'(?<=\<body)(?P<body>.*)(?=body\>)'
text_pattern = r'>([^<>]*)<'

m = re.search(head_pattern, data)
if m:
    head_text = m.group('title')

m = re.search(body_pattern, data)
if m:
    body_html = m.group('body')
    body_text = ''.join(re.findall(text_pattern, body_html))
    while '\n' in body_text:
        body_text = body_text.replace('\n', ' ')
        body_text = body_text.replace('\\n', ' ')


print(f'Title: {head_text}')
print(f'Content: {body_text}')
