from collections import deque

def solution(book_time):
    # 시간을 int형의 분 단위로 변환
    times = change_minutes(book_time)

    # 시작 시간 기준으로 정렬
    times.sort(key=lambda x : x[0])

    dq = deque(times)
    time_tables = []
    while dq:
        start, end = dq.popleft()
        for idx, time_table in enumerate(time_tables):
            if time_table[-1][-1] + 10 <= start:
                time_tables[idx].append((start, end))
                break
        else:
            time_tables.append([(start, end)])

    return len(time_tables)

def change_minutes(times):
    return [[int(time[0:2]) * 60 + int(time[3:]) for time in start_end] for start_end in times]
        
