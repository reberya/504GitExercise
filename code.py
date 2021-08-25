def function1(a):
    b = dict()
    for c in sequence:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    return b

def function2(sequence):
    print('freqs')
    total = float(sum(sequence[b] for b in sequence.keys()]))
    for b in sequence.keys():
        print(b + ':' + str(sequence[b]/total))

function2(function1('ATCTGACGCGCGCCGC'))
