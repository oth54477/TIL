const map = {
    '}': '{',
    ']': '[',
    ')': '(',
}

const openS = new Set(['{', '[', '('])
const closeS = new Set(['}', ']', ')'])

function solution(s) {
    function check(str) {
        let result = true;
        const stack = [];
        
        for (nowS of str) {
            const isOpen = openS.has(nowS);
            
            if (isOpen) {
                stack.push(nowS);
                continue;
            }
            
            const stackS = stack.pop();
            
            if (map[nowS] !== stackS) {
                result = false;
                break;
            }
        }
        
        if (stack.length > 0) {
            return false
        }
        
        return result;
    }
    
    let result = 0
    
    for (let i=0; i<s.length; i++) {
        if (check(s.slice(i) + s.slice(0,i))) {
            result += 1
        }
    }
    
    return result;
}