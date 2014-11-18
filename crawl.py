'''
Usage: MONGODB_URI=mongodb://locahost:27017 BOARD_NAME=R_Language python crawl.py


'''


from ptt_crawler.tasks import *


if __name__ == '__main__':
    import os
    BOARD_NAME = os.environ.get("BOARD_NAME", "R_Language")
    submit_all_subpages_of_a_board.apply_async(kwargs = {"board_name":BOARD_NAME}) 