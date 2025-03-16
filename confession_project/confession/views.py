from django.shortcuts import render,redirect
import requests

# Create your views here.
TELEGRAM_BOT_TOKEN = "7216119815:AAES0SPRSoJwECZ3xR2k_BHKM4W19BsyYzY"
TELEGRAM_CHAT_ID = "-4755612310"


def send_to_telegram(message):
    """Send confession to Telegram bot"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=data)

def confession_submit(request):
    """Handle confession form submission"""
    if request.method == "POST":
        confession_text = request.POST.get("text")
        if confession_text:
            confession_number = request.session.get('confession_number', 1)
            send_to_telegram(f"{confession_text}\n\n#RUFAC{confession_number}")
            request.session['confession_number'] = confession_number + 1
            return redirect('confession_form')
    return render(request, 'confession/index.html')
def confession_success(request):
    """Show success message after submission"""
    return render(request, 'confession_success.html')
