import math;

radius = float(input());

perimeter = 2 * math.pi * radius;
area = math.pi * radius * radius;

areaOutput = f"Area = {area}";
perimeterOutput = f"Perimeter = {perimeter}";

print(areaOutput);
print(perimeterOutput);