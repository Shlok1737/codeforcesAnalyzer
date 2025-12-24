import json

with open("solved.json", "r") as f:
    problems = json.load(f)

# print(len(problems))

buckets = {
    "<1000": 0,
    "1000-1399": 0,
    "1400-1799": 0,
    "1800+": 0
}

for p in problems:
    r = p["rating"]
    if r == 0:
        continue
    elif r < 1000:
        buckets["<1000"] += 1
    elif r < 1400:
        buckets["1000-1399"] += 1
    elif r < 1800:
        buckets["1400-1799"] += 1
    else:
        buckets["1800+"] += 1

# print(f"buckets: {buckets}")
print()

tag_count = {}

for p in problems:
    for tag in p["tags"]:
        if tag not in tag_count:
            tag_count[tag] = 0
        tag_count[tag] += 1

# print(tag_count)


tag_stats = {}

for p in problems:
    r = p["rating"]
    for tag in p["tags"]:
        if tag not in tag_stats:
            tag_stats[tag] = {
                "count": 0,
                "sum_of_all_ratings": 0
            }

        tag_stats[tag]["count"] += 1
        tag_stats[tag]["sum_of_all_ratings"] += r


weakness = []

for tag in tag_stats:
    count = tag_stats[tag]["count"] #get the no of problems solved for tag
    totalRating = tag_stats[tag]["sum_of_all_ratings"] #get the total rating of all solved problems for tag

    avgRating = totalRating / count if count else 0
    tag_stats[tag]["avgRating"] = avgRating

    score = count * avgRating
    weakness.append((score, tag, count, avgRating))

weakness.sort()

print("Weak topics:")
for i in range(min(5, len(weakness))):
    score, tag, count, avgRating = weakness[i] #weakness[i] is a row in weakness list e.g., [
    # (1200, "dp", 3, 400.0),      # weakness[0] is this whole row
    # (2400, "graphs", 8, 300.0),  # weakness[1] is this whole row
    # ...
# ]
    print(f"{tag}: solved={count}, avgRating={avgRating:.0f}, score={score:.0f}")
