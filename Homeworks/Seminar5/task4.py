'''Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.'''
import re

def encode_to_rle(my_str):
    result_str = ""
    step = 0
    while step < len(my_str):
        # обнуляем шаги
        # сохраняем первый символ
        cur_symb = my_str[step]
        # цикл, пока находится символ равный первому
        count = 1
        while (step + count) < len(my_str):
            # если найденный символ равен следующему
            if cur_symb == my_str[step + count]:
                # увеличиваем счетчик
                count += 1
            else: break
        # добавляем в строку количество и символ
        result_str += f"{count}{my_str[step]}"
        # увеличиваем счетчик на количество найденных символов
        step += count
    return result_str

def decode_from_rle(my_encoded_str):
    set_lst = re.findall(r'\d+[^\d]', my_encoded_str)
    result_str = ""
    for i in set_lst:
        result_str += i[1:] * int(i[:len(i)-1])
    return result_str

my_str = "ABCABCABCDDDFFFFFF"
my_encoded_str = encode_to_rle(my_str)
my_decoded_str = decode_from_rle(my_encoded_str)

print(f"Source string: {my_str}.")
print(f"Encoded string: {my_encoded_str}.")
print(f"Decoded string: {my_decoded_str}.")


