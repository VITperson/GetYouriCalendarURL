from caldav import DAVClient
from dotenv import load_dotenv
import os

load_dotenv()

client = DAVClient(
    url="https://caldav.icloud.com/",
    username=os.getenv("ICLOUD_USER"),
    password=os.getenv("ICLOUD_APP_PW")
)

principal = client.principal()
calendars = principal.calendars()

for cal in calendars:
    print("Имя календаря:", cal.name)
    print("Ссылка:", cal.url)
    print()
