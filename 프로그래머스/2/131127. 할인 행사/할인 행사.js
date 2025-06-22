function solution(want, number, discount) {
    const defaultWantObj = want.reduce((acc, cur, index) => {
        acc[cur] = 0
        
        return acc
    }, {})
    
    const wantObj = want.reduce((acc, cur, index) => {
        acc[cur] = number[index]
        
        return acc
    }, {})
    const wantKeys = Object.keys(wantObj)
    
    let wantCount = number.reduce((acc, cur) => {
        return acc + cur
    }, 0)
    
    const discountObj = discount.slice(0, wantCount).reduce((acc, cur, index) => {
        if (Object.hasOwn(wantObj, cur)) {
            if (Object.hasOwn(acc, cur)) {
                acc[cur] += 1
            } else {
                acc[cur] = 1
            }
        } else {
            acc.pass += 1
        }
        
        return acc
    }, {
        ...defaultWantObj,
        pass: 0
    })
    
    const answer = Array(discount.length - wantCount + 1).fill(0).reduce((acc, cur, index) => {
        if (discountObj.pass === 0) {
            
            const isTrue = wantKeys.reduce((isSame, key) => {
                if (!isSame) {
                    return isSame
                }
                
                if (wantObj[key] !== discountObj[key]) {
                    return false
                }
                
                return isSame
            }, true) 
            
            if (isTrue) {
                acc += 1
            }
        }
        
        if (Object.hasOwn(discountObj, discount[index])) {
            discountObj[discount[index]] -= 1    
        } else {
            discountObj.pass -= 1    
        }
        
        const newThing = discount[index + wantCount]
        
        if (Object.hasOwn(wantObj, newThing)) {
            discountObj[newThing] += 1
        } else {
        discountObj.pass += 1    
        }
        
        return acc
    }, 0)
    
    return answer;
}