width = 40  
height = 20  
circle_radius = 6  
circle_center = (width // 2 - 5, height // 2)  

def in_circle(x, y, center, radius):
    return (x - center[0])**2 + (y - center[1])**2 <= radius**2

flag_output = []
for y in range(height):
    row = []
    for x in range(width):
        if in_circle(x, y, circle_center, circle_radius):
            row.append("@")  
        else:
            row.append(" ")  
    flag_output.append("".join(row))

output_str = "\n".join(flag_output)
output_str

