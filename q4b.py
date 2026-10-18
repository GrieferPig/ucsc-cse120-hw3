import pyrtl

if __name__ == "__main__":
    enable = pyrtl.Input(1, "enable")
    reset = pyrtl.Input(1, "reset")
    y = pyrtl.Register(2, "y")

    # TODO: define y.next logic below
    # y.next <<=

    trace = pyrtl.SimulationTrace()
    sim = pyrtl.Simulation(tracer=trace)
    sim.step({"reset" : 1, "enable": 0})
    
    # TODO: write more test cases here
    
    trace.render_trace()