# DADU TOPUP Telegram Bot (Starter)

This is a starter/demo Telegram bot. It displays sample packages only.
It does **not** accept payments and does **not** send Free Fire diamonds.

## Files
- `bot.py` — bot code
- `requirements.txt` — Python dependency
- `render.yaml` — Render Background Worker configuration

## Deploy on Render
1. Upload these files to a GitHub repository.
2. In Render, choose **New + → Blueprint** and connect the repository.
3. When prompted, add `BOT_TOKEN` as an environment variable.
4. Enter your fresh BotFather token in Render's secret field. Never put it in GitHub or share it in chat.
5. Deploy the worker and test `/start` in Telegram.

## Important
Real automatic top-up requires a legitimate provider API, a secure payment flow,
order verification, and provider documentation. Do not claim an order is complete
until the provider confirms it. Test with a sandbox/demo first and have a parent
or guardian help review any paid service or payment setup.
