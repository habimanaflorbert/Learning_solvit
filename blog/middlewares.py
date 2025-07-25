class MyCustomMiddleware:

    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self, request):
        print(request.user.id)
        response=self.get_response(request)
        print(request.user.is_anonymous)

        
        return response
    
    def process_request(self,request):
        print("I'm in middleware custom for request")
        return None
    
    def process_response(self,request,response):
        print("we are in response of middleware")
        return response
        