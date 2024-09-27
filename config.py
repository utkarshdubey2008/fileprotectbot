import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the TOKEN and CHANNEL_ID from environment variables
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

# Check if TOKEN and CHANNEL_ID are None
if TOKEN is None:
    raise ValueError("No TOKEN environment variable set.")
if CHANNEL_ID is None:
    raise ValueError("No CHANNEL_ID environment variable set.")
