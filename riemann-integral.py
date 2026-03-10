# b - a
# f (x) dx
#
#
#

print("Assign a value to 'n': ")
while True:
    n = int(input())
    if n <= 0:
        print("\nInsert a value greater than 0")
        continue
    else:
        break

def riemann_integral(a, b):
    