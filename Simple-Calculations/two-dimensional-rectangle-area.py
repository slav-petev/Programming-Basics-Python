import math;

x1 = float(input());
y1 = float(input());
x2 = float(input());
y2 = float(input());

length = abs(x1 - x2);
width = abs(y1 - y2);

area = width * length;
perimeter = 2 * (width + length);

print(area);
print(perimeter);