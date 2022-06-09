from environs import Env
import configparser

env = Env()
env.read_env()

DATABASE_URL = env.str("DATABASE_URL")
TOKEN = env.str("TOKEN")
ADMINS = env.list("ADMINS", subcast=int)

analytics = configparser.ConfigParser()
analytics.read('analytics.ini')

sql = {name: open(analytics[name]['sql_file']).read()
       for name in analytics.sections()}

