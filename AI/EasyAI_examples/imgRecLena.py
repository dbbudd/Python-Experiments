from scipy.misc import imread

img = imread("3x3.jpg")
#print(img[0,0,:])

print(img[0][0])
print(img[0][1])
print(img[0][2])
print("")
print(img[1][0])
print(img[1][1])
print(img[1][2])
print("")
print(img[2][0])
print(img[2][1])
print(img[2][2])

print("PRINT ALL")
