class Ingredient:
    """
    A class representing an ingredient with its name, meat status, and gluten content.
    """

    def __init__(self, name: str, is_meat: bool):
        """
        Initialize an Ingredient object.

        Args:
        - name (str): The name of the ingredient.
        - is_meat (bool): The status indicating whether the ingredient is meat or not.
        - contains_gluten (bool): The status indicating whether the ingredient contains gluten or not.
        """
        self._name = name
        self._is_meat = is_meat

    @property
    def name(self) -> str:
        """
        Get the name of the ingredient.

        Returns:
        - str: The name of the ingredient.
        """
        return self._name

    @name.setter
    def name(self, new_name: str):
        """
        Set a new name for the ingredient.

        Args:
        - new_name (str): The new name to set for the ingredient.
        """
        self._name = new_name
