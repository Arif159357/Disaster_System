import schedule
import time
from scrapy.scrapping import main


class tasks:
    def annotator_performance(self):
        main()
        schedule.every(1).minute.do(main)
        while True:
            schedule.run_pending()
            time.sleep(1) 

    