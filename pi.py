text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

pypi= list(map(len,text.replace(',','').replace('.','').split()));print(pypi)
answer=""
for i in pypi:
    answer += str(i)

print(answer)