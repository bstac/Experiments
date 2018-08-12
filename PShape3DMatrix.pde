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
  size(displayWidth, displayHeight, P3D);
  background(0);
  shapeMode(CENTER);
  // println("frameRate is " + frameRate);
  //frameRate(30);
  // img = loadImage("atom10e.2.png");
  img = loadImage("atom10e.2.png");
  textureMode(IMAGE);
  textureWrap(REPEAT);
  s = createShape();
  s.beginShape();
  s.texture(img);
  s.tint(0, 255, 255, 255);
  s.stroke(255, 255, 0, 30);
  s.vertex(-100, -100, 0, 100, 100);
  s.vertex(-100, 100, 0, 100, 300);
  s.vertex(100, 100, 0, 300, 300);
  s.vertex(100, -100, 0, 300, 100);
  //s.vertex(-100, -100, 0, 0, 0);
  // next plane
  s.vertex(0, -100, -100, 100, 100);
  s.vertex(0, 100, -100, 100, 300);
  s.vertex(0, 100, 100, 300, 300);
  s.vertex(0, -100, 100, 300, 100);
  //s.vertex(0, -100, -100, 0, 0);
  // next plane
  s.vertex(-100, 0, -100, 100, 100);
  s.vertex(-100, 0, 100, 100, 300);
  s.vertex(100, 0, 100, 300, 300);
  s.vertex(100, 0, -100, 300, 100);
  //s.vertex(-100, 0, -100, 0, 0);
  s.endShape();
}

boolean sketchFullScreen() {
  return true;
  // Also from Preferences "Run sketches on display 2" for dome.
}

int rred = 255 ;
int ggreen = 128;
int bblue = 0 ;
int aalpha = 255 ;
int lastMouseX = -1000 ;
int lastMouseY = -1000 ;
final int dist = 100 ;

void draw() {
  shapeMode(CENTER);
  pushMatrix();
  int zcoord = mouseY - displayHeight/2 ;
  // translate(displayWidth/2, displayHeight/2, zcoord);
  translate(mouseX, mouseY, zcoord);
  rotateX(TWO_PI * mouseX / displayWidth);
  rotateY(TWO_PI * mouseY / displayHeight);
  ellipseMode(CENTER);  // default, X,Y gives center point
  if (abs(lastMouseX - mouseX) < dist && abs(lastMouseY - mouseY) < dist) {
    popMatrix();
    return ;
  }
  int ttint = ((aalpha & 255) << 24) | ((rred & 255) << 16) | ((ggreen & 255) << 8) | (bblue & 255);
  s.setStroke(~ttint);
  s.setTint(ttint);
  // s.setEmissive(ttint);
  rred = (rred + 32) & 255 ;
  ggreen = (ggreen + 31) & 255;
  bblue = (bblue + 30) & 255 ;
  aalpha = (aalpha + 96) & 255 ;
  aalpha = 128 ;
  shape(s, 0, 0);
  popMatrix();
  lastMouseX = mouseX ;
  lastMouseY = mouseY ;
}

