import threading

import sport5
import sport1
import ONE


def update_all():
    threading.Timer(120.0, update_all).start()
    print("Start updating...\n")
    sport5.update_articles()
    sport1.update_articles()
    ONE.update_articles()
    print("Finish updating !\n")


update_all()
