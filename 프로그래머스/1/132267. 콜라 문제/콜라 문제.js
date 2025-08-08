function solution(a, b, n) {
    let result = 0;
    let remain = 0;
    
    while (n >= a) {
        const q = (Math.floor(n / a)) * b;
        const r = n % a;
        n = q + r;
        result += q;
    }
    
    return result;
}