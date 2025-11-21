from flask import Flask
app =Flask("__vijaya__")
@app.route('/')
def home():
    return "hello from cloud pass!"

if __name__ =="__main__":
    app.run()
