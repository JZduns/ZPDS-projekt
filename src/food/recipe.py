class Recipe:
    """
    A class representing a recipe with necessary, additional, and alternative ingredients along with calorie information
    """

    def __init__(
        self,
        name: str,
        necessary_ingredients: list,
        additional_ingredients: list,
        alternative_ingredients: list,
        calories: int,
    ):
        """
        Initialize a Recipe object.

        Args:
        - name (str): The name of the recipe.
        - necessary_ingredients (list): A list of necessary ingredients for the recipe.
        - additional_ingredients (list): A list of additional ingredients for the recipe.
        - alternative_ingredients (list): A list of alternative ingredients for the recipe.
        - calories (int): The calorie information for the recipe.
        """
        self._name = name
        self._necessary_ingredients = necessary_ingredients
        self._additional_ingredients = additional_ingredients
        self._alternative_ingredients = alternative_ingredients
        self._calories = calories

    @property
    def name(self) -> str:
        """
        Get the name of the recipe.

        Returns:
        - str: The name of the recipe.
        """
        return self._name

    @name.setter
    def name(self, new_name: str):
        """
        Set a new name for the recipe.

        Args:
        - new_name (str): The new name to set for the recipe.
        """
        self._name = new_name

    @property
    def necessary_ingredients(self) -> list:
        """
        Get the necessary ingredients for the recipe.

        Returns:
        - list: A list of necessary ingredients for the recipe.
        """
        return self._necessary_ingredients

    @necessary_ingredients.setter
    def necessary_ingredients(self, necessary_ingredients: list):
        """
        Set new necessary ingredients for the recipe.

        Args:
        - necessary_ingredients (list): The new list of necessary ingredients to set for the recipe.
        """
        self._necessary_ingredients = necessary_ingredients

    @property
    def additional_ingredients(self) -> list:
        """
        Get the additional ingredients for the recipe.

        Returns:
        - list: A list of additional ingredients for the recipe.
        """
        return self._additional_ingredients

    @additional_ingredients.setter
    def additional_ingredients(self, additional_ingredients: list):
        """
        Set new additional ingredients for the recipe.

        Args:
        - additional_ingredients (list): The new list of additional ingredients to set for the recipe.
        """
        self._additional_ingredients = additional_ingredients

    @property
    def alternative_ingredients(self) -> list:
        """
        Get the alternative ingredients for the recipe.

        Returns:
        - list: A list of alternative ingredients for the recipe.
        """
        return self._alternative_ingredients

    @alternative_ingredients.setter
    def alternative_ingredients(self, alternative_ingredients: list):
        """
        Set new alternative ingredients for the recipe.

        Args:
        - alternative_ingredients (list): The new list of alternative ingredients to set for the recipe.
        """
        self._alternative_ingredients = alternative_ingredients

    @property
    def calories(self) -> int:
        """
        Get the calorie information for the recipe.

        Returns:
        - int: The calorie information for the recipe.
        """
        return self._calories

    @calories.setter
    def calories(self, new_calories: int):
        """
        Set new calorie information for the recipe.

        Args:
        - new_calories (int): The new calorie information to set for the recipe.
        """
        self._calories = new_calories
