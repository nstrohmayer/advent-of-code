import utilities


def find_first_occurrence(main_string, substrings):
    first_index = float('inf')
    first_substring = None

    for substring in substrings:
        index = main_string.find(substring)
        if index != -1 and index < first_index:
            first_index = index
            first_substring = substring

    return main_string[first_index:] if first_substring else None


def get_calibration_value_from_string(calibration_string):
    first_digit = None
    last_digit = None

    if calibration_string:
        for char in calibration_string:
            if char.isdigit():
                first_digit = int(char)
                break

        for char in reversed(calibration_string):
            if char.isdigit():
                last_digit = int(char)
                break

    return first_digit * 10 + last_digit


if __name__ == '__main__':
    calibrationStrings = utilities.read_file("Day 1.txt")
    sum_calibration_codes = 0

    for calibrationString in calibrationStrings:
        calibrationValue = get_calibration_value_from_string(calibrationString)
        sum_calibration_codes += calibrationValue

    print(sum_calibration_codes)
