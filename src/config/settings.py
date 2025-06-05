from pathlib import Path
from typing import Dict, Any
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class Settings:
    # Project paths
    BASE_DIR = Path(__file__).parent.parent.parent
    MODEL_DIR = BASE_DIR / "models"
    UPLOAD_DIR = BASE_DIR / "uploads"

    # API settings
    API_V1_PREFIX = "/api/v1"
    PROJECT_NAME = "Nutrition AI"
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    # Model settings
    MODEL_PATH = os.getenv("MODEL_PATH", str(MODEL_DIR / "food_recognition_model.h5"))
    MODEL_CONFIDENCE_THRESHOLD = float(os.getenv("MODEL_CONFIDENCE_THRESHOLD", "0.7"))

    # Image processing settings
    MAX_IMAGE_SIZE = (800, 800)  # Maximum dimensions for uploaded images
    SUPPORTED_FORMATS = [".jpg", ".jpeg", ".png"]
    MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

    # Nutritional database settings
    NUTRITION_DB_URL = os.getenv("NUTRITION_DB_URL", "https://api.nutritiondb.example.com")
    NUTRITION_API_KEY = os.getenv("NUTRITION_API_KEY")

    @classmethod
    def create_directories(cls) -> None:
        """Create necessary project directories if they don't exist"""
        cls.MODEL_DIR.mkdir(parents=True, exist_ok=True)
        cls.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    @classmethod
    def get_settings(cls) -> Dict[str, Any]:
        """Get all settings as a dictionary"""
        return {
            "api_prefix": cls.API_V1_PREFIX,
            "project_name": cls.PROJECT_NAME,
            "debug": cls.DEBUG,
            "model_path": cls.MODEL_PATH,
            "confidence_threshold": cls.MODEL_CONFIDENCE_THRESHOLD,
            "max_image_size": cls.MAX_IMAGE_SIZE,
            "supported_formats": cls.SUPPORTED_FORMATS,
            "max_file_size": cls.MAX_FILE_SIZE,
        }

# Create an instance of Settings
settings = Settings()

# Ensure required directories exist
settings.create_directories()
