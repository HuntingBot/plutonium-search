import golly as g

count = 0
found = 0
period_count = [0] * 50

report = open("report.txt", "w")

def convert(slice_id):
	# Convert slice number into binary
	known_cells = ""
	for i in range(7, -1, -1):
		if slice_id // 2 ** i:
			known_cells += "o"
			slice_id -= 2 ** i
		else:
			known_cells += "b"
	return known_cells

def dfs(known_cells, depth):
	if depth == 24:
		period_detection(known_cells)
		return
	if depth % 8 == 0:
		known_cells += "$"
	dfs(known_cells + "b", depth+1)
	dfs(known_cells + "o", depth+1)

def period_detection(upper_half):
        global count
        global found
        count += 1

        boring_periods = [1, 2, 3, 4, 6, 14, 15]
        
	# Mirroring
	g.show(str(count) + "/16777216")
	rows = upper_half.split("$")
	full_rle = upper_half + "$" + "$".join(rows[::-1]) + "!"
	
	pattern = g.parse(full_rle)
	g.new("PlutoniumSearch")
	g.putcells(pattern, 0, 0)

	# Period detection
        g.run(25)
	try:
                h = g.hash(g.getrect())
                for i in range(1, 50):
                        g.run(1)
                        if g.hash(g.getrect()) == h:
                                # Oscillates
                                if not i in boring_periods:
                                        g.reset()
                                        period_count[i] += 1
                                        g.save("p" + str(i) + "_" + str(period_count[i]) + ".rle", "rle")
                                        found += 1
                                        report.write("Found p" + str(i) + "\n")
                                break
        except:
                # The pattern dies
                return
g.show("This is PlutoniumSearch v1.1")
report.write("This is PlutoniumSearch v1.1")

begin = int(g.getstring("From slice:"))
end = int(g.getstring("To slice: "))
report.write("From slice: " + str(begin) + "\nTo slice: " + str(end) + "\n")

all_slice = range(begin, end+1)

for i in all_slice:
	g.show("Slice " + str(i) + " begin")
	report.write("Slice " + str(i) + " begin")
	dfs(convert(i), 0)
g.show("Search complete, " + str(found) + "results found")
report.write("Search complete, " + str(found) + "results found")
report.close()