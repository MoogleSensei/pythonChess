def getKnightMoves(pos, chessBoard) :
    column, row = list(pos.strip().lower())
    row = int(row) - 1
    column = alpha_to_index[column]
    i, j = row, column
    solutionMoves = []

    temp = chessBoard[i + 1][j - 2]
    solutionMoves.append([i + 1, j - 2])

    temp = chessBoard[i + 2][j - 1]
    solutionMoves.append([i + 2, j - 1])

    temp = chessBoard[i + 2][j + 1]
    solutionMoves.append([i + 2, j + 1])

    temp = chessBoard[i + 1][j + 2]
    solutionMoves.append([i + 1, j + 2])

    temp = chessBoard[i - 1][j + 2]
    solutionMoves.append([i - 1, j + 2])

    temp = chessBoard[i - 2][j + 1]
    solutionMoves.append([i - 2, j + 1])

    temp = chessBoard[i - 2][j - 1]
    solutionMoves.append([i - 2, j - 1])

    temp = chessBoard[i - 1][j - 2]
    solutionMoves.append([i - 1, j - 2])

    temp = [i for i in solutionMoves if i[0] >=0 and i[1] >=0]
    allPossibleMoves = ["".join([index_to_alpha[i[1]], str(i[0] + 1)]) for i in temp]
    allPossibleMoves.sort()
    return allPossibleMoves

def getRookMoves(pos, chessBoard) :
	column, row = list(pos.strip().lower())
	row = int(row) - 1
	column = alpha_to_index[column]
	solutionMoves = []

	for j in range(8) :
		if j != column :
			solutionMoves.append((row, j))

	for i in range(8) :
		if i != row :
			solutionMoves.append((i, column))

	solutionMoves = ["".join([index_to_alpha[i[1]], str(i[0] + 1)]) for i in solutionMoves]
	solutionMoves.sort()
	return solutionMoves

def getBishopMoves(pos, chessBoard) :
	column, row = list(pos.strip().lower())
	row = int(row) - 1
	column = alpha_to_index[column]
	solutionMoves = []

	for i in range(1, 8) :
		if 8 > row + i and row + i >= 0 and 8 > column + i and column + i >= 0 :
			solutionMoves.append((row + i, column + i))
		if 8 > row + i and row + i >= 0 and 8 > column - i and column - i >= 0 :
			solutionMoves.append((row + i, column - i))
		if 8 > row - i and row - i >= 0 and 8 > column + i and column + i >= 0 :
			solutionMoves.append((row - i, column + i))
		if 8 > row - i and row - i >= 0 and 8 > column - i and column - i >= 0 :
			solutionMoves.append((row - i, column - i))
	
	solutionMoves = ["".join([index_to_alpha[i[1]], str(i[0] + 1)]) for i in solutionMoves]
	solutionMoves.sort()
	return solutionMoves

def getQueenMoves(pos, chessBoard) :
	rookMoves = getRookMoves(pos, chessBoard)
	bishopMoves = getBishopMoves(pos, chessBoard)

	solutionMoves = rookMoves + bishopMoves
	solutionMoves.sort()
	return solutionMoves

def getKingMoves(pos, chessBoard) : 
	column, row = list(pos.strip().lower())
	row = int(row) - 1
	column = alpha_to_index[column]
	solutionMoves = []

	if 8 > row + 1 :
		solutionMoves.append((row + 1, column))
	if row - 1 >= 0 :
		solutionMoves.append((row - 1, column))
	if 8 > column + 1 :
		solutionMoves.append((row, column + 1))
	if column - 1 >= 0 :
		solutionMoves.append((row, column - 1))
	if 8 > row + 1 and 8 > column + 1 :
		solutionMoves.append((row + 1, column + 1))
	if 8 > row + 1 and column - 1 >= 0 :
		solutionMoves.append((row + 1, column - 1))
	if row - 1 >= 0 and 8 > column + 1 :
		solutionMoves.append((row - 1, column + 1))
	if row - 1 >= 0 and column - 1 >= 0 :
		solutionMoves.append((row - 1, column - 1))
	
	solutionMoves = ["".join([index_to_alpha[i[1]], str(i[0] + 1)]) for i in solutionMoves]
	solutionMoves.sort()
	return solutionMoves

chessBoard = [[1] * 8 for i in range(8)]

alpha_to_index = {
	"a" : 0,
	"b" : 1,
	"c" : 2,
	"d" : 3,
	"e" : 4,
	"f" : 5,
	"g" : 6,
	"h" : 7,
}
index_to_alpha = {
	0 : "a",
	1 : "b",
	2 : "c",
	3 : "d",
	4 : "e",
	5 : "f",
	6 : "g",
	7 : "h",
}

print(getKnightMoves("d4",chessBoard))
print(getRookMoves("d4",chessBoard))
print(getBishopMoves("d4",chessBoard))
print(getQueenMoves("d4",chessBoard))
print(getKingMoves("d4",chessBoard))
