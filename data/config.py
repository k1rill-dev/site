from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
QIWI_TOKEN = env.str("TOKEN")
WALLET_QIWI = env.str("qiwi")
QIWI_PUBKEY = env.str("OPEN_KEY")
LOGIN = env.str("login")
PASSWORD = env.str("password")