# Install: pip install pyrtl
# Run:     python example.py

import pyrtl

# ---- 1. Gates and wires ----
# Inputs come in, Outputs go out. <<= means "connect".
pyrtl.reset_working_block()

a = pyrtl.Input(1, "a")
b = pyrtl.Input(1, "b")
out = pyrtl.Output(1, "out")

out <<= a & b          # AND gate   (also: | for OR, ^ for XOR, ~ for NOT)

sim = pyrtl.Simulation()
sim.step({"a": 1, "b": 1})
print("1 AND 1 =", sim.inspect("out"))   # 1
sim.step({"a": 1, "b": 0})
print("1 AND 0 =", sim.inspect("out"))   # 0


# ---- 2. Mux (pick one of two) ----
# select(s, x, y) gives x when s is 1, y when s is 0.
pyrtl.reset_working_block()

s = pyrtl.Input(1, "s")
x = pyrtl.Input(4, "x")
y = pyrtl.Input(4, "y")
out = pyrtl.Output(4, "out")

out <<= pyrtl.mux(s, x, y)

sim = pyrtl.Simulation()
sim.step({"s": 1, "x": 7, "y": 3})
print("s=1 picks x:", sim.inspect("out"))   # 7
sim.step({"s": 0, "x": 7, "y": 3})
print("s=0 picks y:", sim.inspect("out"))   # 3


# ---- 3. Register (remembers a value) ----
# A counter: each clock tick, count goes up by 1.
pyrtl.reset_working_block()

count = pyrtl.Register(4, "count")   # starts at 0
count.next <<= count + 1             # value for the NEXT tick

out = pyrtl.Output(4, "out")
out <<= count

sim = pyrtl.Simulation()
for tick in range(5):
    sim.step({})                     # one clock tick (no inputs)
    print("tick", tick, "count =", sim.inspect("out"))   # 0,1,2,3,4


# ---- 4. See it as a waveform ----
pyrtl.reset_working_block()

count = pyrtl.Register(4, "count")
count.next <<= count + 1
out = pyrtl.Output(4, "out")
out <<= count

trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=trace)
for tick in range(5):
    sim.step({})
trace.render_trace()                 # draws the signals in the terminal


# ---- 5. Test it ----
# A test = run the circuit and check the answer is what you expect.
pyrtl.reset_working_block()

a = pyrtl.Input(1, "a")
b = pyrtl.Input(1, "b")
out = pyrtl.Output(1, "out")
out <<= a & b

sim = pyrtl.Simulation()
for va in [0, 1]:
    for vb in [0, 1]:
        sim.step({"a": va, "b": vb})
        assert sim.inspect("out") == (va and vb), "AND gate is wrong!"

print("All tests passed!")