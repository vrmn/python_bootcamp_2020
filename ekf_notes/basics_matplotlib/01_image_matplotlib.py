import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Cameras intrinsic parameters [K] (f~420px, w~710px, h~500px)
K = np.array(
    [[420.506712, 0.,          355.208298],
     [0.,         420.610940,  250.336787],
     [0.,         0.,          1.]]
)

# (n = 12) reference 3D points, in the world coordinate, in centimeters
world_corners = 0.01* np.array(
    [[19.4, 9.0,   19.4, 9.0,     19.4,   9.0,     19.4,   9.0,   0.0,   0.0,   0.0,   0.0], #Y
     [0.,   0.,   0.,   0., 10.95, 10.95, 24.45, 24.45, 10.95, 24.45, 10.95, 24.45], #X
     [18.6,   18.6, 5.1, 5.1,   0.0,   0.0,   0.0,   0.0,   12.0,   12.0,    1.6,    1.6]] #Z
)

detected_corners = np.array(
    [[186.5, 264.5, 218.5, 285.5, 292.5, 356.5, 406.5, 461.5, 388.5, 495.5, 396.5, 496.5],
     [187.5, 166.5, 304.5, 270.5, 369.5, 322.5, 418.5, 353.5, 204.5, 211.5, 280.5, 300.5]]
)


# Example image (since we have a greyscale image, reduce dimensionality down to 2)
img = mpimg.imread('/home/tm2/python_bootcamp_2020/ekf_notes/Screenshot from 2020-08-14 19-36-46.png')[:,:,0]
plt.imshow(img, cmap='gray')
plt.scatter(x=detected_corners[0], y=detected_corners[1], c='b', s=10)

plt.show()
