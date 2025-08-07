function solution(N, A, B) {
	let round = 0;
 
	while (A !== B) {
		round++;
		A = Math.ceil(A / 2);
		B = Math.ceil(B / 2);
	}
 
	return round;
}