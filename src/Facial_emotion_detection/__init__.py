import os
import logging
import sys

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logs_dir = "Logs"
log_path = os.path.join(logs_dir, "running.log")
os.makedirs(logs_dir, exist_ok=True)

logging.basicConfig(

    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("Facial_emotion_detection")