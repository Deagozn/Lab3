import price_info

def test_total_cost_shopping():
    result = price_info.total_cost_shopping()
    expected = 46.75

    assert(result == 46.75)

def test_cost_of_fruit():
    result = 0
    input_fruit = 'apple'
    input_quantity = 4
    expected = 4.8

    result = price_info.cost_of_fruits(input_fruit,input_quantity)

    assert(result == expected)

