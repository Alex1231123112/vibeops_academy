"""Конфигурация админки Telegram."""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
CHANNEL_ID = os.getenv("CHANNEL_ID", "@vibeops_academy")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")

BASE_DIR = Path(__file__).resolve().parent
