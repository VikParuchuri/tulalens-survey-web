import settings
from parse_rest.connection import register
from models import Survey, Screen
import os
import yaml
import re

def hide():
    register(settings.APPLICATION_ID, settings.REST_API_KEY, master_key=settings.MASTER_KEY)
    all_surveys = Survey.Query.all()
    for s in all_surveys:
        s.use = False
        s.save()

if __name__ == "__main__":
    hide()