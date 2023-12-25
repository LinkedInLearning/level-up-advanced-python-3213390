from challenge.html2markdown import html2markdown

def test_italics():
    html = 'This is in <em>italics</em>. So is <em>this</em>'
    expected = 'This is in *italics*. So is *this*'
    actual = html2markdown(html)
    assert actual == expected

def test_spaces():
    html = 'This sentence has a    lot of    \ninteresting white spaces.'
    expected = 'This sentence has a lot of interesting white spaces.'
    actual = html2markdown(html)
    assert actual == expected

def test_single_paragraph():
    html = '<p>This is a paragraph.</p>'
    expected = 'This is a paragraph.'
    actual = html2markdown(html)
    assert actual == expected

def test_multiple_paragraphs():
    html = '<p>This is a paragraph.</p><p>This is another\nparagraph.</p>'
    expected = 'This is a paragraph.\n\nThis is another paragraph.'
    actual = html2markdown(html)
    assert actual == expected

def test_urls():
    html = (
            'This is the <a href="https://pypi.org/project/html2markdown/">link</a> to the html2markdown package and '
            'here is <a href="https://github.com/dlon/html2markdown">another link</a> to the project homepage'
    )
    expected = (
            'This is the [link](https://pypi.org/project/html2markdown/) to the html2markdown package and '
            'here is [another link](https://github.com/dlon/html2markdown) to the project homepage'
    )
    actual = html2markdown(html)
    assert actual == expected