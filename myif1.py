def print_cat():
    cat = [
        " /\\_/\\  ",
        "( o.o ) ",
        " > ^ <  "
    ]
    print_ascii_art(cat)

def print_dog():
    dog = [
        " / \\__",
        "(    @\\___",
        " /         O",
        "/   (_____/ ",
        "/_____/   U"
    ]
    print_ascii_art(dog)

def print_rabbit():
    rabbit = [
        "  (\\_/)",
        "  (o o)",
        "  ( > )"
    ]
    print_ascii_art(rabbit)

def print_ascii_art(animal_art):
    for line in animal_art:
        print(line)

def show_menu():
    print("그림 출력 프로그램")
    print("=====================")
    print("1. 고양이")
    print("2. 강아지")
    print("3. 토끼")
    print("0. 종료")
    print("=====================")

def get_user_choice():
    while True:
        try:
            return int(input("선택(0을 입력하면 종료): "))
        except ValueError:
            print("숫자를 입력해주세요.")

def handle_choice(choice):
    if choice == 1:
        print("[고양이]")
        print_cat()
    elif choice == 2:
        print("[강아지]")
        print_dog()
    elif choice == 3:
        print("[토끼]")
        print_rabbit()
    elif choice == 0:
        print("프로그램을 종료합니다.")
        return False
    else:
        print("잘못된 입력입니다. 0~3 사이 숫자를 입력하세요.")
    return True

def select_mode():
    print("실행 모드를 선택하세요:")
    print("1. 5번만 반복")
    print("2. 무한 반복")
    while True:
        try:
            mode = int(input("선택 (1 또는 2): "))
            if mode in [1, 2]:
                return mode
            else:
                print("1 또는 2만 입력 가능합니다.")
        except ValueError:
            print("숫자를 입력해주세요.")

def main():
    mode = select_mode()
    if mode == 1:
        for i in range(5):
            show_menu()
            choice = get_user_choice()
            if not handle_choice(choice):
                break
    else:
        while True:
            show_menu()
            choice = get_user_choice()
            if not handle_choice(choice):
                break
    print("5번 선택이 끝났습니다. 프로그램을 종료합니다")

    # 실행
if __name__ == "__main__":
    main()