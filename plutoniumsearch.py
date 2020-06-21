import golly as g

# Parameters
bx = 4
by = 4
boring_periods = [1, 2, 6]

# Do not change this
patt_count = 0
cnt = [1] * 999

def dfs(known_cells, depth, cell_count):
	global bx, by
	if depth >= bx * by:
		run_patt(known_cells)
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

g.autoupdate(True)
dfs("", 0, 0)
#run_patt("$3o$2o$o!")
