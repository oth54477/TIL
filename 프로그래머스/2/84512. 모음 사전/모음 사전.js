function solution(word) {
    const strArr = ['A', 'E', 'I', 'O', 'U'];
    const set = new Set();
    
    function findAll(str) {
        if (str.length >= 5) {
            return
        }
        for (const s of strArr) {
            set.add(str + s);
            findAll(str + s);
        };
    }
    
    findAll('')
    
    const wordList = Array.from(set);
    
    wordList.sort()
    
    return wordList.findIndex((x) => x === word) + 1
    
}