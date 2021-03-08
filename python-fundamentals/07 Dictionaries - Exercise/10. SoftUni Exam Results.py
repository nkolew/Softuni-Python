exam_stats = {}
submissions_count = {}

while True:
    data = input()
    if data == 'exam finished':
        break
    tokens = data.split('-')
    if len(tokens) == 3:
        username, language, points = tokens
        points = int(points)
        if username not in exam_stats:
            exam_stats[username] = points
        if exam_stats[username] < points:
            exam_stats[username] = points
        if language not in submissions_count:
            submissions_count[language] = 1
        else:
            submissions_count[language] += 1
    else:
        username = tokens[0]
        exam_stats.pop(username)


print('Results:')
for username, points in sorted(exam_stats.items(), key=lambda x: (-x[1], x[0])):
    print(f'{username} | {points}')
print('Submissions:')
for language, count in sorted(submissions_count.items()):
    print(f'{language} - {count}')
