def t_t_t_s(num1_str,base):
    valid_digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:base]
    ans_r=""
    ans_p=[]
    while num1_str>0:
        ans_p=[num1_str%base]+ans_p
        num1_str//=base
    for i in ans_p:
        ans_r=valid_digits[i]
    return ans_r
    
def is_valid_number(num_str, base):
    if base < 2 or base > 36:
        return False
    
    valid_digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:base]
    
    for char in num_str.upper():
        if char not in valid_digits:
            return False
    return True

def char_to_digit(char):
    if '0' <= char <= '9':
        return ord(char) - ord('0')
    else:
        return ord(char.upper()) - ord('A') + 10

def digit_to_char(digit):
    if 0 <= digit <= 9:
        return chr(ord('0') + digit)
    else:
        return chr(ord('A') + digit - 10)

def prepare_numbers(num1_str, num2_str, base):
    num1_digits = [char_to_digit(c) for c in num1_str.upper()]
    num2_digits = [char_to_digit(c) for c in num2_str.upper()]
    return num1_digits[::-1], num2_digits[::-1]

def add(num1_str, num2_str, base):
    num1, num2 = prepare_numbers(num1_str, num2_str, base)
    max_len = max(len(num1), len(num2))
    num1 += [0] * (max_len - len(num1))
    num2 += [0] * (max_len - len(num2))
    
    result = []
    carry = 0
    
    for i in range(max_len):
        digit_sum = num1[i] + num2[i] + carry
        carry = digit_sum // base
        result_digit = digit_sum % base
        result.append(result_digit)
    
    if carry > 0:
        result.append(carry)
    
    result_str = ''.join(digit_to_char(d) for d in result[::-1])
    return result_str

def subtract(num1_str, num2_str, base):
    if not is_greater_or_equal(num1_str, num2_str, base):
        raise ValueError("Результат вычитания отрицательный")
    
    num1, num2 = prepare_numbers(num1_str, num2_str, base)
    
    max_len = max(len(num1), len(num2))
    num1 += [0] * (max_len - len(num1))
    num2 += [0] * (max_len - len(num2))
    
    result = []
    borrow = 0
    
    for i in range(max_len):
        digit_diff = num1[i] - num2[i] - borrow
        if digit_diff < 0:
            digit_diff += base
            borrow = 1
        else:
            borrow = 0
        result.append(digit_diff)
    
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    result_str = ''.join(digit_to_char(d) for d in result[::-1])
    return result_str

def multiply(num1_str, num2_str, base):
    multiplication_table = create_multiplication_table(base)
    
    num1, num2 = prepare_numbers(num1_str, num2_str, base)
    result = [0]
    
    for i, digit2 in enumerate(num2):
        intermediate = []
        carry = 0
        
        for digit1 in num1:
            product = multiplication_table[digit1][digit2] + carry
            carry = product // base
            intermediate.append(product % base)
        
        if carry > 0:
            intermediate.append(carry)
        
        intermediate = [0] * i + intermediate
        
        result = add_lists(result, intermediate, base)
    result_str = ''.join(digit_to_char(d) for d in result[::-1])
    return result_str

def create_multiplication_table(base):
    table = []
    for i in range(base):
        row = []
        for j in range(base):
            row.append(i * j)
        table.append(row)
    return table

def add_lists(num1, num2, base):
    max_len = max(len(num1), len(num2))
    num1 += [0] * (max_len - len(num1))
    num2 += [0] * (max_len - len(num2))
    
    result = []
    carry = 0
    
    for i in range(max_len):
        digit_sum = num1[i] + num2[i] + carry
        carry = digit_sum // base
        result_digit = digit_sum % base
        result.append(result_digit)
    
    if carry > 0:
        result.append(carry)
    
    return result

def is_greater_or_equal(num1_str, num2_str, base):
    if len(num1_str) > len(num2_str):
        return True
    elif len(num1_str) < len(num2_str):
        return False
    
    for i in range(len(num1_str)):
        digit1 = char_to_digit(num1_str[i])
        digit2 = char_to_digit(num2_str[i])
        if digit1 > digit2:
            return True
        elif digit1 < digit2:
            return False
    
    return True


def main():
    try:
        num1_str = input("Введите первое число: ").strip().upper()
        operation = input("Введите операцию (+, -, *): ").strip()
        num2_str = input("Введите второе число: ").strip().upper()
        base = int(input("Введите систему счисления: "))
        num1_str=t_t_t_s(num1_str,base)
        num2_str=t_t_t_s(num2_str,base)
        if base < 2 or base > 36:
            raise ValueError("Система счисления должна быть от 2 до 36")
        
        if not is_valid_number(num1_str, base):
            raise ValueError("Первое число не соответствует системе счисления")
        
        if not is_valid_number(num2_str, base):
            raise ValueError("Второе число не соответствует системе счисления")
        
        if operation not in ['+', '-', '*']:
            raise ValueError("Недопустимая операция")
        
        if operation == '+':
            result = add(num1_str, num2_str, base)
        elif operation == '-':
            result = subtract(num1_str, num2_str, base)
        elif operation == '*':
            result = multiply(num1_str, num2_str, base)
        
        print(f"Результат: {result}")
        
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()
