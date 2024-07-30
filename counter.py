def countDayOfTheWeek():
    # This first line is provided for you
    file_name = input("Enter a file name: ")

    fh = open(file_name)

    lines = fh.readlines()

    weekday = dict()

    for line in lines:
        if line.startswith("From "):
            words = line.split()
            if len(words) > 3:
                dow = words[2]
                if dow not in weekday:
                    weekday[dow] = 1
                else:
                    weekday[dow] += 1

    print(weekday)

            



## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
