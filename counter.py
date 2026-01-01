from pyteal import *

def approval_program():
    counter = Bytes("counter")

    on_create = Seq([
        App.globalPut(counter, Int(0)),
        Return(Int(1))
    ])

    on_increment = Seq([
        App.globalPut(counter, App.globalGet(counter) + Int(1)),
        Return(Int(1))
    ])

    program = Cond(
        [Txn.application_id() == Int(0), on_create],
        [Txn.on_completion() == OnComplete.NoOp, on_increment]
    )

    return program

def clear_program():
    return Return(Int(1))
