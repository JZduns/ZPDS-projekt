class User:
    """
    A class representing a user with username, password, email, premium status, allergies, vegetarian.
    """

    def __init__(
        self,
        username: str,
        password: str,
        email: str,
        premium: bool,
        allergies: list,
        vegetarian: bool,
    ):
        """
        Initialize a User object.

        Args:
        - username (str): The username of the user.
        - password (str): The password of the user.
        - email (str): The email address of the user.
        - premium (bool): The premium status of the user.
        - allergies (list): A list of allergies the user has.
        """
        self._username = username
        self._password = password
        self._email = email
        self._premium = premium
        self._allergies = allergies
        self._vegetarian = vegetarian

    @property
    def username(self) -> str:
        """
        Get the username of the user.

        Returns:
        - str: The username of the user.
        """
        return self._username

    @username.setter
    def username(self, new_username: str):
        """
        Set a new username for the user.

        Args:
        - new_username (str): The new username to set.
        """
        self._username = new_username

    @property
    def password(self) -> str:
        """
        Get the password of the user.

        Returns:
        - str: The password of the user.
        """
        return self._password

    @password.setter
    def password(self, new_password: str):
        """
        Set a new password for the user.

        Args:
        - new_password (str): The new password to set.
        """
        self._password = new_password

    @property
    def email(self) -> str:
        """
        Get the email address of the user.

        Returns:
        - str: The email address of the user.
        """
        return self._email

    @email.setter
    def email(self, new_email: str):
        """
        Set a new email address for the user.

        Args:
        - new_email (str): The new email address to set.
        """
        self._email = new_email

    @property
    def premium(self) -> bool:
        """
        Get the premium status of the user.

        Returns:
        - bool: The premium status of the user.
        """
        return self._premium

    @premium.setter
    def premium(self, is_premium: bool):
        """
        Set the premium status for the user.

        Args:
        - is_premium (bool): The new premium status to set.
        """
        self._premium = is_premium

    @property
    def allergies(self) -> list:
        """
        Get the list of allergies the user has.

        Returns:
        - list: A list of allergies the user has.
        """
        return self._allergies

    @allergies.setter
    def allergies(self, new_allergies: list):
        """
        Set a new list of allergies for the user.

        Args:
        - new_allergies (list): The new list of allergies to set.
        """
        self._allergies = new_allergies

    @property
    def vegetarian(self) -> bool:
        """
        Get the vegetarian status of the user.

        Returns:
        - bool: The vegetarian status of the user.
        """
        return self._vegetarian

    @vegetarian.setter
    def vegetarian(self, vegetarian: bool):
        """
        Set the vegetarian status for the user.

        Args:
        - vegetarian (bool): The new vegetarian status to set.
        """
        self._vegetarian = vegetarian

    def is_allergic_to(self, ingredient):
        """
        Checks if user is allergic to the provided ingredient.

        :param ingredient: The that you want to check if user is allergic to.
        :return: True if user is allergic to specified ingredient.
        """
        for i in self.allergies:
            if i.lower() == ingredient.lower():
                return True
        return False
