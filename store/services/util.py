# 제로필 생성
def generate_next_number(current_number):
    number = int(current_number)
    next_number = number + 1
    next_number_str = str(next_number).zfill(len(current_number))
    return next_number_str