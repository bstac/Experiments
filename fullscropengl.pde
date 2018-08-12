// Getting Processing to work on the planetarium dome.
// D. Parson, Summer 2014

import processing.opengl.* ;  // Not needed for size..OPENGL

/* NOT NEEDED IN 2.X
See http://wiki.processing.org/w/Window_Size_and_Full_Screen
public void init() {
  frame.removeNotify();
  frame.setUndecorated(true);
  frame.addNotify();
  super.init();
}
*/ 

void setup() {
  size(displayWidth, displayHeight, OPENGL);
  background(0);
  // println("frameRate is " + frameRate);
  //frameRate(30);
}

boolean sketchFullScreen() {
  return true;
  // Also from Preferences "Run sketches on display 2" for dome.
}

int [][] colors = {
  {0, 0, 0},
  {255, 0, 0},
  {255, 255, 0},
  {0, 255, 0},
  {0, 255, 255},
  {0, 0, 255},
  {255, 0, 255},
  {255, 255, 255}
};
int colorix = 0 ;
int timeix = 0 ;
int strokeix = colors.length / 2 ;
int stroketime = 0 ;

// Draw ellipses out from the center, changing the color every
// 10 redraws. Innermost ellipse has alpha=255, alpha scales
// dow as bigger ellipses draw atop the smaller ones.
void draw() {
  int numcircles = colors.length ;
  int zcoord = mouseY - displayHeight/2 ;
  translate(displayWidth/2, displayHeight/2, zcoord);
  rotateX(TWO_PI * mouseX / displayWidth);
  rotateY(TWO_PI * mouseY / displayHeight);
  ellipseMode(CENTER);  // default, X,Y gives center point
  if (pmouseX == mouseX && pmouseY == mouseY) {
      return ;
  }
  for (int i = numcircles-1 ; i >=0 ; i--) {
    int width = displayWidth * (i+1) / numcircles ;
    int height = displayHeight * (i+1) / numcircles ;
    int myX = 0 ;// (displayWidth/2) ;
    int myY = 0  ; // (displayHeight/2) ;
    int mycolor = (colorix + i) % numcircles ;
    mycolor = colorix ; // an experiment
    int alpha = (numcircles - i) * 255 / numcircles ;
    fill(colors[mycolor][0], colors[mycolor][1],
            colors[mycolor][2], alpha);
    // mycolor = (mycolor + colors.length/2) % colors.length;
    mycolor = (strokeix /*+ i*/) % numcircles ;
    stroke(colors[mycolor][0], colors[mycolor][1],
            colors[mycolor][2], 255);
    int sw = (displayWidth * mouseX / displayWidth) / colors.length;
    // strokeWeight((numcircles - i) * 2);
    strokeWeight(4 /*sw*/);
    ellipse(myX, myY, width, height);
  }
  timeix += 1 ;
  if (timeix >= 1) {
    colorix = (colorix+1) % numcircles ;
    timeix = 0;
  }
  stroketime += 1 ;
  if (stroketime >= 12) {
    strokeix = (strokeix+3) % numcircles ;
    stroketime = 0;
  }
}
