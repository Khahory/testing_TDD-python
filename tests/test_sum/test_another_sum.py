from sum.another_sum import another_sum


def test_another_sum():
    assert another_sum(1, 2) == 3
    assert another_sum(4, 4) == 8
