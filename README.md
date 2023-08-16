# Django_REST_framework
  - serializers.py(= forms.py) 코딩에 손이 많이 가는 방식
  - serializer : 클라이언트에 출력해주는 내용이나 포맷에 관련된 사항을 담당
  - DRF serializer는 딕셔너리를 기반으로 동작하는 클래스다.

# 참고할만한 사이트
  - DRF: cdrf.co
  - CBV: ccbv.co.uk

# s.M.u.V.(S).T 패턴
1. settings.py - 뼈대제작
2. Models.py
3. urls.py
4. View.py
5. Serializers.py
6. Templates.py
순으로 코딩

#
개념적으로 mixins 클래스들을 모아 Generics 클래스들을 만들었고, 이들을 모아 viewSets 클래스들을 만들었다.
- View > APIView > GenericAPIView + Mixin > ModelView Set
# 

# GenericAPIView 의 기본 5가지 제네릭뷰 (C.R.U.D)
| 순번 | APIView | 구동 원리 | 역할 | HTTP 관점 |
|---|---|---|---|---|
| 1 | CreateAPIView|GenericAPIView + CreateModelMixin | Create | POST |
| 2 | DestroyAPIView|GenericAPIView + DestroyModelMixin | Delete | GET |
| 3 | ListAPIView|GenericAPIView + ListModelMixin | Read | GET |
| 4 | RetrieveAPIView|GenericAPIView + RetrieveModelMixin | - | UPDATE, PATCH |
| 5 | UpdateAPIView|GenericAPIView + UpdateModelMixin | Update | DELETE |

ModelViewSet = CreateAPIView + DestroyAPIView + ListAPIView + RetrieveAPIView + UpdateAPIView
  - ViewSet의 장점은, 테이블을 만들고 나서 테이블의 내용을 있는 그대로 간단하게 볼 수 있다는 것이 장점.
#

# DRF 변경사항 - REST 방식의 url에 맞춰 코딩
| 순번 | AS-IS | TO-BE | 방식 | APIView 상속 |
|---|---|---|---|---|
| 1 | /api/post/list/ | /api2/post/ | GET | ListAPIView |
| 2 | /api/post/99/ | /api2/post/99 | GET | RetrieveAPIView |
| 3 | /api/comment/create/ | /api2/comment/ | POST | CreateAPIView |
| 4 | /api/like/99/ |  | GET |  |
| 5 | /api/catetag/ |  | GET |  |


# GenericView 동작 로직
1. data from database
2. serialize
  - ListAPIView vs RetrieveAPIView
    - ListAPIView(instance = , many = True)
        - queryset을 통해 db로부터 데이터를 가져와서 serializer_class에서 serialize한다.
        - many 옵션을 True로 줘서 인스턴스를 여러개 serialize
    - RetrieveAPIView(instance = , many = False)
        - queryset을 통해 db로부터 데이터를 가져와서 serializer_class에서 serialize한다.
        - many 옵션을 False로 줘서 인스턴스 하나만 serialize
3. response to client


# partial = True
  - 필수 속성(required)가 모두 확인되지 않고 하나만 받더라도 update가 성공한다는 의미.
  - PUT vs PATCH
    - DRF에서는 PatchAPIView는 없고, UpdateAPIView에서 둘 모두를 처리한다.






