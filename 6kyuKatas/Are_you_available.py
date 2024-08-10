"""Dan, president of a Large company could use your help. He wants to implement a system that will switch all his
devices into offline mode depending on his meeting schedule. When he's at a meeting and somebody texts him,
he wants to send an automatic message informing that he's currently unavailable and the time when he's going to be back.

What To Do

Your task is to write a helper function checkAvailability that will take 2 arguments:

schedule, which is going to be a nested array with Dan's schedule for a given day. Inside arrays will consist of 2
elements - start and finish time of a given appointment,
currentTime - is a string with specific time in hh:mm 24-h format for which the function will check availability
based on the schedule.
If no appointments are scheduled for currentTime, the function should return true. If there are no appointments for the day, the output should also be true
If Dan is in the middle of an appointment at currentTime, the function should return a string with the time he's going to be available.
"""


def split_on_hours_minutes(_str):
    return _str.split(":")


def check_availability(schedule, current_time):
    for i in schedule:
        meet_start = i[0]
        meet_end = i[1]

        start_h, start_m = split_on_hours_minutes(meet_start)
        end_h, end_m = split_on_hours_minutes(meet_end)

        cur_time_h, cur_time_m = split_on_hours_minutes(current_time)

        if start_h > cur_time_h or end_h < cur_time_h:
            return True
        if start_h == cur_time_h and end_m < cur_time_m:
            return True
        return meet_end


if __name__ == "__main__":
    print(check_availability([["09:30", "10:15"], ["12:20", "15:50"]], "10:00"))

    assert check_availability([["09:30", "10:15"], ["12:20", "15:50"]], "11:00") == True

    assert check_availability([["09:30", "10:15"], ["12:20", "15:50"]], "10:00") == "10:15"

    assert check_availability([["09:30", "10:15"], ["12:20", "15:50"]], "15:50") == True

    print("ALL test passed!")
