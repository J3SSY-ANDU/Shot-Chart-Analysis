from nba_api.stats.endpoints import playercareerstats

# Get the player career stats for LeBron James
career = playercareerstats.PlayerCareerStats(player_id='2544')
print(career.get_data_frames()[0])