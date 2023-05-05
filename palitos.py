import math

INF = 1000000
DEPTH_MAX = 10
MIN_NUM_STICKS = 1
MAX_NUM_STICKS = 3
num_sticks = 13

def minimax(player, depth, num_sticks):
    if depth == DEPTH_MAX or num_sticks == 0:
        return 0
    val = -INF
    for i in range(MIN_NUM_STICKS, min(MAX_NUM_STICKS+1, num_sticks+1)):
        num_sticks -= i
        tempval = -minimax(1-player, depth+1, num_sticks)
        num_sticks += i
        val = max(val, tempval)
    return val + 2*player - 1

def tras_juega():
    global num_sticks
    val = -INF
    n = 0
    for i in range(MIN_NUM_STICKS, min(MAX_NUM_STICKS+1, num_sticks+1)):
        num_sticks -= i
        tempval = -minimax(1, 1, num_sticks)
        num_sticks += i
        if tempval > val:
            val = tempval
            n = i
    num_sticks -= n
    print(f"La computadora tomó {n} palitos.")

num_sticks = int(input("Ingrese el número inicial de palitos: "))
while num_sticks > 0:
    print(f"Quedan {num_sticks} palitos.")
    player_choice = int(input("¿Cuántos palitos quieres tomar?  de 1 a 3"))
    while player_choice < MIN_NUM_STICKS or player_choice > min(MAX_NUM_STICKS, num_sticks):
        player_choice = int(input("Esa no es una cantidad válida. ¿Cuántos palitos quieres tomar? "))
    num_sticks -= player_choice
    if num_sticks == 0:
        print("¡Has ganado!")
        break
    tras_juega()
    if num_sticks == 0:
        print("¡La computadora ha ganado!")
        break
