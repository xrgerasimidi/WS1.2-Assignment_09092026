from testbook import testbook
import numpy as np

def test_list_comprehension():
    with testbook('5_list_comprehension.ipynb', execute=True) as tb:
        new_list = tb.value('new_list')
        assert new_list == [0.5, 1.0, 1.5, 2.0, 2.5], "new_list values are not half of my_list!"