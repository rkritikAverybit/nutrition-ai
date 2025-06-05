import requests
from typing import Dict, Any, Optional
from ..config.settings import settings

class NutritionDatabase:
    def __init__(self):
        self.base_url = settings.NUTRITION_DB_URL
        self.api_key = settings.NUTRITION_API_KEY
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    async def get_nutrition_info(self, food_item: str) -> Optional[Dict[str, Any]]:
        """Get nutritional information for a food item"""
        try:
            # TODO: Replace with actual API endpoint
            response = requests.get(
                f"{self.base_url}/food/{food_item}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching nutrition info: {e}")
            return None

    def format_nutrition_info(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Format the nutrition information into a standardized structure"""
        return {
            "calories": data.get("calories", 0),
            "macronutrients": {
                "protein": data.get("protein", 0),
                "carbs": data.get("carbohydrates", 0),
                "fat": data.get("fat", 0),
                "fiber": data.get("fiber", 0)
            },
            "micronutrients": {
                "vitamins": data.get("vitamins", {}),
                "minerals": data.get("minerals", {})
            },
            "serving_size": data.get("serving_size", "100g"),
            "allergens": data.get("allergens", [])
        }

    async def search_food(self, query: str) -> Optional[Dict[str, Any]]:
        """Search for food items in the database"""
        try:
            # TODO: Replace with actual API endpoint
            response = requests.get(
                f"{self.base_url}/search",
                params={"q": query},
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error searching food: {e}")
            return None

# Create a singleton instance
nutrition_db = NutritionDatabase()
