# ANSbot
Simple Discord bot that provides real-time player population information for a Dark Age of Camelot private server (Celestius). The bot monitors player counts across the game's three realms and responds to specific commands in Discord channels.

Key Features:
Real-time Player Tracking: Fetches live player data from the Celestius server's API endpoint
Realm-specific Queries: Supports individual realm population checks for the three DAoC factions:
- Hibernia 
- Midgard 
- Albion
- Total Population: Provides overall server population across all realms

Available Commands:
!players - Returns total number of players online across all realms
!hib - Returns number of Hibernia players online
!mid - Returns number of Midgard players online
!alb - Returns number of Albion players online

Technical Implementation:
- Built using the discord.py library
- Makes HTTP requests to https://celestiusrvr.com/.netlify/functions/status API
- Parses JSON responses to extract player count data
- Implements proper bot message filtering to prevent self-responses
- Uses environment variables for secure token management
