from flask import Flask

app = Flask(_name_)

@app.route("/")
def hellow():
  return "Hello World from Jenkins CI/CD!"
if __name__=="__main__":
  app.run(host="0.0.0.0", port=5000)
