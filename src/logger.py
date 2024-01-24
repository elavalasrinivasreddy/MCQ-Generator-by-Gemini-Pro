import logging
import os
from datetime import datetime

# Creating log folder to save the log files
dir_path = os.path.join(os.getcwd(),'logs')
os.makedirs(dir_path, exist_ok=True)
# Today Date
date = datetime.now().strftime('%Y_%m_%d_%H_%M') #_%M_%S
# Log file name
log_file_name = os.path.join(dir_path, f"{date}.log")

# # Logging object
FORMAT = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(filename=log_file_name, 
                    encoding='utf-8', 
                    format=FORMAT,
                    level=logging.INFO
                    )

logging.info('Logging is Initiated...')