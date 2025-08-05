function solution(x, y, n) {
    class Q {
        constructor() {
            this.storage = [];
            this.head = 0;
        }

        enqueue(value) {
            this.storage.push(value);
        }

        dequeue() {
            if (this.head >= this.storage.length) return undefined;
            const item = this.storage[this.head];
            this.head += 1;

            if (this.head > this.storage.length / 2) {
                this.storage = this.storage.slice(this.head);
                this.head = 0;
            }

            return item;
        }

        size() {
            return this.storage.length - this.head;
        }
    }

    const plusN = (x, n) => x + n
    const multiply2 = (x) => x * 2
    const multiply3 = (x) => x * 3

    if (x === y) return 0;

    const visited = new Set();
    const q = new Q();
    q.enqueue([x, 0]);
    visited.add(x);

    while (q.size() > 0) {
        const [current, cnt] = q.dequeue();

        const nx1 = plusN(current, n);
        const nx2 = multiply2(current);
        const nx3 = multiply3(current);

        for (const next of [nx1, nx2, nx3]) {
            if (next === y) {
                return cnt + 1;
            }

            if (next < y && !visited.has(next)) {
                visited.add(next);
                q.enqueue([next, cnt + 1]);
            }
        }
    }

    return -1;
}