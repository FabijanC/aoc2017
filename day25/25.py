tape = dict()
pointer = 0
checksum = 0
state = "A"

transition = {
    ("A", 0) : ("B", 1, +1),
    ("A", 1) : ("C", 0, -1),
    ("B", 0) : ("A", 1, -1),
    ("B", 1) : ("D", 1, -1),
    ("C", 0) : ("D", 1, +1),
    ("C", 1) : ("C", 0, +1),
    ("D", 0) : ("B", 0, -1),
    ("D", 1) : ("E", 0, +1),
    ("E", 0) : ("C", 1, +1),
    ("E", 1) : ("F", 1, -1),
    ("F", 0) : ("E", 1, -1),
    ("F", 1) : ("A", 1, +1)
}

for _ in range(12656374):
    if pointer not in tape:
        tape[pointer] = 0
    state, tape[pointer], mv = transition[(state, tape[pointer])]
    pointer += mv

for x in tape:
    if tape[x] == 1:
        checksum += 1
print(checksum)

