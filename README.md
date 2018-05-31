# Flask wrapper for terraform commands
### To Use:
1. docker build -t flask-one:latest .
2. docker run -d -p 5000:5000 IMAGEID
3. go to localhost:5000/
4. enter your aws access ID and Secret key in the prompt
5. choose to build a vpc.  *This is currently a demo and will create a vpc in ap-south-1 with CIDR 10.71.0.0/16*
6. enter the information for tags that will also be generated.
7. build. *there will be a json response once the vpc is built.  check to validate your vpc is built.*
8. reroute to localhost:5000 and login again.
9. select destroy vpc
10.  validate the vpc was destroyed.
