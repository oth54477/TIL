  const getPermutations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]); 
    // n개중에서 1개 선택할 때(nP1), 바로 모든 배열의 원소 return. 1개선택이므로 순서가 의미없음.

    arr.forEach((fixed, index, origin) => {
      const rest = [...origin.slice(0, index), ...origin.slice(index+1)] 
      // 해당하는 fixed를 제외한 나머지 배열 
      const permutations = getPermutations(rest, selectNumber - 1); 
      // 나머지에 대해서 순열을 구한다.
      const attached = permutations.map((el) => [fixed, ...el]); 
      //  돌아온 순열에 떼 놓은(fixed) 값 붙이기
      results.push(...attached); 
      // 배열 spread syntax 로 모두다 push
    });

    return results; // 결과 담긴 results return
}
 
 function isPrime(num) {
    if(num <= 1) { // 음수와 1은 소수가 아니다
        return false;
    }

    // 2는 짝수 중 유일한 소수이다
    if( num % 2 === 0) { 
        return num === 2 ? true : false;
    }

    // 이제 num이 홀수 일때 다른 수에 나눠지는지 판별한다

    // Math.sqrt(num) 즉, √num까지 나눠 떨어지는지 검사한다
    // 원리는 "에라토스테네스의 체" 참고

    const sqrt = parseInt(Math.sqrt(num));

    for( let divider = 3; divider <= sqrt; divider += 2) {

    if(num % divider === 0) {
      return false;
    }

    }

    return true;
}


function solution(numbers) {
    const numberArr = numbers.split("");
    
    const set = new Set();
    
    for (let i=1; i <= numberArr.length; i++) {
        getPermutations(numbers.split(""), i).forEach((item) => {
            set.add(Number(item.join("")));
        })            
    }
    
    
    
    return Array.from(set).reduce((count, number) => {
        if (isPrime(number)) {
            count += 1
        }
        
        return count
    }, 0)
    
}