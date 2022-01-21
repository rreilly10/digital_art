from email.policy import default
import os
from PIL import Image
import numpy as np
from collections import defaultdict

# assign directory
directory = "images"

d = defaultdict(list)

# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f) and ".jpg" in f:
        image = np.asarray(Image.open(f))
        d[image.shape].append(f)

for k, v in d.items():
    if len(v) > 1:
        print(k, v)
