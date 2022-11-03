# 내일배움캠프 4기 - B반 3조

### 01. 프로젝트 명

- 코딩잘하는 김조한

### 02. 프로젝트 설명

- 김관호, 김익현, 조성락, 한병두, 한세인의 성을 딴 '김조한' 조의 팀 소개 페이지
- 프론트엔드, 백엔드, 서버, DB 구축을 통해 웹 개발의 이해 목표


### 03. 팀원 소개 및 역할
| 이름                      | 역할               | 
|-------------------------|------------------|
| 한병두                     | 팀장 - 프론트엔드/백엔드   | 
| 김익현                     | 팀원 - 프론트엔드/백엔드   |
| 김세인                     | 팀원 - 프론트/백엔드     |
| 조성락                     | 팀원 - 프론트/백엔드    |
| 김관호                     | 팀원 - 프론트/백엔드/서버구축 |

### 04. 사용 기술

<div>
<img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
<img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white">
</div>
<div>
<img src="https://img.shields.io/badge/mongoDB-47A248?style=for-the-badge&logo=MongoDB&logoColor=white">
<img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white">
<img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/Amazone EC2-FF9900?style=for-the-badge&logo=amazon&logoColor=white">
</div>


### 05. 구현 API

| URL                     | Method | Function    | Request                                            | Response                                                                             |
|-------------------------|--------|-------------|----------------------------------------------------|--------------------------------------------------------------------------------------|
| /                       | GET    | 메인 페이지      | -                                                  | index.html                                                                           |
| /teaminto               | GET    | 팀원 리스트      | -                                                  | teaminto.html                                                                        |
| /{member-name}          | GET    | 팀원 별 소개 페이지 | -                                                  | 팀원 별 소개 페이지.html                                                                     |
| /api/{member-name}      | GET    | 댓글 가져오기     | -                                                  | {<br/>"name" : "홍길동",<br/>"comment": "들렀다가요"<br/>}, ...                              |
| /api/{member-name}      | POST   | 댓글 등록       | {<br/>"name" : "홍길동",<br/>"comment": "들렀다가요"<br/>} | -                                                                                    |
| /api/{member-name}/like | GET    | 좋아요 가져오기    | -                                                  | { "like" : 0 }                                                                       |
| /api/{member-name}/like | POST   | 좋아요 등록      | -                                                  | -                                                                                    |
| /api/music              | GET    | 김조한 음악 크롤링  | -                                                  | {<br/>"image": "imageLink",<br/>"title": "titleName",<br/>"album": "albumName"<br/>} |


### 06. 데이터베이스 구조

#### - Database
- johan

#### - Collections
- byungdoo, byungdoolike
- ikhyun, ikhyunlike
- sein, seinlike
- seongrak, seongraklike
- gwanho, gwanholike

#### - Documents
- {memberName} : [{ "name" : (String), "comment" : (String) }, ...]
- {memberName + "like"} : { "count" : (Int) }

### 07. 관련 링크
<a href="http://43.201.105.241"> 사이트 접속 </a> <br>
<a href="https://giant-honeycrisp-305.notion.site/6901a11fdc3d45349e38f0171c85dacb"> 개발 일지 노션 </a>