function solution(s) {
    const numberStrings = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    
    for (index in numberStrings) {
        const numberString = numberStrings[index];
        
        s = s.replaceAll(numberString, index)
    }
    
    return Number(s)
}