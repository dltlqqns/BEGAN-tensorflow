import os
import scipy.misc

#data_dir = 'D:/v-yusuh/dataset/web1000/horse'
data_dir = '/home/yumin/dataset/web1000/horse'
# Read the image
for fn in sorted(os.listdir(data_dir)):
    print(fn)
    image = scipy.misc.imread(os.path.join(data_dir, fn))
    image = image.astype('uint8')
    print(image.shape)
    image_resize = scipy.misc.imresize(image, [64, 64], 'bicubic')
    scipy.misc.imsave('64/' + fn, image_resize)

#    for (x, y, w, h) in faces:
#        print x, y, w, h
#       cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)




