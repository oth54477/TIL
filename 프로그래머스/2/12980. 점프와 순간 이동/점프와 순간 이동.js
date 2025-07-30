function solution(n) {
    let result = 0;
    let x = n;
    
    while (x > 0) {
        const q = x >> 1;
        const r = x % 2;
        
        if (r) {
            result += r;
        }
        
        x = q;
    }
    
    return result;
}