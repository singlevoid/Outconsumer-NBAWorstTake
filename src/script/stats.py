
from nba_api.stats.endpoints import Scoreboard, BoxScoreTraditionalV2
import datetime


if __name__ == "__main__":

    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday_date = yesterday.strftime('%m/%d/%Y')

    scoreboard = Scoreboard(day_offset=-1, game_date=yesterday_date)
    games = scoreboard.game_header.get_data_frame()


    for i, game in games.iterrows():

        scoreboard =  BoxScoreTraditionalV2(game['GAME_ID'])
        home = scoreboard.data_sets[0].get_data_frame()
        print(str(scoreboard.data_sets[0].get_data_frame()))
        print(str(scoreboard.data_sets[1].get_data_frame()))
        print("\n\n\n\n\n\n\n")

      