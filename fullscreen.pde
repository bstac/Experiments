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

void setup() {
  size(displayWidth, displayHeight);
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

// Draw ellipses out from the center, changing the color every
// 10 redraws. Innermost ellipse has alpha=255, alpha scales
// dow as bigger ellipses draw atop the smaller ones.
void draw() {
  background(0);
  int numcircles = colors.length ;
  ellipseMode(CENTER);  // default, X,Y gives center point
  for (int i = 0 ; i < numcircles ; i++) {
    int width = displayWidth * (i+1) / numcircles ;
    int height = displayHeight * (i+1) / numcircles ;
    int myX = (displayWidth/2) ;
    int myY = (displayHeight/2) ;
    int mycolor = (colorix + i) % numcircles ;
    mycolor = colorix ; // an experiment
    int alpha = (numcircles - i) * 255 / numcircles ;
    fill(colors[mycolor][0], colors[mycolor][1],
            colors[mycolor][2], alpha);
    ellipse(myX, myY, width, height);
  }
  timeix += 1 ;
  if (timeix >= 10) {
    colorix = (colorix+1) % numcircles ;
    timeix = 0;
  }
}
