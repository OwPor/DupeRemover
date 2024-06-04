lines_seen = set()
with open('nodupe.txt', "w", encoding='utf-8') as outfile:
    with open('dupe.txt', "r", encoding='utf-8') as infile:
        for line in infile:
            if line not in lines_seen:
                outfile.write(line)
                lines_seen.add(line)
