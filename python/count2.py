def case_counter(text): 
    uppercase_count=0
    lowercase_count=0
    for char in text:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
    print(f"Uppercase letters: {uppercase_count}, Lowercase letters: {lowercase_count}")
    return 0

case_counter("IVE")

# Test cases
print(case_counter("Hello World!"))  # Expected: Uppercase letters: 2, Lowercase letters: 8
print(case_counter("PYTHON"))  # Expected: Uppercase letters: 6, Lowercase letters: 0
print(case_counter("python"))  # Expected: Uppercase letters: 0, Lowercase letters: 6
print(case_counter("1234!@#$"))  # Expected: Uppercase letters: 0, Lowercase letters: 0