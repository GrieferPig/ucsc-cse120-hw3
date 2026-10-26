import pyrtl

def datapath(zero, lt, opcode):
    # TODO: implement logic to assign branch below using the specification in Q4.a)
    # For example: branch = zero & lt ~opcode
    branch = pyrtl.mux(opcode, lt, ~lt, zero, ~zero)
    return branch

if __name__ == "__main__":
    zero = pyrtl.Input(1, "zero")
    lt = pyrtl.Input(1, "lt")
    opcode = pyrtl.Input(2, "opcode")

    branch_out = datapath(zero, lt, opcode)

    branch = pyrtl.Output(1, "branch")
    branch <<= branch_out

    sim = pyrtl.Simulation()

    # Example test case below, this should PASS
    try:
        sim.step({"zero" : 0, "lt" : 1, "opcode": 0})
        assert sim.inspect("branch") == 1
        print("Test PASS")
    except:
        print("Test FAIL")
    
    # TODO: write test cases here
    for op in range(4):
        for z in range(2):
            for l in range(2):
                expected = (l, 1 - l, z, 1 - z)[op]
                sim.step({"zero": z, "lt": l, "opcode": op})
                assert sim.inspect("branch") == expected, (op, z, l)
    print("Test PASS")
