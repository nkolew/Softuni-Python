import os


desktop = os.path.expanduser("~/Desktop")
filename = f'{desktop}/report.txt'


_, _, files = next(os.walk(input()))

files_grouped_by_ext = {}
for file in files:
    ext = file.split('.')[-1]

    if ext not in files_grouped_by_ext:
        files_grouped_by_ext[ext] = []
    files_grouped_by_ext[ext].append(file)

    with open(filename, 'w') as fh:
        output = []
        for ext in sorted(files_grouped_by_ext):
            files = sorted(files_grouped_by_ext[ext])
            output.append(f'.{ext}')
            for file in files:
                output.append(f'---{file}')
        output = '\n'.join(output)
        fh.write(output)
