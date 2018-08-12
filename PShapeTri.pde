PShape tri;

void setup() {
  size(400, 400, P3D);
  tri = createShape();
  tri.beginShape();
  tri.noStroke();
  tri.fill(255);
  tri.vertex(0, 0);
  tri.vertex(50, 0);
  tri.vertex(50, 50);
  tri.endShape(CLOSE);
}

void draw() {
  background(0);
  translate(mouseX, mouseY);
  shape(tri);
}
