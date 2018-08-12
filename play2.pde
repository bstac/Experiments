// Getting Processing to work on the planetarium dome.
// D. Parson, Summer 2014

public void init() {
  frame.removeNotify();
  frame.setUndecorated(true);
  frame.addNotify();
  super.init();
}

void setup() {
   size(displayWidth,displayHeight); // uses initial display
   frame.setLocation(0,0);
}

void draw() {
  fill(0,255,0,128);
  ellipse(100,100,100,100);
  fill(255,0,0,128);
  ellipse(110,110,50,50);
}

