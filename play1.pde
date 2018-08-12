import fullscreen.*;

size(displayWidth,displayHeight);
//frame.setSize(displayWidth, displayHeight);
FullSceen fs = new FullScreen(this);
fs.enter();
fill(0,255,0,128);
ellipse(100,100,100,100);
fill(255,0,0,128);
ellipse(110,110,50,50);

boolean sketchFullScreen() { return true; }

