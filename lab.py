import numpy as np

#флаг бангладеша
WIDTH = 22  
HEIGHT = 11  
CIRCLE_RADIUS = 3  
CIRCLE_CENTER = (WIDTH // 2 - 5, HEIGHT // 2)  

def in_circle(x, y, center, radius):
    return (x - center[0])**2 + (y - center[1])**2 <= radius**2

for y in range(HEIGHT):
    for x in range(WIDTH):
        if in_circle(x, y, CIRCLE_CENTER, CIRCLE_RADIUS):
            print("\033[41m \033[31m", end="")
        else:
            print("\033[42m \033[0m", end="")
    print()

#############################################################################
#график функции y=2x+3

x_values = np.arange(0, 6, 1)
y_values = 2 * x_values + 3  

HEIGHT = 9
WIDTH = 6

graph = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

for i in range(HEIGHT):
    graph[i][0] = '|'
for j in range(WIDTH):
    graph[HEIGHT - 1][j] = '_'

for x, y in zip(x_values, y_values):
    if y < HEIGHT: 
        graph[HEIGHT - 1 - y][x] = 'x'


COLOR_RESET = "\033[0m"
COLOR_AXIS = "\033[34m"  
COLOR_POINT = "\033[32m"   

#вывод на график
for line in graph:
    output_line = ''.join(line)
    output_line = output_line.replace('|', f'{COLOR_AXIS}|{COLOR_RESET}')
    output_line = output_line.replace('-', f'{COLOR_AXIS}-{COLOR_RESET}')
    output_line = output_line.replace('x', f'{COLOR_POINT}x{COLOR_RESET}')
    print(output_line)


print('012345')
print() 
#############################################################################


#Узор на репите
def draw_pattern():
    RED = '\033[91;31m'
    RESET = '\033[0m'
    pattern = [
        "######   ",
        "#    #   ",
        "#  ###   ",
        "#  #     ",
        "#  ######",
        "  "
    ]
    
    REPEAT_VERTICAL = 2
    REPEAT_HORIZONTAL = 5
    
    for _ in range(REPEAT_VERTICAL):
        for line in pattern:
            colored_line = line.replace('#', f'{RED}#')
            print(colored_line * REPEAT_HORIZONTAL + RESET)
            
draw_pattern()


#############################################################################

#ДИАГРАММА по sequence.txt
# def load_numbers_from_file(filename):
#     with open(filename, 'r') as file:
#         numbers = [float(line.strip()) for line in file.readlines()]
#     return numbers

# def main():
#     numbers = load_numbers_from_file('sequence.txt')
    
    
#     first_half = numbers[:125]
#     second_half = numbers[125:250]

#     sum_first_half = sum(abs(num) for num in first_half)
#     sum_second_half = sum(abs(num) for num in second_half)

#     labels = ['Первые 125 чисел', 'Вторые 125 чисел']
#     sizes = [sum_first_half, sum_second_half]

#     plt.figure(figsize=(8, 6))
#     plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
#     plt.axis('equal') 
#     plt.title('Соотношение суммы по модулю первых и вторых 125 чисел')
#     plt.show()

#############################################################################

with open('sequence.txt', 'r') as file:
    numbers = list(map(float, file.read().strip().split()))

first_part = numbers[:125]
second_part = numbers[125:250]  

sum_first_part = sum(abs(num) for num in first_part)
sum_second_part = sum(abs(num) for num in second_part)

total_sum = sum_first_part + sum_second_part
percent_first = (sum_first_part / total_sum) * 100
percent_second = (sum_second_part / total_sum) * 100

def print_ascii_bar(label, percentage):
    bar_length = int(percentage // 2) 
    bar = '#' * bar_length
    print(f'{label}: [{bar:<50}] {percentage:.2f}%')

print("\nПроцентное соотношение:")
print_ascii_bar('Первые 125 чисел', percent_first)
print_ascii_bar('Вторые 125 чисел', percent_second)



if __name__ == "__main__":
    draw_pattern()
   