import js
p5 = js.window

state = 'AWAKE'
timer_ms = 0

def setup():
    p5.createCanvas(300, 300)  
    print('finished setup..')

def draw():
    p5.background(255)
    global timer_ms, state
    p5.text('Press mouse to wake them up!', 10, 15)
    p5.text('Status : ' + str(state), 10, 35)
    msec = p5.millis()  
    sec = int(msec / 1000)  

    if(p5.millis() > timer_ms + 2500):
        if(state == 'AWAKE'):
            state = 'TIRED'
            timer_ms = p5.millis()  # update timer
        elif(state == 'TIRED'):
            state = 'ASLEEP'
            timer_ms = p5.millis()  # update timer

    if(state == 'AWAKE'):
        draw_eye_awake(120, 150)
        draw_eye_awake(180, 150)
        p5.text('!!!', 145, 280)
    elif(state == 'TIRED'):
        draw_eye_tired(120, 150)
        draw_eye_tired(180, 150)
        p5.text('...', 145, 280)
    elif(state == 'ASLEEP'):
        draw_eye_asleep(120, 150)
        draw_eye_asleep(180, 150)
        p5.text('zzz...', 145, 280)

def mousePressed(event):
    global timer_ms, state
    if(state == 'ASLEEP'):
        state = 'AWAKE'
        timer_ms = p5.millis()
        print('I am awake!')
    

def draw_eye_awake(x, y):
    p5.push()
    p5.translate(x, y)
    p5.fill(0, 0, 0, 0)
    p5.arc(0, -18, 50, 50, p5.radians(50), p5.radians(130))  # lower lid
    p5.arc(0, 18, 50, 50, p5.radians(230), p5.radians(310))  # upper lid
    p5.fill(0)
    p5.ellipse(0, 0, 10, 10)
    p5.fill(255)
    p5.pop()

def draw_eye_tired(x, y):
    p5.push()
    p5.translate(x, y)
    p5.fill(0, 0, 0, 0)
    p5.arc(0, -18, 50, 50, p5.radians(50), p5.radians(130)) # lower lid
    p5.fill(0)
    p5.ellipse(0, 0, 10, 10) # iris
    p5.fill(255)
    p5.noStroke()
    p5.rect(-20, -15, 40, 15) # white of upper lid
    p5.stroke(0)
    p5.line(-17, 0, 17, 0) # upper lash
    p5.fill(0, 0, 0, 0)
    p5.stroke(200, 200, 200)
    p5.arc(0, 18, 50, 50, p5.radians(230), p5.radians(310)) # upper lid
    p5.pop()

def draw_eye_asleep(x, y):
    p5.push()
    p5.translate(x, y)
    p5.fill(0, 0, 0, 0)
    p5.arc(0, -18, 50, 50, p5.radians(50), p5.radians(130)) # lower lid
    p5.stroke(200, 200, 200)
    p5.arc(0, 18, 50, 50, p5.radians(230), p5.radians(310)) # upper lid
    p5.pop()

def keyPressed(event):
    pass

def keyReleased(event):
    pass

def mouseReleased(event):
    pass
