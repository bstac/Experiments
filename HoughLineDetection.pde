import gab.opencv.*;

OpenCV opencv;
PImage src;
ArrayList<Line> lines;
//film_scan.jpg
void setup() {
  src = loadImage("test.jpg");
  src.resize(600, 600);
  size(src.width, src.height);

  opencv = new OpenCV(this, src);
  opencv.findCannyEdges(20, 75);

  // Find lines with Hough line detection
  // Arguments are: threshold, minLengthLength, maxLineGap
  lines = opencv.findLines(100, 30, 20);
}

void draw() {
  //image(opencv.getOutput(), 0, 0);
  image(src,0,0);
  strokeWeight(1);
  
  for (Line line : lines) {
    // lines include angle in radians, measured in double precision
    // so we can select out vertical and horizontal lines
    // They also include "start" and "end" PVectors with the position
    if (line.angle >= radians(0) && line.angle < radians(1)) {
      stroke(0, 255, 0);
      line(line.start.x, line.start.y, line.end.x, line.end.y);
    }

    if (line.angle > radians(89) && line.angle < radians(91)) {
      stroke(0, 255, 0);
      line(line.start.x, line.start.y, line.end.x, line.end.y);
    }
  }
}

