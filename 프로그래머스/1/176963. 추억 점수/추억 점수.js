function solution(name, yearning, photo) {
    const pointObj = name.reduce((acc, cur, index) => {
        acc[cur] = yearning[index];
        
        return acc;
    }, {})
    
    return photo.reduce((acc, cur) => {
        acc.push(cur.reduce((point, name) => {
            const currentPoint = pointObj[name];
            if (currentPoint) {
                point += pointObj[name];    
            }
            
            return point;
        }, 0))
        
        return acc;
    }, [])
}