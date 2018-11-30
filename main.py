from PIL import Image
import numpy as np

GradientKernelX = np.zeros((5, 5), dtype=int)
GradientKernelX[2, 0] = -2
GradientKernelX[2, 1] = -1
GradientKernelX[2, 2] = 0
GradientKernelX[2, 3] = 1
GradientKernelX[2, 4] = 2

GradientKernelY = GradientKernelX.transpose()

print('hello world')

im = Image.open('C:/Depp Data/Others/Wallpaper/Lord of the Ring/new_test_1.JPG')

test = np.asarray(im.getdata())
matrix_r = np.reshape([test[i][0] for i in range(len(test))], im.size)
matrix_g = np.reshape([test[i][1] for i in range(len(test))], im.size)
matrix_b = np.reshape([test[i][2] for i in range(len(test))], im.size)

im.show()
