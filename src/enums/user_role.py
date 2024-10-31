from src.enums.translated_enum import TranslatedEnum


class UserRole(TranslatedEnum):
    ADMIN = "admin"
    LAB_STAFF = "lab-staff"

    @classmethod
    def to_choices(self):
        return tuple((user_role.value, user_role.name) for user_role in self)
