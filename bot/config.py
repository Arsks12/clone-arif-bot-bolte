import os
import json
from distutils.util import strtobool as stb

# --------------------------------------
BOT_TOKEN = "5165652203:AAEitVev-U0Tk-VEOY7iccHF4Q1n2EkLcS0"
GDRIVE_FOLDER_ID = "0AApUSh93yDzLUk9PVA"
# Default folder id.
OWNER_ID = 1261618989
# Example: OWNER_ID = 619418070
AUTHORISED_USERS = [1261618989, -1001748163527]
# Example: AUTHORISED_USERS = [63055333, 100483029, -10039439]
INDEX_URL = ""
IS_TEAM_DRIVE = True
USE_SERVICE_ACCOUNTS = False
THREAD_COUNT = 4 
# --> THREAD_COUNT: How many parralel transfers of every single clone at the same time
# ----> eg. I'm running 2 clones, and THREAD_COUNT is set to 4; so each clone will have 4 threads of it's own
# Suggested value is the number of CPU Cores + 2 or CPU Cores x 2. Try what suits you best :3
# --------------------------------------

# dont edit below this >



BOT_TOKEN = os.environ.get('BOT_TOKEN', BOT_TOKEN)
GDRIVE_FOLDER_ID = os.environ.get('GDRIVE_FOLDER_ID', GDRIVE_FOLDER_ID)
OWNER_ID = int(os.environ.get('OWNER_ID', OWNER_ID))
AUTHORISED_USERS = json.loads(os.environ.get('AUTHORISED_USERS', json.dumps(AUTHORISED_USERS)))
INDEX_URL = os.environ.get('INDEX_URL', INDEX_URL)
IS_TEAM_DRIVE = stb(os.environ.get('IS_TEAM_DRIVE', str(IS_TEAM_DRIVE)))
USE_SERVICE_ACCOUNTS = stb(os.environ.get('USE_SERVICE_ACCOUNTS', str(USE_SERVICE_ACCOUNTS)))
THREAD_COUNT = int(os.environ.get('THREAD_COUNT', THREAD_COUNT))
