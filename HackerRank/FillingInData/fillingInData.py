# A time series of daily readings of mercury levels in a river is provided 
# to you. In each test case, the day's highest level is missing for certain 
# days. By analyzing the data, try to identify the missing mercury levels for 
# those days. Each row of data contains two tab-separated values: a time-stamp 
# and the day's highest reading.
#
# There are exactly twenty rows marked missing in each input file. The missing 
# values are marked as "Missing_1", "Missing_2", .... "Missing_20". These missing 
# records have been randomly dispersed in the rows of data.
#
# Complete the calcMissing function in the editor below. It should print 20 rows, 
# one for each missing value, as floats.
#
# Constraints: Mercury levels are all < 400.
# The first line contains an integer n, the number of rows of data to follow.
# Each of the next n lines contains a string of data in the format described.

def calcMissing(readings):
    n = len(readings)

    vals = []              # float or None
    missing_pos = {}       # k -> index of Missing_k

    for i, row in enumerate(readings):
        # each row: "date time<TAB>value"
        parts = row.strip().split()
        val_str = parts[-1]

        if val_str.startswith("Missing_"):
            vals.append(None)
            k = int(val_str.split("_")[1])  # Missing_1 -> 1
            missing_pos[k] = i
        else:
            vals.append(float(val_str))

    # fill missing values by linear interpolation
    i = 0
    while i < n:
        if vals[i] is not None:
            i += 1
            continue

        start = i
        while i < n and vals[i] is None:
            i += 1
        end = i - 1

        left = start - 1       # index of known value before block
        right = i              # index of known value after block

        if left >= 0 and right < n:
            # interpolate between vals[left] and vals[right]
            step = (vals[right] - vals[left]) / (right - left)
            for j in range(start, end + 1):
                vals[j] = vals[left] + step * (j - left)
        elif left < 0 and right < n:
            # missing at the very beginning: copy first known value
            for j in range(start, end + 1):
                vals[j] = vals[right]
        elif right >= 0 and left >= 0:
            # missing at the very end: copy last known value
            for j in range(start, end + 1):
                vals[j] = vals[left]

    # print Missing_1 ... Missing_20 in order
    for k in range(1, 21):
        v = vals[missing_pos[k]]
        # print with a few decimal places; scoring uses floats
        print(f"{v:.4f}")