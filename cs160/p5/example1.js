function setup() {
    var canvas = createCanvas(windowWidth/2, windowHeight/2);
    canvas.parent('container');
    background(255);
}

function draw() {
    if (mouseIsPressed) {
        fill(0);
    } else {
        fill(255);
    }
    ellipse(mouseX, mouseY, 80, 80);
}

function windowResized() {
  centerCanvas();
}
