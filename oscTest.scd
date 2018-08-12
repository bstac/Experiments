//http://vimeo.com/71100719

//not my code

//When an Array is given as an input to a unit generator it causes
//an array of multiple copies of that unit generator to be made,
//each with a different value from the input array. This is called
//multichannel expansion. All but a few special unit generators
//perform multichannel expansion. Only Arrays are expanded, no
//other type of Collection, not even subclasses of Array.

//relationships
//amp = 1/r
//reverb = r
//speaker value =

s.boot;
s.freeAll;
s.quit;


(
SynthDef('funsynth', {
	arg pitch=200;
	var sound = SinOsc.ar(pitch, mul:0.2);
	var linen = Env.linen(0.01, sustainTime:0, releasetime:1);
	var env = EnvGen.kr(linen, doneAction:2);
	Out.ar(0, sound * env);
}).add;
)



NetAddr.localAddr

(
OSCdef('cubeListener',
	{
		arg msg;
		Synth('funsynth', [pitch:(msg[1]*100+50)]);
	},
	"/cube");

)

