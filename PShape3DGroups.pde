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
  //ortho();
  /*
  float fov = PI/4;
   float cameraZ = (height/2.0) / tan(fov/2.0);
   perspective(fov, float(width)/float(height), cameraZ/10.0, cameraZ*10.0);
   */
  background(0);
  shapeMode(CENTER);
  // println("frameRate is " + frameRate);
  //frameRate(30);
  // img = loadImage("atom10e.2.png");
  img = loadImage("atom10e.2.png");
  textureMode(IMAGE);
  textureWrap(REPEAT);
  PShape s1 = createShape();
  s1.beginShape();
  s1.texture(img);
  s1.tint(0, 0, 0, 0);
  s1.stroke(255, 255, 0, 30);
  s1.vertex(-100, -100, 0, 100, 100);
  s1.vertex(-100, 100, 0, 100, 300);
  s1.vertex(100, 100, 0, 300, 300);
  s1.vertex(100, -100, 0, 300, 100);
  s1.endShape();
  //s.vertex(-100, -100, 0, 0, 0);
  // next plane
  PShape s2 = createShape();
  s2.beginShape();
  s2.texture(img);
  s2.tint(0, 0, 0, 0);
  s2.stroke(255, 255, 0, 30);
  s2.vertex(0, -100, -100, 100, 100);
  s2.vertex(0, 100, -100, 100, 300);
  s2.vertex(0, 100, 100, 300, 300);
  s2.vertex(0, -100, 100, 300, 100);
  s2.endShape();
  //s.vertex(0, -100, -100, 0, 0);
  // next plane
  PShape s3 = createShape();
  s3.beginShape();
  s3.texture(img);
  s3.tint(0, 0, 0, 0);
  s3.stroke(255, 255, 0, 30);
  s3.vertex(-100, 0, -100, 100, 100);
  s3.vertex(-100, 0, 100, 100, 300);
  s3.vertex(100, 0, 100, 300, 300);
  s3.vertex(100, 0, -100, 300, 100);
  s3.endShape();
  s = createShape(GROUP);
  // s.beginShape();
  // s.texture(img);
  // s.tint(0, 255, 255, 255);
  // s.stroke(255, 255, 0, 30);
  s.addChild(s1);
  s.addChild(s2);
  s.addChild(s3);
  // s.endShape();
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
final int dist = 5 ;
boolean mouseReady = true ;

void draw() {
  shapeMode(CENTER);
  if (lastMouseX < -100) {
    lastMouseX = mouseX ;
    lastMouseY = mouseY ;
    mouseReady = true ;
  } else if (! mousePressed) {
    mouseReady = true ;
    return ;
  } else if (! mouseReady) {
    return ;
  } else if (abs(lastMouseX - mouseX) < dist && abs(lastMouseY - mouseY) < dist) {
    //return;
  }
  int zcoord = mouseY - displayHeight/2 ;
  // zcoord = 0 ;
  translate(mouseX+s.width/2, mouseY+s.height/2, zcoord);
  //s.rotateX(TWO_PI * mouseX / displayWidth);
  //s.rotateY(TWO_PI * mouseY / displayHeight);
  //s.rotateZ(TWO_PI * (mouseX+mouseY) / (displayWidth*displayHeight));
  int ttint = ((aalpha & 255) << 24) | ((rred & 255) << 16) | ((ggreen & 255) << 8) | (bblue & 255);
  s.setStroke(~ttint);
  s.setTint(ttint);
  // s.setEmissive(ttint);
  rred = (rred + 32) & 255 ;
  ggreen = (ggreen + 31) & 255;
  bblue = (bblue + 30) & 255 ;
  aalpha = (aalpha + 96) & 255 ;
  //aalpha = 32 ;
  shape(s, 0, 0);
  lastMouseX = mouseX ;
  lastMouseY = mouseY ;
  mouseReady = false ;
}

