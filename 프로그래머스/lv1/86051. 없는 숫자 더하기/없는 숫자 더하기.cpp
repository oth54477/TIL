#include <string>
#include <vector>
#include<iostream>
#include<algorithm>
using namespace std;

int solution(vector<int> numbers) {
    int answer = 0;
    
    int x = numbers.size();

    for (int i=0; i < 10; i++) {
        if (find(numbers.begin(), numbers.end(), i)== numbers.end()) {
            answer += i;
        }
    }

    return answer;
}