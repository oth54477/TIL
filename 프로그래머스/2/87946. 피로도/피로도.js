function solution(k, dungeons) {     
    function permutation(arr,n){   
        let result =[]

        function dfs(current){
            if(current.length===n){
                result.push([...current])
                return 
            }
            for(let i=0; i<arr.length;i++){
                if(!current.includes(arr[i])){
                    current.push(arr[i])
                    dfs(current)
                    current.pop()
                }
            }
        }
        dfs([])

        return result
    }
    
    const cases = permutation(dungeons, dungeons.length)
    
    return cases.reduce((acc, cur, index) => {
        let nowK = k
        const nowCnt = cur.reduce((cnt, d) => {
            if (nowK >= d[0]) {
                cnt += 1
                nowK -= d[1]
            }
            
            return cnt
        }, 0)

        return Math.max(nowCnt, acc)
    }, 0)
}