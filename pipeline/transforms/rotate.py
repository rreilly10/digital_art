from pipeline.transforms.image_transform import ImageTransform


class RotateTransform(ImageTransform):
    def apply(self, image, angle=45):
        return image.rotate(float(angle))
