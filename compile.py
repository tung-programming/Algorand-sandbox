from pyteal import *
from counter import approval_program, clear_program

if __name__ == "__main__":
    with open("approval.teal", "w") as f:
        f.write(compileTeal(approval_program(), Mode.Application, version=8))

    with open("clear.teal", "w") as f:
        f.write(compileTeal(clear_program(), Mode.Application, version=8))
