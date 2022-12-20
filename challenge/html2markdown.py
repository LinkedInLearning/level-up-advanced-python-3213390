import re

SPACES = re.compile(r'\s+')
ITALICS = re.compile(r'<em>(.+?)</em>')
PARAGRAPHS = re.compile(r'<p>(.+?)</p>')
URLS = re.compile(r'<a href="(.+?)">(.+?)</a>')


def html2markdown(html):
    '''Take in a single string of html text as input and return markdown'''

    # remove extraneous whitespace from html
    markdown = SPACES.sub(r' ', html)

    # next change any <em>{string}</em> to *{string}
    markdown = ITALICS.sub(r'*\1*', markdown)

    # next change any <p>{string}</p> to {string}\n\n
    markdown = PARAGRAPHS.sub(r'\1\n\n', markdown)

    # next change any <a href={URL}>TEXT</a> to [TEXT](URL)
    markdown = URLS.sub(r'[\2](\1)', markdown)

    return markdown.strip()
