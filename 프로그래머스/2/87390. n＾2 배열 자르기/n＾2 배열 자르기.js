function solution(n, left, right) {
    const arr = Array(right-left+1).fill(left).map((i, index) => i + index)
    
    const getQuotient = (x) => Math.ceil((x+1) / n) - 1
    const getRemain = (x) => x % n
    const getValue = (x) => {
        const q = getQuotient(x)
        const r = getRemain(x)
        return Math.max(q + 1, r + 1)
    }
    
    return arr.reduce((acc, cur) => {
        acc.push(getValue(cur))
        return acc
    }, [])
}