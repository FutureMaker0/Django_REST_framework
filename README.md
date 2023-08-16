# Django_REST_framework

# 참고할만한 사이트
  - DRF: cdrf.co
  - CBV: ccbv.co.uk

# s.M.u.V.T 패턴
1. settings.py - 뼈대제작
2. Models.py
3. urls.py
4. View.py
5. Templates.py
순으로 코딩

#
개념적으로 mixins 클래스들을 모아 Generics 클래스들을 만들었고, 이들을 모아 viewSets 클래스들을 만들었다.
# 
View > APIView > GenericAPIView + Mixin > ModelView Set
# 
GenericAPIView 의 기본 5가지 제네릭뷰 (C.R.U.D)
| 순번 | APIView | 구동 원리 | 역할 | HTTP 관점 |
|---|---|---|---|---|
| 1. | CreateAPIView|GenericAPIView + CreateModelMixin | Create | POST |
| 2. | DestroyAPIView|GenericAPIView + DestroyModelMixin | Delete | GET |
| 3. | ListAPIView|GenericAPIView + ListModelMixin | Read | GET |
| 4. | RetrieveAPIView|GenericAPIView + RetrieveModelMixin | - | UPDATE, PATCH |
| 5. | UpdateAPIView|GenericAPIView + UpdateModelMixin | Update | DELETE |
ModelViewSet = CreateAPIView + DestroyAPIView + ListAPIView + RetrieveAPIView + UpdateAPIView

