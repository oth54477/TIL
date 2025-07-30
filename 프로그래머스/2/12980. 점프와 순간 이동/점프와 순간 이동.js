function solution(n) {
    let result = 0;
    let x = n;
    
    while (x > 0) {
        const q = parseInt(x / 2);
        const r = x % 2;
        
        if (r) {
            result += r;
        }
        
        x = q;
    }
    
    return result;
}