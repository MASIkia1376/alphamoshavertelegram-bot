import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ===== تنظیمات =====
TOKEN = os.environ.get("BOT_TOKEN")  # توکن از Render
ADMIN_ID = int(os.environ.get("ADMIN_ID"))  # آیدی عددی خودت

# ===== /start =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    # پیام به ادمین
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=(
            "👤 کاربر جدید وارد ربات شد\n\n"
            f"نام: {user.first_name}\n"
            f"یوزرنیم: @{user.username}\n"
            f"ID: {user.id}"
        ),
    )

    # پاسخ به کاربر
    await update.message.reply_text(
        "✅ ثبت شد\nممنون از شما"
    )

# ===== پیام‌های متنی =====
async def get_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("پیام شما دریافت شد")

# ===== اجرای ربات =====
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, get_text))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
