import flask
app = flask.Flask("guests")

def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

def get_guests():
    guestlist = open("guestlist.txt")
    content = guestlist.read()
    guestlist.close()
    guests = content.split("\n")
    new_guests = []
    for guest in guests:
        if guest:
            name, surname = guest.split(" ")
            new_guest = ", ".join([surname, name])
            new_guests.append(new_guest)
    new_guests.sort()
    return new_guests

@app.route("/")
def homepage():
    return get_html("index")

@app.route("/guests")
def guests():
    html_page = get_html("guests")
    guests = get_guests()
    actual_values = ""
    for guest in guests:
        actual_values += '<p class="guest">' + guest + '</p>'
    return html_page.replace("$$GUESTS$$", actual_values)


#FLASK_APP=guestlist.py flask run