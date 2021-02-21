import conducto as co
def main() -> co.Serial:
    with co.Serial(image=co.Image(copy_repo=True)) as node:
        node["hello"] = co.Exec("ls")
    return node
co.main(default=main)
