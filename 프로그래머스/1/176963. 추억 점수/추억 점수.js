function solution(name, yearning, photo) {
    const makePointObjByName = (name, yearning) => {
        return name.reduce((acc, cur, index) => {
            acc[cur] = yearning[index];

            return acc;
        }, {})
    }
    
    const getPoint = (pointObj, photoItem) => {
        return photoItem.reduce((point, name) => {
            const currentPoint = pointObj[name];
            if (currentPoint) {
                point += pointObj[name];    
            }
            
            return point;
        }, 0)
    }
    
    const pointObj = makePointObjByName(name, yearning);
    
    return photo.reduce((acc, cur) => {
        acc.push(getPoint(pointObj, cur))
        
        return acc;
    }, [])
}