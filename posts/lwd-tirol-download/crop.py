import skimage


path = "LPUI2-snow-depth.png"

pic = skimage.io.imread(path)

ratio = 1200 / 852

cropped = pic[: 426 * 3, : 600 * 3, :]

skimage.io.imsave("sd-crop.png", cropped)
