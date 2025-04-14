# 기본 텍스트 출력
from rich import print

print("[bold magenta]Hello[/bold magenta] [green]World![/green] :sparkles:")
# console 사용해서 출력
from rich.console import Console
# 테이
console = Console()
console.print("Hello, [bold blue]Rich[/bold blue]!", style="italic")

from rich.table import Table
from rich.console import Console

console = Console()
table = Table(title="학생 목록")

table.add_column("이름", style="cyan", no_wrap=True)
table.add_column("나이", style="magenta")
table.add_column("전공", justify="right", style="green")

table.add_row("지민", "21", "연극영화")
table.add_row("서연", "22", "디자인")
table.add_row("윤호", "20", "컴퓨터공학")

console.print(table)
# 코드블록
from rich.console import Console
from rich.syntax import Syntax

console = Console()
code = '''def hello():
    print("Hello, world!")'''

syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)
# 마크다운운
from rich.console import Console
from rich.markdown import Markdown

md = Markdown("# 제목\n\n**굵은 글씨**와 _이탤릭체_도 가능해요!")
console = Console()
console.print(md)


