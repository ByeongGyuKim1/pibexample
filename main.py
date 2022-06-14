import typer

app = typer.Typer()

def pib_list(n: int) -> list:
    result = [0, 1]
    for i in range(n):
        result.append(result[i] + result[i+1])
    return result

@app.command()
def pib(name: str, n: int, agg: bool = False):
    piblist = pib_list(n)
    if agg:
        for line in range(n):
            for i in range(1, line+2):
                print(piblist[i], end=' ')
            print(" ")
    else:
        for line in range(1, n+1):
            print(piblist[line], end=' ')
        print("")

if __name__ == "__main__":
    app()