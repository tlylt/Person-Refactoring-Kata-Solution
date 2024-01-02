class PersonalNumber:
    def __init__(self, personal_number: str):
        personal_number = personal_number.replace("-", "")
        if personal_number.__len__() != 12:
            raise ValueError("invalid personal number " + personal_number)
        self.personal_number = personal_number
    def __str__(self) -> str:
        return self.personal_number
    def get_birth_year(self) -> int:
        # works for swedish PN
        year = self.personal_number[0:4]
        return int(year)


class PhoneNumber:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
    def __str__(self) -> str:
        return self.phone_number
    def get_country_code(self) -> str:
        code = ""
        if self.phone_number.startswith("00"):
            code = self.phone_number[2:4]
        elif self.phone_number.startswith("+"):
            code = self.phone_number[1:3]
        if code != "":
            return "+" + code
        return ""        


class Role:
    def __init__(self, role: int):
        if role < 0 or role > 4:
            raise ValueError("illegal role " + role)
        self.role = role
    def can_delete_users(self) -> bool:
        return self.role == Person.USER_ROLE_MANAGER or self.role == Person.USER_ROLE_ADMIN


class Person:
    USER_ROLE_ADMIN = 0
    USER_ROLE_ENGINEER = 1
    USER_ROLE_MANAGER = 2
    USER_ROLE_SALES = 3
    def __init__(self, role: int, swedish_personal_number: str, phone_number: str):
        self.role = Role(role)
        self.swedish_personal_number = PersonalNumber(swedish_personal_number)
        self.phone_number = PhoneNumber(phone_number)

    def get_swedish_personal_number_str(self) -> str:
        return str(self.swedish_personal_number)

    def get_phone_number_str(self) -> str:
        return str(self.phone_number)

    def birth_year(self) -> int:
        return self.swedish_personal_number.get_birth_year()

    def country_code(self) -> str:
        return self.phone_number.get_country_code()

    def can_delete_users(self) -> bool:
        return self.role.can_delete_users()
