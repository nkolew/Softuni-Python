def gen_html(article: dict) -> str:
    """Generate HTML tags for the dict object, supplied

    Args:
        article (dict): Article dic, 'title: str', content: str', 'comments: list'

    Returns:
        str: HTML code
    """
    article_html = ''
    nl = '\n'
    head_html = f"<h1>{nl}    {article['title']}{nl}</h1>{nl}"
    content_html = f"<article>{nl}    {article['content']}{nl}</article>{nl}"
    article_html += head_html + content_html
    for comment in article['comments']:
        comment_html = f"<div>{nl}    {comment}{nl}</div>{nl}"
        article_html += comment_html
    return article_html


article = {}
article_title = input()
article_content = input()
article['title'] = article_title
article['content'] = article_content
article['comments'] = []

while True:
    data = input()
    if data == 'end of comments':
        break
    article['comments'].append(data)

print(gen_html(article))
