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
  s = loadShape("star1.svg");
}

boolean sketchFullScreen() {
  return true;
  // Also from Preferences "Run sketches on display 2" for dome.
}

int rred = 255 ;
int ggreen = 128;
int bblue = 0 ;
int aalpha = 255 ;

void draw() {
  shapeMode(CENTER);
  int zcoord = mouseY - displayHeight/2 ;
  // translate(displayWidth/2, displayHeight/2, zcoord);
  translate(mouseX, mouseY, zcoord);
  rotateX(TWO_PI * mouseX / displayWidth);
  rotateY(TWO_PI * mouseY / displayHeight);
  ellipseMode(CENTER);  // default, X,Y gives center point
  if (pmouseX == mouseX && pmouseY == mouseY) {
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
  s.setTexture(img);
  shape(s, 0, 0);
}

