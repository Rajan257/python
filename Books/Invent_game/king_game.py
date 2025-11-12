

import chess
import chess.pgn
import random
import sys
from datetime import datetime

def print_board(board):
    # ascii board with ranks 8..1 on top to match conventional view
    print(board)  # python-chess prints a nice ASCII board
    print(f"Turn: {'White' if board.turn else 'Black'}")

def ask_mode():
    print("Select mode:")
    print("1) Human vs Human")
    print("2) Human vs AI (random moves)")
    choice = input("Choice (1/2): ").strip()
    return choice == '2'

def parse_move(user_input, board):
    user_input = user_input.strip()
    # Try SAN (algebraic) first
    try:
        move = board.parse_san(user_input)
        return move
    except Exception:
        pass
    # Try UCI
    try:
        move = chess.Move.from_uci(user_input)
        if move in board.legal_moves:
            return move
    except Exception:
        pass
    return None

def random_ai_move(board):
    moves = list(board.legal_moves)
    if not moves:
        return None
    return random.choice(moves)

def play_game(vs_ai=False):
    board = chess.Board()
    game = chess.pgn.Game()
    node = game

    print("Starting a new game. Moves: algebraic (e4) or UCI (e2e4). Type 'resign' to resign or 'draw' to offer draw.")
    while True:
        print_board(board)

        if board.is_checkmate():
            print("Checkmate!")
            break
        if board.is_stalemate():
            print("Stalemate!")
            break
        if board.is_insufficient_material():
            print("Draw — insufficient material.")
            break
        if board.can_claim_fifty_moves():
            print("Draw — fifty-move rule possible.")
            break
        if board.can_claim_threefold_repetition():
            print("Draw — threefold repetition possible.")
            break

        if vs_ai and not board.turn:  # black is AI (set AI to play black)
            print("[AI is thinking...]")
            move = random_ai_move(board)
            if move is None:
                print("No legal moves for AI.")
                break
            print(f"AI plays: {board.san(move)} ({move.uci()})")
            board.push(move)
            node = node.add_variation(move)
            continue

        # Human move
        prompt = "White move: " if board.turn else "Black move: "
        user_input = input(prompt).strip()
        if user_input.lower() in ('quit', 'exit'):
            print("Exiting game.")
            return
        if user_input.lower() == 'resign':
            print(f"{'White' if not board.turn else 'Black'} wins by resignation.")
            break
        if user_input.lower() == 'draw':
            print("Draw offered. Accept? (y/n)")
            ans = input().strip().lower()
            if ans == 'y':
                print("Draw agreed.")
                break
            else:
                print("Draw declined. Continue.")
                continue

        move = parse_move(user_input, board)
        if move is None:
            print("Invalid move. Use algebraic like 'Nf3' or UCI like 'g1f3'. Try again.")
            continue

        board.push(move)
        node = node.add_variation(move)

    # Game over — print result and save PGN
    result = board.result()
    print("Final board:")
    print_board(board)
    print("Result:", result)

    # Fill game headers
    game.headers["Event"] = "Local Game"
    game.headers["Date"] = datetime.now().strftime("%Y.%m.%d")
    game.headers["Result"] = result

    pgn_text = str(game)
    filename = f"game_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pgn"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(pgn_text)
        print(f"Saved PGN to {filename}")
    except Exception as e:
        print("Could not save PGN:", e)

def main():
    print("=== Console Chess (python-chess) ===")
    vs_ai = ask_mode()
    # if vs_ai True, human plays White and AI plays Black
    play_game(vs_ai=vs_ai)
    print("Thanks for playing.")

if __name__ == "__main__":
    main()
