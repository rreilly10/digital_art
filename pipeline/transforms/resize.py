from pipeline.transforms.image_transform import ImageTransform


class ResizeTransform(ImageTransform):
    def apply(self, image, size=[1000, 1000]):
        return image.resize(size)
