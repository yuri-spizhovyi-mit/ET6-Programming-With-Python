from ps4 import Climate

clim = Climate("data.csv")
print(clim.get_daily_temp("BOSTON", 1, 10, 2001))
