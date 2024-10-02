# Размеры флага
width = 40  # ширина
height = 20  # высота
circle_radius = 6  # радиус круга
circle_center = (width // 2 - 5, height // 2)  # центр круга

# Функция проверки, находится ли точка внутри круга
def in_circle(x, y, center, radius):
    return (x - center[0])**2 + (y - center[1])**2 <= radius**2

# Построение флага
flag_output = []
for y in range(height):
    row = []
    for x in range(width):
        if in_circle(x, y, circle_center, circle_radius):
            row.append("@")  # Красный круг
        else:
            row.append(" ")  # Зелёный фон
    flag_output.append("".join(row))

# Соединение строк для вывода
output_str = "\n".join(flag_output)
output_str
