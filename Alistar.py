def initialize():
	board = [[0, 0, 0, 0, 0, 0,], [0, 0, 0, 0, 0, 0,], [0, 0, 0, 0, 0, 0,], [0, 0, 0, 0, 0, 0,], [0, 0, 0, 0, 0, 0,], [0, 0, 0, 0, 0, 0,], [0, 0, 0, 0, 0, 0,]]
	player = 1
	return(board, player)

def taketurn(collumn, board, player):
	switcher = {
		"A": 6,
		"B": 5,
		"C": 4,
		"D": 3,
		"E": 2,
		"F": 1,
		"G": 0,
		"a": 6,
		"b": 5,
		"c": 4,
		"d": 3,
		"e": 2,
		"f": 1,
		"g": 0,
	}
	x = switcher.get(collumn, 7)
	if x == 7:
		return(board, False)
	y=0
	while 1 == 1:
		if board[x][y] == 0:
			board[x][y] = player
			break
		y+=1
		if y >= 6:
			return(board, False)
	return(board, True)

def wincheck(board, collumn):
	switcher = {
		"A": 6,
		"B": 5,
		"C": 4,
		"D": 3,
		"E": 2,
		"F": 1,
		"G": 0,
		"a": 6,
		"b": 5,
		"c": 4,
		"d": 3,
		"e": 2,
		"f": 1,
		"g": 0,
	}
	x = switcher.get(collumn, 7)
	if x == 7:
		return(error)
	y=0
	while 1 == 1:
		if board[x][y] == 0:
			y-=1
			break
		y+=1
		if y > 5:
			y-=1
			break
	wincount = 0
	wincount = vertcount(board, x, y)
	if wincount >= 4:
		return True
	wincount = 0
	wincount = horizcount(board, x, y)
	if wincount >= 5:
		return True
	wincount = 0
	wincount = angleupcount(board, x, y)
	if wincount >= 5:
		return True
	wincount = 0
	wincount = angledowncount(board, x, y)
	if wincount >= 5:
		return True
	return False

def vertcount(board, x, y):
	check = 0
	for z in range(4):
		if board[x][y-z] == board[x][y]:
			check+=1
	return(check)

def horizcount(board, x, y):
	check = 0
	for z in range(4):
		if x-z < 0:
			break
		if board[x-z][y] == board[x][y]:
			check+=1
		else:
			break
	for z in range(4):
		if x+z > 6:
			break
		if board[x+z][y] == board[x][y]:
			check+=1
		else:
			break
	return(check)

def angleupcount(board, x, y):
	check = 0
	for z in range(4):
		if x-z < 0:
			break
		if board[x-z][y-z] == board[x][y]:
			check+=1
		else:
			break
	for z in range(4):
		if x+z > 6:
			break
		if y+z > 4:
			break
		if board[x+z][y+z] == board[x][y]:
			check+=1
		else:
			break
	return(check)

def angledowncount(board, x, y):
	check = 0
	for z in range(4):
		if y+z > 4:
			break
		if x-z < 0:
			break
		if board[x-z][y+z] == board[x][y]:
			check+=1
		else:
			break
	for z in range(4):
		if x+z > 6:
			break

		if board[x+z][y-z] == board[x][y]:
			check+=1
		else:
			break
	return(check)

def stalecheck(board):
	check = 0
	for x in range(7):
		if board[x-1][5] != 0:
			check+=1
	if check >= 7:
		return True
	else:
		return False

def printboard(board):
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	for x in range(6):
		row = ['         ']
		for y in range(7):
			if board[6-y][5-x] == 0:
				z = '_ '
			if board[6-y][5-x] == 1:
				z = 'X '
			if board[6-y][5-x] == 2:
				z = 'O '
			row.append(z)
		line = '  '.join(row)
		print(line, "\n")
	print("           A   B   C   D   E   F   G\n")
	return

def playgame():
	board, player = initialize()
	choice = input("Choose difficulty (easy/hard): ")
	switcher = {
		"easy": 0,
		"Easy": 0,
		"e": 0,
		"E": 0,
		"hard": 1,
		"Hard": 1,
		"h": 1,
		"H": 1,
	}
	dif = switcher.get(choice, 0)
	printboard(board)
	while 1 == 1:
		if player == 1:
			print("player ", player, " enter move: ")
			collumn = input()
			board, valid = taketurn(collumn, board, player)
		else:
			if dif == 0:
				collumn = alistar_v1(board)
			elif dif == 1:
				collumn = alistar_v2(board)
			board, valid = taketurn(collumn, board, player)
		if valid == False:
			print("invalid move")
			continue
		printboard(board)
		check = wincheck(board, collumn)
		if check == True:
			print("Player ", player, " wins!")
			return
		check = stalecheck(board)
		if check == True:
			print("Stalemate!")
			return
		if player == 1:
			player = 2
		else:
			player = 1

def game():
	cont = True
	yesno = {
		"y": True,
		"yes": True,
		"Yes": True,
		"Y": True,
	}
	while cont == True:
		playgame()
		choice = input("Play again? ")
		cont = yesno.get(choice, False)

def checkturn(collumn, board, player):
	x = collumn
	if x == 7:
		return(board, False)
	y=0
	while 1 == 1:
		if board[x][y] == 0:
			board[x][y] = player
			break
		y+=1
		if y >= 6:
			return(board, False)
	return(board, True)

def checkturn2(collumn, board, player):
	x = collumn
	if x == 7:
		return(board, False)
	y=0
	while 1 == 1:
		if board[x][y] == 0:
			break
		y+=1
		if y >= 6:
			return(board, False)
	return(board, True)

def playchecker(board, collumn):
	switcher = {
		"A": 6,
		"B": 5,
		"C": 4,
		"D": 3,
		"E": 2,
		"F": 1,
		"G": 0,
		"a": 6,
		"b": 5,
		"c": 4,
		"d": 3,
		"e": 2,
		"f": 1,
		"g": 0,
	}
	x = switcher.get(collumn, 7)
	if x == 7:
		return(error)
	y=0
	while 1 == 1:
		if board[x][y] == 0:
			y-=1
			break
		y+=1
		if y > 5:
			y-=1
			break
	wincount = 0
	wincount = vertcount(board, x, y)
	if wincount >= 4:
		return True
	wincount = 0
	wincount = horizcount(board, x, y)
	if wincount >= 5:
		return True
	wincount = 0
	wincount = angleupcount(board, x, y)
	if wincount >= 5:
		return True
	wincount = 0
	wincount = angledowncount(board, x, y)
	if wincount >= 5:
		return True
	return False

def vertcounter(board, x, y, p):
	check = 0
	for z in range(4):
		if y - z - 1 < 0:
			break
		if board[x][y-z-1] != p:
			break
		if board[x][y-z-1] == p:
			check+=1
	return(check)

def horizcounter(board, x, y, p):
	check = 0
	for z in range(4):
		if x-z-1 < 0:
			break
		if board[x-z-1][y] != p:
			break
		if board[x-z-1][y] == p:
			check+=1
		else:
			break
	for z in range(4):
		if x+z+1 > 6:
			break
		if board[x+z+1][y] != p:
			break
		if board[x+z+1][y] == p:
			check+=1
		else:
			break
	return(check)

def angleupcounter(board, x, y, p):
	if p == 1:
		p2 = 2
	else:
		p2 = 1
	check = 0
	for z in range(4):
		if x-z-1 < 0:
			break
		if y-z-1 < 0:
			break
		if board[x-z-1][y-z-1] == p2:
			break
		if board[x-z-1][y-z-1] == p:
			check+=1
		else:
			break
	for z in range(4):
		if x+z+1 > 6:
			break
		if y+z+1 > 4:
			break
		if board[x+z+1][y+z+1] == p2:
			break
		if board[x+z+1][y+z+1] == p:
			check+=1
		else:
			break
	return(check)

def angledowncounter(board, x, y, p):
	if p == 1:
		p2 = 2
	else:
		p2 = 1
	check = 0
	for z in range(4):
		if y+z+1 > 4:
			break
		if x-z-1 < 0:
			break
		if board[x-z-1][y+z+1] == p2:
			break
		if board[x-z-1][y+z+1] == p:
			check+=1
		else:
			break
	for z in range(4):
		if x+z+1 > 6:
			break
		if y-z-1 < 0:
			break
		if board[x+z+1][y-z-1] == p2:
			break
		if board[x+z+1][y-z-1] == p:
			check+=1
		else:
			break
	return(check)

def alistar_v1(board):
	choices = []
	for x in range(7):
		z = 0
		y = 0
		while 1 == 1:
			if board[x][y] == 0:
				break
			y+=1
			if y > 5:
				y-=1
				break
		if vertcounter(board, x, y, 2) >= 3:
			z = 1000
		if horizcounter(board, x, y, 2) >= 3:
			z = 1000
		if angleupcounter(board, x, y, 2) >= 3:
			z = 1000
		if angledowncounter(board, x, y, 2) >= 3:
			z = 1000
		if vertcounter(board, x, y, 1) >= 3:
			z = 800
		if horizcounter(board, x, y, 1) >= 3:
			z = 800
		if angleupcounter(board, x, y, 1) >= 3:
			z = 800
		if angledowncounter(board, x, y, 1) >= 3:
			z = 800
		z = z + 2 * vertcounter(board, x, y, 2)
		z = z + 2 * vertcounter(board, x, y, 1)
		z = z + 2 * horizcounter(board, x, y, 2)
		z = z + 2 * horizcounter(board, x, y, 1)
		z = z + 2 * angleupcounter(board, x, y, 2)
		z = z + 2 * angleupcounter(board, x, y, 1)
		z = z + 2 * angledowncounter(board, x, y, 2)
		z = z + 2 * angledowncounter(board, x, y, 1)
		if y >= 5:
			z = -100000
		choices.append(z)
	for x in range(7):
		z = 0
		y = 1
		while 1 == 1:
			if board[x][y] == 0:
				break
			y+=1
			if y > 5:
				y-=1
				break
		if vertcounter(board, x, y, 1) >= 3:
			choices[x] -= 800
		if horizcounter(board, x, y, 1) >= 3:
			choices[x] -= 800
		if angleupcounter(board, x, y, 1) >= 3:
			choices[x] -= 800
		if angledowncounter(board, x, y, 1) >= 3:
			choices[x] -= 800
		choices[x] = choices[x] - vertcounter(board, x, y, 1)
		choices[x] = choices[x] - horizcounter(board, x, y, 1)
		choices[x] = choices[x] - angleupcounter(board, x, y, 1)
		choices[x] = choices[x] - angledowncounter(board, x, y, 1)
	for x in range(7):
		tempboard = [0, 0, 0, 0, 0, 0, 0]
		for z in range(7):
			tempboard[z] = list(board[z])
		tempboard, check = checkturn(x, tempboard, 1)
		if check == False:
			continue
		y = 0
		while 1 == 1:
			if tempboard[x][y] == 0:
				break
			y+=1
			if y > 5:
				y-=1
				break
		if vertcounter(tempboard, x, y, 1) >= 3:
			choices[x] += 800
		if horizcounter(tempboard, x, y, 1) >= 3:
			choices[x] -= 800
		if angleupcounter(tempboard, x, y, 1) >= 3:
			choices[x] -= 800
		if angledowncounter(tempboard, x, y, 1) >= 3:
			choices[x] -= 800
		choices[x] = choices[x] + 2 * (vertcounter(board, x, y, 1))
		choices[x] = choices[x] + 2 * (horizcounter(board, x, y, 1))
		choices[x] = choices[x] + 2 * (angleupcounter(board, x, y, 1))
		choices[x] = choices[x] + 2 * (angledowncounter(board, x, y, 1))
	curchoice = 0
	for x in range(6):
		if choices[x+1] > choices[curchoice]:
			curchoice = x + 1		
	choice = curchoice
	switcher = {
		6: "A",
		5: "B",
		4: "C",
		3: "D",
		2: "E",
		1: "F",
		0: "G"
	}
	collumn = switcher.get(choice, "D")
	return(collumn)

def alistar_v2(board):
	choices = []
	for x in range(7):
		print("thinking...")
		level = 0
		z = 0
		y = 0
		while 1 == 1:
			if board[x][y] == 0:
				break
			y+=1
			if y > 5:
				y-=1
				break
		tempboard = [0, 0, 0, 0, 0, 0, 0]
		for z in range(7):
			tempboard[z] = list(board[z])
		f, z = alistar_recusive(tempboard, x, level, 1000, 1000)
		a = f-z
		choices.append(a)
	choices.append(10000)
	curchoice = 7

	
	for x in range(7):

		g = 0
		while 1 == 1:
			if g > 5:
				break
			if board[x][g] == 0:
				break
			g+=1	
		if choices[x] < choices[curchoice]:

			curchoice = x



	choice = curchoice
	switcher = {
		6: "A",
		5: "B",
		4: "C",
		3: "D",
		2: "E",
		1: "F",
		0: "G"
	}
	collumn = switcher.get(choice, "D")

	return(collumn)

def alistar_recusive(board, x, level, cur_score, cur_opp_score):
	level += 1	
	score = 1000
	opp_score = 1000
	if level > 7:
		return(score, opp_score)
	if level > cur_score and level > cur_opp_score:
		return(score, opp_score)
	board, valid_check = checkturn(x, board, 2)
	if valid_check != False:
		switcher = {
			6: "A",
			5: "B",
			4: "C",
			3: "D",
			2: "E",
			1: "F",
			0: "G"
		}
		collumn = switcher.get(x, "D")
		check = playchecker(board, collumn)
		if check == True:
			score = level
			return(score, opp_score)
		for y in range(7):
			tempboard = [0, 0, 0, 0, 0, 0, 0]
			for z in range(7):
				tempboard[z] = list(board[z])
			tempboard, valid_check = checkturn(y, tempboard, 1)
			if valid_check == False:
				continue
			switcher = {
				6: "A",
				5: "B",
				4: "C",
				3: "D",
				2: "E",
				1: "F",
				0: "G"
			}
			collumn = switcher.get(y, "D")
			check = playchecker(tempboard, collumn)
			if check == True:
				opp_score = level
				return(score, opp_score)
			temp, opp_temp = alistar_recusive(tempboard, y, level, score, opp_score)
			if temp < score:
				score = temp
			if opp_temp < opp_score:
				opp_score = opp_temp
	return(score, opp_score)


game()