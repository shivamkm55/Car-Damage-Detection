import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Read variables
print("SECRET_KEY =", os.getenv("FDMYD-9NK6Q-FHT6T-86XJ4-VMH8Y"))
print("DB_HOST =", os.getenv("DB_HOST"))
print("DB_USER =", os.getenv("DB_USER"))
print("DB_PASSWORD =", os.getenv("DB_PASSWORD"))
print("DB_NAME =", os.getenv("DB_NAME"))
