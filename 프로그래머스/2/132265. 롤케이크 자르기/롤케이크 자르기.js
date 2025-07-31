function solution(topping) {
    let result = 0;

    const b = topping.reduce((acc, cur) => {
        if (acc[cur]) {
            acc[cur] += 1;
        } else {
            acc[cur] = 1;
        }

        return acc;
    }, {})

    let index = 0;
    let mSet = new Set();
    let bSet = new Set(topping);

    while (index < topping.length) {
        const currentTopping = topping[index];
        mSet.add(currentTopping);

        b[currentTopping] -= 1;

        if (b[currentTopping] === 0) {
            bSet.delete(currentTopping);
        }

        if (mSet.size === bSet.size) {
            result += 1;
        }

        index += 1;
    }

    return result;
}