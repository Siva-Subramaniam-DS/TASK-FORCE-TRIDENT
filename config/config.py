import json
import os

CONFIG_FILE = "bot_config.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_config(config_data):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config_data, f, indent=4)

config = load_config()

# Global Roles & Channels (pulled from config)
ROLE_IDS = {
    "head_organizer": config.get("roles", {}).get("head_organizer", 1502073772113395833),  # Org
    "head_helper":    config.get("roles", {}).get("head_helper",    1502073833102905424),  # Helper
    "helper_team":    config.get("roles", {}).get("helper_team",    1502073833102905424),  # Helper
    "judge":          config.get("roles", {}).get("judge",          1502079518079455283),  # Judge
    "recorder":       config.get("roles", {}).get("recorder",       1502079518079455283),  # Judge (fallback)
    "staff":          config.get("roles", {}).get("staff",          1502073772113395833),  # Org (fallback)
}

CHANNEL_IDS = {
    "rules":        config.get("channels", {}).get("rules",         1500279213754945596),  # Rules
    "bracket":      config.get("channels", {}).get("bracket",       1500279696154165411),  # Bracket
    "deadlines":    config.get("channels", {}).get("deadlines",     1500279734502953060),  # Deadlines
    "staff_attendance": config.get("channels", {}).get("attendance",1500276360868790304),  # Attendance
    "take_schedule": config.get("channels", {}).get("schedule",     1500276285027516456),  # Schedule
    "results":      config.get("channels", {}).get("results",       1500279846704513074),  # Result
    "category_1":   config.get("channels", {}).get("category_1",   1493422365902897194),
    "category_2":   config.get("channels", {}).get("category_2",   1493422524967686184),
    "closed_tickets_category": config.get("channels", {}).get("closed_tickets_category", 1493423252658323598),
}

ORGANIZATION_NAME = config.get("organization_name", "TASK FORCE TRIDENT")
TOURNAMENT_SYSTEM_NAME = config.get("tournament_system_name", "TASK FORCE TRIDENT Tournament System")

# Active tournament properties
BRACKET_LINK = config.get("bracket_link", "")
BRACKET_API_KEY = config.get("bracket_api_key", "")
GOOGLE_SHEET_LINK = config.get("google_sheet_link", "")
CURRENT_TOURNAMENT_NAME = config.get("tournament_name", "")
EVENTS_FILE = "events.json"
RULES_FILE = "tournament_rules.json"
