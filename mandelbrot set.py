from PIL import Image
import math, time
start = time.time()
size = int(input("Size: "))
image = Image.new("L", (size, size), (255))
for x in range(size):
    for y in range(size):
        z = 0
        c = (x - size/2 + (size/2 - y) * 1j)/(size/4)
        for n in range(255):
            if math.sqrt(z.real**2+z.imag**2) > 2:
                image.putpixel((x, y), (255 - n))
                break
            z = z**2+c
        else:
            image.putpixel((x, y), (0))
    if x%100 == 0:print("\r", x ,"/", size,end="")
image.save("Mandelbrot Set.png")
print(time.time()-start)