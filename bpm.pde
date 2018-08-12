/**
constructors:
BeatDetect();
BeatDetect(timeSize, sampleRate);

  * This sketch demonstrates how to use the BeatDetect object song SOUND_ENERGY mode.<br />
  * You must call <code>detect</code> every frame and then you can use <code>isOnset</code>
  * to track the beat of the music.
  * <p>
  * This sketch plays an entire song, so it may be a little slow to load.
  * <p>
  * For more information about Minim and additional features, 
  * visit http://code.compartmental.net/minim/
  
The BeatDetect class allows you to analyze an audio stream for beats (rhythmic onsets). Beat Detection Algorithms by Frederic Patin describes beats in the following way:
The human listening system determines the rhythm of music by detecting a pseudo periodical succession of beats. The signal which is intercepted by the ear contains a certain energy, 
this energy is converted into an electrical signal which the brain interprets. Obviously, The more energy the sound transports, the louder the sound will seem. But a sound will be heard 
as a beat only if his energy is largely superior to the sound's energy history, that is to say if the brain detects a brutal variation in sound energy. Therefore if the ear intercepts 
a monotonous sound with sometimes big energy peaks it will detect beats, however, if you play a continuous loud sound you will not perceive any beats. Thus, the beats are big variations 
of sound energy.
In fact, the two algorithms in this class are based on two algorithms described in that paper.
To use this class, inside of draw() you must first call detect(), passing the AudioBuffer you want to analyze. You may then use the isXXX functions to find out what beats have occurred 
in that frame. For example, you might use isKick() to cause a circle to pulse.

BeatDetect has two modes: sound energy tracking and frequency energy tracking. In sound energy mode, the level of the buffer, as returned by level(), is used as the instant energy 
in each frame. Beats, then, are spikes in this value, relative to the previous one second of sound. In frequency energy mode, the same process is used but instead of tracking the 
level of the buffer, an FFT is used to obtain a spectrum, which is then divided into average bands using logAverages(), and each of these bands is tracked individually. The result 
is that it is possible to track sounds that occur in different parts of the frequency spectrum independently (like the kick drum and snare drum).

In sound energy mode you use isOnset() to query the algorithm and in frequency energy mode you use isOnset(int i), isKick(), isSnare(), and isRange() to 
query particular frequnecy bands or ranges of frequency bands. It should be noted that isKick(), isSnare(), and isHat() merely call isRange() with values 
determined by testing the algorithm against music with a heavy beat and they may not be appropriate for all kinds of music. If you find they are performing 
poorly with your music, you should use isRange() directly to locate the bands that provide the most meaningful information for you.
  */
  
import ddf.minim.*;
import ddf.minim.analysis.*;

Minim minim;
AudioPlayer song;
BeatDetect beat;
AudioSample kick;
AudioSample snare;
AudioSample hat;

float cRadius;
float dRadius;
float eRadius;

void setup()
{
  size(600, 500, P3D);
  minim = new Minim(this);
  
    // load BD.wav from the data folder
  kick = minim.loadSample( "BD.mp3", 512); //file and buffer size
                         
  // if a file doesn't exist, loadSample will return null
  if ( kick == null ) println("Didn't get kick!");
  
  // load SD.wav from the data folder
  snare = minim.loadSample("SD.wav", 512);
  if ( snare == null ) println("Didn't get snare!");
  
  hat = minim.loadSample("HH.wav", 512);
  if ( hat == null ) println("Didn't get high hat!");
  
  //"Albert Hofmann.mp3"
  song = minim.loadFile("Rain Has Tone.mp3", 1024);
  song.play();
  // a beat detection object song SOUND_ENERGY mode with a sensitivity of 10 milliseconds
  beat = new BeatDetect(1024, 1024);
  
  ellipseMode(RADIUS);
  eRadius = 20;
  dRadius = 20;
  cRadius = 20;
}

boolean trip = false;
boolean trip2 = false;
boolean trip3 = false;
int count = 0;
int count2 = 0;
int count3 = 0;

void draw()
{
  println(beat.dectectSize());
  background(0);
  beat.detect(song.mix);
  float a = map(eRadius, 20, 80, 60, 255);
  
  if (!trip && beat.isRange(0,2,2)) 
  {
    trip = true;
    eRadius = 80;
    kick.trigger();
  }
  if (!trip2 && beat.isRange(2,4,2)) 
  {
    trip2 = true;
    dRadius = 80;
    snare.trigger();
  }
  if (!trip3 && beat.isRange(5,7,3)) 
  {
    trip3 = true;
    cRadius = 80;
    hat.trigger();
  }
  
  if(trip){count++;}
  if(count > 8){trip = false; count = 0;}
  if(trip2){count2++;}
  if(count2 > 10){trip2 = false; count2 = 0;}
  if(trip3){count3++;}
  if(count3 > 16){trip3 = false; count3 = 0;}
  
  
  fill(200, 30, 255, a);
  ellipse(width/3, height/4, cRadius, cRadius);
  cRadius *= 0.95;
  fill(10, 25, 200, a);
  ellipse(width-100, height/2, dRadius, dRadius);
  dRadius *= 0.95;
  fill(60, 255, 0, a);
  ellipse(width/2, height-100, eRadius, eRadius);
  eRadius *= 0.95;
  if ( eRadius < 20 ) eRadius = 20;
  if ( cRadius < 20 ) cRadius = 20;
  if ( dRadius < 20 ) dRadius = 20;
}
