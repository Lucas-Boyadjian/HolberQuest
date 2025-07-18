<<<<<<< HEAD
# Flask config (dev/prod)

import os
from dotenv import load_dotenv

load_dotenv()  # charge .env automatiquement

class Config:
    SLACK_SIGNING_SECRET = os.getenv('SLACK_SIGNING_SECRET')
    SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')
=======
>>>>>>> origin/dev2
