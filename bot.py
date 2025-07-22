from telegram import Update
from telegram.ext import Application, MessageHandler, filters
from chart_vision import ChartReader
from trade_manager import TradeManager
from config import Config

chart_reader = ChartReader()
trade_manager = TradeManager()

async def handle_chart(update: Update, context):
    try:
        photo = await update.message.photo[-1].get_file()
        img_bytes = await photo.download_as_bytearray()
        
        analysis = chart_reader.analyze(img_bytes)
        plan = trade_manager.evaluate(analysis)
        
        await update.message.reply_markdown_v2(
            f"""
📊 *Trade Signal* 🚀
• *Pattern*: {analysis['pattern']}
• *Entry*: `{plan['entry']}`
• *Stop*: `{plan['stop']}`
• *Target*: `{plan['target']}`
• *R/R*: `1:{plan['rr_ratio']}`
"""
        )
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

app = Application.builder().token(Config.TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.PHOTO, handle_chart))

if __name__ == "__main__":
    app.run_polling()
