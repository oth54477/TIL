function solution(arr1, arr2) {
    let result = []
    
    for (let r1=0; r1 < arr1.length; r1++) {
        result.push([])
        for (let c2=0; c2 < arr2[0].length; c2++) {
            let value = 0
            for (let c1=0; c1 < arr1[0].length; c1++) {
                value += arr1[r1][c1] * arr2[c1][c2]
            }
            result[r1].push(value)    
        }
        
    }
    
    return result
}