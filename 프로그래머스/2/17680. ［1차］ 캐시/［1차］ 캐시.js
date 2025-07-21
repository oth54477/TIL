function solution(cacheSize, cities) {
    const cacheMap = new Map();
    
    const hitCache = (city, map) => {
        map.delete(city);
        
        if (map.size < cacheSize) {
        map.set(city, 1);    
        }
        
    };
    
    const missCache = (city, map) => {
        if (map.size === cacheSize) {
            map.delete(map.keys().next().value);
        };
        
        if (map.size < cacheSize) {
            map.set(city, 1);    
        }
    };
    
    return cities.reduce((time, city, index) => {
        const lowerCity = city.toLowerCase()
        if (cacheMap.has(lowerCity)) {
            time += 1;
            hitCache(lowerCity, cacheMap);
        } else {
            time += 5;
            missCache(lowerCity, cacheMap);
        };
        
        return time;
    }, 0);
}