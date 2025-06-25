class Queue {
    constructor() {
        this.q = {}
        this.front = 0
        this.rear = 0
   }
    
    size() {
        return this.rear - this.front;
    }
    
    enqueue(e) {
        this.q[this.rear] = e
        this.rear++
    }
    
    dequeue() {
        const e = this.q[this.front]
        delete this.q[this.front]
        this.front++
        
        if (this.front === this.rear) {
          this.front = 0;
          this.rear = 0;
        }
        
        return e
    }
}

function solution(progresses, speeds) {
    const times =  progresses.reduce((acc, cur, index) => {
        acc.enqueue(Math.ceil((100-cur) / speeds[index]))
        return acc
    }, new Queue())
    
    let result = [1]
    let prev = times.dequeue()
    
    while (times.size() > 0) {
        const time = times.dequeue()
        
        if (time <= prev) {
            result[result.length-1] += 1
        } else {
            result.push(1)
            prev = time
        }
    }
    
    return result
}