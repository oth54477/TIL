# Git

## 깃(Git) 이란?
- Git은 분산 버전 관리를 할 수 있는 툴중 하나이다.
- 백업, 복구, 협업의 역할로 이루어져 있다.
- 로컬 저장소는 Working Directory, Staging Area, Commits으로 이루어져 있다. 


## 갓허브와 깃의 차이
- Git은 로컬에서 버전 관리 시스템을 운영하는 방식이고, Github는 저장소를 깃허브에서 제공해주는 클라우드 서버를 이용한다는 것의 차이이다.
- Github를 이용하면 전세계의 다양한 사람들과 공유하고, 협업할 수 있다.

## Git 명령어
- Git 버전 확인하기
  ```bash
  git --version
  ```

- 초기화
  ```bash
  git init
  git config --global user.name [본인의 깃 닉네임]
  git config --global user.email [본인의 깃 이메일]
  ```

- 현재상태 확인하기
  ```bash
  git status
  ```

- Working Directory -> Staging Area

  ```bash
  git add [File_Name]
  git add . # 모든 파일 add
  ```
  
- Staging Area -> commits

  ```bash
  git commit -m "commit message"
  ```

- commits 목록 출력

  ```bash
  git log
  git log --oneline # 한줄로 보기 옵션
  git log -p # 커밋마다 차이 보기 옵션
  ```
  
- 로컬 저장소와 원격 저장소를 연결

  ```bash
  git remote add origin [Github repository URL]
  ```

- 연결된 원격 저장소 목록 조회

  ```bash
  git remote -v
  ```

- 원격 저장소 연결 삭제

  ```bash
  git remote rm origin
  git remote remove origin
  ```

- 로컬 저장소의 commits을 원격 저장소에 반영

  ```bash
  git push origin master
  git push -u origin master # -u옵션을 했다면 이후 push할 때는 git push만으로도 가능
  ```

