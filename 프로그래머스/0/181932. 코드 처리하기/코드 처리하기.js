function solution(code) {
    const toggleMode = () => {
        mode = mode === 0 ? 1 : 0;
    }

    const checkIsEven = (index) => {
        return index % 2 === 0;
    }

    const checkCondition = (mode, index) => {
        if (mode === 0 && checkIsEven(index)) {
            return true;
        }

        if (mode === 1 && !checkIsEven(index)) {
            return true;
        }
    }

    let mode = 0;
    let ret = '';

    for (let index in code) {
        const current = code[index];

        if (current === '1') {
            toggleMode();
            continue;
        }

        if (checkCondition(mode, index)) {
            ret += current;
        }
    }

    return ret === '' ? 'EMPTY' : ret;
}