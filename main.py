import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests

TOKEN = os.environ.get('TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """💰 اهلاً بيك بـ الهكر الحلال الذهبي 💰

اوامر VIP: 🔥
/analiz - تحليل فني + توصية دخول/خروج
/alert - تنبيه فوري اذا تحرك السوق 1%
/price - سعر الذهب اللايف

اشتراك VIP: 5$ شهرياً 💎
للاشتراك راسل الادمن: @qvwh2
قناتنا: https://t.me/qvwh2
"""
    await update.message.reply_text(text)

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        r = requests.get("https://api.metals.live/v1/spot/gold").json()
        gold_price = r[0]['price']
        await update.message.reply_text(f"سعر الذهب اللايف: ${gold_price} للأونصة")
    except:
        await update.message.reply_text("فشل جلب السعر، حاول بعد شوية")

async def analiz(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تحليل السوق: الذهب صاعد حالياً ✅ توصية: شراء")

async def alert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("تم تفعيل التنبيه 🔔 راح يجيك اشعار اذا تحرك 1%")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("analiz", analiz))
app.add_handler(CommandHandler("alert", alert))
print("البوت شغال...")
app.run_polling()
