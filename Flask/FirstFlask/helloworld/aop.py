# 요청이 왔을 경우 자바의 AOP처럼 사용 하기 위한 기능을 제공 함 
# Flask에서는 HTTP요청 전후에 사용 할 수 있는 데코레이터를 제공 함 

# before_first_request : Web applicaiton 기동 후 최초로 http요청에 대한 실행 ( 한번만 실행 됨 )
# before_request : 매 http 요청이 들어 올 떄 마다 실행 됨
# after_request : 매 http 요청이 끝나 브라우저에 응답하기 전에 실행 됨
# teardown_request : http 요청의 결과가 브라우저에 응답 한 다음 실행
# teardown_appcontext : http 요엋이 완전히 완료 되면 싷앵 되어, Application 컨텍스트 내에서 실행됨 

