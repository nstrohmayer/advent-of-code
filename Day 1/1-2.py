import utilities

digit_mappings = [
    ("zero", 0),
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9)
]
digitStrings = [key for key, _ in digit_mappings]
digitNumbers = [str(value) for _, value in digit_mappings]
digitNumbersAndStrings = digitNumbers + digitStrings


def find_first_occurrence(main_string, substrings):
    first_index = float('inf')
    first_substring = None

    for substring in substrings:
        index = main_string.find(substring)
        if index != -1 and index < first_index:
            first_index = index
            first_substring = substring

    return first_substring


def find_last_occurrence(main_string, substrings):
    last_index = -1
    last_substring = None

    for substring in substrings:
        index = main_string.rfind(substring)
        if index != -1 and index > last_index:
            last_index = index
            last_substring = substring

    return last_substring


def map_string_to_integer(input_string):
    if input_string.isdigit():
        return int(input_string)  # If input is a digit, return its integer value directly

    for string_representation, integer_value in digit_mappings:
        if string_representation == input_string:
            return integer_value

    # Return None or handle invalid input strings as needed
    return None  # Or raise an exception for invalid input


def get_calibration_value_from_string(calibration_string):
    first_digit = None
    last_digit = None

    if calibration_string:
        first_digit_string = find_first_occurrence(calibration_string, digitNumbersAndStrings)
        first_digit = map_string_to_integer(first_digit_string)

        last_digit_string = find_last_occurrence(calibration_string, digitNumbersAndStrings)
        last_digit = map_string_to_integer(last_digit_string)

    return first_digit * 10 + last_digit


if __name__ == '__main__':
    calibrationStrings = utilities.read_file("Day 1.txt")
    sum_calibration_codes = 0

    for calibrationString in calibrationStrings:
        calibrationValue = get_calibration_value_from_string(calibrationString)
        sum_calibration_codes += calibrationValue

    print(sum_calibration_codes)
