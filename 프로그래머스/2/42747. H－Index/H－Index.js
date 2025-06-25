function solution(citations) {
    const sortedArr =  citations.sort((a, b) => b - a)
    
    for (let h=0; h < sortedArr.length; h++) {
        const nowC = sortedArr[h]
        
        if (nowC < h+1) return h
    }
    
    const lastC = sortedArr[sortedArr.length - 1]
    return lastC > sortedArr.length ? sortedArr.length : lastC === 0 ? 0 : 1
}