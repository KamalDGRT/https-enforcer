from flask import Flask, redirect

app=Flask(__name__)

redirectionPage="""
                <noscript>JavaScript needed for redirection. Please use https to visit the website.</noscript>
                <script>
                    var currentUrl=new URL(window.location.href);
                    currentUrl.protocol='https';
                    window.location.href=currentUrl.href;
                </script>
                """

@app.route('/')
def main():
    return redirectionPage

@app.errorhandler(404)
def handleEveryRoute(e):
    return redirectionPage

if __name__=="__main__":
    app.run(host='0.0.0.0', port=80)

