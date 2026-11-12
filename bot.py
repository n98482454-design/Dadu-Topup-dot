import os
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# Demo-only package names. Edit these when configuring your shop.
PACKAGES = [
    ("100 Diamonds", "demo_100"),
    ("210 Diamonds", "demo_210"),
    ("530 Diamonds", "demo_530"),
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("💎 ডায়মন্ড প্যাকেজ", callback_data="show_packages")],
        [InlineKeyboardButton("ℹ️ সাহায্য", callback_data="help")],
    ]
    await update.message.reply_text(
        "স্বাগতম DADU TOPUP-এ! 🎮\n\n"
        "এটি একটি প্রাথমিক ডেমো বট। এখনো আসল ডায়মন্ড অর্ডার বা পেমেন্ট চালু নেই।",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

async def packages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton(f"💎 {name}", callback_data=callback)]
        for name, callback in PACKAGES
    ]
    await update.message.reply_text(
        "ডেমো প্যাকেজ তালিকা:\nএগুলো শুধু নমুনা—দাম ও অর্ডার চালু করা হয়নি।",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "কমান্ড:\n/start — বট চালু\n/packages — ডেমো প্যাকেজ\n/help — সাহায্য\n\n"
        "আসল টপ-আপ চালুর জন্য অনুমোদিত Diamond API Provider, নিরাপদ পেমেন্ট "
        "ব্যবস্থা এবং অর্ডার যাচাই যুক্ত করতে হবে।"
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "help":
        await query.edit_message_text("সাহায্য: /start, /packages অথবা /help ব্যবহার করো।")
        return

    if query.data == "show_packages":
        keyboard = [
            [InlineKeyboardButton(f"💎 {name}", callback_data=callback)]
            for name, callback in PACKAGES
        ]
        await query.edit_message_text(
            "ডেমো প্যাকেজ—এখনো কেনাকাটা বা টপ-আপ চালু নেই:",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )
        return

    selected = next((name for name, callback in PACKAGES if callback == query.data), None)
    if selected:
        await query.edit_message_text(
            f"তুমি {selected} নির্বাচন করেছ।\n\n"
            "এটি শুধু ডেমো। API ও পেমেন্ট যুক্ত না হওয়া পর্যন্ত "
            "UID পাঠিও না এবং কোনো টাকা দিও না।"
        )

def main() -> None:
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise RuntimeError(
            "BOT_TOKEN পাওয়া যায়নি। Render-এর Environment Variables-এ BOT_TOKEN সেট করো।"
        )

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("packages", packages))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CallbackQueryHandler(button_handler))
    logger.info("DADU TOPUP demo bot is starting...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
