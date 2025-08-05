function solution(code) {
    let mode = 0;
    let ret = '';
    
    for (let index in code) {
        const current = code[index];

        if (current === '1') {
            mode = mode === 0 ? 1 : 0;
            continue;
        }

        if (mode === 0 && index % 2 === 0) {
            ret += current;
        }
        
        if (mode === 1 && index % 2 === 1) {
            ret += current;
        }
    }

    return ret === '' ? 'EMPTY' : ret;
}