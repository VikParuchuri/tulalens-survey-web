import settings
from parse_rest.connection import register
from models import Survey, Screen
import os
import yaml
import re

def survey_loader(survey_path):
    with open(survey_path, 'r') as survey_file:
        survey_data = survey_file.read()

    survey_data = re.split("-{4,}", survey_data)
    survey_data = [yaml.safe_load(i) for i in survey_data]
    meta = survey_data[1]
    screens = [i for i in survey_data[2:] if i is not None]

    return meta, screens

def sync():
    register(settings.APPLICATION_ID, settings.REST_API_KEY, master_key=settings.MASTER_KEY)
    surveys = [s for s in os.listdir(settings.SURVEY_DIR) if s.endswith(".yaml")]
    for s in surveys:
        survey_path = os.path.join(settings.SURVEY_DIR, s)
        meta, screens = survey_loader(survey_path)
        all_versions = Survey.Query.filter(survey_number=meta["survey_number"])

        version = 0
        for v in all_versions:
            if v.version > version:
                version = v.version
        version += 1
        meta["version"] = version
        survey = Survey()
        for f in survey.fields:
            setattr(survey, f, meta[f])

        survey.save()
        for i, s in enumerate(screens):
            screen = Screen()
            s["screen_number"] = (i + 1)
            s["survey"] = survey
            for f in screen.fields:
                val = s.get(f, None)
                if val:
                    setattr(screen, f, val)
            screen.save()

if __name__ == "__main__":
    sync()