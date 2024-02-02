import pytest
import compound_interest
def test_compound_interest_calculator():
    # Correctness Tests
    assert compound_interest.compound_interest_calculator(1000, 0.05, 12, 5) == 1000 * (1 + 0.05 / 12) ** (12 * 5), "Test Case 1 Failed"
    """
    这个 assert 语句具体做的是：
    调用 compound_interest.compound_interest_calculator(1000, 0.05, 12, 5) 并获取返回值。
    计算表达式 1000 * (1 + 0.05 / 12) ** (12 * 5) 的值。
    检查这两个值是否相等。
    如果不相等，抛出 AssertionError 并显示消息 "Test Case 1 Failed"。
    """
    assert compound_interest.compound_interest_calculator(500, 0.07, 4, 10) == 500 * (1 + 0.07 / 4) ** (4 * 10), "Test Case 2 Failed"
    assert compound_interest.compound_interest_calculator(1500, 0.03, 6, 7) == 1500 * (1 + 0.03 / 6) ** (6 * 7), "Test Case 3 Failed"
    
    # Edge Case Tests
    assert compound_interest.compound_interest_calculator(0, 0.05, 12, 5) == 0, "Test Case 4 Failed"  # Principal amount is 0
    assert compound_interest.compound_interest_calculator(1000, 0, 12, 5) == 1000, "Test Case 5 Failed"  # Interest rate is 0
    assert compound_interest.compound_interest_calculator(1000, 0.05, 12, 0) == 1000, "Test Case 6 Failed"  # Investment duration is 0

    # Input Error Handling Tests
    assert compound_interest.compound_interest_calculator(-1000, 0.05, 12, 5) == "All input values should be non-negative, and 'n' should be positive.", "Test Case 7 Failed"
    assert compound_interest.compound_interest_calculator(1000, -0.05, 12, 5) == "All input values should be non-negative, and 'n' should be positive.", "Test Case 8 Failed"
    assert compound_interest.compound_interest_calculator(1000, 0.05, 0, 5) == "All input values should be non-negative, and 'n' should be positive.", "Test Case 9 Failed"
    assert compound_interest.compound_interest_calculator(1000, 0.05, 12, -5) == "All input values should be non-negative, and 'n' should be positive.", "Test Case 10 Failed"

# Run the tests
test_compound_interest_calculator()
