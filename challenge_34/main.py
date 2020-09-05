
def draw_board(start_list: list):
    print('\nTic tac toe. \n Pick a position to place your bet.')
    print(f'\n~~~~~~~~~~~~~~~~~')
    print(f'\n|| {start_list[0]} || {start_list[1]} || {start_list[2]} ||')
    print(f'\n~~~~~~~~~~~~~~~~~')
    print(f'\n|| {start_list[3]} || {start_list[4]} || {start_list[5]} ||')
    print(f'\n~~~~~~~~~~~~~~~~~')
    print(f'\n|| {start_list[6]} || {start_list[7]} || {start_list[8]} ||')
    print(f'\n~~~~~~~~~~~~~~~~~')


def get_player_input(player: str, pieces: list):
    play = True
    while play:
        move = int(
            input(f'{player} : Where you would like to place your bet : '))
        if 0 < move < 10:
            if pieces[move - 1] == '_':
                return move
            else:
                print('That spot has already been taken! Try again.')
        else:
            print('That spot doesn\'t exist on the board. Try again. ')


def place_char_on_board(player: str, move: str, pieces: list):
    pieces[move - 1] = player


def is_winner(pieces_on_board: list, player: str):
    # 3 horizontal 3 vertical or 2 vertical
    return ((pieces_on_board[0] == player and pieces_on_board[1] == player and pieces_on_board[2] == player) or
            (pieces_on_board[3] == player and pieces_on_board[4] == player and pieces_on_board[5] == player) or
            (pieces_on_board[6] == player and pieces_on_board[7] == player and pieces_on_board[8] == player) or

            (pieces_on_board[0] == player and pieces_on_board[3] == player and pieces_on_board[6] == player) or
            (pieces_on_board[1] == player and pieces_on_board[4] == player and pieces_on_board[7] == player) or
            (pieces_on_board[2] == player and pieces_on_board[5] == player and pieces_on_board[8] == player) or

            (pieces_on_board[0] == player and pieces_on_board[4] == player and pieces_on_board[8] == player) or
            (pieces_on_board[2] == player and pieces_on_board[4] == player and pieces_on_board[6] == player))


if __name__ == '__main__':
   player_1: str = 'X'
   player_2: str = 'O'
   c_list: list = ['_']*9
   n_list: list = [i for i in range(1, 10)]

   # start game
   print('Board positions')
   draw_board(n_list)
   print('Board\'s current state. ')
   draw_board(c_list)

   while True:
       # get the player move
       move_1 = get_player_input(player_1, c_list)
       # update the list
       place_char_on_board(player_1, move_1, c_list)
       # draw the number board
       draw_board(n_list)
       draw_board(c_list)

       # check if player_1 is winner
       respone_1 = is_winner(c_list, player_1)
       if respone_1:
           print(f'Player {player_1} won.')
           break
       elif "_" not in c_list :
            print("The game was a tie! ")
       
       # get the player move
       move_2 = get_player_input(player_2, c_list)
       # update the list
       place_char_on_board(player_2,move_2,c_list)
       # draw the number board
       draw_board(n_list)
       draw_board(c_list)
       response_2 = is_winner(c_list, player_2)
       if response_2 : 
           print(f'Player {player_2} won. ')
           break
             
