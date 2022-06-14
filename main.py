import typer

app = typer.Typer()

def pib_list(n: int) -> list:
    result = [0, 1]
    for i in range(n):
        result.append(result[i] + result[i+1])
    return result

@app.command()
def pib(name: str, n: int = typer.Argument(..., min = 1), agg: bool = False):
    piblist = pib_list(n)
    piblist_str = [str(a) for a in piblist]
    if agg:
        for line in range(n):
            piblist_ans = ' '.join(piblist_str[1:line+2])
            print(piblist_ans)

    else:
        piblist_ans = ' '.join(piblist_str[1:n+1])
        print(piblist_ans)

if __name__ == "__main__":
    app()