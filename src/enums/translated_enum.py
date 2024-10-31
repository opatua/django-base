from enum import Enum

from django.utils.translation import get_language


class TranslatedEnum(Enum):
    # FIXME Use i18n
    def get_dictionary(self):
        pass

    def get_translation(self):
        dictionary = self.get_dictionary()
        if not dictionary:
            return self.value

        return dictionary.get(
            get_language(),
            dictionary.get("en-us", {}),
        ).get(
            self,
            self.value,
        )
