function solution(k, tangerine) {
    const countObj = tangerine.reduce((acc, cur) => {
        if (acc[cur]) {
            acc[cur] += 1;
        } else {
            acc[cur] = 1;
        }
        
        return acc;
    }, {})
    
    const sortedArr = Object.entries(countObj).sort((a,b) => b[1]-a[1]);
    
    let remainK = k;
    let index = 0;
    
    while (remainK > 0 && index < sortedArr.length) {
        remainK -= sortedArr[index][1];
        
        index += 1;
    }
    
    return index;
    
    
    
}