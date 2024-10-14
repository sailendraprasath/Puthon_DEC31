"""Question: If the light is green, go; else stop."""

light_is = input("Enert crt state of signal red or green : ")

if light_is.lower() == "green":
    print(f"now light is {light_is.upper()} you may GO")
else:
    print(f"now light is {light_is.upper()} you must dtop")