import threading
import time
from app.utils.helpers import auto_fail_combat

# combat_data = { user_id: {'timestamp': ..., 'qcm_id': ...} }

combat_data = {}

def start_timer(user_id, quest_id, duration=120):
    combat_data[user_id] = {'qcm_id': quest_id, 'timestamp': time.time()}

    def timer():
        time.sleep(duration)
        if user_id in combat_data:
            print(f"[⏰ Timeout] Utilisateur {user_id} n'a pas répondu en {duration}s")
            auto_fail_combat(user_id)
            combat_data.pop(user_id, None)

    thread = threading.Thread(target=timer)
    thread.daemon = True
    thread.start()
