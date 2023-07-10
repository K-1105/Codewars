# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.
#
# Valid inputs examples:
# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89
# Invalid input examples:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
# Notes:
# Leading zeros (e.g. 01.02.03.04) are considered invalid
# Inputs are guaranteed to be a single string

def is_valid_IP(strng):
    # make a list of the numbers to iterate through
    separated_strng_list = strng.split(".")

    # check there are 4 potential octects that were separated by "."
    if len(separated_strng_list) != 4:
        is_valid= False

    else:
        for octet in separated_strng_list:
            # check the string contains numbers
            if not octet.isnumeric():
                is_valid = False
                break
            # check the numbers are 8bit
            elif int(octet) not in range(2**8):
                is_valid= False
                break
            # check the numbers larger than 1 character dont start with a "0"
            elif len(octet) >1 and octet[0] == "0":
                is_valid= False
                break
            else:
                is_valid= True

    return is_valid
