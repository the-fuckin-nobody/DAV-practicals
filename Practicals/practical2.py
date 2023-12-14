'''
Given below is a dictionary having two keys ‘Boys’ and ‘Girls’ and having two lists of heights of five Boys and
Five Girls respectively as values associated with these keys
Original dictionary of lists:
{'Boys': [72, 68, 70, 69, 74], 'Girls': [63, 65, 69, 62, 61]}
From the given dictionary of lists create the following list of dictionaries:
[{'Boys': 72, 'Girls': 63}, {'Boys': 68, 'Girls': 65}, {'Boys': 70, 'Girls': 69}, {'Boys': 69, 'Girls': 62}, {‘Boys’:74,
‘Girls’:61]
'''
def ques1(d1: dict) -> None:
    result = []
    keys = list(d1.keys())
    for i in range (len(d1[keys[0]])):
        result.append({keys[0]: d1[keys[0]][i], keys[1]: d1[keys[1]][i]})
    print(result)
    return None

def main() -> None:
    d1 = {"Boys": [72, 68, 70, 69, 74], "Girls": [63, 65, 69, 62, 61]}
    ques1(d1)

if __name__ == "__main__":
    main()
