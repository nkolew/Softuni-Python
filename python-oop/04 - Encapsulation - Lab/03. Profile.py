class Profile:
    __username: str
    __password: str

    def __init__(self, username: str, password: str) -> None:

        def username_is_valid(username) -> bool:
            return 5 <= len(username) <= 15

        def password_is_valid(password) -> bool:
            password_special_chars = {
                'upper': 0,
                'digits': 0
            }

            for c in password:
                if c.isupper():
                    password_special_chars['upper'] += 1
                elif c.isdigit():
                    password_special_chars['digits'] += 1

            return len(password) >= 8 and password_special_chars['upper'] > 0 and password_special_chars['digits'] > 0

        if not username_is_valid(username):
            raise ValueError(
                f'The username must be between 5 and 15 characters.')
        self.__username = username

        if not password_is_valid(password):
            raise ValueError(
                f'The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
        self.__password = password

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*"*len(self.password)}'

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, value: str) -> None:
        self.__username = value

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, value: str) -> None:
        self.__password = value


profile_with_invalid_password = Profile('My_username', 'My-password')
profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
