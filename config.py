# config.py

# ── YouTube MCP Configuration ─────────────────────────────────────────────────

# Max transcript length to send to Claude (characters)
MAX_TRANSCRIPT_LENGTH = 15000

# Max key points to extract
MAX_KEY_POINTS = 10

# Supported languages for transcripts (in order of preference)
TRANSCRIPT_LANGUAGES = ["en", "en-US", "en-GB"]

# Summary styles
SUMMARY_STYLES = ["brief", "detailed", "bullet"]