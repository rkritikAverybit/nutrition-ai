import cv2
import numpy as np
from PIL import Image
from pathlib import Path
from typing import Tuple, Union

class ImageProcessor:
    @staticmethod
    def load_image(image_path: Union[str, Path]) -> Image.Image:
        """Load an image from path and convert to PIL Image"""
        return Image.open(image_path)

    @staticmethod
    def resize_image(image: Image.Image, size: Tuple[int, int]) -> Image.Image:
        """Resize image to target size while maintaining aspect ratio"""
        return image.resize(size, Image.LANCZOS)

    @staticmethod
    def enhance_image(image: Image.Image) -> Image.Image:
        """Enhance image quality for better recognition"""
        # Convert PIL Image to OpenCV format
        cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        # Apply basic image enhancements
        # 1. Denoise
        denoised = cv2.fastNlMeansDenoisingColored(cv_image)
        
        # 2. Adjust brightness and contrast
        lab = cv2.cvtColor(denoised, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        cl = clahe.apply(l)
        enhanced_lab = cv2.merge((cl,a,b))
        enhanced_bgr = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)
        
        # Convert back to PIL Image
        enhanced_rgb = cv2.cvtColor(enhanced_bgr, cv2.COLOR_BGR2RGB)
        return Image.fromarray(enhanced_rgb)

    @staticmethod
    def normalize_image(image: Image.Image) -> np.ndarray:
        """Normalize image pixel values"""
        img_array = np.array(image)
        return img_array / 255.0

    @staticmethod
    def segment_food(image: Image.Image) -> Image.Image:
        """Segment the food portion from the image"""
        # TODO: Implement food segmentation logic
        # This could include:
        # - Background removal
        # - Food item isolation
        # - Multiple food item separation
        return image
