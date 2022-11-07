# 내일배움캠프 Team 텔레토비태양
***
## 심화DRF 추천시스템프로젝트 저장소
***
frontend repo = (asdasdasdasdasd)

# 팀원 역할 및 약속
## 팀원 역할
  - **김남훈** 머신러닝/백엔드 [블로그 링크](https://hunss.tistory.com/)
  - **김서영** 머신러닝/백엔드 [블로그 링크](https://velog.io/@ksykma)
  - **김인해** 프론트엔드/백엔드 [블로그 링크](https://oceandevelopment.tistory.com/)
  - **서장원** 프론트엔드/백엔드 [블로그 링크](https://sjw887.tistory.com/)
  - **최윤선** 머신러닝/백엔드 [블로그 링크](https://iced-coriander-f89.notion.site/TIL-WIL-Tistory-e8463c7836844157a40c2c76fbaf1c61)
## 우리팀의 약속
  - 주말에도 프로젝트에 시간 할애하기
  - 하루의 해야 할 양을 정해서 하기
  - 커밋 약속: 생성 [Add], 수정 [Mod], 내용 자세하게 쓰기, 수시로 커밋하기, 브랜치 확인하기

# 프로젝트 주제
+ 가게 추천 웹 사이트
  - 별점이 높은 가게를 랜덤으로 리스트업해주고, 사용자의 선택과 유사한 리뷰를 가진 가게를 추천해주는 서비스

# 프로젝트 포함 사항
  - DRF의 CBV를 활용하여 구현
  - Serializer기능을 활용
  - Django의 기본 user model이 아닌, custom user model을 사용
  - 크롤링한 데이터를 바탕으로 유사한 콘텐츠 추천 - 추천시스템
  - Frontend와 Backend 서버를 별도로 구축하고 구현
 

 # 와이어프레임
***
![image](https://user-images.githubusercontent.com/103415295/200363425-45d9095e-3a07-4162-8ab3-ef1abf46b152.png)
 
 # API설계
***

 # DB설계

 # 프로젝트 기능 명세서
 + 회원가입
   - 닉네임과 비밀번호 길이 최소치 지정
   - 
 + 로그인
 + 메인페이지
   - CSV데이터를 카카오맵에 상호명 + 주소로 크롤링
   - 크롤링 정보
     * 상호명
     * 가게 이미지
     * 가게 리뷰 내용
     * 별점
   - 사용자는 별점이 높은 가게를 랜덤 리스트업
   - 마음에 드는 가게 선택 가능
 + 머신러닝페이지
   - 리뷰내용으로 코사인유사도검사
   - 사용자가 선택한 가게와 유사한 가게 리스트업




# 기술 스택

### 백엔드
<img alt="Python" src ="https://img.shields.io/badge/Python-3776AB.svg?&style=for-the-badge&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">

### 프론트엔드
<img alt="JavaScript" src ="https://img.shields.io/badge/JavaScriipt-F7DF1E.svg?&style=for-the-badge&logo=JavaScript&logoColor=black"/> <img alt="Html" src ="https://img.shields.io/badge/HTML5-E34F26.svg?&style=for-the-badge&logo=HTML5&logoColor=white"/> <img alt="Css" src ="https://img.shields.io/badge/CSS3-1572B6.svg?&style=for-the-badge&logo=CSS3&logoColor=white"/>

### 데이터베이스
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=SQLite&logoColor=white">

### 머신러닝
<img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white">

### 협업
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
