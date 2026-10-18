import pyrtl

def datapath(zero, lt, opcode):
    #TODO: implement logic to assign branch below using the specification in Q4.a)
    # For example: branch = zero & lt ~opcode  
    return branch

if __name__ == "__main__":
    zero = pyrtl.Input(1, "zero")
    lt = pyrtl.Input(1, "lt")
    opcode = pyrtl.Input(2, "opcode")

    branch_out = datapath(zero, lt, opcode)

    branch = pyrtl.Output(1, "branch")
    branch <<= branch_out

    sim = pyrtl.Simulation()
    # TODO: write test cases here