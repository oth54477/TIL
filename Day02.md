# Git

###### 07.15 (금)

## README.md

- 프로젝트를 설명하는 문서
- 프로젝트를 시작할때 꼭 생성해준다.
- README는 대문자로
- [https://github.com/woowacourse-teams](https://github.com/woowacourse-teams)

## .gitignore

- 남에게 보여주면 안되는 보안 파일
- 굳이 올리지 않아도 되는 파일
- .gitignore안에 무시할 파일 작성
  - 맨 앞에 .은 숨김파일이라는 뜻
- 이미 git이 관리하고 있는 파일은 안된다.
- .gitignore, README.md는 프로젝트를 생성하고 맨 처음에 무조건 만든다.
- [https://gitignore.io](https://www.toptal.com/developers/gitignore/)
  - 사용할 기술 입력하고 복사해서 .gitignore에 붙여넣기

## Clone & Pull

### 1. Clone

- git clone = 다운로드
  `git clone [Github repository URL]`
- 작동 순서
  1. 폴더 생성
  2. git init
  3. git remote add
  4. 버전, 파일 생성
- 폴더를 만들고 싶은 곳에서
  1. 오른쪽 클릭
  2. git bash here
  3. git clone [git 프로젝트 주소]

### 2. Pull

- git pull = 업데이트
  `git pull origin master`

## Github profiles

- 계정명으로 프로젝트 만들고, README.md에 작성

## git commit convention

- 커밋 메세지는 규칙을 따라서 하기 (중요)
- 전 세계적으로 정해진 규칙 x
- feat : 새로운 기능 추가
- fix : 버그 수정
- docs : 문서 수정
- style : 포맷팅, 세미클론 빠졌을 때, 코드 변경이 없는 수정
- refactor : 리팩토링
- test : 테스트 코드 추가, 테스트 코드 리팩토링
- chore : 빌드관련 수정, 패키지 매니저 수정
