import numpy as np

#флаг бангладеша
width = 22  
height = 11  
circle_radius = 3  
circle_center = (width // 2 - 5, height // 2)  

def in_circle(x, y, center, radius):
    return (x - center[0])**2 + (y - center[1])**2 <= radius**2

for y in range(height):
    for x in range(width):
        if in_circle(x, y, circle_center, circle_radius):
            print("\033[41m \033[31m", end="")
        else:
            print("\033[42m \033[0m", end="")
    print()


#график функции y=2x+3

x_values = np.arange(0, 6, 1)
y_values = 2 * x_values + 3  

height = 9
width = 6

graph = [[' ' for _ in range(width)] for _ in range(height)]

for i in range(height):
    graph[i][0] = '|'
for j in range(width):
    graph[height - 1][j] = '_'

for x, y in zip(x_values, y_values):
    if y < height: 
        graph[height - 1 - y][x] = 'x'


color_reset = "\033[0m"
color_axis = "\033[34m"  
color_point = "\033[32m"  

#вывод на график
for line in graph:
    output_line = ''.join(line)
    output_line = output_line.replace('|', f'{color_axis}|{color_reset}')
    output_line = output_line.replace('-', f'{color_axis}-{color_reset}')
    output_line = output_line.replace('x', f'{color_point}x{color_reset}')
    print(output_line)


print('012345') 
