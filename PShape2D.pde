// Getting Processing to work on the planetarium dome.
// D. Parson, Summer 2014

/* NOT NEEDED IN 2.X
See http://wiki.processing.org/w/Window_Size_and_Full_Screen
public void init() {
  frame.removeNotify();
  frame.setUndecorated(true);
  frame.addNotify();
  super.init();
}
*/ 

PShape s ;
PImage img ;

void setup() {
  size(displayWidth, displayHeight, P2D);
  background(0);
  // println("frameRate is " + frameRate);
  //frameRate(30);
  img = loadImage("atom10e.2.png");
  //textureMode(IMAGE);
  s = createShape();
  s.beginShape();
  // s.noFill();
  // s.noStroke();
  s.texture(img);
  s.tint(0, 255, 255);
  s.vertex(30, 75, 0, 0);
  s.vertex(40, 20, 0, 408);
  s.vertex(50, 75, 407, 407);
  s.vertex(60, 20, 407, 0);
  s.vertex(70, 75, 0, 0);
  s.vertex(80, 20, 0, 407);
  s.vertex(90, 75, 407, 407);
  s.endShape();
}

boolean sketchFullScreen() {
  return true;
  // Also from Preferences "Run sketches on display 2" for dome.
}

void draw() {
  int zcoord = mouseY - displayHeight/2 ;
  // translate(displayWidth/2, displayHeight/2, zcoord);
  translate(mouseX, mouseY);
  // rotateX(TWO_PI * mouseX / displayWidth);
  rotate(TWO_PI * mouseY / displayHeight);
  ellipseMode(CENTER);  // default, X,Y gives center point
  if (pmouseX == mouseX && pmouseY == mouseY) {
      return ;
  }
  shape(s, 0, 0);
}
