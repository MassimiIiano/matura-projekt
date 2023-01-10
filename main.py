import threading
from decoder_live import decode_videocapture

# start rading barcodes
read_code_thread = threading.Thread(target=decode_videocapture)
read_code_thread.start()

