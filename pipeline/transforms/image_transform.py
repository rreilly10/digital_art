from abc import ABC, abstractmethod


class ImageTransform(ABC):
    @abstractmethod
    def apply(self, image, *args, **kwargs):
        pass
