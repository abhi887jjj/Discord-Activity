from pypresence import Presence
import time
import datetime

client_id = "1484585106348838912"  # replace this

start_time = int(datetime.datetime(2025, 5, 12, 0, 0, 0).timestamp())

while True:
    try:
        RPC = Presence(client_id)
        RPC.connect()

        while True:
            RPC.update(
                state="Working on Project Supreme",
                details="Since May 12, 2025",
                start=start_time,
                large_image="supreme",   # your uploaded image name
                large_text="Project Supreme"
            )
            time.sleep(15)

    except Exception as e:
        print("Reconnecting...", e)
        time.sleep(10)
