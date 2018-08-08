from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	fav_swimmers=["sarah","me", "sarah again"]
	return render_template(
		"index.html",fav_swimmers=fav_swimmers,
		likes_same_sport=True)


    

if __name__ == '__main__':
   app.run(debug = True, port=8080)