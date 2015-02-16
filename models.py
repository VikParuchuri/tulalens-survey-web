from parse_rest.datatypes import Object

class TulaLensObject(Object):
    PROTECTED_ATTRIBUTES = Object.PROTECTED_ATTRIBUTES + ['fields']

class Survey(TulaLensObject):
    fields = ["name", "description", "survey_number", "language", "author", "version", "use"]

class Screen(Object):
    fields = ["screen_number", "type", "question", "options", "next_screen", "survey"]