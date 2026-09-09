from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "OVDJE_STAVI_TOKEN_BOTA"

products = {
    "1": ("Majica", "15 €"),
    "2": ("Kačket", "10 €"),
    "3": ("Dukserica", "25 €"),
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(f"{name} — {price}", callback_data=key)]
        for key, (name, price) in products.items()
    ]

    await update.message.reply_text(
        "🛍 Dobrodošli u naš shop!\n\nIzaberite proizvod:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def product_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    name, price = products[query.data]

    await query.edit_message_text(
        f"📦 {name}\n"
        f"💰 Cijena: {price}\n\n"
        "Za narudžbu kontaktirajte prodavca."
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(product_selected))

    print("Bot je pokrenut!")
    app.run_polling()

if __name__ == "__main__":
    main()
