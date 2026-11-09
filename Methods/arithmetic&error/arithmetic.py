
import struct
import sys
import math


# 1. IEEE 754 floating-point representation
def ieee754_representation(number):
    number = float(number)

    packed = struct.pack(">d", number)
    bits = "".join(f"{byte:08b}" for byte in packed)

    sign_bit = bits[0]
    exponent_bits = bits[1:12]
    fraction_bits = bits[12:]

    exponent_value = int(exponent_bits, 2)
    fraction_value = int(fraction_bits, 2)

    if exponent_value == 0 and fraction_value == 0:
        classification = "zero"
    elif exponent_value == 0:
        classification = "subnormal"
    elif exponent_value == 2047 and fraction_value == 0:
        classification = "infinity"
    elif exponent_value == 2047:
        classification = "NaN"
    else:
        classification = "normal"

    return {
        "number": number,
        "bits": bits,
        "sign_bit": sign_bit,
        "exponent_bits": exponent_bits,
        "fraction_bits": fraction_bits,
        "classification": classification,
        "hexadecimal": packed.hex()
    }


# 2. Basic computer arithmetic
def perform_arithmetic(a, b):
    a = float(a)
    b = float(b)

    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b if b != 0 else None
    }


# 3. Floating-point precision demonstration
def floating_point_example():
    a = 0.1
    b = 0.2

    result = a + b

    return {
        "first_number": a,
        "second_number": b,
        "computer_result": result,
        "expected_result": 0.3,
        "difference": abs(result - 0.3)
    }


# 4. Machine epsilon
def get_machine_epsilon():
    return sys.float_info.epsilon


# 5. Floating-point limits
def get_float_limits():
    info = sys.float_info

    return {
        "mantissa_bits": info.mant_dig,
        "decimal_digits": info.dig,
        "minimum_positive_normal": info.min,
        "maximum_finite": info.max,
        "machine_epsilon": info.epsilon
    }


# 6. Overflow and underflow demonstration
def demonstrate_overflow_underflow():

    overflow = 1e308 * 1e308
    underflow = 1e-300 * 1e-300

    return {
        "overflow_result": overflow,
        "overflow_occurred": math.isinf(overflow),
        "underflow_result": underflow,
        "underflow_to_zero": underflow == 0.0
    }
