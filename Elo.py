elo = dict()

def addserver(name):
	elo[name] = dict()

def adduser(server,user):
	elo[server][user]=(400,0,0)

def CheckElo(server,user):
	return(elo[server][user])

def CalcElo(server,user):
	wins = Elo.get[server][user][1]
	losses = Elo.get[server][user][2]
	TotalOScore = Elo.get[server][user][0]
	games = wins + losses
	score = wins - losses
	EloScore = (TotalOscore + (400 * score)) / games
	return(Eloscore)
