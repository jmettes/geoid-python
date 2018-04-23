from IPython.core.display import HTML


def test(cond1, cond2):
    if cond1 == cond2:
        return HTML("<span style='background-color: green; color: white; padding: 0.25em 1em;'>Passed</span>")
    else:
        if type(cond1) == list:
            for m,t in zip(cond1, cond2):
                if m != t:
                    print(m)
                    print(t)
                    print()
        else:
            print(cond1)
            print(cond2)
        return HTML("<span style='background-color: red; color: white; padding: 0.25em 1em;'>Failed</span>")

