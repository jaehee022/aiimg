from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt

console = Console()

def print_cat():
    cat = [
        " /\\_/\\  ",
        "( o.o ) ",
        " > ^ <  "
    ]
    print_ascii_art(cat, title="고양이 🐱")

def print_dog():
    dog = [
        " / \\__",
        "(    @\\___",
        " /         O",
        "/   (_____/ ",
        "/_____/   U"
    ]
    print_ascii_art(dog, title="강아지 🐶")

def print_rabbit():
    rabbit = [
        "  (\\_/)",
        "  (o o)",
        "  ( > )"
    ]
    print_ascii_art(rabbit, title="토끼 🐰")

def print_ascii_art(animal_art, title=""):
    art = "\n".join(animal_art)
    panel = Panel(art, title=title, title_align="left", border_style="bright_magenta")
    console.print(panel)

def show_menu():
    console.rule("[bold blue]🎨 그림 출력 프로그램 🎨[/bold blue]")
    console.print("[cyan]1.[/cyan] 🐱 고양이")
    console.print("[cyan]2.[/cyan] 🐶 강아지")
    console.print("[cyan]3.[/cyan] 🐰 토끼")
    console.print("[cyan]0.[/cyan] ❌ 종료")
    console.rule()

def get_user_choice():
    while True:
        try:
            return IntPrompt.ask("[green]선택 (0을 입력하면 종료)[/green]")
        except ValueError:
            console.print("[red]숫자를 입력해주세요.[/red]")

def handle_choice(choice):
    if choice == 1:
        print_cat()
    elif choice == 2:
        print_dog()
    elif choice == 3:
        print_rabbit()
    elif choice == 0:
        console.print("[bold red]👋 프로그램을 종료합니다.[/bold red]")
        return False
    else:
        console.print("[red]잘못된 입력입니다. 0~3 사이 숫자를 입력하세요.[/red]")
    return True

def select_mode():
    console.print("[bold yellow]⚙ 실행 모드를 선택하세요:[/bold yellow]")
    console.print("1. 🔁 5번만 반복")
    console.print("2. ♾️ 무한 반복")
    while True:
        try:
            mode = IntPrompt.ask("선택 (1 또는 2)")
            if mode in [1, 2]:
                return mode
            else:
                console.print("[red]1 또는 2만 입력 가능합니다.[/red]")
        except ValueError:
            console.print("[red]숫자를 입력해주세요.[/red]")

def main():
    mode = select_mode()
    if mode == 1:
        for _ in range(5):
            show_menu()
            choice = get_user_choice()
            if not handle_choice(choice):
                break
        console.print("[bold green]✅ 5번 선택이 끝났습니다. 프로그램을 종료합니다.[/bold green]")
    else:
        while True:
            show_menu()
            choice = get_user_choice()
            if not handle_choice(choice):
                break

# 실행
if __name__ == "__main__":
    main()
