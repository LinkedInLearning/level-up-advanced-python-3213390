from challenge.pairwise_offset import pairwise_offset

def test_no_offset():
    actual = list(pairwise_offset('abcde'))
    expected = [('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e')]
    assert expected == actual

def test_fillvalue():
    actual = list(pairwise_offset('abcd', fillvalue='-', offset=1))
    expected = [('a', '-'), ('b', 'a'), ('c', 'b'), ('d', 'c'), ('-', 'd')]
    assert expected == actual

def test_offset():
    actual = list(pairwise_offset([(1, 2), (3, 4), (5, 6)], offset=2))
    expected = [((1, 2), '*'), ((3, 4), '*'), ((5, 6), (1, 2)), ('*', (3, 4)), ('*', (5, 6))]
    assert expected == actual

def test_more_offset_than_items():
    actual = list(pairwise_offset([(1, 2), (3, 4), (5, 6)], offset=4))
    expected = [((1, 2), '*'), ((3, 4), '*'), ((5, 6), '*'), ('*', '*'), ('*', (1, 2)), ('*', (3, 4)), ('*', (5, 6))]
    assert expected == actual


