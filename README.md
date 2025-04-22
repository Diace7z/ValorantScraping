This python module use to scrap data in Tracker website. This module including leaderboard function to track players ID in high rank elo and encounter function to track players who played with or against with certain player. I recommend to instal Cloudflare Warp to prevent block from website.

Main function is **scraper(filename, r = 1, ep_act = 'V25A2', error = 'n'):**

**filename** : name file in csv have "id" columns. The id for should be in riot ID format (Name#Tag)

**r**        : ratio, this parameter to determine ids will you scrap. default is 1 or 100% id in file will scraped. fill the parameter with float number in range 0 to 1.

**ep_act**   : episode act, Parameter to determine episode and act that player played to obtain the overview. default is 'V25A2'

**error**    : to reveal or not the error when scrap each element in webpage. default is 'n'
