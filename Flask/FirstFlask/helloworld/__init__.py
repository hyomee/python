from flask import Flask
from flask import Response, make_response

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "hello world"

@app.route("/response")
def response_test():
    custome_response = Response("고객 요청 응답", 200, {
        "Program":"Flask Wrb Application"
    })

    return make_response(custome_response)

@app.route("/responseno")
def responseno():
    return make_response("Response 없이 응답 .....")


@app.route("/wsgi")
def responseWsgi():
    def application(environ, start_response):
        response_body = "The Request method was %s" % environ['REQUEST_METHOD']
        status = "200 OK"
        response_header = [('Content-Type', 'text/plan'),
                           ('Content-Length', str(len(response_body)))]
        start_response(status, response_header)
        return [response_body]

    return make_response(application)

@app.route("/tuple")
def responsetuple():
    return make_response(('튜플[Tuple] => 고객 요청', 'OK', {
        'response_method':'Tuple Response'
    }))