import time
from pyrogram import Client
app = Client(
    "My_Account",
    api_id = 9899039,
    api_hash ="5bab03171ae5e0d92e3e0ce70137943c")
with app:
    while True:
        time.sleep(60)
        time1 = time.localtime()
        soat = time.strftime("%H:%M", time1)
        app.update_profile(first_name=f"Niceboiii|{soat}")
