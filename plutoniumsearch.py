import golly as g

# Parameters
w = int(g.getstring("Search width:", "8"))
h = int(g.getstring("Search height:", "8"))
sym = g.getstring("Symmetry (C1, D2)", "D2")
seed = int(g.getstring("Slice number:"))
if sym == "C1":
	boring_periods = [1, 2, 3, 4, 6, 8, 10]
if sym == "D2":
	boring_periods = [1, 2, 3, 4, 6, 10, 14, 15]
preset = int(g.getstring("Preset cells:", "8"))

# Do not change this
patt_count = 0
cnt = [1] * 999

def convert(seed):
	global bx
	known_cells = ""
	res = ""
	while seed >= 2:
		res += str(seed % 2)
		seed /= 2
	if seed:
		res += str(seed)
	res += "0" * (preset - len(res))
	res = res[::-1]
	for i in range(len(res)):
		if i % bx == 0:
			known_cells += "$"
		if res[i] == "0":
			known_cells += "b"
		else:
			known_cells += "o"
	return known_cells

def symmetrify(known_cells, sym):
	global h
	rows = known_cells.split("$")
	if h % 2 == 0:
		rows.extend(rows[::-1])
	else:
		rows.extend(rows[-1::-1])
	return "$".join(rows)

def dfs(known_cells, depth, cell_count):
	global bx, by
	if depth >= bx * by:
		run_patt(symmetrify(known_cells, sym))
		return
	if depth % bx == 0:
		dfs(known_cells + "$b", depth + 1, cell_count)
		dfs(known_cells + "$o", depth + 1, cell_count + 1)
		return
	dfs(known_cells + "b", depth + 1, cell_count)
	dfs(known_cells + "o", depth + 1, cell_count + 1)

def run_patt(known_cells):
	global patt_count, meth_count
	g.new("PlutoniumSearch")
	g.reset()
	g.update()
	patt_count += 1
	#patt = g.parse(known_cells + "!")
	patt = g.parse(known_cells[1:] + "!")
	#g.note(known_cells[1:] + "!")
	g.putcells(patt)
	g.update()
	hashlist = {}
	for gene in range(999):
		if g.empty():
			break
		if g.hash(g.getrect()) in hashlist:
			p = int(g.getgen()) - hashlist[g.hash(g.getrect())]
			if not p in boring_periods:
				g.reset()
				g.save("p" + str(p) + "_" + str(cnt[p]) + ".rle", "rle")
				cnt[p] += 1
			break
		else:
			hashlist[g.hash(g.getrect())] = int(g.getgen())
			g.run(1)
		"""
		except:
			# Pattern dies
			if int(g.getgen()) > min_lifespan:
				meth_count += 1
				newlifespan = int(g.getgen())
				g.new("Saving methuselah")
				g.putcells(patt)
				try:
					g.save("diehard-" + str(newlifespan) + ".rle", "rle")
				except:
					pass
				g.update()
				#max_final_pop = newpop
			break"""
	#g.warn(str(hashlist))
	g.show(str(patt_count) + "/" + str(2 ** (bx * by)))

#g.autoupdate(True)
if sym == "C1":
	bx = w
	by = h
elif sym == "D2":
	bx = w
	if h % 2 == 0:
		by = h / 2
	else:
		by = h / 2 + 1
else:
	g.note("Not a valid symmetry!")
	g.exit()
dfs(convert(seed), preset, preset)
#run_patt("$3o$2o$o!")
