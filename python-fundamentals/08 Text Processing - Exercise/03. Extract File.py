filepath = input().split('\\')
filename, file_ext = filepath[-1].split('.')

print(f'File name: {filename}')
print(f'File extension: {file_ext}')