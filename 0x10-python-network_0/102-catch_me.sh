#!/bin/bash
#makes a request that causes server to respond in the body of the response
curl -sL -X PUT -H "Origin: You got me!" -d "user_id=98" 0.0.0.0:5000/catch_me
