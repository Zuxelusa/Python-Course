import generate_file
import converter
import keyboard

file = "file.txt"
while True:
    length = input("Введите количество строк в файле: ")
    if length.isdigit(): break

print("Генерируем файл...")
generate_file.generate_file(file, int(length)) #генерируем файл
print("Файл готов!\n Сконвертировать файл?\nс - конвертировать в CSV\nh - конвертировать в HTML\nq - Выйти")

while True:
    try:
        if keyboard.is_pressed("c"):
            print(f"\nКонвертируем в CSV...")
            converter.convert_to_csv(file)
            print("Готово!")
            break
        if keyboard.is_pressed("h"):
            print(f"\nКонвертируем в HTML...")
            converter.convert_to_html(file)
            print("Готово!")
            break
        if keyboard.is_pressed("q"):
            print(f"\nДо свидания!")
            break
    except:
        break




