function solution(k, m, score) {
    const makeBox = (score, m, boxCount) => {
        return score.reduce((acc, cur, index) => {
            const i = Math.floor(index / m);

            if (i < boxCount) {
                acc[i].push(cur);    
            }

            return acc;
        }, Array(boxCount).fill(0).map(() => []))
    }
    
    const checkScore = (boxes) => {
        return boxes.reduce((acc, cur) => {
            return acc + cur[cur.length-1] * m
        }, 0)
    }
    
    score.sort((a, b) => b - a);
    
    const boxCount = Math.floor(score.length / m);
    
    return checkScore(makeBox(score, m, boxCount))
}