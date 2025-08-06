function solution(phoneBook) {
    phoneBook.sort((a,b) => a.length - b.length)
    return !(new Array(20).fill(0).some((_, index) => {
        if (!phoneBook.some((num) => num.length === index)) return false;
        
        const [set, __] = phoneBook.reduce((acc, num) => {
            const temp = num.slice(0, index)
            !acc[1].has(temp) && num.length !== index ? acc[0].add(num) : acc[0].add(temp)
            if (num.length === index) acc[1].add(temp)
            
            return acc
        }, [new Set(), new Set()])

        console.log(index, set.size, phoneBook.length)
        
        return set.size !== phoneBook.length;
    }))
}