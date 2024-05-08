from os import environ as env
import re
id_pattern = re.compile(r'^.\d+$')
import os

class Telegram:
    API_ID = int(env.get("API_ID", "24010108"))
    API_HASH = str(env.get("API_HASH", "8d89700b2fc09a3aa6c906cbed65b040"))
    BOT_TOKEN = str(env.get("BOT_TOKEN", "6609449380:AAGle29QwW3faG8wxXCGFDGVFEVoEfc-hyw"))
    BASE_SITE = env.get('BASE_SITE', 'falconfiles.in')
    METHOD = env.get("METHOD", "shortener")
    API_KEY = env.get('API_KEY', "6d03cea4840640ac95c24ad6f233b4055b812f09")
    OWNER_ID = int(env.get('OWNER_ID', '5791145987'))
    WORKERS = int(env.get("WORKERS", "30"))  # 6 workers = 6 commands at once
    DATABASE_URL = str(env.get('DATABASE_URL', "mongodb+srv://sonukumarkrbbu69:R2fY8z1SQXKxTF6r@cluster0.jgjic4e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
    BOT_USERNAME = env.get("BOT_USERNAME", "Falconfilesbot")
    UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "Falconfiles"))
    SESSION_NAME = str(env.get('SESSION_NAME', 'indexing'))
    FORCE_SUB_ID = env.get('FORCE_SUB_ID', "-1002083734102")
    FORCE_SUB = env.get('FORCE_UPDATES_CHANNEL', 0)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "30"))
    FILE_PIC = env.get('FILE_PIC')
    START_PIC = env.get('START_PIC')
    VERIFY_PIC = env.get('VERIFY_PIC')
    DELETE_TIME = int(env.get('AUTO_DELETE_TIME', 1800))
    MOVIE_PIC = (env.get('MOVIE_PIC', "https://graph.org/file/70b6bbd733b2b2dffd96f.png https://graph.org/file/4df724f05028b3b4eacce.jpg https://graph.org/file/f617ed08634217edc26ea.jpg")).split()
    VERIFIED_PIC = env.get('VERIFIED_PIC')
    MULTI_CLIENT = True
    GROUP = int(env.get("GROUP", "-1004142352920"))
    FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", "-1002090524947"))   # Logs channel for file logs
    ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", "-1002000855166"))   # Logs channel for user logs
    MODE = env.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split()))
    ADMINS_PERSONS = list(set(int(x) for x in str(env.get("ADMINS_PERSONS", "5791145987")).split()))
    UPLOAD_CHANNEL = int(env.get("UPLOAD_CHANNEL", "-1002137802831"))
    UPDATE_CHANNEL = int(env.get("UPDATE_CHANNEL", "-1002093160666"))   #-1002083903461
    INDEX_CHANNELS = int(env.get("INDEX_CHANNELS", "-1002145329802"))
class Server:
    PORT = int(env.get("PORT", 9896))
    BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
    HAS_SSL = str(env.get("HAS_SSL", "1").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(env.get("NO_PORT", "1").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(env.get("FQDN", "streaamstore.shop"))
    URL = "http{}://{}{}/".format(
        "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
    )


MULTI_TOKEN1 = str(env.get("MULTI_TOKEN1", "6342113383:AAHjIB0upZ0RTPvhRbiI14wKvska4rmI-Zg"))