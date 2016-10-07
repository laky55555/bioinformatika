states = ('postena', 'nepostena')

observations = ('1', '2', '3', '4', '5', '5', '6', '6', '6', '6', '6', '6', '1', '2', '3', '4', '5', '2')
 
start_probability = {'postena': 1, 'nepostena': 1}
 
transition_probability = {
   'postena' : {'postena': 0.9, 'nepostena': 0.1},
   'nepostena' : {'postena': 0.2, 'nepostena': 0.8}
   }
 
emission_probability = {
   'postena' : {'1':0.166, '2':0.166, '3':0.166, '4':0.166, '5':0.166, '6':0.166},
   'nepostena' : {'1':0.1, '2':0.1, '3':0.1, '4':0.1, '5':0.1, '6':0.5}
   }



def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}
 
    # Initialize base cases (t == 0)
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]
 
    # alternative Python 2.7+ initialization syntax
    # V = [{y:(start_p[y] * emit_p[y][obs[0]]) for y in states}]
    # path = {y:[y] for y in states}
 
    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}
 
        for y in states:
            (prob, state) = max((V[t-1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]
 
        # Don't need to remember the old paths
        path = newpath
 
    

    print_dptable(V)
    (prob, state) = max((V[t][y], y) for y in states)
    return (prob, path[state])
 
# Don't study this, it just prints a table of the steps.
def print_dptable(V):
    s = "    " + " ".join(("%7d" % i) for i in range(len(V))) + "\n"
    for y in V[0]:
        s += "%.5s: " % y
        s += " ".join("%.7s" % ("%f" % v[y]) for v in V)
        s += "\n"
    print(s)


def example():
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)
print(example())

