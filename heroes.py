def getRerollPercentages(level):
  if level == 1 or level == 2:
    return [1,0,0,0,0]
  elif level == 3:
    return [.75,.25,0,0,0]
  elif level == 4:
    return [.55,.3,.15,0,0]
  elif level == 5:
    return [.45,.33,.20,.2,0]
  elif level == 6:
    return [.25,.40,.30,.05,0]
  elif level == 7:
    return [.19,.30,.35,.15,.01]
  elif level == 8:
    return [.16,.20,.35,.25,.04]
  elif level == 9:
    return [.09,.15,.30,.30,.16]