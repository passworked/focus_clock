import time
from tqdm import tqdm
from colorama import Fore, Style, init

# 初始化 colorama
init()

def pomodoro_timer(focus_minutes, break_minutes):
    def run_timer(minutes, label, color):
        seconds = minutes * 60
        with tqdm(total=seconds, bar_format="{l_bar}{bar}| {desc}") as pbar:
            for second in range(seconds):
                time.sleep(1)
                pbar.update(1)
                percentage = (second + 1) / seconds * 100
                time_display = f"{color}{second // 60:02d}:{second % 60:02d}{Style.RESET_ALL}"
                percent_display = f"{color}{percentage:.2f}%{Style.RESET_ALL}"
                pbar.set_description(f"{label} Time: {time_display}, Percent: {percent_display}")

    while True:
        print(f"{Fore.GREEN}Focus Time!{Style.RESET_ALL}")
        run_timer(focus_minutes, "Focus", Fore.GREEN)
        print(f"{Fore.BLUE}Break Time!{Style.RESET_ALL}")
        run_timer(break_minutes, "Break", Fore.BLUE)

if __name__ == "__main__":
    focus_minutes = int(input("Enter the number of minutes for focus time: "))
    break_minutes = int(input("Enter the number of minutes for break time: "))
    pomodoro_timer(focus_minutes, break_minutes)
