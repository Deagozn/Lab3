import Lab2.bmi as bmi

def test_bmi_normal_weight():
    result = 0
    input_weight = 60
    input_height = 1.7
    test_result = 0

    result = bmi.calculate_bmi(input_height, input_weight)

    assert (result == test_result)

def test_bmi_over_weight():
    result = 0
    input_weight = 80
    input_height = 1.7
    test_result = 1

    result = bmi.calculate_bmi(input_height, input_weight)

    assert (result == test_result)

def test_bmi_under_weight():
    result = 0
    input_weight = 50
    input_height = 1.7
    test_result = -1

    result = bmi.calculate_bmi(input_height, input_weight)

    assert (result == test_result)

