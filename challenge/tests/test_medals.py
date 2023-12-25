from challenge.medals import medal, medals, get_medals

def test_two_medals():
    expected = [medal(City='Los Angeles', Edition='1984', Sport='Athletics', Discipline='Athletics', Athlete='LEWIS, Carl', NOC='USA', Gender='Men', Event='100m', Event_gender='M', Medal='Gold'),
              medal(City='Seoul', Edition='1988', Sport='Athletics', Discipline='Athletics', Athlete='LEWIS, Carl', NOC='USA', Gender='Men', Event='100m', Event_gender='M', Medal='Gold')]
    actual = get_medals(Athlete='LEWIS, Carl', Event='100m')
    assert actual == expected

def test_pipe_dream():
    expected = []
    actual = get_medals(Athlete='FERNANDES, Jonathan')
    assert actual == expected

def test_one_kwarg():
    expected = 1459
    actual = len(get_medals(Edition='1984'))
    assert actual == expected