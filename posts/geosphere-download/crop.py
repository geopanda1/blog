import skimage


path = "temp.png"

pic = skimage.io.imread(path)

ratio = 1200 / 852

cropped = pic[:426, :600, :]

skimage.io.imsave("temp_crop.png", cropped)
