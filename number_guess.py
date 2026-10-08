"""숫자 맞추기 게임

컴퓨터가 고른 숫자를 맞혀 보세요. 매 시도마다 '업' 또는 '다운' 힌트를 줍니다.
"""

import random

DIFFICULTIES = {
    "1": ("쉬움", 1, 50, 10),
    "2": ("보통", 1, 100, 7),
    "3": ("어려움", 1, 500, 9),
}


def choose_difficulty():
    print("\n난이도를 선택하세요:")
    for key, (name, low, high, tries) in DIFFICULTIES.items():
        print(f"  {key}. {name} ({low}~{high}, 기회 {tries}번)")
    while True:
        choice = input("선택 (1/2/3): ").strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("1, 2, 3 중에서 골라 주세요.")


def read_guess(low, high):
    while True:
        text = input(f"{low}~{high} 사이의 숫자를 입력하세요: ").strip()
        try:
            guess = int(text)
        except ValueError:
            print("숫자만 입력해 주세요.")
            continue
        if low <= guess <= high:
            return guess
        print(f"{low}부터 {high} 사이의 숫자여야 합니다.")


def play_round():
    name, low, high, max_tries = choose_difficulty()
    answer = random.randint(low, high)
    print(f"\n[{name}] {low}부터 {high} 사이의 숫자를 하나 골랐어요. 기회는 {max_tries}번!")

    for attempt in range(1, max_tries + 1):
        guess = read_guess(low, high)
        if guess == answer:
            print(f"정답입니다! {attempt}번 만에 맞혔어요.")
            return attempt
        hint = "업! (더 큰 수)" if guess < answer else "다운! (더 작은 수)"
        remaining = max_tries - attempt
        print(f"{hint}  남은 기회: {remaining}번")

    print(f"아쉽네요. 기회를 모두 썼어요. (정답: {answer})")
    return None


def main():
    print("=== 숫자 맞추기 게임 ===")
    best = None
    while True:
        result = play_round()
        if result is not None and (best is None or result < best):
            best = result
            print(f"새 최고 기록: {best}번!")
        again = input("\n다시 하시겠어요? (y/n): ").strip().lower()
        if again != "y":
            break
    print("게임을 종료합니다. 고마워요!")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n게임을 종료합니다.")
