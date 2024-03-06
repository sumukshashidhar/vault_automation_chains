from vault import File, Vault
from dotenv import load_dotenv
import rules

import os

load_dotenv()

VAULT_PATH = os.environ["VAULT_PATH"]

vault = Vault(VAULT_PATH)

for file in vault.get_old_daily_notes():
    content = file.get_file()
    todoist_tasks = "```todoist\nname: Today's Tasks\nfilter: \"today | overdue\"\n```"
    new_content = rules.remove_blocks(content, todoist_tasks)
    file.write_file(new_content)
