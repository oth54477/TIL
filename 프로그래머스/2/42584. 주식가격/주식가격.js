function solution(prices) {
    const result = new Array(prices.length).fill(0);
 
    const stack = [];
    
    for (let index=0; index < prices.length; index++) {
        const price = prices[index]
        
        while (stack.length > 0 && price < stack.at(-1)[0]) {
            const [targetPrice, targetIndex] = stack.pop()
            
            result[targetIndex] = index - targetIndex
        }
        
        stack.push([price, index])
    }

    stack.forEach(([price, index]) => {
        result[index] = prices.length - index - 1;    
    })
    
    return result
}