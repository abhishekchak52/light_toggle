from bottle import run, get, post, request

light = {
	'status' : 'Off' 
} # Start off


@get('/')
def get_status():
	return light

@post('/set')
def toggle_status():
	set_request = request.json.get('state')
	light['status'] = set_request
	return {'message': 'Light Toggled'}


run(host='localhost', port=8080, debug=True, reloader=True)