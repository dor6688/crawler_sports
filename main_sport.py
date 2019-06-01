import threading

import sport5
import sport1
import ONE


def update_all():

    print("Start updating...\n")
    new_article_sport5 = sport5.update_articles()
    new_article_sport1 = sport1.update_articles()
    new_article_one = ONE.update_articles()
    print("\nFinish updating !\n")

    return [new_article_sport5, new_article_sport1, new_article_one]



