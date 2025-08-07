function solution(k, score) {
    function addRankAndSort(rank, current) {
        rank.push(current);
            rank.sort((a, b) => b - a)
    }
    
    function addMinScoreToResult(result, rank) {
        result.push(rank.at(-1));
    }
    
    const rank = [];
    const result = [];
    
    for (let i in score) {
        const current = score[i];
        
        if (rank.length < k) {
            addRankAndSort(rank, current)
        } else if (current > rank.at(-1)) {
            rank.pop();
            addRankAndSort(rank, current)
        }
        
        addMinScoreToResult(result, rank);
    }
    
    return result
}