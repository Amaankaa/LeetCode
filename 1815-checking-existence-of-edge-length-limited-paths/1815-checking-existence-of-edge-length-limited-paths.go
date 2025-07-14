type UF struct {
    parent []int
    size []int
}

func newUF(n int) *UF {
    parent := make([]int, n)
    size := make([]int, n)
    for i := range parent {
        parent[i] = i
        size[i] = 1
    }
    return &UF {
        parent: parent,
        size: size,
    }
}

func (self *UF) find(x int) int {
    if self.parent[x] != x {
        self.parent[x] = self.find(self.parent[x])
    }
    return self.parent[x]
}

func (self *UF) union(x, y int) bool {
    rx, ry := self.find(x), self.find(y)
    if rx == ry {return false}
    if self.size[rx] < self.size[ry] {
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
    } else {
        self.parent[rx] = ry
        self.size[ry] += self.size[rx]
    }
    return true
}

func (self *UF) isConnected(x, y int) bool {
    return self.find(x) == self.find(y)
}

func distanceLimitedPathsExist(n int, edgeList [][]int, queries [][]int) []bool {
    uf := newUF(n)
    sort.Slice(edgeList, func(i, j int) bool {
        return edgeList[i][2] < edgeList[j][2]
    })

    for i, _ := range queries {
        queries[i] = append(queries[i], i)
    }

    sort.Slice(queries, func(i, j int) bool {
        return queries[i][2] < queries[j][2]
    })

    m := len(edgeList)
    ans := make([]bool, len(queries))
    j := 0

    for _, edge := range queries {
        u, v, limit, idx := edge[0], edge[1], edge[2], edge[3]
        for j < m && edgeList[j][2] < limit {
            uf.union(edgeList[j][0], edgeList[j][1])
            j += 1
        }
        ans[idx] = uf.isConnected(u, v)
    }

    return ans
}