from apscheduler.schedulers.background import BackgroundScheduler
from app.utils.helpers import send_message_to_user
from app.models.user import User
from app.models.quest import Quest
from app import app, db

def send_daily_question():
    with app.app_context():
        users = User.query.all()
        quest = Quest.query.order_by(db.func.random()).first()
        if not quest:
            return
        # Mets ici l'URL de ton site ou de ngrok
        base_url = "	https://eef55bc7c368.ngrok-free.app"  # à adapter
        quest_url = f"{base_url}/quest/view/{quest.id}"
        for user in users:
            blocks = [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": (
                            f"*⚔️ Question du jour :*\n"
                            f"<{quest_url}|Prêt à relever le défi!>"
                        )
                    }
                }
            ]
            send_message_to_user(user.slack_id, "Voici ta question du jour !", blocks=blocks)

scheduler = BackgroundScheduler()
scheduler.add_job(send_daily_question, 'cron', hour=10, minute=0)
scheduler.start()

if __name__ == "__main__":
    with app.app_context():
        send_daily_question()