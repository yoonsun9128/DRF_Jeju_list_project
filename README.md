# ![25](https://user-images.githubusercontent.com/103415295/200451827-97c67713-e0d2-4558-bf6f-f2b9846c0829.png)내일배움캠프 Team 텔레토비태양

## 심화DRF 추천시스템프로젝트 저장소


frontend repo = https://github.com/yoonsun9128/DRF_Jeju_list_project-frontend-

# ![25](https://user-images.githubusercontent.com/103415295/200451827-97c67713-e0d2-4558-bf6f-f2b9846c0829.png)팀원 역할 및 약속
### 팀원 역할
  - **김남훈** 머신러닝/백엔드 [블로그 링크](https://hunss.tistory.com/)
  - **김서영** 머신러닝/백엔드 [블로그 링크](https://velog.io/@ksykma)
  - **김인해** 프론트엔드/백엔드 [블로그 링크](https://oceandevelopment.tistory.com/)
  - **서장원** 프론트엔드/백엔드 [블로그 링크](https://sjw887.tistory.com/)
  - **최윤선** 머신러닝/백엔드 [블로그 링크](https://iced-coriander-f89.notion.site/TIL-WIL-Tistory-e8463c7836844157a40c2c76fbaf1c61)
### 우리팀의 약속
  - 주말에도 프로젝트에 시간 할애하기
  - 하루의 해야 할 양을 정해서 하기
  - 커밋 약속: 생성 [Add], 수정 [Mod], 내용 자세하게 쓰기, 수시로 커밋하기, 브랜치 확인하기

# 프로젝트 주제
+ 가게 추천 웹 사이트
  - 별점이 높은 가게를 랜덤으로 리스트업해주고, 사용자의 선택과 유사한 리뷰를 가진 가게를 
    추천해주는 서비스

# 프로젝트 포함 사항
  - DRF의 CBV를 활용하여 구현
  - Serializer기능을 활용
  - Django의 기본 user model이 아닌, custom user model을 사용
  - 크롤링한 데이터를 바탕으로 유사한 콘텐츠 추천 - 추천시스템
  - Frontend와 Backend 서버를 별도로 구축하고 구현
 

 # ![25](https://user-images.githubusercontent.com/103415295/200451837-221980f5-74f3-46f2-a56b-704e7c5ad91b.png)와이어프레임
![image](https://user-images.githubusercontent.com/103415295/200363425-45d9095e-3a07-4162-8ab3-ef1abf46b152.png)
 
 # ![25](https://user-images.githubusercontent.com/103415295/200451854-3a9e805d-e24e-4035-a7b0-c6238b5c487b.png)API설계
 + STORE APP
![image](https://user-images.githubusercontent.com/103415295/200448140-faaad562-a249-42fe-8b7c-26d5ba67ef61.png)

 + USER APP
 ![image](https://user-images.githubusercontent.com/103415295/200448271-7cf56e80-a2ad-4d46-a376-bcfdf97d6ba4.png)



 # ![25](https://user-images.githubusercontent.com/103415295/200451920-fa94cae7-f866-4c65-bbe0-3976fd8b350b.png)DB설계
![image](https://user-images.githubusercontent.com/103415295/200444788-1995485e-5b1b-4132-af8e-ed4ca790e7b8.png)


 # ![25](https://user-images.githubusercontent.com/103415295/200451928-7782261a-3148-4069-a03c-eb79678a59cb.png)프로젝트 기능 명세서
 ### 회원가입 & 로그인
   + 닉네임과 비밀번호 길이 최소치 지정
   + 빈 값으로 회원가입 시도시 경고창 생성
   
 ### 메인페이지
   + CSV데이터를 카카오맵에 상호명 + 주소로 크롤링
   + 크롤링 정보
     - 상호명
     - 가게 이미지
     - 가게 리뷰 내용
     - 별점
   + 사용자는 별점이 높은 가게를 랜덤 리스트업
   + 마음에 드는 가게를 선택할 시 머신러닝페이지로 이동
   + 모달을 통해 가게에 대한 상세 정보 확인과 댓글 생성 가능
 ### 머신러닝페이지
   + 리뷰내용으로 코사인유사도검사
   + 메인페이지에서 사용자가 선택한 가게와 유사한 가게 리스트업
   + 모달을 통해 가게에 대한 상세 정보 확인과 댓글 생성 가능
   
 
 ### 앞으로 추가할 기능
   + 소셜 회원가입/로그인 기능
   + 마이페이지를 이용해 자신이 작성한 댓글 확인
   + 가게에 대해 좋아요 기능


# ![25](https://user-images.githubusercontent.com/103415295/200451936-b234dac2-a60a-4249-8a04-f03662eb0122.png)기술 스택

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
