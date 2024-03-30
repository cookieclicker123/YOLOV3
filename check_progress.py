import os
import time
import config
import utils

checkpoint_file = config.CHECKPOINT_FILE
print(f"Attempting to access file at: {checkpoint_file}")
if not os.path.exists(checkpoint_file):
    print(f"File not found: {checkpoint_file}")
else:
    modification_time = os.path.getmtime(checkpoint_file)
    print("Last modification time: ", time.ctime(modification_time))
