import typer

app = typer.Typer()

@app.command()
def pib(n: int, agg: bool = False):
    f1 = 0
    f2 = 1
    f3 = 1
    temp = f2
    answer = "1"
    if agg:  # agg 일 시 모든 결과 출력
        for j in range(n):
            answer = "1"
            f1 = 0
            f2 = 1
            f3 = 1
            for i in range(j):
                temp = f2
                f3 = f1 + f2
                answer = answer + " " + str(f3)
                f2 = f3
                f1 = temp
            typer.echo(f"{answer}")

    else:  # 기본값
        for i in range(n - 1):
            temp = f2
            f3 = f1 + f2
            answer = answer + " " + str(f3)
            f2 = f3
            f1 = temp
        typer.echo(f"{answer}")

@app.command()
def n2():
    typer.echo(f"hello")


if __name__ == "__main__":
    app()