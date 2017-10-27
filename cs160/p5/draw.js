function setup() {
    var canvas = createCanvas(windowWidth/2, windowHeight/2);
    canvas.parent('container');
    background(255);
}

let ticks = 0;
var lastMouseX = null;
var lastMouseY = null;

function draw() {
    const color = tinycolor({h: mouseX / 2, s: 100, v: 100});
    const rgbColor = color.toRgb();
    stroke(rgbColor.r, rgbColor.g, rgbColor.b, 250);
    if (mouseIsPressed) {
        if (lastMouseX == null || lastMouseY == null) {
            lastMouseX = mouseX;
            lastMouseY = mouseY;
        } 
        line(lastMouseX, lastMouseY, mouseX, mouseY);
        lastMouseX = mouseX;
        lastMouseY = mouseY;
    } else {
        lastMouseX = null;
        lastMouseY = null;
    }
    ticks += 1;
}

function windowResized() {
  centerCanvas();
}
