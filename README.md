# Pawns-Gaming-Algorithm

PersonA is playing checkers with his friend PersonB. Checkers is a board game in which both players take tums to move their pawns. PersonA has just one pawn left, and he is going to take a final turn, beating as many of PersonB's pawns as possible. 

Pawns in checkers move diagonally. The pawn always moves one step in the up-right or up-left direction. If PersonA's pawn moves and its target field is occupied by one of PersonB's pawns, PersonB's pawn can be beaten: PersonA's pawn leaps over PersonB's pawn. taking two steps In the chosen direction and removing PersonB's pawn from the board. PersonA can beat PersonB's pawn in this way only when the field beyond PersonB's pawn is empty. 

After beating PersonB's pawn. PersonA can continue his turn and make another move, but only if he will again beat another one of PersonB's pawns Of course. after this additional move, PersonA can continue his turn again by beating another of PersonB's pawns, and so on for as long as there are further pawns to beat. When it is no longer possible to beat one of PersonB's pawns, PersonA's turn ends 
The maximum number of pawns owned by PersonB that PersonA can beat in his turn

This is the algorithm which, gives a square board of N x N size describing PersonB and PersonA pawns, returns the maximum number of pawns personA can beat in one turn. If none of personB’s pawns can be beaten, the algorithm should return 0.
Person’s pawn is describing by the ‘O’ character, PersonB’s pawns by ‘X’ character and empty fields by ‘.’(dots). The board is describing from top to bottom and from the left to right.

For example, given,
B[0] = “..X…”
B[1] = “……”
B[2] = “….x.”
B[3] = “.X.…”
B[4] = “..X.X.”
B[5] = “…O..”

The function returns 2

Given input
B[0] = “X….”
B[1] = ”.X…”
B[2] = “..O..”
B[3] = “…X.”
B[4] = “…..”

This functions returns 0.
 



