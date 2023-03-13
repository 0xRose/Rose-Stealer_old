import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})
    
@sio.event
def coco_webhook(data):
    print('message received with ', data)

@sio.event
def disconnect():
    print('disconnected from server')
    
sio.connect('https://socketiotest.toopicogaming.repl.co')


while True: #Input and emit socket
    message = input()
    sio.emit('my_message', {'data': message})
