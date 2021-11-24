from PIL import Image, ImageDraw

coord = []

with open('DS4.txt') as file:
    l = file.readlines()

for line in l:
    formatted_line = line[:-1].split(' ')
    single_coordinate = (int(formatted_line[0]), int(formatted_line[1]))
    coord.append(single_coordinate)

# Создание картинки 
out = Image.new("RGB", (540, 960), (255, 255, 255))
draw = ImageDraw.Draw(out)
# Заполнение  канвас  координатами
draw.point(coord, fill='green')
# Вывод картинки
out.show()
# сохранение картинки 
out.save("result_image.jpg")
