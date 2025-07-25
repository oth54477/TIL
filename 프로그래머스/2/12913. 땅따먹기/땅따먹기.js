function solution(land) {
    while (land.length > 1) {
        const r = land.pop()
        
        const row = r.reduce((acc, cur, index) => {
            acc.push([cur, index])
            return acc
        }, [])
        
        row.sort((a,b) => b[0] - a[0])
        
        for (let i=0; i<4; i++) {
            if (row[0][1] === i) {
                land[land.length-1][i] += row[1][0]    
            } else {
                land[land.length-1][i] += row[0][0]    
            }
        }
    }
    
    land[0].sort((a,b) => b - a)
    
    return land[0][0]
}