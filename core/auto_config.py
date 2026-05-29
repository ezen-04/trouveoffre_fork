from datetime import datetime
from system.detect import detection

now = datetime.now()
now_re = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


headers = detection()