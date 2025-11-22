import time

sessions = []
start = 0

while True:
    print("\n--- Study Time Tracker ---")
    print("1. Start Session")
    print("2. Stop Session")
    print("3. Show Report")
    print("4. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        start = time.time()
        print("Session Started")

    elif ch == "2":
        if start == 0:
            print("You did not start any session")
        else:
            end = time.time()
            dur = end - start
            sessions.append(dur)
            print("Session Time:", round(dur, 2), "seconds")
            start = 0

    elif ch == "3":
        if len(sessions) == 0:
            print("No session recorded")
        else:
            total = 0
            print("All Study Sessions:")
            for i in range(len(sessions)):
                print("Session", i+1, ":", round(sessions[i], 2), "seconds")
                total = total + sessions[i]
            print("Total Study Time:", round(total, 2), "seconds")

    elif ch == "4":
        f = open("study_report.txt", "w")
        t = 0
        f.write("Study Time Tracker Report\n")
        for i in range(len(sessions)):
            f.write("Session " + str(i+1) + ": " + str(round(sessions[i], 2)) + " seconds\n")
            t = t + sessions[i]
        f.write("Total Study Time: " + str(round(t, 2)) + " seconds\n")
        f.close()
        print("Report Saved. Exiting...")
        break

    else:
        print("Wrong Choice")
