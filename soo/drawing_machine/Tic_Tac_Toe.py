import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        # 초기화
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        # 버튼 생성
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                button = tk.Button(root, text='', width=10, height=2, command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

    def on_button_click(self, row, col):
        # 버튼이 클릭되었을 때 호출되는 함수
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("게임 종료", f"{self.current_player} 플레이어가 이겼습니다!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("게임 종료", "무승부입니다!")
                self.reset_game()
            else:
                self.switch_player()

    def switch_player(self):
        # 플레이어 전환
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # 승자 확인
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True  # 가로
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True  # 세로

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True  # 대각선
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True  # 대각선

        return False

    def is_board_full(self):
        # 보드가 모두 채워졌는지 확인
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return False
        return True

    def reset_game(self):
        # 게임 재설정
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text='')
        self.current_player = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()