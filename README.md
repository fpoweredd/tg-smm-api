# Telegram SMM Bot
This script is a simple Telegram bot interface for interacting with the SMM (Social Media Marketing) Panel API v2. It allows users to order social media promotion services easily through Telegram.

## Features

- **User Authorization**:
    - Checks if the user has access to the bot by comparing their ID with a predefined list of allowed user IDs.

- **Link Processing**:
    - When a user sends a message containing a link, the bot saves the link and presents the user with a list of promotion packages to choose from.

- **Ordering Services via SMM API**:
    - Based on the selected package and provided link, the bot sends requests to the SMM API to order the specified services.
    - Uses random values for certain parameters, such as the number of likes on TikTok.

- **Feedback**:
    - Notifies the user that the order has been placed and displays the user's current balance on .

## Setup
1. Replace `SMM_API_KEY` and `TG_API_TOKEN` with your actual SMM panel API key and the token from BotFather for your Telegram bot.
2. Add user IDs to the `allowed_user_ids` list to authorize users.
3. Customize API Requests
