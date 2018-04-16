squareSize = int(input());

squareFullRow = "*" * squareSize;
emptySpacesCount = squareSize - 2;

print(squareFullRow);
for row in range(0, squareSize - 2):
    row = "*{0}*".format(" " * emptySpacesCount);
    print(row);
print(squareFullRow);