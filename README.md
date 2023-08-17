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


# Serializer 직렬화 / 역직렬화
  - form vs mode
  - form은 HTML의 form을 다루기 위한 클래스, model은 db의 테이블을 다루기 위한 클래스.
  - 둘 모두 직렬화기능, 유효성 체크 기능을 제공하고 있어서 본래 다른 목적의 클래스이지만 거의 비슷한 기능을 제공하는 클래스
  - DRF의 Serializer가 이 두 가지 기능을 제공하기 때문에 기능적으로 둘과 유사해 보임.
  - Serialization 이해를 위해 알아야 할 2가지 상황
    - 메모리 내부, 외부 상황
        - 데이터를 주고 받을 때 메모리 내/외부 상황이 다르기 때문에 포맷을 무시하고 아무렇게나 데이터를 전송/수신할 수 없다.
    - 복원 시, 정보 유지
        - 데이터를 주고 받으면서 포맷이 변할 수 있다. (int->string, string->int)
        --> 이런 상황이 문제점으로 극명히 드러나는 떄가 class를 다룰때이다.
    
        | | class | 설명 |
        |--|---|---|
        |  |<img width="163" src="https://github.com/FutureMaker0/Django_REST_framework/assets/120623320/85f4ad27-deef-4a50-b4a2-c5b8cc053270">| name변수는 string이지만 Person이란 class에 속해 있으며, age 또한 그냥 int가 아니라 Person에 속한 integer이다. Person이라는 class는 name, age라는 속성을 가진 class라는 정보가 그대로 전달되어야 한다. 이 과정에서 serialize 전처리 과정이 필요하며, 꺼내고 나서는 deserialize가 필요한 것이다. serialize 방법 중에서는 json 포맷으로 하는 것이 가장 간편한 방법이다. 거의 타입 변환만 해주는 수준이다. number, string, object, list, null 5가지를 주로 사용하며, 중괄호 사용 및 "" 사용만 숙지하면 된다. |


#
- serialize (read operation, get method)
  1. data record = instance
  2. dictionary로 변환 - 디비에서 가져온 인스턴스 데이터를 시리얼라이져에 태운다. 이 때, 데이터 인자가 아닌 인스턴스 인자에 데이터 넣는다.
  3. byte string으로 변환 - json data
    --> 이를 클라이언트에 응답
     
- deserialize (write operation, post/update/delete/patch method)
  1. byte string으로 수신 - json data
  2. dictionary로 변환
      - S(data=xxx)
      - is_valid, validated_data
  3. instance로 변환 후 DB에 save()
 







