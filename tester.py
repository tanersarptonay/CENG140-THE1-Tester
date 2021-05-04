"""
You may need to change the paths on the 17th, 20th, 23rd, 25th and 39th lines according to your path
"""
import os

length = input("Which cases do you want to test? [short/long]\n")
print("Testing...\n")

if length == "short":
    passed_cases = 630
    all_cases = 630
else:
    passed_cases = 1000
    all_cases = 1000

for i in range(all_cases):
    with open(f"results_{length}/result{i}.txt", "r") as result_file:
        result = float(result_file.read()[:-1])

    with open(f"cases_{length}/case{i}.txt", "r") as case_file:
        case = case_file.read()

    os.system(f"cat cases_{length}/case{i}.txt | ./the1 > output.txt")

    with open("output.txt", "r") as output_file:
        given_output = float(output_file.read())

    delta_time = float(case[:case.find("\n")])

    if abs(given_output - result) <= delta_time:
        pass

    else:
        passed_cases -= 1
        print(f"CASE {i} WRONG")

percentage = passed_cases * 100 / all_cases
print(f"Evaluation has finished.\nProposed Grade: %{percentage}")
os.system("rm -f output.txt")
os.system(f"notify-send 'THE1 Tester' 'Proposed Grade: %{percentage}'")
